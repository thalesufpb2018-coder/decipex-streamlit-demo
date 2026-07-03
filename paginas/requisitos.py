import streamlit as st

st.title("📋 Requisitos por tipo de processo")
st.caption("Guia de referência — mesmo conteúdo institucional do sistema real, sem dado pessoal envolvido.")

PROCESSO_REQUISITOS = {
    "Alteração de dados bancários": [
        "Verificar se é conta salário",
        "Comprovante bancário anexado",
        "Validar titularidade no SIGEPE (BACEN)",
        "Se a pessoa está sem pagamento, acionar COATE-FINAN (não enviar ao SouGov)",
        "Se já foi alterada manualmente, indeferir informando que já foi feita",
    ],
    "Exclusão por óbito": [
        "Verificar se há certidão de óbito ou apenas declaração",
        "Identificar vínculo (40806, 40805, 17000)",
        "Verificar se a folha está aberta ou fechada",
        "Verificar se há mais de um vínculo em órgãos distintos",
        "Verificar se há pedido de pensão junto (duplicar processo se sim)",
    ],
    "Repagamento": [
        "Verificar conta cadastrada no e-SIAPE",
        "Identificar competências em aberto",
        "Verificar se a conta foi devolvida pelo banco antes de processar",
        "Encaminhar à COATE-FINAN com dados completos",
        "OB só cai em conta corrente, nunca em conta salário ou poupança",
    ],
    "Fiscalização de contrato (Speedmais)": [
        "Conferir Ind.1 — % de atendimentos em até 30s (meta 85%)",
        "Conferir Ind.2 — atendimentos concluídos no prazo (meta 90%)",
        "Conferir Ind.4 — NPS/satisfação (meta 85%)",
        "Avaliar se a glosa pode ser desconsiderada",
        "Usar o valor do Relatório de Atividades (realizado), não o previsto na OS",
    ],
}

tipo = st.radio("Tipo de processo", list(PROCESSO_REQUISITOS.keys()), horizontal=True)
st.subheader(tipo)
for item in PROCESSO_REQUISITOS[tipo]:
    st.markdown(f"- {item}")
