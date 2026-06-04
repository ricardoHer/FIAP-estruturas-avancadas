# FIAP-estruturas-avancadas — Guia de Onboarding

## O que você precisa saber primeiro
O **FIAP-estruturas-avancadas** é um repositório bem direto: é uma **aplicação em Python no formato de script de console**, com um fluxo **sequencial** de entrada → cálculo → saída. Não existe uma arquitetura em camadas (tipo controllers/services/domain), nem testes/containers; o foco é a implementação do **algoritmo** para o exercício.

O problema de domínio trata de **perdas na colheita de cana-de-açúcar**: você informa a **produção mensal (em toneladas)** de um ano (12 meses) e o script calcula a projeção de desperdício comparando dois métodos:
- **Colheita manual:** perda de **5%** da produção mensal
- **Colheita com máquinas:** perda de **15%** da produção mensal  
Ao final, o script exibe **valores mensais** e **totais anuais consolidados** (colheita total e perdas projetadas para os dois métodos).

A validação de entrada é parte importante do comportamento: **não aceita números negativos** e pede novamente enquanto o valor estiver inválido. O algoritmo também deve rejeitar valores que não sejam numéricos (inteiro ou decimal), garantindo que só **positivos** sejam aceitos como toneladas.

## Como rodar localmente

### Pré-requisitos
- **Python 3.10+** (ou compatível)
  - Instale via:
    - Windows: baixe do site oficial (python.org) e marque “Add Python to PATH”
    - macOS: `brew install python@3.11` (ou versão equivalente)
    - Linux (Debian/Ubuntu): `sudo apt-get update && sudo apt-get install -y python3 python3-pip`

### Passos
```bash
# 1) Clone
git clone <COLOQUE_AQUI_O_URL_DO_REPOSITORIO>
cd FIAP-estruturas-avancadas

# 2) (Opcional) Crie e ative um ambiente virtual
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

# 3) Rode o script
python main.py
```

### Configurações necessárias
> Este repositório, pelo estado acumulado, não descreveu variáveis de ambiente/config. O comportamento depende de input via console.

| Variável | Valor local | Para que serve |
|---|---|---|
| PREENCHER | PREENCHER | PREENCHER |

## Arquitetura em 5 minutos
Pense no projeto como **um único “pipeline”** dentro de `main.py`:

1. **Loop de 12 meses**: para cada mês, o script pede ao usuário as **toneladas colhidas**.
2. **Validação de entrada**:
   - deve aceitar **inteiro/decimal** e ser **> 0**
   - se houver **valor negativo** (ou inválido), ele **exibe mensagem** e **solicita novamente** até o valor ficar correto
3. **Cálculo** (por mês e acumulado):
   - perda_manual_mensal = toneladas * 0.05
   - perda_maquinas_mensal = toneladas * 0.15
   - acumula colheita total e perdas totais
4. **Saída**: imprime os **resultados mensais** (e provavelmente no formato definido pelo script) e, ao final, os **totais do ano**.

Como é tudo “linear”, para entender/alterar regras você normalmente só precisa localizar:
- onde o input do mês é lido
- onde a validação acontece
- onde as perdas são calculadas e somadas
- onde a impressão dos resultados é feita

## Onde está cada coisa
| O que procuro | Onde encontro |
|---|---|
| Ponto de entrada / fluxo do programa | `main.py` |
| Especificação do problema / regras e contexto | `README.md` |
| Regras de perda (5% e 15%) | `main.py` (trecho onde calcula manual/máquinas) |
| Validação (rejeitar negativos e/ou não-numéricos) | `main.py` (função/trecho do input com `try/except` e checks) |

## Fluxos principais para entender primeiro
1. **Entrada mensal + validação** — começa no `main.py` ao pedir toneladas do mês; termina quando o usuário fornece um valor **numérico positivo** (inteiro/decimal) para aquele mês.
2. **Cálculo de perdas e acumulação anual** — começa após cada input mensal válido; termina ao somar colheita total e perdas (manual e máquinas) e, no final do loop de 12 meses, consolidar o relatório anual.
3. **Relatório final de saída** — começa quando o loop termina (após 12 meses); termina ao exibir totais anuais (e, conforme implementado, também os mensais durante o loop).

## Armadilhas comuns
- **Assumir que “0” é válido**: o estado acumulado diz “somente positivos”; então `0` deve ser tratado como inválido **(confirmar no código)** e continuar pedindo. Se o código aceitar `0`, isso conflita com a regra.
- **Validação incompleta para não-números**: se o script só valida “negativo” mas não trata `ValueError` ao converter string para `float`, o comportamento pode quebrar. Procure por `try/except` e reforços de `isinstance/float`.
- **Percentuais aplicados duas vezes**: em scripts simples é comum errar o acumulado (ex.: calcular perdas e depois somar o valor já perdido novamente na colheita total). Garanta que:
  - colheita total soma apenas toneladas “colhidas”
  - perdas totais somam toneladas * percentual
- **Bug de arredondamento/formatção**: cálculos em `float` podem gerar casas decimais “estranhas” na impressão. Se existir, ajuste apenas na apresentação (formatação) e não na lógica.

## Quem perguntar
- **Dúvidas de negócio:** PREENCHER (provavelmente professor/tutor do exercício FIAP ou responsável pelo enunciado)
- **Dúvidas técnicas:** PREENCHER (autor do repositório / time que revisa o `main.py`)

---
> ⚠️ Rascunho gerado automaticamente pelo Alicerce by Malha. Adicione os passos reais de setup antes de mergear.