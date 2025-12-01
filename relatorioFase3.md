# RELATÓRIO CRISP-DM – FASE 2 E FASE 3

## Análise de Padrões e Eficiência dos Gastos Parlamentares da Câmara dos Deputados (2023–2024)

**Disciplina:** Coleta, Preparação e Análise de Dados  
**Professor:** Lucas Rafael Costella Pessutto  
**Semestre:** 2025/2  
**Equipe:** Victor Closs Duarte, Pedro Augusto Wagner, Leonardo Lersch Forner, Diego Prestes Graudenz

---

## SUMÁRIO EXECUTIVO

Este relatório consolida as fases de **Compreensão dos Dados (Fase 2)** e **Preparação dos Dados (Fase 3)**, aplicadas aos dados de gastos parlamentares da Câmara dos Deputados, com foco na Cota para o Exercício da Atividade Parlamentar (CEAP) no período de 2023 a 2024.

A partir do feedback da Fase 1, o escopo foi ajustado para tornar o projeto mais específico e viável:

- Período analisado: **2023–2024** (24 meses)  
- Escopo de despesas: quatro categorias principais  
- Questão de pesquisa: padrões de eficiência e consistência em categorias selecionadas, considerando variáveis de contexto (região e tamanho do estado)

Situação das fases:

- Fase 1 – Compreensão do Negócio: concluída  
- Fase 2 – Compreensão dos Dados: concluída  
- Fase 3 – Preparação dos Dados: concluída (fase final do projeto)

---

## 1. REVISÃO E REFINAMENTO DA FASE 1

### 1.1 Ajustes no Escopo do Projeto

Com base no retorno sobre o escopo original, considerou-se que a proposta inicial era ampla demais para o tempo disponível e para o nível de detalhamento desejado.

**Escopo original (Fase 1):**

- Período: 2022–2025 (4 anos completos)  
- Todas as categorias de despesas  
- Todos os 513 deputados  
- Vários objetivos simultâneos

**Escopo refinado (Fase 2):**

- Período: 2023–2024 (24 meses)  
- Categorias selecionadas:
  1. Combustíveis e lubrificantes  
  2. Passagens aéreas  
  3. Divulgação da atividade parlamentar  
  4. Consultoria, pesquisa e trabalhos técnicos  

- Questão de pesquisa:  
  *Quais são os padrões de eficiência e consistência nos gastos com combustíveis, passagens aéreas, divulgação parlamentar e consultorias entre os deputados federais no período 2023–2024, considerando variáveis contextuais como região geográfica e tamanho do estado?*

### 1.2 Justificativa do Refinamento

O escopo refinado foi adotado pelos seguintes motivos:

1. **Viabilidade temporal:** 24 meses permitem observar padrões consistentes, sem extrapolar demais o período de análise.  
2. **Profundidade analítica:** quatro categorias específicas possibilitam explorar melhor o comportamento em cada tipo de despesa.  
3. **Relevância pública:** as categorias escolhidas são recorrentes no debate público sobre uso de recursos.  
4. **Contexto estável:** o período não inclui eleição geral para o Legislativo federal, reduzindo interferências de calendário eleitoral.  
5. **Viabilidade técnica:** o volume de dados resultante é significativo, mas manejável para o contexto da disciplina.

---

## 2. COMPREENSÃO DOS DADOS (FASE 2)

### 2.1 Coleta de Dados

#### 2.1.1 Fontes de Dados

- Fonte: Portal de Dados Abertos da Câmara dos Deputados  
- Endereço: https://dadosabertos.camara.leg.br/

**Datasets utilizados:**

| Dataset             | Formato | Período       | Tamanho            | Status    |
|---------------------|---------|---------------|--------------------|-----------|
| Gastos CEAP 2023    | .csv    | Jan–Dez/2023  | 232.000 registros  | Utilizado |
| Gastos CEAP 2024    | .csv    | Jan–Dez/2024  | 231.908 registros  | Utilizado |
| Dados dos Deputados | .json   | Atual         | 513 deputados      | Utilizado |

Total de transações analisadas (após filtro das quatro categorias): **332.094** registros.

