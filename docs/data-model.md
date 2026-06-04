```md
# FIAP-estruturas-avancadas — Modelo de Dados

> ⚠️ Rascunho gerado automaticamente pelo Alicerce by Malha. Valide com o schema real do banco antes de mergear.

## Entidades Principais

### MonthlyHarvestInput
- **Propósito:** Representar a produção (toneladas colhidas) informada para um mês específico do ano, que será base para calcular as perdas projetadas.
- **Campos principais:**
  - **ano** *(int)* — ano do relatório (PREENCHER se existe no script)
  - **mes** *(int 1-12)* — mês da entrada
  - **toneladas_colhidas** *(decimal > 0)* — quantidade de cana colhida no mês (entrada do usuário)
  - **perda_manual_percentual** *(decimal = 0.05)* — percentual fixo aplicado àquele mês
  - **perda_maquinas_percentual** *(decimal = 0.15)* — percentual fixo aplicado àquele mês
  - **perda_manual_toneladas** *(decimal)* — toneladas perdidas estimadas via manual (calculado)
  - **perda_maquinas_toneladas** *(decimal)* — toneladas perdidas estimadas via máquinas (calculado)
  - **created_at** *(PREENCHER — timestamp)* — PREENCHER se persistido
- **Relacionamentos:**
  - **MonthlyHarvestInput** (N) pertence a **AnnualReportTotals** (1) via *(ano)* e/ou *(relatorio_id)* (PREENCHER o identificador exato)
- **Observações:**
  - **Validação de integridade:** rejeitar entradas negativas e valores ≤ 0; ao ocorrer erro, solicitar novamente.
  - **Dominio do campo:** somente números inteiros ou decimais positivos.
  - **Cálculo determinístico:** perdas do mês = `toneladas_colhidas * percentual` (5% manual e 15% máquinas).

### AnnualReportTotals
- **Propósito:** Consolidar os totais do ano: colheita total e perdas projetadas (manual e máquinas), somando os 12 meses.
- **Campos principais:**
  - **ano** *(int)* — ano consolidado
  - **colheita_total_toneladas** *(decimal)* — soma das `toneladas_colhidas` dos 12 meses
  - **perda_manual_total_toneladas** *(decimal)* — soma das `perda_manual_toneladas` dos 12 meses
  - **perda_maquinas_total_toneladas** *(decimal)* — soma das `perda_maquinas_toneladas` dos 12 meses
  - **colheita_total_percentual_perdida_manual** *(PREENCHER — decimal)* — derivado (se for exibido/armazenado)
  - **colheita_total_percentual_perdida_maquinas** *(PREENCHER — decimal)* — derivado (se for exibido/armazenado)
  - **created_at** *(PREENCHER — timestamp)* — PREENCHER se persistido
  - **report_id** *(PREENCHER — UUID/string)* — PREENCHER se existir
- **Relacionamentos:**
  - **AnnualReportTotals** (1) agrega **MonthlyHarvestInput** (N) para o mesmo ano e/ou relatório.
- **Observações:**
  - **Regra de consolidação:** somar ao longo dos 12 meses.
  - **Não há menção de soft delete, auditoria ou versionamento** no repositório descrito.

## Diagrama de Relacionamentos

```mermaid
[AnnualReportTotals] 1---N [MonthlyHarvestInput]
```

> O vínculo exato pode ser por **ano** (se o script apenas consolida por ano) ou por um **report_id/relatorio_id** (PREENCHER).

## Fluxos de Dados Principais

### Coleta de Entrada Mensal (12 meses)
1. **Origem do dado:** interação via console do usuário no `main.py`, solicitando toneladas colhidas mês a mês.
2. **Transformação/validação:**
   - Validar que **toneladas_colhidas** é **numérica** (int/decimal) e **estritamente positiva**.
   - Se for negativa (ou inválida/≤ 0): rejeitar e **solicitar novamente** com mensagem de validação.
   - Aplicar percentuais fixos:
     - perda_manual_toneladas = toneladas_colhidas * 0.05
     - perda_maquinas_toneladas = toneladas_colhidas * 0.15
3. **Persistência / saída:**
   - **Persistência:** PREENCHER (pela descrição, o cálculo ocorre **em memória** e o script só **exibe** os valores).
   - **Saída:** exibir perdas mensais e, ao final, consolidados anuais.

### Consolidação Anual (totais do ano)
1. **Origem do dado:** resultados calculados para os 12 objetos mensais (ou variáveis em memória equivalentes).
2. **Transformação:**
   - Somar:
     - colheita_total_toneladas = Σ toneladas_colhidas(mês)
     - perda_manual_total_toneladas = Σ perda_manual_toneladas(mês)
     - perda_maquinas_total_toneladas = Σ perda_maquinas_toneladas(mês)
3. **Persistência / saída:**
   - **Persistência:** PREENCHER (não descrita).
   - **Saída:** exibir **totais consolidados** do ano.

## Estratégia de Persistência
- **Banco principal:** *Não identificado* — o repositório descrito é um **script monolítico sequencial** em console, aparentemente **sem persistência**.
- **Cache:** não aplicável / não identificado.
- **Event store:** não aplicável / não identificado.

## Considerações de Performance
- Como o processamento é **O(12)** (12 meses fixos) e executado em **memória**, não há necessidade de índices/particionamento.
- Precisão numérica: para toneladas decimais, é recomendado (se houver persistência futura) usar tipo decimal/numérico no banco; no script atual, PREENCHER se há uso de `float` ou `decimal.Decimal`.
```