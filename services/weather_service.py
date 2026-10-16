
import httpx

from services.geocoding_service import buscar_cidades

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


class WeatherServiceError(Exception):
    """Falha na consulta meteorológica."""


def consultar_clima(cidade, dias=5):
    if not 1 <= dias <= 16:
        raise ValueError("Informe entre 1 e 16 dias.")

    # 1. Localizar a cidade
    locais = buscar_cidades(cidade, limite=1)

    if not locais:
        raise WeatherServiceError(
            f"Cidade não encontrada: {cidade}"
        )

    local = locais[0]

    # 2. Preparar parâmetros da previsão
    parametros = {
        "latitude": local["latitude"],
        "longitude": local["longitude"],
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "weather_code",
            "wind_speed_10m"
        ],
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "precipitation_probability_max",
            "weather_code"
        ],
        "timezone": local.get("timezone") or "auto",
        "forecast_days": dias
    }

    # 3. Consultar API
    try:
        resposta = httpx.get(
            WEATHER_URL,
            params=parametros,
            timeout=15.0
        )
        resposta.raise_for_status()
        dados = resposta.json()

        atual = dados["current"]
        diario = dados["daily"]

    except (httpx.HTTPError, ValueError, KeyError) as erro:
        raise WeatherServiceError(
            f"Não foi possível obter a previsão: {erro}"
        ) from erro

    # 4. Organizar a previsão diária
    previsao = []

    for i, data in enumerate(diario["time"]):
        previsao.append({
            "data": data,
            "maxima": diario["temperature_2m_max"][i],
            "minima": diario["temperature_2m_min"][i],
            "precipitacao_mm": diario["precipitation_sum"][i],
            "probabilidade_chuva": diario[
                "precipitation_probability_max"
            ][i],
            "codigo_tempo": diario["weather_code"][i]
        })

    # 5. Retornar dados padronizados
    return {
        "cidade": local["nome"],
        "estado": local["estado"],
        "pais": local["pais"],
        "fonte": "Open-Meteo",
        "consulta_atual": {
            "horario": atual["time"],
            "temperatura": atual["temperature_2m"],
            "sensacao_termica": atual["apparent_temperature"],
            "umidade": atual["relative_humidity_2m"],
            "vento": atual["wind_speed_10m"],
            "codigo_tempo": atual["weather_code"]
        },
        "previsao": previsao
    }
