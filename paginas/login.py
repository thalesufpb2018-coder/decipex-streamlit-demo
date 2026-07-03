import streamlit as st

st.title("🏛️ Painel DECIPEX — versão de estudo")
st.caption("Contas fictícias, só para praticar Streamlit. Nenhum dado real do DECIPEX está aqui.")

st.info("Contas de teste — **gestor@demo.com** ou **colaborador@demo.com**, senha `demo123`. Contas criadas na página Usuários também funcionam aqui, nesta mesma sessão.")

email = st.text_input("E-mail")
senha = st.text_input("Senha", type="password")

if st.button("Entrar", type="primary"):
    conta = st.session_state.contas.get(email)
    if conta and conta["senha"] == senha:
        st.session_state.logged_in = True
        st.session_state.nome = conta["nome"]
        st.session_state.tipo = conta["tipo"]
        st.rerun()
    else:
        st.error("E-mail ou senha inválidos.")
