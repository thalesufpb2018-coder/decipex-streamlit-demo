import json

import streamlit as st

st.title("📖 Base de Orientações")

with open("dados_orientacoes.json", encoding="utf-8") as f:
    dados = json.load(f)

nomes_grupos = [g["nome"] for g in dados["grupos"]]
grupo_escolhido = st.selectbox("Grupo", nomes_grupos)
grupo = next(g for g in dados["grupos"] if g["nome"] == grupo_escolhido)
st.caption(grupo["subtitulo"])

nomes_cats = {c["id"]: c["nome"] for c in grupo["cats"]}
cat_escolhida = st.selectbox("Categoria", ["Todas"] + list(nomes_cats.values()))

busca = st.text_input("Buscar")

itens = grupo["orientacoes"]
if cat_escolhida != "Todas":
    itens = [o for o in itens if nomes_cats.get(o["c"]) == cat_escolhida]
if busca:
    termo = busca.lower()
    itens = [o for o in itens if termo in o["q"].lower() or termo in o["p"].lower()]

st.caption(f"{len(itens)} orientação(ões)")
for o in itens:
    with st.expander(o["q"]):
        st.write(o["p"])
        meta = [m for m in [o.get("u"), o.get("fonte"), o.get("data")] if m]
        if meta:
            st.caption(" · ".join(meta))
