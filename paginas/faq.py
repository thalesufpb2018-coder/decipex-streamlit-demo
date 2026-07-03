import json

import streamlit as st

st.title("❓ FAQ")

with open("dados_orientacoes.json", encoding="utf-8") as f:
    dados = json.load(f)

itens = []
for grupo in dados["grupos"]:
    nomes_cats = {c["id"]: c["nome"] for c in grupo["cats"]}
    for o in grupo["orientacoes"]:
        itens.append({**o, "categoria": nomes_cats.get(o["c"], ""), "grupo": grupo["nome"]})

categorias = sorted({it["categoria"] for it in itens})
cat_escolhida = st.selectbox("Categoria", ["Todas"] + categorias)
busca = st.text_input("Buscar pergunta")

filtrados = itens
if cat_escolhida != "Todas":
    filtrados = [it for it in filtrados if it["categoria"] == cat_escolhida]
if busca:
    termo = busca.lower()
    filtrados = [it for it in filtrados if termo in it["q"].lower() or termo in it["p"].lower()]

st.caption(f"{len(filtrados)} pergunta(s)")
for categoria in categorias:
    do_grupo = [it for it in filtrados if it["categoria"] == categoria]
    if not do_grupo:
        continue
    st.subheader(categoria)
    for it in do_grupo:
        with st.expander(it["q"]):
            st.write(it["p"])
            st.caption(it["grupo"])
