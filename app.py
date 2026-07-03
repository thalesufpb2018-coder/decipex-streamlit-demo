import pandas as pd
import streamlit as st

from dados_ficticios import gerar_registros

# st.set_page_config precisa ser o primeiro comando Streamlit do script
st.set_page_config(page_title="Demo Pendentes", page_icon="📊", layout="wide")

st.title("📊 Demo: Pagamentos Pendentes (dados fictícios)")
st.caption("Réplica de estudo do painel real do DECIPEX — todos os nomes e valores aqui são inventados.")

# 1) Fonte de dados: em produção isso viria de um upload real (mais abaixo tem um exemplo).
#    st.session_state guarda algo "vivo" entre uma interação e outra, senão o Streamlit
#    esqueceria tudo a cada rerun (toda vez que você mexe em um filtro, o script roda de novo do zero).
if "registros" not in st.session_state:
    st.session_state.registros = gerar_registros()

df = pd.DataFrame(st.session_state.registros)
df["processo_status"] = df["processo"].apply(lambda p: "Com processo" if p else "Sem processo")
df["ob_status"] = df["ob_solicitada_em"].apply(lambda d: "Solicitada" if pd.notna(d) else "Aguardando pagamento")

# 2) Filtros na barra lateral
st.sidebar.header("Filtros")
ug_filtro = st.sidebar.selectbox("Órgão (UG)", ["Todos"] + sorted(df["ug"].unique()))
banco_filtro = st.sidebar.selectbox("Banco", ["Todos"] + sorted(df["banco"].unique()))
mes_filtro = st.sidebar.selectbox("Mês", ["Todos"] + sorted(df["mes"].unique()))

filtrado = df.copy()
if ug_filtro != "Todos":
    filtrado = filtrado[filtrado["ug"] == ug_filtro]
if banco_filtro != "Todos":
    filtrado = filtrado[filtrado["banco"] == banco_filtro]
if mes_filtro != "Todos":
    filtrado = filtrado[filtrado["mes"] == mes_filtro]

# 3) Indicadores (cards) lado a lado, usando st.columns
col1, col2, col3, col4 = st.columns(4)
col1.metric("Registros", len(filtrado))
col2.metric("Com processo", (filtrado["processo_status"] == "Com processo").sum())
col3.metric("Sem processo", (filtrado["processo_status"] == "Sem processo").sum())
col4.metric("OB solicitada", (filtrado["ob_status"] == "Solicitada").sum())

# 4) Gráfico simples: quantidade de registros por banco
st.subheader("Registros por banco")
st.bar_chart(filtrado["banco"].value_counts())

# 5) Tabela
st.subheader(f"Detalhamento ({len(filtrado)} registro(s))")
st.dataframe(
    filtrado[["nome", "ug", "banco", "valor", "mes", "ob_status", "processo_status"]],
    use_container_width=True,
    hide_index=True,
)

# 6) Upload — no app real isso leria a planilha .xlsx de verdade (igual o Flask faz).
#    Aqui só mostramos a mecânica: o Streamlit te dá o arquivo, você decide o que fazer com ele.
st.divider()
st.subheader("Enviar nova planilha (exemplo)")
arquivo = st.file_uploader("Selecione um .xlsx", type=["xlsx"])
if arquivo is not None:
    st.info(f"Recebi o arquivo **{arquivo.name}** — aqui entraria a leitura com pandas.read_excel(), como no sistema real.")
