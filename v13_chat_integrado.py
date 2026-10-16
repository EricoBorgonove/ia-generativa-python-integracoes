
import unicodedata

from core.source_router import identificar_fonte
from services.weather_service import (
    consultar_clima,
    WeatherServiceError
)
from services.geocoding_service import GeocodingError
from services.database_service import (
    resumo_atendimentos,
    listar_atendimentos
)
from services.llm_service import gerar_resposta


CIDADES_TESTE = [
    "Manaus",
    "Belém",
    "Curitiba"
]


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    return "".join(
        c for c in texto
        if not unicodedata.combining(c)
    )


def extrair_cidade(pergunta):
    texto = normalizar(pergunta)

    for cidade in CIDADES_TESTE:
        if normalizar(cidade) in texto:
            return cidade

    return None


def obter_dados(pergunta, fonte):
    dados = {}

    if fonte in ("clima", "multipla"):
        cidade = extrair_cidade(pergunta)

        if cidade is None:
            return None, (
                "Qual cidade deseja consultar? "
                "Nesta versão, utilize Manaus, "
                "Belém ou Curitiba."
            )

        dados["meteorologia"] = consultar_clima(
            cidade,
            dias=5
        )

    if fonte in ("banco", "multipla"):
        dados["atendimentos"] = {
            "resumo": resumo_atendimentos(),
            "registros": listar_atendimentos(
                limite=100
            )
        }

    return dados if dados else None, None


def executar_chat():
    historico = []

    print("\n=== ASSISTENTE INTELIGENTE ===")
    print("Digite 'sair' para encerrar.")

    while True:
        pergunta = input("\nVocê: ").strip()

        if pergunta.lower() == "sair":
            break

        if not pergunta:
            continue

        fonte = identificar_fonte(pergunta)

        print("Fonte selecionada:", fonte)

        try:
            dados, aviso = obter_dados(
                pergunta,
                fonte
            )

            if aviso:
                print("\nAssistente:", aviso)
                continue

            resposta = gerar_resposta(
                pergunta,
                dados=dados,
                historico=historico
            )

            print("\nAssistente:", resposta)

            historico.append({
                "role": "user",
                "content": pergunta
            })

            historico.append({
                "role": "assistant",
                "content": resposta
            })

        except (
            WeatherServiceError,
            GeocodingError,
            ValueError,
            KeyError
        ) as erro:
            print(
                "\nNão foi possível consultar a fonte:",
                erro
            )


if __name__ == "__main__":
    executar_chat()
