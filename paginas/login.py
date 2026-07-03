import streamlit as st

st.title("🏛️ Painel DECIPEX — versão de estudo")
st.caption("Contas fictícias, só para praticar Streamlit. Nenhum dado real do DECIPEX está aqui.")

DEMO_USERS = {
    "gestor@demo.com": {"senha": "demo123", "nome": "Gestor Demo", "tipo": "gestor"},
    "colaborador@demo.com": {"senha": "demo123", "nome": "Colaborador Demo", "tipo": "colaborador"},
}

st.info("Contas de teste — **gestor@demo.com** ou **colaborador@demo.com**, senha `demo123`")

email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Entrar", type="primary"):
    usuario = DEMO_USERS.get(email)
    if usuario and usuario["senha"] == senha:
        st.session_state.logged_in = True
        st.session_state.nome = usuario["nome"]
        st.session_state.tipo = usuario["tipo"]
        st.rerun()
    else:
        st.error("E-mail ou senha inválidos.")