---

### 2.2 Análise Exploratória de Dados (EDA)

#### 2.2.1 Estatísticas Descritivas Gerais

**Volume de dados (2023–2024):**

- Total de transações: **332.094**  
- Deputados únicos: **818**  
- Fornecedores únicos: **22.274**  
- Período efetivo de emissão: **01/01/2023** a **31/12/2024**

**Distribuição temporal (dados filtrados):**

- 2023: **154.613** transações (46,6%)  
- 2024: **177.481** transações (53,4%)  
- Média aproximada: **13.837** transações por mês  

---

#### 2.2.2 Análise das Categorias Selecionadas

##### 2.2.2.1 Combustíveis e Lubrificantes

| Métrica                 | Valor               |
|-------------------------|---------------------|
| Total de transações     | 142.080             |
| Valor total             | R$ 2.969.627.948,00 |
| Média por transação     | R$ 20.901,10        |
| Mediana por transação   | R$ 17.204,50        |
| Desvio padrão           | R$ 51.435,07        |
| Valor mínimo            | R$ 6,00             |
| Valor máximo            | R$ 938.991,00       |
| Coeficiente de variação | 246,10%             |

A mediana é inferior à média e o coeficiente de variação é elevado, indicando forte dispersão e assimetria à direita: poucos valores muito altos influenciam a média, enquanto a maior parte das transações se concentra em faixas menores.

---

##### 2.2.2.2 Passagens Aéreas

| Métrica                 | Valor                |
|-------------------------|----------------------|
| Total de transações     | 96.620               |
| Valor total             | R$ 10.006.513.515,00 |
| Média por transação     | R$ 103.565,65        |
| Mediana por transação   | R$ 124.522,00        |
| Desvio padrão           | R$ 74.430,93         |
| Valor mínimo            | R$ 1,00              |
| Valor máximo            | R$ 962.498,00        |
| Coeficiente de variação | 71,90%               |

Trata-se da categoria com maior volume financeiro total. A dispersão é relevante, mas menor que a de Combustíveis. A mediana superior à média sugere distribuição levemente assimétrica à esquerda.

---

##### 2.2.2.3 Divulgação da Atividade Parlamentar

| Métrica                 | Valor                |
|-------------------------|----------------------|
| Total de transações     | 72.941               |
| Valor total             | R$ 2.650.270.965,00  |
| Média por transação     | R$ 36.334,45         |
| Mediana por transação   | R$ 5.000,00          |
| Desvio padrão           | R$ 105.676,75        |
| Valor mínimo            | R$ 6,00              |
| Valor máximo            | R$ 999.998,00        |
| Coeficiente de variação | 290,80%              |

A diferença entre média e mediana destaca a existência de muitas transações de baixo valor e poucas transações de valor muito elevado, que aumentam significativamente a variabilidade.

---

##### 2.2.2.4 Consultoria, Pesquisa e Trabalhos Técnicos

| Métrica                 | Valor              |
|-------------------------|--------------------|
| Total de transações     | 133                |
| Valor total             | R$ 2.005.350,00    |
| Média por transação     | R$ 15.077,82       |
| Mediana por transação   | R$ 10.000,00       |
| Desvio padrão           | R$ 19.539,97       |
| Valor mínimo            | R$ 650,00          |
| Valor máximo            | R$ 145.593,00      |
| Coeficiente de variação | 129,60%            |

É a categoria com menor volume de registros e menor impacto no total de gastos, mas ainda com alta dispersão relativa, sugerindo concentração de valores em alguns contratos específicos.

---

#### 2.2.3 Análise por Região Geográfica

Gasto médio total por deputado (valores aproximados em reais):

| Região        | Combustível | Passagens    | Divulgação   | Consultoria | Total médio      |
|--------------|-------------|-------------:|-------------:|------------:|-----------------:|
| Norte        | 216.074,23  | 872.291,13   | 104.880,89   | 461,62      | 1.193.707,86     |
| Nordeste     | 245.705,49  | 866.609,55   | 171.370,62   | 134,75      | 1.283.820,41     |
| Centro-Oeste | 262.078,55  | 294.401,64   | 208.358,18   | 172,18      | 765.010,54       |
| Sudeste      | 211.984,67  | 831.302,25   | 257.667,70   | 106,93      | 1.301.061,55     |
| Sul          | 306.898,98  | 889.264,73   | 296.845,58   | 89,52       | 1.493.098,82     |

