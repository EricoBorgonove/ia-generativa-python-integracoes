
import httpx

URL = "https://api.open-meteo.com/v1/forecast"

parametros = {
    "latitude": -3.12,
    "longitude": -60.02,
    "daily": [
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "precipitation_probability_max",
        "weather_code"
    ],
    "timezone": "America/Manaus",
    "forecast_days": 5
}

try:
    resposta = httpx.get(
        URL,
        params=parametros,
        timeout=15.0
    )
    resposta.raise_for_status()

    dados = resposta.json()
    diario = dados["daily"]

    print("\n=== PREVISÃO PARA MANAUS ===")

    for i, data in enumerate(diario["time"]):
        print(f"\nData: {data}")

        print(
            "Máxima:",
            diario["temperature_2m_max"][i],
            "°C"
        )

        print(
            "Mínima:",
            diario["temperature_2m_min"][i],
            "°C"
        )

        print(
            "Precipitação:",
            diario["precipitation_sum"][i],
            "mm"
        )

        print(
            "Probabilidade de chuva:",
            diario["precipitation_probability_max"][i],
            "%"
        )

except (httpx.HTTPError, KeyError, ValueError) as erro:
    print("Erro ao consultar previsão:", erro)
