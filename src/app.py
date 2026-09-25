import streamlit as st
from agente import AgenteFinanceiro

st.set_page_config(page_title="Téo — Treinador Financeiro", page_icon="💰")
st.title("💰 Téo — Seu Treinador Financeiro")
st.caption("Sem julgamento, sem jargão. Bora bater suas metas.")


def exibir(texto: str):
    """Escapa o '$' para o Streamlit não interpretar como LaTeX."""
    st.markdown(texto.replace("$", r"\$"))


if "agente" not in st.session_state:
    st.session_state.agente = AgenteFinanceiro()
    st.session_state.mensagens = [{
        "role": "assistant",
        "content": (
            "E aí, João! Vi que sua meta é completar a reserva de emergência "
            "até junho/2026 — faltam R$ 5.000. Quer dar uma olhada no "
            "seu mês e ver onde dá pra acelerar?"
        ),
    }]

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        exibir(msg["content"])

if pergunta := st.chat_input("Pergunte algo sobre suas finanças..."):
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        exibir(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Deixa eu calcular..."):
            resposta = st.session_state.agente.responder(pergunta)
        exibir(resposta)

    st.session_state.mensagens.append({"role": "assistant", "content": resposta})