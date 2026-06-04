# FIAP-estruturas-avancadas — Arquitetura

## Visão Geral
O repositório `FIAP-estruturas-avancadas` foi estruturado como uma aplicação **monolítica e linear de console (script único)**. A escolha por um fluxo sequencial (entrada → cálculo → consolidação → saída) reduz complexidade e overhead para um problema eminentemente **determinístico e de baixo volume de dados**: ler 12 valores (toneladas mensais), aplicar percentuais fixos de perda (5% manual e 15% máquinas) e apresentar totais consolidados do ano. Como não há persistência, integrações externas ou processamento assíncrono, a arquitetura em camadas ou microsserviços não agrega valor e aumentaria a superfície de erro e manutenção.

## Stack Tecnológico
| Camada | Tecnologia | Motivo |
|---|---|---|
| Linguagem / Execução | Python | Implementação direta do algoritmo educacional, com validações simples de entrada e cálculo em memória. |
| Camada de entrada/saída | Console (STDIN/STDOUT) | Atende ao formato do problema: solicitar valores ao usuário e exibir resultados imediatamente, sem necessidade de interface web/serviço. |

## Padrões Adotados
- **Fluxo sequencial procedural (entrada-processamento-saída):** usado como principal mecanismo organizacional. Isso é apropriado porque o domínio do exercício exige apenas uma passagem única por 12 meses, com cálculos determinísticos e consolidação final.
- **Validação de entrada no ponto de uso:** rejeita valores inválidos (negativos) e força repetição da coleta até que o usuário informe um número positivo, mantendo o algoritmo em estado consistente.

## Decisões de Arquitetura (ADRs)

### ADR 1 — Manter aplicação monolítica em formato de script de console
- **Contexto:** O algoritmo solicitado envolve apenas leitura de 12 meses, aplicação de percentuais fixos de perda e cálculo de totais anuais, sem requisitos de persistência, múltiplas rotas, autenticação, concorrência ou integração.
- **Decisão:** Implementar tudo em um único fluxo procedural dentro do `main.py`, com lógica sequencial: coletar toneladas mensais, calcular perdas por método (manual 5% / máquinas 15%), consolidar totais e exibir resultados.
- **Consequências:**
  - **Prós:** menor complexidade; mais fácil de entender/validar para o objetivo do exercício; baixo custo de execução; sem necessidade de estruturação em camadas (controllers/services/repositories).
  - **Contras (trade-offs):** menor extensibilidade caso o escopo evolua (ex.: múltiplos anos, cenários configuráveis, API HTTP, persistência); testes e manutenção podem ficar menos segmentados se a lógica de validação e cálculo crescer.

### ADR 2 — Validar toneladas no momento da coleta e rejeitar valores negativos
- **Contexto:** As regras de negócio exigem que somente números (inteiro ou decimal) positivos sejam aceitos como toneladas, e que a entrada negativa seja rejeitada com repetição da solicitação ao usuário.
- **Decisão:** Na etapa de input do mês, aplicar validação imediata: se a entrada for negativa (ou inválida conforme o parsing do Python), exibir mensagem de validação e solicitar novamente o valor do mês.
- **Consequências:**
  - **Prós:** garante integridade do estado do algoritmo (não há cálculos com valores negativos); simplifica o raciocínio do cálculo, pois todas as toneladas usadas serão válidas.
  - **Contras:** a responsabilidade de validação fica acoplada ao fluxo de console; se a aplicação evoluir para API/serviço, será necessário refatorar para reaproveitar a validação em outros pontos de entrada.

### ADR 3 — Cálculo direto em memória sem persistência
- **Contexto:** O problema calcula projeções e totais apenas para exibição imediata, somando perdas e colheita ao longo de 12 meses.
- **Decisão:** Manter os valores mensais e totais apenas em memória durante a execução do script; ao final, consolidar e imprimir os resultados.
- **Consequências:**
  - **Prós:** reduz dependências (nenhum banco/filas necessárias); minimiza requisitos de infraestrutura.
  - **Contras:** não há histórico armazenado; reexecução é necessária para comparar cenários.

## Dependências Externas
| Dependência | Tipo | Propósito |
|---|---|---|
| Nenhuma identificada | PREENCHER | PREENCHER |

## Pontos de Atenção
- **Escalabilidade funcional:** a estrutura monolítica e procedural é adequada para o exercício atual, mas pode exigir refatoração caso surjam novos requisitos (ex.: múltiplos anos, percentuais parametrizáveis, exportação de dados, interface web/API, persistência).
- **Robustez de parsing de entrada:** como a coleta é via console, é importante garantir que o tratamento de conversão (inteiro/decimal) seja consistente e que o comportamento para entradas não numéricas esteja bem definido no `main.py` (ex.: strings, vazio, valores com formatação inesperada).  
- **Testabilidade:** sem separação clara em funções/isolamento de lógica, testes unitários podem ficar mais difíceis se o código crescer.