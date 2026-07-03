import streamlit as st

st.title(f"Bem-vindo, {st.session_state.nome}")
st.write("Ferramentas disponíveis no menu à esquerda — a mesma ideia do painel real, remontada em Streamlit para estudo.")

col1, col2, col3 = st.columns(3)
col1.page_link("paginas/orientacoes.py", label="📖 Base de Orientações", width="stretch")
col2.page_link("paginas/faq.py", label="❓ FAQ", width="stretch")
col3.page_link("paginas/checklist.py", label="✅ Checklist", width="stretch")

col4, col5 = st.columns(2)
col4.page_link("paginas/requisitos.py", label="📋 Requisitos por Processo", width="stretch")
col5.page_link("paginas/pendentes.py", label="📊 Pagamentos Pendentes", width="stretch")

if st.session_state.tipo == "gestor":
    st.page_link("paginas/usuarios.py", label="👥 Usuários (só gestor)", width="stretch")
