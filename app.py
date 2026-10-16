
import streamlit as st

from core.assistant import responder

st.set_page_config(
    page_title="Assistente IA - Aula 6",
    page_icon="🤖",
    layout="wide"
)

# Estado inicial da aplicação
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Barra lateral
with st.sidebar:
    st.title("⚙️ Configurações")

    modo = st.selectbox(
        "Fonte de informação",
        [
            "Automático",
            "Clima",
            "Banco de dados",
            "Documentos (RAG)",
            "Conhecimento geral"
        ]
    )

    cidade = st.selectbox(
        "Cidade para consultas meteorológicas",
        [
            "Não selecionada",
            "Manaus",
            "Belém",
            "Curitiba"
        ]
    )

    cidade_escolhida = (
        None if cidade == "Não selecionada"
        else cidade
    )

    st.divider()

    if st.button(
        "🗑️ Nova conversa",
        use_container_width=True
    ):
        st.session_state.mensagens = []
        st.rerun()

    st.caption("Curso: IA Generativa com Python")
    st.caption("Aula 6 — Integrações Externas")

# Cabeçalho
st.title("🤖 Assistente Inteligente")
st.write(
    "Consulte informações meteorológicas, "
    "atendimentos, documentos e o modelo local."
)

st.info(f"Fonte selecionada: {modo}")

# Exibir histórico
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

        if mensagem.get("fonte"):
            st.caption(
                f"Fonte: {mensagem['fonte']}"
            )

# Entrada do usuário
pergunta = st.chat_input(
    "Digite sua pergunta..."
)

if pergunta:
    # Exibir pergunta
    with st.chat_message("user"):
        st.markdown(pergunta)

    # Preparar histórico anterior
    historico = [
        {
            "role": item["role"],
            "content": item["content"]
        }
        for item in st.session_state.mensagens
    ]

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    # Consultar fonte e LLM
    with st.chat_message("assistant"):
        with st.spinner(
            "Consultando fontes e gerando resposta..."
        ):
            try:
                resultado = responder(
                    pergunta=pergunta,
                    modo=modo,
                    cidade=cidade_escolhida,
                    historico=historico[-8:]
                )

                resposta = resultado["resposta"]
                fonte = resultado["fonte"]

                st.markdown(resposta)
                st.caption(f"Fonte: {fonte}")

            except Exception as erro:
                # Detalhes técnicos não são exibidos
                # na interface destinada ao usuário.
                print(
                    "Erro de integração:",
                    repr(erro)
                )

                resposta = (
                    "Não foi possível concluir a consulta. "
                    "Verifique o serviço selecionado."
                )
                fonte = None

                st.error(resposta)

    # Registrar resposta no histórico
    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta,
        "fonte": fonte
    })
