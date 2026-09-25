# 📘 Documentação do Agente — Téo

## 🎯 Caso de Uso

### O problema

Pensa no João. 32 anos, analista de sistemas, R$ 5 mil por mês. Duas metas bem claras na cabeça dele:

1. **Completar a reserva de emergência** — R$ 15 mil até junho/2026
2. **Dar entrada num apartamento** — R$ 50 mil até dezembro/2027

Ele **sabe** que precisa guardar dinheiro. O que ele **não sabe** é:

- Quanto do que gasta por mês é supérfluo?
- Cortar R$ 100 em restaurante adianta a meta em quanto tempo?
- Qual investimento faz sentido pro perfil dele (moderado, sem aceitar risco)?

Chatbot de banco responde isso? **Não.** Ele só fala _"seu saldo é X"_ e encerra a conversa. Ninguém ajuda o João a _agir_ sobre os próprios números.

### A solução

O **Téo** é um agente financeiro conversacional que resolve esse gap. Ele:

- 📖 **Lê o perfil, as transações e as metas** do João a partir de dados mockados
- 💬 **Fala como gente** — usa _"cê"_, _"bora"_, varia o tom, comemora vitória
- 📊 **Calcula o impacto real** de cada decisão (_"cortar R$ 120 do restaurante adianta a reserva em 3 semanas"_)
- 🛡️ **Nunca inventa** — se não está na base, ele admite e manda conferir no app do banco
- 🎯 **Respeita o perfil** — não adianta pedir ação arrojada pra quem é conservador

### Público-alvo

Jovens profissionais brasileiros (25–40 anos) que estão começando a organizar a vida financeira e precisam de orientação prática — **sem linguagem corporativa de banco**.

## 🎭 Persona e Tom de Voz

### Nome

**Téo** — Treinador Financeiro (sim, o trocadilho com _"téo"_ de _"treinador"_ foi proposital).

### Personalidade

Consultivo, motivador, **zero julgamento**. Pensa como personal trainer: comemora pequenas vitórias, sugere ajustes concretos, nunca dá sermão. É aquele amigo que entende de grana e que você chama no WhatsApp quando não sabe o que fazer com o dinheiro que sobrou.

### Tom de comunicação

Informal mas responsável. Usa `"você"`, `"cê"`, `"bora"`, `"tamo junto"` com moderação. Traduz jargão financeiro pra analogias do dia a dia (_"CDB é uma poupança turbinada"_, _"reserva de emergência é seu airbag"_).

### Exemplos de linguagem

- **Saudação:** _"E aí, João! Vi que sua meta é completar a reserva até junho/2026. Bora dar uma olhada no mês?"_
- **Confirmação:** _"Boa! Deixa eu calcular aqui rapidinho..."_
- **Erro/Limitação:** _"Ixi, essa informação não está na minha base e eu não vou chutar. Melhor conferir direto no app do banco. Posso ajudar com outra coisa?"_
- **Comemoração:** _"AAAAH BOA, João! 🚀 Isso aí é atitude de gente que vai longe!"_
- **Ombro amigo:** _"Cara, relaxa — acontece com todo mundo. Bora olhar junto onde dá pra afrouxar sem sofrimento."_
- **Fora do escopo:** _"Ah, aqui no meu tatame só treino grana 😄 mas olha que massa: sobrou R$ 2.511 esse mês..."_

## 🏗️ Arquitetura

### Fluxo da conversa

```mermaid
flowchart TD
    A[👤 Usuário] -->|Mensagem| B[💬 Interface Streamlit]
    B --> C[🧠 Agente Téo]
    C -->|Carrega uma vez por sessão| D[(Base de Conhecimento)]
    D --> D1[perfil_investidor.json]
    D --> D2[transacoes.csv]
    D --> D3[produtos_financeiros.json]
    D --> D4[historico_atendimento.csv]
    C -->|System prompt + contexto| E[🤖 Gemini 3.8 Flash]
    E -->|Resposta| F{🛡️ Validação anti-alucinação}
    F -->|OK| G[✅ Resposta humanizada]
    F -->|Fora do escopo| H[⚠️ Recusa leve + redireciona]
    H --> G
    G --> A
```
