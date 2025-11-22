import pandas as pd

# ================================
# CONFIG: input/output paths
# ================================
PATH_2023 = "data/raw/Ano-2023.csv"
PATH_2024 = "data/raw/Ano-2024.csv"
PATH_DEPUTADOS = "data/raw/Deputados.csv"

OUT_FACT_DESPESAS = "data/out/fact_despesas_2023_2024.csv"
OUT_DIM_DEPUTADO = "data/out/dim_deputado.csv"
OUT_DIM_TEMPO = "data/out/dim_tempo.csv"
OUT_DIM_SUBCOTA = "data/out/dim_subcota.csv"
OUT_FACT_DESPESAS_DEP = "data/out/fact_despesas_2023_2024_com_deputado.csv"  # optional

# ================================
# 1. Load raw data
# ================================
print("Loading raw CSVs...")
desp23_raw = pd.read_csv(PATH_2023, sep=";", encoding="utf-8-sig", low_memory=False)
desp24_raw = pd.read_csv(PATH_2024, sep=";", encoding="utf-8-sig", low_memory=False)
dep_raw = pd.read_csv(PATH_DEPUTADOS, sep=";", encoding="utf-8-sig", low_memory=False)

print("  2023 shape:", desp23_raw.shape)
print("  2024 shape:", desp24_raw.shape)
print("  Deputados shape:", dep_raw.shape)

# ================================
# 2. Cleaning helpers
# ================================
def clean_despesas(df: pd.DataFrame, origem_ano: int) -> pd.DataFrame:
    df = df.copy()

    # Strip whitespace from all text columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip()

    # Convert numeric identifiers to nullable integers
    int_cols = ["ideCadastro", "nuCarteiraParlamentar", "numRessarcimento"]
    for col in int_cols:
        if col in df.columns:
            df[col] = df[col].astype("Int64")

    # CPF as zero-padded string (11 digits)
    if "cpf" in df.columns:
        cpf_int = df["cpf"].astype("Int64")
        df["cpf"] = cpf_int.astype("string").str.zfill(11)

    # Parse dates
    for col in ["datEmissao", "datPagamentoRestituicao"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Ensure numeric measures
    for col in ["vlrDocumento", "vlrGlosa", "vlrLiquido", "vlrRestituicao"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Keep explicit source year (in addition to numAno)
    df["origemAno"] = origem_ano

    # Convert datEmissao & datPagamentoRestituicao to pure date (for Power BI)
    df["datEmissao"] = df["datEmissao"].dt.date
    if "datPagamentoRestituicao" in df.columns:
        df["datPagamentoRestituicao"] = df["datPagamentoRestituicao"].dt.date

    # Create a single textual key for subcota + especificação (for easy relationships)
    df["chaveSubCota"] = (
        df["numSubCota"].astype(str).str.zfill(2)
        + "-"
        + df["numEspecificacaoSubCota"].astype(str).str.zfill(2)
    )

    return df


def clean_deputados(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Strip whitespace
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip()

    # Extract ideCadastro from URI (last numeric segment)
    df["ideCadastro"] = df["uri"].str.extract(r"(\d+)$")[0].astype("Int64")

    # Parse dates
    for col in ["dataNascimento", "dataFalecimento"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce").dt.date

    # CPF as string (all missing, but we keep type consistent)
    if "cpf" in df.columns:
        df["cpf"] = df["cpf"].astype("Int64").astype("string").str.zfill(11)

    return df

# ================================
# 3. Clean expense tables
# ================================
print("\nCleaning despesas 2023...")
desp23 = clean_despesas(desp23_raw, 2023)
print("  dtypes 2023:")
print(desp23.dtypes)

print("\nCleaning despesas 2024...")
desp24 = clean_despesas(desp24_raw, 2024)
print("  dtypes 2024:")
print(desp24.dtypes)

# Integrate 2023 + 2024 into single fact table
fact_despesas = pd.concat([desp23, desp24], ignore_index=True)
print("\nIntegrated fact_despesas shape:", fact_despesas.shape)

# ================================
# 4. Clean Deputados and build dim_deputado
# ================================
print("\nCleaning Deputados...")
dep_clean = clean_deputados(dep_raw)
print("  Deputados dtypes:")
print(dep_clean.dtypes)

# One row per ideCadastro (already unique, but we are explicit)
dim_deputado = (
    dep_clean
    .sort_values(["ideCadastro", "idLegislaturaFinal"])
    .drop_duplicates(subset=["ideCadastro"], keep="last")
)

print("dim_deputado shape:", dim_deputado.shape)

# ================================
# 5. Build extra dimensions
# ================================
print("\nBuilding dim_tempo (calendar table based on datEmissao)...")

# Build date dimension from min/max datEmissao
min_date = pd.to_datetime(fact_despesas["datEmissao"], errors="coerce").min()
max_date = pd.to_datetime(fact_despesas["datEmissao"], errors="coerce").max()

date_range = pd.date_range(start=min_date, end=max_date, freq="D")
dim_tempo = pd.DataFrame({"data": date_range})
dim_tempo["ano"] = dim_tempo["data"].dt.year
dim_tempo["mes"] = dim_tempo["data"].dt.month
dim_tempo["dia"] = dim_tempo["data"].dt.day
dim_tempo["ano_mes"] = dim_tempo["data"].dt.to_period("M").astype(str)
dim_tempo["trimestre"] = dim_tempo["data"].dt.quarter

print("dim_tempo shape:", dim_tempo.shape)

print("\nBuilding dim_subcota...")
dim_subcota = (
    fact_despesas[
        ["chaveSubCota", "numSubCota", "txtDescricao",
         "numEspecificacaoSubCota", "txtDescricaoEspecificacao"]
    ]
    .drop_duplicates()
    .sort_values(["numSubCota", "numEspecificacaoSubCota"])
)
print("dim_subcota shape:", dim_subcota.shape)

# ================================
# 6. Optional: denormalised table (fact + deputado)
# ================================
print("\nBuilding denormalised fact_despesas_2023_2024_com_deputado...")

fact_despesas_dep = fact_despesas.merge(
    dim_deputado[
        ["ideCadastro", "nome", "nomeCivil", "siglaSexo",
         "dataNascimento", "ufNascimento", "municipioNascimento"]
    ],
    on="ideCadastro",
    how="left",
)

print("fact_despesas_dep shape:", fact_despesas_dep.shape)
missing_dep = fact_despesas_dep["nome"].isna().sum()
print("  Rows without matching deputado (nome is NaN):", missing_dep)

# ================================
# 7. Save all prepared tables as CSV (UTF-8, ; separator)
# ================================
print("\nSaving prepared CSVs (UTF-8 with BOM, ; as separator)...")

fact_despesas.to_csv(OUT_FACT_DESPESAS, index=False, sep=";", encoding="utf-8-sig")
dim_deputado.to_csv(OUT_DIM_DEPUTADO, index=False, sep=";", encoding="utf-8-sig")
dim_tempo.to_csv(OUT_DIM_TEMPO, index=False, sep=";", encoding="utf-8-sig")
dim_subcota.to_csv(OUT_DIM_SUBCOTA, index=False, sep=";", encoding="utf-8-sig")
fact_despesas_dep.to_csv(OUT_FACT_DESPESAS_DEP, index=False, sep=";", encoding="utf-8-sig")

print("Done. Files created:")
print("  -", OUT_FACT_DESPESAS)
print("  -", OUT_DIM_DEPUTADO)
print("  -", OUT_DIM_TEMPO)
print("  -", OUT_DIM_SUBCOTA)
print("  -", OUT_FACT_DESPESAS_DEP, "(optional analysis table)")
