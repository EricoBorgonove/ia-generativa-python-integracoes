
import httpx

BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"


class GeocodingError(Exception):
    """Erro ao consultar o serviço de geocodificação."""


def buscar_cidades(nome, limite=5):
    nome = nome.strip()

    if len(nome) < 2:
        raise ValueError(
            "O nome da cidade deve ter pelo menos 2 caracteres."
        )

    parametros = {
        "name": nome,
        "count": limite,
        "language": "pt",
        "countryCode": "BR"
    }

    try:
        resposta = httpx.get(
            BASE_URL,
            params=parametros,
            timeout=10.0
        )

        resposta.raise_for_status()
        dados = resposta.json()

    except (httpx.HTTPError, ValueError) as erro:
        raise GeocodingError(
            f"Falha na consulta de cidades: {erro}"
        ) from erro

    cidades = []

    for local in dados.get("results", []):
        cidades.append({
            "nome": local["name"],
            "estado": local.get("admin1"),
            "pais": local["country"],
            "latitude": local["latitude"],
            "longitude": local["longitude"],
            "timezone": local.get("timezone")
        })

    return cidades
