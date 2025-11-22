# README – Modelo de Dados Preparado para Power BI

Este repositório contém os **datasets preparados** a partir das bases brutas:

- `Ano-2023.csv`
- `Ano-2024.csv`
- `Deputados.csv`

O objetivo desta etapa é cumprir a fase de **Preparação de Dados (CRISP-DM)**, gerando um modelo consistente e integrado para construção de um **dashboard em Power BI**.

A partir dos arquivos originais, foram criadas novas tabelas em formato CSV, já limpas e integradas, organizadas em um **modelo dimensional (esquema em estrela)**:

- **Tabela fato**
  - `fact_despesas_2023_2024`
- **Tabelas dimensão**
  - `dim_deputado`
  - `dim_tempo`
  - `dim_subcota`
- **Tabela auxiliar (desnormalizada)**
  - `fact_despesas_2023_2024_com_deputado` (opcional, para análises rápidas)

---

## 1. Visão Geral do Modelo

O modelo foi construído para:

- Integrar as despesas de 2023 e 2024 em uma única tabela fato;
- Enriquecer os registros de despesa com informações dos deputados;
- Padronizar datas, CPFs, códigos de subcota e tipos de dados;
- Facilitar a criação de medidas e visuais no Power BI.

O **nível de detalhe (grain)** da tabela fato é:

> **Uma linha = um registro de despesa (documento/linha de reembolso) de um deputado em um determinado dia.**

As dimensões permitem analisar as despesas por:

- **Deputado** (nome, sexo, local de nascimento, etc.);
- **Tempo** (dia, mês, ano, trimestre);
- **Tipo de despesa** (subcota e especificação).

---

## 2. Tabela Fato: `fact_despesas_2023_2024`

### 2.1. Descrição

Tabela central do modelo. Contém todas as despesas da Cota Parlamentar dos Deputados para os anos de **2023 e 2024**, já unificadas e limpas.

### 2.2. Finalidade

- Servir de base para as medidas de valor financeiro (soma, médias, comparações);
- Ser o ponto de ligação com as dimensões:
  - Deputado (`dim_deputado`);
  - Tempo (`dim_tempo`);
  - Subcota (`dim_subcota`).

### 2.3. Principais campos

**Chaves e identificação**

- `ideDocumento` – identificador do documento de despesa.
- `ideCadastro` – identificador do deputado (FK → `dim_deputado.ideCadastro`).
- `nuDeputadoId` – identificador alternativo do deputado (não usado como chave no modelo, apenas para referência).
- `nuCarteiraParlamentar` – identificador adicional do parlamentar.
- `chaveSubCota` – chave textual da subcota, formada por `numSubCota` + `numEspecificacaoSubCota`  
  (FK → `dim_subcota.chaveSubCota`).

**Tempo**

- `datEmissao` – **data** de emissão do documento (FK → `dim_tempo.data`).
- `datPagamentoRestituicao` – data de pagamento ou restituição (pode ser vazia).
- `numAno` – ano de referência da despesa.
- `numMes` – mês de referência da despesa.
- `origemAno` – ano de origem do arquivo bruto (`2023` ou `2024`).

**Valores monetários**

- `vlrDocumento` – valor total do documento.
- `vlrGlosa` – valor glosado (não aceito).
- `vlrLiquido` – valor líquido reembolsado.
- `vlrRestituicao` – valor restituído ao erário (quando houver).

> Observação: valores negativos são mantidos, pois representam ajustes, estornos ou correções.

**Classificação da despesa**

- `numSubCota` – código numérico da subcota.
- `txtDescricao` – descrição da subcota.
- `numEspecificacaoSubCota` – código numérico da especificação da subcota.
- `txtDescricaoEspecificacao` – descrição da especificação da subcota (pode estar vazia).

**Atributos de análise**

- `txNomeParlamentar` – nome parlamentar exibido nas notas.
- `sgUF` – sigla da unidade da federação do deputado.
- `sgPartido` – sigla do partido.
- `txtFornecedor` – nome do fornecedor.
- `txtCNPJCPF` – CNPJ/CPF do fornecedor (string).
- `cpf` – CPF do deputado, formatado como string com 11 dígitos (quando disponível).
- `txtPassageiro` – nome do passageiro (para despesas de passagem).
- `txtTrecho` – trecho de viagem (ida/volta, origem/destino).
- `urlDocumento` – link para o PDF do documento de despesa.

---

## 3. Dimensão de Deputado: `dim_deputado`

### 3.1. Descrição

Tabela de dimensão contendo atributos dos deputados obtidos a partir do dataset `Deputados.csv`.

