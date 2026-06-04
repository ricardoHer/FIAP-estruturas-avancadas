# FIAP-estruturas-avancadas — Glossário de Domínio

> Termos e conceitos usados neste serviço e seus significados no contexto do negócio.
> Use este glossário ao ler o código, escrever tickets ou comunicar com outros times.

## Termos de Negócio

### Agrotech
**Definição:** Segmento de startups que desenvolvem/adaptam tecnologias para o setor agropecuário (inclui softwares e ferramentas para apoio ao produtor).
**No código:** Presente apenas no `README.md` como contexto do problema (não há classe/enum específica no algoritmo).
**Não confundir com:** “Agroindústria” (cadeia produtiva) ou “tecnologia agrícola” (termo amplo sem foco em startups/soluções).

---

### Perda na colheita de cana-de-açúcar
**Definição:** Parcela da produção que é desperdiçada durante a colheita, calculada por método de colheita (manual vs máquinas).
**No código:** Calculada no `main.py` aplicando percentuais fixos sobre a **produção mensal**:
- manual: 5%
- máquinas: 15%
**Não confundir com:** “Desperdício” como custo financeiro (aqui é uma parcela de massa em toneladas).

---

### Produção mensal (toneladas)
**Definição:** Quantidade de cana colhida informada para cada mês do ano, utilizada como base para projetar perdas.
**No código:** Entrada coletada no `main.py` para 12 meses (valores positivos inteiros ou decimais).
**Não confundir com:** “Produção anual” (soma consolidada; a produção mensal é a granularidade de entrada).

---

### Colheita manual (projeção de perda)
**Definição:** Cenário de colheita em que se assume perda equivalente a 5% da produção mensal informada.
**No código:** Percentual constante aplicado no `main.py` para calcular a perda projetada mensal e os totais anuais.
**Não confundir com:** perda real histórica (o serviço projeta, não mede).

---

### Colheita com máquinas (projeção de perda)
**Definição:** Cenário de colheita em que se assume perda equivalente a 15% da produção mensal informada.
**No código:** Percentual constante aplicado no `main.py` para calcular a perda projetada mensal e os totais anuais.
**Não confundir com:** “eficiência operacional” (métrica diferente; aqui o foco é percentual de perda em massa).

---

## Termos Técnicos do Domínio

### MonthlyHarvestInput
**Definição:** Representação da entrada do algoritmo para as toneladas colhidas em um mês específico do ano.
**No código:** Conceito usado na coleta sequencial de entradas em `main.py` (12 valores, um por mês), validando que sejam positivos e numéricos (inteiro/decimal).
**Não confundir com:** DTO genérico de qualquer sistema — aqui o contexto é especificamente a massa colhida por mês.

---

### AnnualReportTotals
**Definição:** Totais consolidados do ano para:
- colheita total (soma das 12 produções mensais)
- perdas projetadas por método (manual e máquinas), também consolidadas ao final dos 12 meses
**No código:** Estrutura/variáveis acumuladoras no `main.py` usadas para exibir os totais anuais após o loop pelos 12 meses.
**Não confundir com:** relatório detalhado mensal (o mensal é calculado/exibido durante o processamento).

---

### Perda projetada (mensal)
**Definição:** Quantidade de toneladas perdidas em um mês, estimada como percentual fixo da produção mensal para um cenário de colheita (manual ou máquinas).
**No código:** `main.py` — cálculo para cada mês usando o valor de **produção mensal** e os percentuais (5% e 15%).
**Não confundir com:** perda cumulativa (somatório anual).

---

### Totais anuais consolidados
**Definição:** Resultado agregado ao final do processamento de 12 meses contendo:
- colheita total do ano
- perda total projetada (manual)
- perda total projetada (máquinas)
**No código:** `main.py` — acumuladores somando ao longo de 12 meses e exibindo no final.
**Não confundir com:** projeção sem agregação (o serviço consolida).

---

### Validação de entrada de toneladas
**Definição:** Regra de consistência aplicada ao valor informado pelo usuário para cada mês:
- deve ser numérico (inteiro ou decimal)
- deve ser **positivo** (não aceita zero/negativo)
- se houver erro/entrada negativa, o serviço solicita novamente e emite mensagem de validação
**No código:** `main.py` — lógica de validação durante a leitura sequencial dos 12 meses.
**Não confundir com:** validação de formato textual (a validação aqui é de valor numérico positivo).

---

## Acrônimos e Abreviações

| Sigla | Significado | Contexto |
|---|---|---|
| PREENCHER | PREENCHER | PREENCHER |