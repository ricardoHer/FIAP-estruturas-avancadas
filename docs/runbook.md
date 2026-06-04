# FIAP-estruturas-avancadas — Runbook Operacional

## Informações Básicas
| Item | Valor |
|---|---|
| Porta padrão | PREENCHER (script console não expõe porta) |
| Health check | PREENCHER (não há endpoint; ver “Verificar execução” abaixo) |
| Logs | `PREENCHER` (verifique onde o ambiente captura stdout/stderr: terminal, CI, ou arquivo de log) |
| Métricas | PREENCHER (não há métricas/observabilidade nativa no script) |
| Alertas críticos | PREENCHER (não há integração declarada) |

> **Observação importante (console/script):** Como o repositório descreve um **aplicativo de console monolítico (script único) em Python**, “health check”, logs e métricas normalmente estão ligados à **execução (stdout/stderr)** e ao ambiente (CI/servidor/terminal), não a endpoints HTTP.

## Health Check e Monitoramento

### Verificar se a execução está “saudável”
Não existe `GET /health`. O equivalente operacional é confirmar que o script:
1) inicia sem erro,
2) solicita entrada,
3) valida corretamente os valores,
4) entrega o relatório final.

**Como verificar (local):**
```bash
python main.py
```

**Critérios de sucesso:**
- O programa pede a entrada de toneladas mensal (12 meses).
- Para cada mês, **aceita apenas números positivos** (inteiro/decimal).
- Para valores inválidos/negativos, **rejeita e solicita novamente**.
- Ao final, exibe: totais de colheita e projeções de desperdício (manual 5% e máquinas 15%) para o ano.

### Indicadores de problema
- **Execução encerrou com traceback** (erro não tratado) — falha do script.
- **Loop infinito/entrada recusada indevidamente** — validação possivelmente quebrada.
- **Cálculo inconsistente**: perdas não batem com `5%` e `15%` da colheita mensal informada (ex.: arredondamento/precisão).
- **Saída não é consolidada corretamente** (totais anuais ausentes/errados).

## Procedimentos Comuns

### Reiniciar o serviço
Como é um script, “reiniciar” = **reexecutar** o comando.

```bash
# No diretório do repositório
python main.py
```

Se estiver rodando em ambiente automatizado (CI/Job/Container), reinicie o **job/pod** conforme sua plataforma (PREENCHER).

### Verificar logs de erro
Se estiver rodando diretamente:
- O erro sai em **stderr/traceback** no terminal.

Para ambientes que capturam logs em arquivo/CI:
```bash
# PREENCHER: comando específico do seu ambiente (ex.: cat /var/log/...)
```

Se você conseguir reexecutar com redirecionamento:
```bash
python main.py 2> erro.log 1> saida.log
```
- `saida.log`: inclui o relatório e prompts (se houver).
- `erro.log`: inclui traceback/erros.

### Forçar re-processamento de mensagem
Não se aplica como “mensagens/fila” (não há mensageria descrita).  
Se a necessidade for repetir o cálculo após uma entrada inválida:
1) o script já **re-solicita** o mês com validação
2) continue a partir do mês afetado.

Caso o script falhe no meio e você precise reprocessar:
- **reexecute o script** e informe novamente os 12 meses (não há persistência descrita) — procedimento operacional:
```bash
python main.py
```

## Troubleshooting

### Problema: Script não inicia / dá erro ao executar
**Causa provável:** ambiente Python incorreto, dependência ausente (se existir), arquivo `main.py` não encontrado, erro de sintaxe.
**Como diagnosticar:**
- Verifique o caminho e existência do arquivo:
  ```bash
  ls -la
  python --version
  ```
- Execute e capture traceback:
  ```bash
  python main.py
  ```
**Como resolver:**
- Use o Python correto:
  ```bash
  python main.py
  ```
- Se existir `requirements.txt` (não informado), instale:
  ```bash
  pip install -r requirements.txt
  ```
- Se o erro for de código, corrigir `main.py` e redeploy (PREENCHER).

### Problema: Entrada negativa (ou zero) deveria ser rejeitada, mas o script aceita
**Causa provável:** regra de validação implementada incorretamente, comparação com string vs número, ou validação só para inteiros.
**Como diagnosticar:**
1) rode o script
2) insira, por exemplo: `-1`, `0`, `-3.5`
3) observe se ele re-solicita o mesmo mês ou segue calculando.
**Como resolver:**
- Ajustar a validação no `main.py` para garantir **somente números positivos** (ex.: `value > 0`).
- Garanta que o parse trate decimais e convertam para `float`/`Decimal` antes de validar.

### Problema: O script trava em loop pedindo entrada indefinidamente
**Causa provável:** validação falha ao aceitar algum formato esperado (ex.: vírgula decimal “3,5” vs ponto “3.5”), ou tratamento de erro não atualiza o estado do mês.
**Como diagnosticar:**
- Teste entradas com formatos diferentes:
  - `3.5` (decimal com ponto)
  - `4` (inteiro)
- Se “3,5” for usada e o parser só aceitar “.”, isso causará rejeição contínua.
**Como resolver:**
- Padronize o formato aceito (recomendar ponto decimal) — operacionalmente.
- Se necessário, ajuste o parser no `main.py` para suportar vírgula (PREENCHER).

### Problema: Cálculo de perdas não confere (5%/15%)
**Causa provável:** percentual aplicado errado, uso de base errada (ex.: 5% do total anual ao invés do mensal), ou erro de consolidação.
**Como diagnosticar:**
- Escolha um mês de teste com valor simples, por exemplo `100` toneladas:
  - Perda manual esperada: `5` toneladas
  - Perda máquinas esperada: `15` toneladas
- Compare com a saída do script.
**Como resolver:**
- Verificar no `main.py` se:
  - perda manual = `0.05 * toneladas_mes`
  - perda máquinas = `0.15 * toneladas_mes`
  - totais anuais somam mensalmente.
- Corrigir e reexecutar.

### Problema: Totais anuais não são exibidos ou saem parcialmente
**Causa provável:** fluxo de execução interrompido antes da consolidação (ex.: exceção após o loop), ou lógica de consolidação incompleta.
**Como diagnosticar:**
- Execute novamente e observe onde a execução para (qual mês/etapa).
- Capture stderr:
  ```bash
  python main.py 2> erro.log
  ```
**Como resolver:**
- Corrigir o ponto onde a consolidação ocorre (provável no `main.py` após leitura dos 12 meses).
- Se houver saída parcial por exceção, corrigir a exceção e reexecutar.

## Dependências Críticas
| Dependência | O que acontece se cair | Fallback |
|---|---|---|
| Ambiente Python (interpretação/execução) | Script não inicia | Usar Python correto (PREENCHER: versão) e recriar ambiente |
| Sistema de execução (terminal/CI/container) | logs e execução falham | Executar localmente para diagnóstico (python main.py) |
| Persistência/arquivo de entrada (se existir) | não há como reprocessar sem nova entrada | reexecutar e informar 12 meses novamente (sem fallback descrito) |

## Contatos de Escalação
- **Primeiro:** PREENCHER (responsável pelo repositório FIAP-estruturas-avancadas / manutenção do `main.py`)
- **Segundo:** PREENCHER (time de plataforma SRE/DevOps ou líder de engenharia responsável pelo ambiente de execução)

---  
> ⚠️ Rascunho gerado automaticamente pelo Alicerce by Malha. Preencha os valores reais de porta, dashboard e comandos antes de mergear.