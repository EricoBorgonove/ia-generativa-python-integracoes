
class RAGNotConfiguredError(Exception):
    """O mecanismo RAG ainda não foi conectado."""


def consultar_documentos(pergunta):
    """
    Integração com o RAG desenvolvido na aula 5.

    Deve retornar um dicionário contendo:
    - fonte
    - pergunta
    - trechos
    """

    raise RAGNotConfiguredError(
        "Integre aqui a função de recuperação "
        "documental desenvolvida na aula 5."
    )
