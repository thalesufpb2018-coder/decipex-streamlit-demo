import streamlit as st

EXTENSOES_PERMITIDAS = {"pdf", "jpg", "jpeg", "png", "doc", "docx", "xls", "xlsx"}

email = st.session_state.email
tipo = st.session_state.tipo
nomes_unidades = {u["id"]: u["nome"] for u in st.session_state.unidades}
minhas_unidades = set(st.session_state.usuario_unidades.get(email, []))


def pode_ver(o):
    return tipo == "gestor" or o["criado_por"] == email or bool(minhas_unidades & set(o["unidades"]))


def encontrar(oid):
    return next((o for o in st.session_state.ouvidorias if o["id"] == oid), None)


# ---------- vista de detalhe (quando há ?id=... na URL) ----------
oid = st.query_params.get("id")
if oid:
    o = encontrar(int(oid))
    if not o or not pode_ver(o):
        st.error("Você não tem acesso a essa ouvidoria (ou ela não existe).")
        if st.button("← Voltar"):
            st.query_params.clear()
            st.rerun()
        st.stop()

    if st.button("← Voltar à ouvidoria"):
        st.query_params.clear()
        st.rerun()

    st.title(f"Ouvidoria #{o['id']}")
    status_label = {"recebida": "Recebida", "em_atendimento": "Em atendimento", "concluida": "Concluída"}
    st.caption(
        f"Status: **{status_label[o['status']]}** · Cadastrada por {o['criado_por']} em {o['data_recebimento']} "
        f"· Unidade(s): {', '.join(nomes_unidades[uid] for uid in o['unidades'])}"
    )

    st.subheader("Conteúdo recebido")
    st.write(o["conteudo"])

    if o["resposta"]:
        st.subheader(f"Resposta de {o['respondido_por']}")
        st.write(o["resposta"])
        if o["documentos"]:
            st.write("**Documentos anexados:**")
            for doc in o["documentos"]:
                st.download_button(f"📄 {doc['nome']}", data=doc["bytes"], file_name=doc["nome"], key=f"doc_{o['id']}_{doc['nome']}")

    pode_responder = o["status"] == "recebida" and (tipo == "gestor" or bool(minhas_unidades & set(o["unidades"])))
    if pode_responder:
        st.subheader("Responder")
        with st.form(f"responder_{o['id']}"):
            resposta = st.text_area("Resposta")
            arquivos = st.file_uploader(
                "Documentos (opcional — PDF, imagem, Word ou Excel)",
                accept_multiple_files=True,
                type=list(EXTENSOES_PERMITIDAS),
            )
            if st.form_submit_button("Enviar resposta") and resposta:
                o["resposta"] = resposta
                o["respondido_por"] = email
                o["status"] = "em_atendimento"
                o["documentos"] = [{"nome": a.name, "bytes": a.getvalue()} for a in (arquivos or [])]
                st.rerun()

    pode_concluir = o["status"] == "em_atendimento" and o["criado_por"] == email
    if pode_concluir:
        st.info("A resposta acima já pode ser copiada e enviada por e-mail a quem procurou a ouvidoria.")
        if st.button("Concluir ouvidoria"):
            o["status"] = "concluida"
            st.rerun()

    st.stop()

# ---------- lista / linha do tempo ----------
st.title("📨 Ouvidoria")
st.caption("Réplica de estudo — exemplos fictícios, sem dado real de cidadão.")

unidades_ativas = [u for u in st.session_state.unidades if u["ativa"]]
st.subheader("Nova ouvidoria")
if not unidades_ativas:
    st.warning("Nenhuma unidade ativa. Cadastre uma na página Unidades primeiro.")
else:
    with st.form("nova_ouvidoria", clear_on_submit=True):
        conteudo = st.text_area("Conteúdo (cole o texto do e-mail recebido)")
        col1, col2 = st.columns(2)
        data_recebimento = col1.date_input("Data de recebimento")
        escolhidas = col2.multiselect(
            "Unidade(s) responsável(is)",
            options=[u["id"] for u in unidades_ativas],
            format_func=lambda uid: nomes_unidades[uid],
        )
        if st.form_submit_button("Cadastrar ouvidoria"):
            if not conteudo or not escolhidas:
                st.error("Preencha o conteúdo e ao menos uma unidade responsável.")
            else:
                st.session_state.ouvidorias.append({
                    "id": st.session_state.proximo_id_ouvidoria,
                    "conteudo": conteudo,
                    "data_recebimento": str(data_recebimento),
                    "unidades": escolhidas,
                    "status": "recebida",
                    "criado_por": email,
                    "resposta": None,
                    "respondido_por": None,
                    "documentos": [],
                })
                st.session_state.proximo_id_ouvidoria += 1
                st.success("Ouvidoria cadastrada.")
                st.rerun()

visiveis = [o for o in st.session_state.ouvidorias if pode_ver(o)]
colunas = {"recebida": [], "em_atendimento": [], "concluida": []}
for o in visiveis:
    colunas[o["status"]].append(o)

st.divider()
col_r, col_a, col_c = st.columns(3)
for coluna, titulo, itens in [
    (col_r, "Recebida", colunas["recebida"]),
    (col_a, "Em atendimento", colunas["em_atendimento"]),
    (col_c, "Concluída", colunas["concluida"]),
]:
    with coluna:
        st.markdown(f"**{titulo}** ({len(itens)})")
        for o in itens:
            with st.container(border=True):
                st.write(o["conteudo"][:110] + ("…" if len(o["conteudo"]) > 110 else ""))
                st.caption(f"{o['data_recebimento']} · {', '.join(nomes_unidades[uid] for uid in o['unidades'])}")
                if st.button("Abrir", key=f"abrir_{o['id']}"):
                    st.query_params["id"] = str(o["id"])
                    st.rerun()
