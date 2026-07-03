import streamlit as st

st.title("👥 Usuários")
st.caption("Só quem entra como gestor vê essa página — igual no sistema real.")
st.info("Contas criadas aqui passam a funcionar no login, mas só durante esta sessão do navegador (sem banco de dados na demo).")

st.subheader("Nova conta")
with st.form("nova_conta", clear_on_submit=True):
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")
    tipo = st.selectbox("Tipo", ["colaborador", "gestor"])
    senha = st.text_input("Senha inicial", type="password")
    enviado = st.form_submit_button("Criar conta")
    if enviado:
        if not nome or not email or not senha:
            st.error("Preencha nome, e-mail e senha.")
        elif email in st.session_state.contas:
            st.error("Já existe uma conta com esse e-mail.")
        else:
            st.session_state.contas[email] = {"nome": nome, "senha": senha, "tipo": tipo}
            st.success(f"Conta de {nome} criada — já pode entrar com {email} e a senha definida.")

st.subheader(f"Contas cadastradas ({len(st.session_state.contas)})")
st.dataframe(
    [{"nome": c["nome"], "email": email, "tipo": c["tipo"]} for email, c in st.session_state.contas.items()],
    width="stretch",
    hide_index=True,
)
