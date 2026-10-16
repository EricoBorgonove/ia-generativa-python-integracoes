
import re
import unicodedata

from core.source_router import identificar_fonte

from services.weather_service import consultar_clima
from services.database_service import (
    resumo_atendimentos,
    listar_atendimentos
)
from services.rag_service import consultar_documentos
from services.llm_service import gerar_resposta


CIDADES_TESTE = ["Manaus", "Belém", "Curitiba"]

MODOS = {
    "Automático": "automatico",
    "Clima": "clima",
    "Banco de dados": "banco",
    "Documentos (RAG)": "rag",
    "Conhecimento geral": "geral"
}


def normalizar(texto):
    texto = unicodedata.normalize(
        "NFKD", texto.lower()
    )
    return "".join(
        c for c in texto
        if not unicodedata.combining(c)
    )


def identificar_cidade(pergunta):
    texto = normalizar(pergunta)

    for cidade in CIDADES_TESTE:
        padrao = rf"\b{re.escape(normalizar(cidade))}\b"

        if re.search(padrao, texto):
            return cidade

    return None


def resolver_fonte(pergunta, modo):
    if modo != "Automático":
        return MODOS[modo]

    return identificar_fonte(pergunta)


def consultar_fonte(pergunta, fonte, cidade=None):
    dados = {}

    if fonte in ("clima", "multipla"):
        cidade = cidade or identificar_cidade(pergunta)

        if not cidade:
            raise ValueError(
                "Informe uma cidade na barra lateral "
                "ou escreva Manaus, Belém ou Curitiba."
            )

        dados["clima"] = consultar_clima(
            cidade,
            dias=5
        )

    if fonte in ("banco", "multipla"):
        dados["banco"] = {
            "resumo": resumo_atendimentos(),
            "registros": listar_atendimentos(100)
        }

    if fonte == "rag":
        dados["documentos"] = consultar_documentos(
            pergunta
        )

    return dados if dados else None


def responder(pergunta, modo, cidade=None, historico=None):
    fonte = resolver_fonte(pergunta, modo)

    dados = consultar_fonte(
        pergunta,
        fonte,
        cidade
    )

    resposta = gerar_resposta(
        pergunta=pergunta,
        dados=dados,
        historico=historico
    )

    nomes = {
        "clima": "Open-Meteo",
        "banco": "SQLite",
        "rag": "RAG",
        "multipla": "Open-Meteo + SQLite",
        "geral": "Ollama"
    }

    return {
        "resposta": resposta,
        "fonte": nomes.get(fonte, "Ollama"),
        "dados": dados
    }
