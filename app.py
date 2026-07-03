import streamlit as st

st.set_page_config(page_title="Painel DECIPEX (demo)", page_icon="🏛️", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Contas da demo, guardadas só nesta sessão do navegador (sem banco de dados de verdade).
# É aqui que login.py busca pra conferir a senha, e usuarios.py adiciona novas contas.
if "contas" not in st.session_state:
    st.session_state.contas = {
        "gestor@demo.com": {"nome": "Gestor Demo", "senha": "demo123", "tipo": "gestor"},
        "colaborador@demo.com": {"nome": "Colaborador Demo", "senha": "demo123", "tipo": "colaborador"},
    }


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

    pg = st.navigation(paginas, position="top")

pg.run()
