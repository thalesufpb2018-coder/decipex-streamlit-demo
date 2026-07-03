import streamlit as st

st.title("✅ Checklist de tarefas")
st.info(
    "No sistema real isso fica salvo num banco de dados (SQLite), então continua lá mesmo "
    "fechando o navegador. Aqui na demo, guardo só na sessão (`st.session_state`) — se recarregar "
    "a página do zero, as marcações somem. É a limitação de uma demo sem banco de dados."
)

FASES = {
    "Início do mês": [
        "Atualizar a planilha de repagamentos com os arquivos recebidos por e-mail",
        "Cadastrar no PETRVS a execução do mês passado",
    ],
    "Meio do mês": [
        "Receber a nota fiscal do contrato Speedmais e analisar os relatórios",
        "Analisar os processos sobrestados",
    ],
    "Final do mês": [
        "Cadastrar o plano de trabalho do mês seguinte no PETRVS",
        "Enviar os processos dos contracheques físicos",
    ],
}

if "checklist_estado" not in st.session_state:
    st.session_state.checklist_estado = {}

for fase, tarefas in FASES.items():
    st.subheader(fase)
    for tarefa in tarefas:
        chave = f"{fase}::{tarefa}"
        marcado = st.checkbox(tarefa, value=st.session_state.checklist_estado.get(chave, False), key=chave)
        st.session_state.checklist_estado[chave] = marcado
        if marcado:
            with st.expander("📝 observação (opcional)"):
                st.text_area("Observação", key=f"nota::{chave}", label_visibility="collapsed")
