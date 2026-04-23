# GMUD (Gerenciamento de Mudanças)

GMUD é o processo de gerenciamento de mudanças em TI, comum em empresas brasileiras.

É o fluxo de aprovação formal exigido antes de implantar alterações em sistemas de produção.

Equivalente ao `Change Request (CR)`

- O objetivo desse documento é garantir que mudanças em produção sejam revisadas, aprovadas e tenham um plano de rollback antes da execução
- Você submete uma solicitação de mudança descrevendo o quê, por quê, quando e como fazer rollback; passa por um comitê de aprovação (CAB — `Change Advisory Board`)

## O que uma solicitação de GMUD inclui

- Descrição da mudança
- Justificativa de negócio
- Avaliação de risco
- Análise de impacto (quais sistemas/usuários são afetados)
- Passos de implementação
- Plano de rollback
- Janela de manutenção (data/horário)

## Tipos de mudança

- **Padrão** — baixo risco, mudanças recorrentes pré-aprovadas (caminho rápido)
- **Normal** — passa pela revisão completa do CAB
- **Emergencial** — aprovação expedita para correções urgentes, revisada após a execução

## Na prática

O processo de GMUD geralmente vive em um sistema de tickets (ServiceNow, Jira, etc.) e os pipelines de deploy são bloqueados até que o ticket de GMUD seja aprovado.