### 3.2. Finalidade

- Permitir análises de despesas por:
  - deputado,
  - sexo,
  - local de nascimento,
  - período de legislatura, etc.
- Armazenar atributos relativamente estáveis (não variam linha a linha na tabela fato).

### 3.3. Grain

> Uma linha = um deputado (identificado por `ideCadastro`).

### 3.4. Principais campos

**Chave**

- `ideCadastro` – chave primária da dimensão, extraída da parte numérica final do campo `uri`.  
  Relaciona-se com `fact_despesas_2023_2024.ideCadastro`.

**Identificação**

- `nome` – nome público/curto do deputado.
- `nomeCivil` – nome civil completo.

**Legislatura**

- `idLegislaturaInicial` – primeira legislatura do deputado.
- `idLegislaturaFinal` – última legislatura registrada.

**Dados demográficos**

- `siglaSexo` – sexo do deputado (`M`, `F`).
- `dataNascimento` – data de nascimento.
- `dataFalecimento` – data de falecimento (quando aplicável, geralmente vazia).
- `ufNascimento` – UF de nascimento.
- `municipioNascimento` – município de nascimento.

**Web / contato**

- `uri` – endereço do recurso na API de dados abertos da Câmara (identifica o deputado na origem).
- `urlRedeSocial` – URLs de redes sociais (quando disponíveis).
- `urlWebsite` – website pessoal (quando disponível).

**CPF**

- `cpf` – CPF do deputado como string (neste dataset específico, o campo é majoritariamente vazio, mas mantido por consistência de schema).

---

## 4. Dimensão de Tempo: `dim_tempo`

### 4.1. Descrição

Tabela de calendário gerada automaticamente a partir do intervalo de datas existente em `fact_despesas_2023_2024.datEmissao`, contendo uma linha por dia.

### 4.2. Finalidade

- Centralizar informações de tempo para análise de séries temporais;
- Servir como **tabela de datas oficial** no Power BI (pode ser marcada como “Table of Dates”).

### 4.3. Grain

> Uma linha = uma data do calendário.

### 4.4. Principais campos

- `data` – chave primária da dimensão (tipo data).  
  Relaciona-se com `fact_despesas_2023_2024.datEmissao`.
- `ano` – ano (ex.: 2023).
- `mes` – número do mês (1–12).
- `dia` – dia do mês (1–31).
- `ano_mes` – representação “YYYY-MM” (ex.: `2023-05`).
- `trimestre` – trimestre (1–4).

---

## 5. Dimensão de Subcota: `dim_subcota`

### 5.1. Descrição

Tabela de dimensão com a classificação das despesas, a partir da combinação de **subcota** e **especificação** existentes na tabela fato.

### 5.2. Finalidade

- Analisar as despesas por tipo de gasto:
  - categoria principal (subcota),
  - detalhamento (especificação).
- Reduzir redundância de textos descritivos na tabela fato.

### 5.3. Grain

> Uma linha = uma combinação (`numSubCota`, `numEspecificacaoSubCota`).

### 5.4. Principais campos

- `chaveSubCota` – chave textual da dimensão  
  (formada por `numSubCota` + `numEspecificacaoSubCota`, ex.: `"13-00"`).  
  Relaciona-se com `fact_despesas_2023_2024.chaveSubCota`.
- `numSubCota` – código da subcota.
- `txtDescricao` – descrição da subcota.
- `numEspecificacaoSubCota` – código da especificação.
- `txtDescricaoEspecificacao` – descrição da especificação (pode ser vazia para subcotas sem detalhamento).

---

## 6. Tabela Auxiliar: `fact_despesas_2023_2024_com_deputado`

### 6.1. Descrição

Tabela desnormalizada, derivada da junção de:

- `fact_despesas_2023_2024`  
  com  
- `dim_deputado`

usando o campo `ideCadastro`.

### 6.2. Finalidade

- Facilitar análises rápidas (por exemplo, em testes ou ferramentas simplificadas);
- Verificar a consistência dos dados (ex.: conferência visual de despesas e atributos de deputado na mesma linha).

> Em um modelo dimensional bem organizado, recomenda-se utilizar `fact_despesas_2023_2024` + dimensões, e considerar esta tabela como apoio/diagnóstico.

---

## 7. Esquema do Modelo (Mermaid)

Abaixo está um diagrama do modelo em notação Mermaid.  
Se o README estiver em um repositório GitHub, GitLab ou for visualizado em um preview com suporte a Mermaid, o diagrama será renderizado automaticamente.

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
