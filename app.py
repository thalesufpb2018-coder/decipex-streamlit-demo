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

# Unidades/ouvidoria — também só na sessão, com um exemplo fictício já pronto pra explorar
if "unidades" not in st.session_state:
    st.session_state.unidades = [
        {"id": 1, "nome": "COATE-CADAS", "ativa": True},
        {"id": 2, "nome": "COATE-FINAN", "ativa": True},
    ]
if "usuario_unidades" not in st.session_state:
    st.session_state.usuario_unidades = {"colaborador@demo.com": [1]}
if "ouvidorias" not in st.session_state:
    st.session_state.ouvidorias = [
        {
            "id": 1,
            "conteudo": "Exemplo fictício: cidadão relata que o pagamento não caiu na conta informada.",
            "data_recebimento": "2026-06-20",
            "unidades": [1],
            "status": "recebida",
            "criado_por": "gestor@demo.com",
            "resposta": None,
            "respondido_por": None,
            "documentos": [],
        }
    ]
if "proximo_id_unidade" not in st.session_state:
    st.session_state.proximo_id_unidade = 3
if "proximo_id_ouvidoria" not in st.session_state:
    st.session_state.proximo_id_ouvidoria = 2


def logout():
    st.session_state.logged_in = False
    st.rerun()


def contar_pendencias_ouvidoria(email, tipo):
    minhas_unidades = set(st.session_state.usuario_unidades.get(email, []))
    pendentes_unidade = sum(
        1 for o in st.session_state.ouvidorias
        if o["status"] == "recebida" and set(o["unidades"]) & minhas_unidades
    )
    pendentes_criador = sum(
        1 for o in st.session_state.ouvidorias
        if o["status"] == "em_atendimento" and o["criado_por"] == email
    )
    return pendentes_unidade + pendentes_criador


if not st.session_state.logged_in:
    pg = st.navigation([st.Page("paginas/login.py", title="Entrar", icon="🔑")])
else:
    pendencias = contar_pendencias_ouvidoria(st.session_state.email, st.session_state.tipo)
    titulo_ouvidoria = f"Ouvidoria ({pendencias})" if pendencias else "Ouvidoria"
    paginas = [
        st.Page("paginas/painel.py", title="Painel", icon="🏠", default=True),
        st.Page("paginas/orientacoes.py", title="Base de Orientações", icon="📖"),
        st.Page("paginas/faq.py", title="FAQ", icon="❓"),
        st.Page("paginas/checklist.py", title="Checklist", icon="✅"),
        st.Page("paginas/requisitos.py", title="Requisitos por Processo", icon="📋"),
        st.Page("paginas/pendentes.py", title="Pagamentos Pendentes", icon="📊"),
        st.Page("paginas/ouvidoria.py", title=titulo_ouvidoria, icon="📨"),
    ]
    if st.session_state.tipo == "gestor":
        paginas.append(st.Page("paginas/usuarios.py", title="Usuários", icon="👥"))
        paginas.append(st.Page("paginas/unidades.py", title="Unidades", icon="🏢"))

    with st.sidebar:
        st.markdown(f"**{st.session_state.nome}** · {st.session_state.tipo}")
        if st.button("Sair", width="stretch"):
            logout()

    pg = st.navigation(paginas, position="top")

pg.run()
