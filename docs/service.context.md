# FIAP-estruturas-avancadas — Contexto de Negócio

## Propósito
O **FIAP-estruturas-avancadas** projeta **perdas na colheita de cana-de-açúcar** ao longo de um ano com base na **produção mensal (toneladas)** informada pelo usuário. A motivação de negócio é apoiar o entendimento de quanto da colheita pode ser desperdiçada dependendo do método de colheita, permitindo comparações objetivas entre **colheita manual** e **colheita com máquinas**.

O serviço realiza a leitura de **12 valores mensais**, aplica as taxas de perda definidas para cada método, e entrega **relatórios mensais e totais anuais consolidados**. Com isso, o usuário consegue estimar o impacto de diferentes abordagens de colheita em termos de volume perdido, apoiando análises de planejamento e decisão.

## Conceitos-chave
- **Perda na colheita:** parcela da produção que não se transforma em produto aproveitável, variando conforme o método (manual vs máquinas).
- **Produção mensal (toneladas):** quantidade de cana colhida em cada mês do ano, usada como base para calcular as perdas projetadas.
- **Relatório anual (totais consolidados):** soma dos volumes colhidos e das perdas projetadas por método ao longo dos 12 meses.

## Regras de Negócio Críticas
- A **perda por colheita manual** é **5%** da produção mensal informada.
- A **perda por colheita com máquinas** é **15%** da produção mensal informada.
- O cálculo consolida, ao longo dos **12 meses**, os totais de:
  - **colheita total**;
  - **perdas projetadas** por método (manual e máquinas).
- **Não aceitar toneladas negativas**: se o usuário informar valor menor que zero, o serviço deve **rejeitar** e **solicitar novamente** com mensagem de validação.
- **Somente valores numéricos positivos** (inteiro ou decimal) são aceitos como toneladas.
- A projeção mensal e os totais dependem diretamente dos valores aceitos na entrada; portanto, validação é mandatória para manter consistência dos resultados.

## Integrações Principais
### Publica (eventos que emite)
- Nenhum. (Serviço de execução local via console/algoritmo sequencial, sem barramento/eventos.)

### Consome (eventos que processa)
- Nenhum. (Não há consumo de eventos externos; a entrada vem do usuário.)

### Chamadas HTTP
- Nenhuma. (Não realiza integrações via rede.)

## O que este serviço NÃO faz
- **Não coleta dados reais automaticamente** de fontes externas (ex.: sensores, ERPs, bases agrícolas).
- **Não realiza previsão estatística** baseada em séries históricas; trabalha apenas com **percentuais fixos** (5% e 15%) sobre a produção mensal informada.
- **Não executa cálculos financeiros** (custos, receitas, ROI) — o foco é **volume perdido** projetado.
- **Não gerencia persistência/armazenamento** de relatórios; os resultados são produzidos na execução do script e exibidos ao usuário.
- **Não modela variações sazonais, qualidade de cana ou eficiência variável** por mês; as taxas são constantes conforme a regra.

## Decisões de Arquitetura Relevantes
- **Aplicação em formato de script sequencial (console)**: a decisão prioriza simplicidade operacional para cálculo e apresentação direta dos resultados, evitando camadas adicionais e mantendo o fluxo focado em entrada → cálculo → saída.

## Owner
- Time: PREENCHER
- Contato: PREENCHER

---
> ⚠️ Rascunho gerado automaticamente pelo Alicerce by Malha. Revise e enriqueça com contexto tácito antes de mergear.