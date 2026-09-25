---

# 🗂️ Base de Conhecimento — Téo

Todo agente inteligente precisa de dados pra trabalhar. Aqui eu explico quais arquivos o Téo usa e como eles entram na conversa.

## 📁 Dados utilizados

| Arquivo                     | Formato | Como o Téo usa                                        |
| --------------------------- | ------- | ----------------------------------------------------- |
| `perfil_investidor.json`    | JSON    | Personalizar recomendações + contextualizar metas     |
| `produtos_financeiros.json` | JSON    | Base única e oficial pra qualquer recomendação        |
| `transacoes.csv`            | CSV     | Analisar padrão de gastos e sugerir cortes concretos  |
| `historico_atendimento.csv` | CSV     | Lembrar do que já foi conversado antes (continuidade) |

## 🔧 Adaptações nos dados

Não modifiquei nada dos dados mockados originais. Usei os 4 arquivos exatamente como fornecidos no repositório base do desafio.

Por quê? Porque o cenário proposto já é realista o suficiente — cliente fictício (João Silva), perfil moderado, sem aceitar risco, duas metas concretas. Mexer nisso só ia afastar o projeto do que o desafio pediu.

Se eu fosse evoluir, adicionaria:

- Mais produtos com prazos variados (CDB com carência, Tesouro IPCA+)
- Histórico de transações de 2–3 meses pra mostrar tendências
- Registros de atendimentos anteriores com temas variados

## 🔌 Estratégia de integração

### Como os dados são carregados?

Os 4 arquivos são lidos uma única vez no início da sessão pela função `montar_contexto()` em `src/dados.py`.

O resultado é uma string formatada com tudo que o Téo precisa saber.

### Como os dados entram no prompt?

Vão inteiramente no `system_instruction` do modelo. Não uso RAG dinâmico.

Por quê?

- O volume de dados é pequeno (mockado) — cabe folgado no contexto;
- É mais previsível e auditável — eu sei exatamente o que o modelo vê;
- Menos partes móveis = menos bugs.

## 🧩 Exemplo de contexto montado

É isso que o Téo recebe antes da primeira mensagem:

```text
=== PERFIL DO CLIENTE ===
Nome: João Silva | Idade: 32
Profissão: Analista de Sistemas | Renda: R$ 5000.00
Perfil investidor: moderado
Aceita risco: Não
Reserva atual: R$ 10000.00

Metas:
- Completar reserva de emergência: R$ 15000.00 até 2026-06
- Entrada do apartamento: R$ 50000.00 até 2027-12

=== GASTOS DO MÊS (por categoria) ===
moradia: R$ 1380.00
alimentacao: R$ 570.00
saude: R$ 188.00
transporte: R$ 295.00
lazer: R$ 55.90

Total saídas: R$ 2488.90
Total entradas: R$ 5000.00
Sobrou no mês: R$ 2511.10

=== PRODUTOS DISPONÍVEIS (base oficial) ===
Tesouro Selic | renda_fixa | risco baixo | 100% da Selic | mín R$ 30.00 | indicado para: Reserva de emergência e iniciantes
CDB Liquidez Diária | renda_fixa | risco baixo | 102% do CDI | mín R$ 100.00 | indicado para: Quem busca segurança com rendimento diário
LCI/LCA | renda_fixa | risco baixo | 95% do CDI | mín R$ 1000.00 | indicado para: Quem pode esperar 90 dias (isento de IR)
Fundo Multimercado | fundo | risco medio | CDI + 2% | mín R$ 500.00 | indicado para: Perfil moderado que busca diversificação
Fundo de Ações | fundo | risco alto | Variável | mín R$ 100.00 | indicado para: Perfil arrojado com foco no longo prazo

=== HISTÓRICO DE ATENDIMENTOS ===
2025-09-15 (chat): CDB — Cliente perguntou sobre rentabilidade e prazos
2025-09-22 (telefone): Problema no app — Erro ao visualizar extrato foi corrigido
2025-10-01 (chat): Tesouro Selic — Cliente pediu explicação sobre o Tesouro Direto
2025-10-12 (chat): Metas financeiras — Cliente acompanhou o progresso da reserva
2025-10-25 (email): Atualização cadastral — Cliente atualizou e-mail e telefone
```

```

```
