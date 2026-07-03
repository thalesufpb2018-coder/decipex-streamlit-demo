import streamlit as st

_, meio, _ = st.columns([1, 1.4, 1])

with meio:
    st.markdown(
        "<div style='text-align:center;font-size:44px;margin-bottom:-10px'>🏛️</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h2 style='text-align:center;margin-bottom:0'>Painel DECIPEX</h2>"
        "<p style='text-align:center;color:#5a6b7b;margin-top:4px'>Versão de estudo — Streamlit</p>",
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.caption("Contas fictícias, só para praticar. Nenhum dado real do DECIPEX está aqui.")

        email = st.text_input("E-mail", placeholder="gestor@demo.com")
        senha = st.text_input("Senha", type="password", placeholder="demo123")

        if st.button("Entrar", type="primary", width="stretch"):
            conta = st.session_state.contas.get(email)
            if conta and conta["senha"] == senha:
                st.session_state.logged_in = True
                st.session_state.nome = conta["nome"]
                st.session_state.tipo = conta["tipo"]
                st.session_state.email = email
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos.")

        st.info("Contas de teste: **gestor@demo.com** ou **colaborador@demo.com** · senha `demo123`\n\nContas criadas na página Usuários também funcionam, nesta mesma sessão.")
