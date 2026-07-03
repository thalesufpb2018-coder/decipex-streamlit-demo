import streamlit as st

st.set_page_config(page_title="Painel DECIPEX (demo)", page_icon="🏛️", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def logout():
    st.session_state.logged_in = False
    st.rerun()


if not st.session_state.logged_in:
    pg = st.navigation([st.Page("paginas/login.py", title="Entrar", icon="🔑")])
else:
    paginas = [
        st.Page("paginas/painel.py", title="Painel", icon="🏠", default=True),
        st.Page("paginas/orientacoes.py", title="Base de Orientações", icon="📖"),
        st.Page("paginas/faq.py", title="FAQ", icon="❓"),
        st.Page("paginas/checklist.py", title="Checklist", icon="✅"),
        st.Page("paginas/requisitos.py", title="Requisitos por Processo", icon="📋"),
        st.Page("paginas/pendentes.py", title="Pagamentos Pendentes", icon="📊"),
    ]
    if st.session_state.tipo == "gestor":
        paginas.append(st.Page("paginas/usuarios.py", title="Usuários", icon="👥"))

    with st.sidebar:
        st.markdown(f"**{st.session_state.nome}** · {st.session_state.tipo}")
        if st.button("Sair", width="stretch"):
            logout()

    pg = st.navigation(paginas)

pg.run()
