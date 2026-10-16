
import re
import unicodedata


PALAVRAS_CLIMA = [
    "clima",
    "tempo",
    "temperatura",
    "chuva",
    "chover",
    "previsao",
    "umidade",
    "vento"
]

PALAVRAS_BANCO = [
    "atendimento",
    "atendimentos",
    "pendente",
    "pendentes",
    "concluido",
    "concluidos",
    "categoria",
    "categorias",
    "chamado",
    "chamados"
]


def normalizar(texto):
    texto = unicodedata.normalize(
        "NFKD",
        texto.lower()
    )

    return "".join(
        caractere
        for caractere in texto
        if not unicodedata.combining(caractere)
    )


def contem_palavra(texto, palavras):
    return any(
        re.search(
            rf"\b{re.escape(palavra)}\b",
            texto
        )
        for palavra in palavras
    )


def identificar_fonte(pergunta):
    texto = normalizar(pergunta)

    eh_clima = contem_palavra(
        texto,
        PALAVRAS_CLIMA
    )

    eh_banco = contem_palavra(
        texto,
        PALAVRAS_BANCO
    )

    if eh_clima and eh_banco:
        return "multipla"

    if eh_clima:
        return "clima"

    if eh_banco:
        return "banco"

    return "geral"
