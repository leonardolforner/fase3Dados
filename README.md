# Modelo de Dados para Dashboard em Power BI

Este projeto contém os **datasets preparados** a partir das bases brutas:

- `data/raw/Ano-2023.csv`
- `data/raw/Ano-2024.csv`
- `data/raw/Deputados.csv`

O objetivo da preparação é disponibilizar um **modelo integrado** para construção de dashboards em Power BI, seguindo um esquema em estrela (star schema).

---

## Tabelas Geradas

### 1. Fato: `fact_despesas_2023_2024`

Tabela central com todas as despesas dos anos de 2023 e 2024.

**Grão:** uma linha = um registro de despesa (documento de reembolso).

**Principais campos:**

- Chaves:
  - `ideDocumento` – identificador do documento.
  - `ideCadastro` – identificador do deputado (FK para `dim_deputado`).
  - `chaveSubCota` – chave da subcota (FK para `dim_subcota`).
- Tempo:
  - `datEmissao` – data de emissão (FK para `dim_tempo`).
  - `datPagamentoRestituicao` – data de pagamento/restituição (opcional).
  - `numAno`, `numMes`, `origemAno`.
- Valores:
  - `vlrDocumento`, `vlrGlosa`, `vlrLiquido`, `vlrRestituicao`.
- Atributos adicionais:
  - `txNomeParlamentar`, `sgUF`, `sgPartido`,
  - `txtFornecedor`, `txtCNPJCPF`, `cpf`,
  - `txtPassageiro`, `txtTrecho`, `urlDocumento`.

---

### 2. Dimensão: `dim_deputado`

Informações de cadastro dos deputados.

**Grão:** uma linha = um deputado.

**Principais campos:**

- Chave:
  - `ideCadastro` – PK, relaciona com a fato.
- Identificação:
  - `nome`, `nomeCivil`.
- Legislatura:
  - `idLegislaturaInicial`, `idLegislaturaFinal`.
- Dados demográficos:
  - `siglaSexo`, `dataNascimento`, `dataFalecimento`,
  - `ufNascimento`, `municipioNascimento`.
- Web:
  - `uri`, `urlRedeSocial`, `urlWebsite`.
- `cpf` – CPF (pode estar vazio).

---

### 3. Dimensão: `dim_tempo`

Tabela calendário gerada a partir do intervalo de datas das despesas.

**Grão:** uma linha = uma data.

**Principais campos:**

- `data` – PK, relaciona com `fact_despesas_2023_2024.datEmissao`.
- `ano`, `mes`, `dia`.
- `ano_mes` – string no formato `YYYY-MM`.
- `trimestre` – número do trimestre (1–4).

---

### 4. Dimensão: `dim_subcota`

Classificação das despesas.

**Grão:** uma linha = uma combinação de subcota + especificação.

**Principais campos:**

- Chave:
  - `chaveSubCota` – PK (ex.: `"13-00"`).
- Classificação:
  - `numSubCota`, `txtDescricao`,
  - `numEspecificacaoSubCota`, `txtDescricaoEspecificacao`.

---

### 5. Tabela auxiliar (opcional): `fact_despesas_2023_2024_com_deputado`

Tabela desnormalizada com a junção de `fact_despesas_2023_2024` e `dim_deputado` via `ideCadastro`.  
Pode ser usada para testes rápidos, mas o modelo recomendado é fato + dimensões.

---

## Relacionamentos do Modelo

- `fact_despesas_2023_2024.ideCadastro` → `dim_deputado.ideCadastro` (muitos-para-um)
- `fact_despesas_2023_2024.datEmissao` → `dim_tempo.data` (muitos-para-um)
- `fact_despesas_2023_2024.chaveSubCota` → `dim_subcota.chaveSubCota` (muitos-para-um)

Diagrama em Mermaid:

```mermaid
erDiagram
    FACT_DESPESAS_2023_2024 {
        int ideDocumento
        int ideCadastro
        string chaveSubCota
        date datEmissao
        int numAno
        int numMes
        int origemAno
        float vlrDocumento
        float vlrGlosa
        float vlrLiquido
        float vlrRestituicao
    }

    DIM_DEPUTADO {
        int ideCadastro
        string nome
        string nomeCivil
        string siglaSexo
        date dataNascimento
        date dataFalecimento
        string ufNascimento
        string municipioNascimento
    }

    DIM_TEMPO {
        date data
        int ano
        int mes
        int dia
        string ano_mes
        int trimestre
    }

    DIM_SUBCOTA {
        string chaveSubCota
        int numSubCota
        string txtDescricao
        int numEspecificacaoSubCota
        string txtDescricaoEspecificacao
    }

    DIM_DEPUTADO ||--o{ FACT_DESPESAS_2023_2024 : "ideCadastro"
    DIM_TEMPO   ||--o{ FACT_DESPESAS_2023_2024 : "data = datEmissao"
    DIM_SUBCOTA ||--o{ FACT_DESPESAS_2023_2024 : "chaveSubCota"