As regiões mais distantes de Brasília tendem a apresentar valores médios mais elevados em Passagens Aéreas. O Centro-Oeste, por estar mais próximo da capital, apresenta o menor gasto médio total por deputado. A região Sul tem o maior total médio, impulsionada por Combustíveis e Divulgação.

---

#### 2.2.4 Análise Temporal (2023 vs 2024)

Evolução dos gastos totais por categoria:

| Categoria   | 2023 Total              | 2024 Total (12 meses)    | Variação % |
|------------|-------------------------|--------------------------|-----------:|
| Combustível| R$ 1.416.362.621,00     | R$ 1.553.265.327,00      | +9,7%      |
| Passagens  | R$ 5.227.617.427,00     | R$ 4.778.896.088,00      | -8,6%      |
| Divulgação | R$ 1.277.509.806,00     | R$ 1.372.761.159,00      | +7,5%      |
| Consultoria| R$ 2.005.350,00         | R$ 0,00                  | -100,0%    |

Observa-se aumento em Combustível e Divulgação e redução em Passagens Aéreas na comparação entre 2023 e 2024. Consultoria aparece apenas em 2023 no recorte adotado.

---

#### 2.2.5 Detecção Preliminar de Outliers

Contagem de outliers por categoria (método do intervalo interquartil – IQR):

| Categoria   | Outliers | % do total |
|------------|---------:|-----------:|
| Combustível| 3.189    | 2,24%      |
| Passagens  | 525      | 0,54%      |
| Divulgação | 10.583   | 14,51%     |
| Consultoria| 5        | 3,76%      |

A proporção de outliers em Divulgação reforça a alta variabilidade da categoria. A presença de outliers indica pontos que exigem análise contextual e cuidado na interpretação de médias e comparações.

---

### 2.3 Qualidade dos Dados

#### 2.3.1 Completude

Campos com maior incidência de valores ausentes:

| Campo                     | Ausentes | % Missing | Impacto |
|---------------------------|---------:|----------:|--------:|
| txtDescricaoEspecificacao | 189.985  | 57,21%    | Médio   |
| cnpj_cpf                  | 113.352  | 34,13%    | Médio   |

A completude em campos críticos (identificadores de parlamentar e valores monetários) é boa. Os campos com maior percentual de ausência referem-se a detalhes complementares.

---

#### 2.3.2 Consistência

Verificações realizadas:

1. Relação `vlrLiquido = vlrDocumento - vlrGlosa` respeitada na maior parte dos registros, com exceções associadas a lançamentos negativos e ajustes.  
2. Categorias de despesa compatíveis com a estrutura da CEAP, ainda que o dado original traga mais categorias que as quatro selecionadas para o projeto.  
3. Não foi realizada validação completa de CNPJs ou unificação de fornecedores, por não ser requisito central para o objetivo deste estudo.

---

#### 2.3.3 Duplicatas

- Duplicatas identificadas: 12 registros (aproximadamente 0,00% do total).  
- Esses casos foram interpretados como possíveis duplicações de lançamento ou reembolsos duplicados. A decisão específica de exclusão ou manutenção é documentada na fase de preparação, junto com as demais escolhas de limpeza.

---

#### 2.3.4 Distribuições

Teste de normalidade (Shapiro–Wilk) para valores de cada categoria:

| Categoria   | Estatística W | p-valor  | Conclusão  |
|------------|---------------|----------|-----------:|
| Combustível| 0,284         | < 0,001  | Não-normal |
| Passagens  | 0,896         | < 0,001  | Não-normal |
| Divulgação | 0,353         | < 0,001  | Não-normal |
| Consultoria| 0,515         | < 0,001  | Não-normal |

