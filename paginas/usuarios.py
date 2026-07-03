import streamlit as st

st.title("👥 Usuários")
st.caption("Só quem entra como gestor vê essa página — igual no sistema real.")

if "usuarios_demo" not in st.session_state:
    st.session_state.usuarios_demo = [
        {"nome": "Gestor Demo", "email": "gestor@demo.com", "tipo": "gestor"},
        {"nome": "Colaborador Demo", "email": "colaborador@demo.com", "tipo": "colaborador"},
    ]

st.subheader("Nova conta")
with st.form("nova_conta"):
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")
    tipo = st.selectbox("Tipo", ["colaborador", "gestor"])
    enviado = st.form_submit_button("Criar conta")
    if enviado and nome and email:
        st.session_state.usuarios_demo.append({"nome": nome, "email": email, "tipo": tipo})
        st.success(f"Conta de {nome} criada (só nesta sessão de demonstração).")

st.subheader(f"Contas cadastradas ({len(st.session_state.usuarios_demo)})")
st.dataframe(st.session_state.usuarios_demo, width="stretch", hide_index=True)
