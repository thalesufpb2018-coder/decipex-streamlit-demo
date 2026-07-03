import streamlit as st

st.title("🏢 Unidades")
st.caption("Cadastro de unidades/setores e atribuição de usuários — usado para direcionar as ouvidorias.")

st.subheader("Nova unidade")
with st.form("nova_unidade", clear_on_submit=True):
    nome = st.text_input("Nome da unidade")
    if st.form_submit_button("Criar") and nome:
        st.session_state.unidades.append(
            {"id": st.session_state.proximo_id_unidade, "nome": nome, "ativa": True}
        )
        st.session_state.proximo_id_unidade += 1
        st.success(f'Unidade "{nome}" criada.')

st.subheader(f"Unidades cadastradas ({len(st.session_state.unidades)})")
for u in st.session_state.unidades:
    col1, col2 = st.columns([4, 1])
    status = "🟢 Ativa" if u["ativa"] else "⚪ Desativada"
    col1.write(f"**{u['nome']}** — {status}")
    if col2.button("Desativar" if u["ativa"] else "Ativar", key=f"toggle_{u['id']}"):
        u["ativa"] = not u["ativa"]
        st.rerun()

st.divider()
st.subheader("Unidades de cada usuário")
nomes_unidades = {u["id"]: u["nome"] for u in st.session_state.unidades}
for email, conta in st.session_state.contas.items():
    atuais = st.session_state.usuario_unidades.get(email, [])
    escolhidas = st.multiselect(
        f"{conta['nome']} ({email})",
        options=list(nomes_unidades.keys()),
        default=atuais,
        format_func=lambda uid: nomes_unidades[uid],
        key=f"unidades_{email}",
    )
    if escolhidas != atuais:
        st.session_state.usuario_unidades[email] = escolhidas