Todas as categorias apresentam distribuições que se afastam da normalidade, o que levou à preferência por medidas robustas (como a mediana) e à opção por testes não paramétricos na análise estatística.

---

#### 2.3.5 Correlações Preliminares

Correlação de Spearman entre gastos totais por deputado:

|            | Combustível | Passagens | Divulgação | Consultoria |
|------------|------------:|----------:|-----------:|------------:|
| Combustível| 1,00        | 0,00      | -0,02      | -0,09       |
| Passagens  | 0,00        | 1,00      | -0,06      | 0,01        |
| Divulgação | -0,02       | -0,06     | 1,00       | -0,10       |
| Consultoria| -0,09       | 0,01      | -0,10      | 1,00        |

As correlações são baixas, indicando que altos gastos em uma categoria não implicam necessariamente altos gastos em outra. Isso sugere perfis de gasto distintos entre deputados.

---

### 2.4 Problemas Identificados

| Problema                   | Severidade | Registros afetados | Estratégia adotada                         |
|----------------------------|-----------:|--------------------:|--------------------------------------------|
| Valores negativos          | Média      | 20.254              | Manter e interpretar como ajustes/estornos |
| Campos de detalhe ausentes | Média      | > 100.000           | Manter, focando em campos principais       |

---

## 3. PREPARAÇÃO DOS DADOS (FASE 3)

Esta fase descreve o que foi feito para transformar as bases originais em um conjunto de dados pronto para análise e para a construção de dashboards em Power BI. As atividades incluíram limpeza, padronização, criação de atributos, geração de tabelas derivadas e integração entre as diferentes fontes.

### 3.1 Limpeza dos dados

Foram utilizadas três bases principais:

- `Ano-2023.csv` – despesas da cota parlamentar em 2023  
- `Ano-2024.csv` – despesas da cota parlamentar em 2024  
- `Deputados.csv` – cadastro de deputados (dados pessoais e de legislatura)

As principais ações de limpeza foram:

**Padronização de codificação e texto**

- Leitura com `encoding="utf-8-sig"` e separador `";"`, garantindo acentuação correta.  
- Remoção de espaços em branco no início e no fim de valores textuais, reduzindo problemas de duplicidade por formatação.

**Ajuste de tipos**

- Identificadores numéricos (`ideCadastro`, `nuCarteiraParlamentar`, `numRessarcimento`, `nuDeputadoId`, `ideDocumento`) convertidos para inteiros com suporte a valores ausentes.  
- Campo `cpf` nas despesas convertido para string com 11 dígitos (zeros à esquerda quando necessário).  
- Datas (`datEmissao`, `datPagamentoRestituicao` em despesas; `dataNascimento`, `dataFalecimento` em deputados) convertidas para tipo data.  
- Medidas monetárias (`vlrDocumento`, `vlrGlosa`, `vlrLiquido`, `vlrRestituicao`) convertidas para tipo numérico, com entradas inválidas tratadas como nulas.

**Tratamento de valores faltantes**

- Campos naturalmente não aplicáveis a todas as linhas, como `txtPassageiro`, `txtTrecho`, `txtDescricaoEspecificacao`, `datPagamentoRestituicao` e `vlrRestituicao`, foram mantidos como nulos quando ausentes.  
- Em `Deputados.csv`, campos como `dataFalecimento`, `urlRedeSocial`, `urlWebsite` e `cpf` foram mantidos mesmo com alta taxa de ausência, por se tratar de informação complementar e não obrigatória para os objetivos centrais.

**Valores negativos**

- Valores negativos em `vlrDocumento` e `vlrLiquido` foram mantidos, pois refletem ajustes, estornos ou restituições. Esses registros foram considerados nas estatísticas e análises, com a devida atenção ao interpretar resultados agregados.

**Seleção de features**

- Nas despesas, foram preservadas as colunas necessárias à análise e à construção das chaves de relacionamento.  
- Na base de deputados, o campo `cpf` foi mantido por consistência, apesar da ausência quase total de valores.

---

### 3.2 Criação de atributos e registros

Além da limpeza, foram criados novos atributos e tabelas derivadas que estruturam o modelo de dados em formato dimensional.

