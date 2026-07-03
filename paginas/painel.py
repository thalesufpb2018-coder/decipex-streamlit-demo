import streamlit as st

st.title(f"Bem-vindo, {st.session_state.nome}")
st.caption("Ferramentas disponíveis no menu acima — a mesma ideia do painel real, remontada em Streamlit para estudo.")
st.write("")

FERRAMENTAS = [
    ("📖", "Base de Orientações", "Dúvidas de outros setores, organizadas por assunto e pesquisáveis.", "paginas/orientacoes.py"),
    ("❓", "FAQ", "Perguntas e respostas em formato de FAQ, com busca por categoria.", "paginas/faq.py"),
    ("✅", "Checklist", "Tarefas semanais e mensais, por fase do mês, com observações.", "paginas/checklist.py"),
    ("📋", "Requisitos por Processo", "Guia do que cada tipo de processo exige.", "paginas/requisitos.py"),
    ("📊", "Pagamentos Pendentes", "Dashboard com filtros por órgão, banco e mês.", "paginas/pendentes.py"),
    ("📨", "Ouvidoria", "Linha do tempo das ouvidorias, por unidade responsável.", "paginas/ouvidoria.py"),
]

if st.session_state.tipo == "gestor":
    FERRAMENTAS += [
        ("👥", "Usuários", "Cadastro de contas — só gestor.", "paginas/usuarios.py"),
        ("🏢", "Unidades", "Setores usados para direcionar ouvidorias — só gestor.", "paginas/unidades.py"),
    ]

colunas = st.columns(3)
for i, (icone, titulo, descricao, destino) in enumerate(FERRAMENTAS):
    with colunas[i % 3]:
        with st.container(border=True):
            st.markdown(f"<div style='font-size:28px'>{icone}</div>", unsafe_allow_html=True)
            st.markdown(f"**{titulo}**")
            st.caption(descricao)
            st.page_link(destino, label="Abrir", width="stretch")
