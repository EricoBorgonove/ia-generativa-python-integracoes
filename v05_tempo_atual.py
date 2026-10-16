
import httpx

# Coordenadas aproximadas de Manaus
LATITUDE = -3.12
LONGITUDE = -60.02

URL = "https://api.open-meteo.com/v1/forecast"

parametros = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "current": [
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature",
        "precipitation",
        "weather_code",
        "wind_speed_10m"
    ],
    "timezone": "America/Manaus"
}

try:
    resposta = httpx.get(
        URL,
        params=parametros,
        timeout=15.0
    )

    resposta.raise_for_status()

    dados = resposta.json()
    atual = dados["current"]

    print("\n=== TEMPO ATUAL EM MANAUS ===")
    print("Horário:", atual["time"])
    print("Temperatura:", atual["temperature_2m"], "°C")
    print("Sensação:", atual["apparent_temperature"], "°C")
    print("Umidade:", atual["relative_humidity_2m"], "%")
    print("Precipitação:", atual["precipitation"], "mm")
    print("Vento:", atual["wind_speed_10m"], "km/h")
    print("Código meteorológico:", atual["weather_code"])

except httpx.HTTPError as erro:
    print("Falha na requisição:", erro)

except (KeyError, ValueError) as erro:
    print("Resposta inesperada da API:", erro)