**Novos atributos na tabela de despesas**

- `origemAno`: indica o ano do arquivo de origem (2023 ou 2024), auxiliando na rastreabilidade e em comparações.  
- `chaveSubCota`: chave textual combinando `numSubCota` e `numEspecificacaoSubCota` no formato `"NN-MM"`, utilizada como chave estrangeira para a dimensão de subcotas.  
- Datas normalizadas: `datEmissao` e `datPagamentoRestituicao` convertidas para datas puras, prontas para relacionamento com a dimensão de tempo.

**Novos atributos na tabela de deputados**

- `ideCadastro` padronizado: extraído da parte numérica final do campo `uri`, adotado como chave primária de `dim_deputado` e chave estrangeira na tabela fato.  
- Datas normalizadas (`dataNascimento`, `dataFalecimento`): convertidas para tipo data.

**Tabelas derivadas**

- `fact_despesas_2023_2024`: união das despesas de 2023 e 2024 em uma única tabela fato, já limpa e padronizada; cada linha representa um lançamento de despesa.  
- `dim_deputado`: dimensão com uma linha por deputado, contendo atributos pessoais e de legislatura.  
- `dim_tempo`: dimensão calendário, construída a partir do menor e maior valor de `datEmissao`, com uma linha por data e atributos derivados (ano, mês, dia, ano-mês, trimestre).  
- `dim_subcota`: dimensão com as combinações distintas de subcota e especificação, com descrições textuais associadas.  
- `fact_despesas_2023_2024_com_deputado`: versão desnormalizada da fato com junção à `dim_deputado` via `ideCadastro`, utilizada para inspeção e validação.

---

### 3.3 Integração de dados

A integração consolidou as despesas de 2023 e 2024 e conectou os registros aos dados dos deputados em um modelo em estrela.

**Integração das bases de despesas (2023 e 2024)**

- `Ano-2023.csv` e `Ano-2024.csv` possuem o mesmo layout. Após a limpeza, foram concatenadas para formar `fact_despesas_2023_2024`.  
- O campo `numAno` diferencia o ano de referência, enquanto `origemAno` registra o arquivo fonte.  
- Não foram identificadas duplicidades relevantes entre anos, o que dispensou deduplicação adicional.

**Integração com a base de deputados**

- A base `Deputados.csv` foi utilizada para enriquecer as despesas com atributos dos parlamentares.  
- A chave de junção adotada foi `ideCadastro`, padronizada tanto em `dim_deputado` quanto na tabela de despesas.  
- A junção foi do tipo left join a partir da tabela fato, preservando todos os registros de despesa; quando não há `ideCadastro` válido ou correspondente, os campos da dimensão permanecem vazios.

**Dimensões de apoio**

- `dim_subcota` concentra descrições de subcotas e especificações, reduzindo redundância textual na tabela fato.  
- `dim_tempo` agrupa a lógica de calendário.  
- Com isso, a tabela fato fica mais focada em chaves e medidas, enquanto as dimensões armazenam os atributos descritivos.

---

### 3.4 Descrição do dataset final

Após o pré-processamento, o modelo de dados resultante está estruturado em formato dimensional (esquema em estrela), composto por:

- **Tabela fato**  
  - `fact_despesas_2023_2024`  
    - Contém as despesas da cota parlamentar em 2023 e 2024.  
    - Inclui chaves (`ideCadastro`, `chaveSubCota`, `datEmissao`, `ideDocumento`), atributos de contexto (UF, partido, fornecedor, informações de viagem) e medidas numéricas (`vlrDocumento`, `vlrGlosa`, `vlrLiquido`, `vlrRestituicao`).

- **Tabelas dimensão**  
  - `dim_deputado`: uma linha por deputado (`ideCadastro`), com dados pessoais, local de nascimento e intervalo de legislatura.  
  - `dim_tempo`: uma linha por data (`data`), com campos derivados (ano, mês, dia, ano-mês, trimestre).  
  - `dim_subcota`: uma linha por combinação de subcota e especificação (`chaveSubCota`), com descrições textuais das categorias de despesa.

