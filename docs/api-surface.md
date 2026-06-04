# FIAP-estruturas-avancadas — Superfície de API

## Visão Geral
- **Tipo:** PREENCHER (não há API HTTP/GraphQL/gRPC documentada no repositório; o projeto aparenta ser um **script de console** em Python)
- **Base URL:** PREENCHER
- **Autenticação:** sem auth (não aplicável ao script de console)
- **Formato:** PREENCHER (o comportamento é de **entrada via console**, não por JSON)

> Observação: com base no contexto acumulado, **não existem endpoints** expostos por rede. O “contrato” funcional é a interação de entrada/validação e o cálculo de totais.

## Endpoints
Não aplicável (PREENCHER: não há endpoints documentados).

---

## Autenticação e Autorização
- **Não aplicável:** o sistema roda como **aplicação de console** (script único `main.py`), sem autenticação/roles.

---

## Rate Limiting
- **Não aplicável:** execução local/console.

---

## Versionamento
- **Não aplicável:** não há API versionada (apenas execução de script).

---

## Contrato funcional (interação de console) — equivalente à “API”
Embora não exista API de rede, o algoritmo define um contrato de entrada e saída consistente com as regras de negócio.

### Entrada: toneladas colhidas por mês (12 meses)
**Descrição:** Solicita ao usuário as toneladas colhidas em cada mês do ano e valida que os valores sejam **apenas positivos** (inteiro ou decimal). Em caso de valor negativo, rejeita e solicita novamente com mensagem de validação.

**Regras de validação (requisito):**
- Aceitar **somente números positivos** (inteiro ou decimal)
- **Rejeitar negativos**
- Ao ocorrer erro, **solicitar novamente** e emitir mensagem de validação
- (Condição não explicitada): não informado se **zero** é aceito como válido; como a regra diz “positivos”, pode haver rejeição de `0`. **PREENCHER** a regra exata para zero caso o código trate diferente.

**Exemplo de inputs esperados (12 valores):**
- `Mês 1: <número positivo>`
- …
- `Mês 12: <número positivo>`

### Cálculo: perdas projetadas
**Descrição:** Para cada mês, calcula as perdas usando percentuais fixos:
- Perda por **colheita manual:** 5% da produção mensal
- Perda por **colheita com máquinas:** 15% da produção mensal

**Cálculos mensais (para um mês com `t` toneladas):**
- `perda_manual_mensal = t * 0.05`
- `perda_maquinas_mensal = t * 0.15`

### Saída: valores mensais e totais anuais
**Descrição:** Exibe:
- valores mensais (produção e perdas projetadas por método)
- totais consolidados do ano (soma da produção e das perdas manual e por máquinas)

**Entidades (conforme análise de domínio):**
- **MonthlyHarvestInput:** toneladas colhidas em um mês (entrada)
- **AnnualReportTotals:** totais consolidados do ano:
  - **colheita total** (soma das 12 produções)
  - **perdas projetadas manual** (soma das 12 perdas manuais)
  - **perdas projetadas máquinas** (soma das 12 perdas por máquinas)

### Erros comuns (equivalentes)
| Situação | Quando ocorre |
|---|---|
| PREENCHER (erro de validação) | Usuário informa toneladas **negativas**; o programa deve rejeitar e solicitar novamente |
| PREENCHER (erro de parse) | Usuário informa valor que não é numérico (ex.: texto). **PREENCHER** se o código trata isso e qual mensagem exata |

> Status HTTP: **não aplicável** (não existe camada HTTP). Os “erros comuns” acima são os equivalentes funcionais previstos pelas regras (validação de negativos e de formato numérico).

---

## Notas de implementação (impacto na “API de console”)
- **Entrada:** sequência de 12 solicitações no `main.py` (um valor por mês)
- **Sem persistência/requisições externas:** cálculo em memória, sem integrações e sem chamadas de rede
- **Parâmetros fixos do domínio:** percentuais de perda **5% (manual)** e **15% (máquinas)** definidos no algoritmo

---

> ⚠️ Rascunho gerado automaticamente pelo Alicerce by Malha. Valide os contratos com o código/OpenAPI spec antes de mergear.