- **Tabela auxiliar**  
  - `fact_despesas_2023_2024_com_deputado`: fato já unida à `dim_deputado`, utilizada para inspeção e conferência de consistência.

Principais relacionamentos:

- `fact_despesas_2023_2024.ideCadastro` → `dim_deputado.ideCadastro`  
- `fact_despesas_2023_2024.datEmissao` → `dim_tempo.data`  
- `fact_despesas_2023_2024.chaveSubCota` → `dim_subcota.chaveSubCota`  

Nesse formato, o conjunto de dados encontra-se limpo, integrado e adequado para a análise e a construção do dashboard final em Power BI.

---

## 4. AUTOCRÍTICA E LIÇÕES APRENDIDAS

### 4.1 Avaliação do Progresso

Pontos positivos identificados pela equipe:

1. Escopo refinado e aderente ao tempo disponível.  
2. Qualidade dos dados analisada de forma consistente.  
3. Análise exploratória detalhada para as categorias selecionadas.  
4. Modelo de dados preparado em formato compatível com ferramentas de BI e aplicado na construção do dashboard.

Desafios encontrados:

1. Volume de dados elevado para determinadas operações.  
2. Interpretação contextual de outliers, especialmente na categoria Divulgação.  
3. Heterogeneidade de fornecedores, que dificulta análises mais finas sem trabalho adicional de padronização.

---

### 4.2 Autoavaliação

A equipe considera que o resultado combinado da Fase 3 é coerente com o planejamento e com os objetivos da disciplina. A exploração dos dados e a preparação do modelo possibilitaram a construção de um dashboard informativo em Power BI, com capacidade de responder à questão de pesquisa proposta e de destacar padrões relevantes de gastos parlamentares, assim é consideramos na nossa autoavaliação a nota 10 para o projeto.

---

## 5. CONCLUSÕES FINAIS

Principais conclusões do projeto:

1. O conjunto de dados filtrado totaliza 332.094 transações, com boa completude em campos-chave e estrutura compatível com análises em nível de deputado, categoria e tempo.  
2. Foram identificados padrões regionais marcantes nos gastos, principalmente em Passagens Aéreas e na comparação entre regiões mais próximas e mais distantes de Brasília.  
3. A categoria Divulgação apresenta a maior variabilidade, com proporção elevada de outliers, o que demanda cautela na interpretação de médias e rankings.  
4. Observa-se aumento de gastos em Combustível e Divulgação e redução em Passagens entre 2023 e 2024, dentro do período analisado.  
5. A preparação de dados resultou em um modelo dimensional com uma tabela fato e três dimensões principais, adequado para a construção de dashboards em Power BI e para a análise da eficiência e consistência dos gastos na CEAP.

---

## ANEXOS

### Anexo A – Dicionário de Dados (resumo)

**Campos principais na tabela fato (exemplos):**

- `txNomeParlamentar`, `ideCadastro`, `sgUF`, `sgPartido`,  
  `txtDescricao`, `txtFornecedor`, `txtCNPJCPF`,  
  `datEmissao`, `vlrDocumento`, `vlrGlosa`, `vlrLiquido`,  
  `numMes`, `numAno`, `chaveSubCota`.

**Campos principais nas dimensões:**

- `dim_deputado`: `ideCadastro`, `nome`, `nomeCivil`, `siglaSexo`, `dataNascimento`, `ufNascimento`, `municipioNascimento`.  
- `dim_tempo`: `data`, `ano`, `mes`, `dia`, `ano_mes`, `trimestre`.  
- `dim_subcota`: `chaveSubCota`, `numSubCota`, `txtDescricao`, `numEspecificacaoSubCota`, `txtDescricaoEspecificacao`.

### Anexo B – Referências

1. Portal de Dados Abertos da Câmara dos Deputados – https://dadosabertos.camara.leg.br/  
2. Documentação da API – https://dadosabertos.camara.leg.br/swagger/api.html  
3. Regulamentação da CEAP – https://www2.camara.leg.br/transparencia/  
4. Metodologia CRISP-DM – Chapman et al. (2000)
