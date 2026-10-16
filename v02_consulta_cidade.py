
import httpx

URL = "https://geocoding-api.open-meteo.com/v1/search"

cidade = input("Digite o nome da cidade: ").strip()

if len(cidade) < 2:
    print("Digite pelo menos dois caracteres.")
else:
    parametros = {
        "name": cidade,
        "count": 5,
        "language": "pt",
        "countryCode": "BR"
    }

    resposta = httpx.get(
        URL,
        params=parametros,
        timeout=10.0
    )

    resposta.raise_for_status()
    dados = resposta.json()

    resultados = dados.get("results", [])

    if not resultados:
        print("Nenhuma cidade encontrada.")
    else:
        for local in resultados:
            print("----------------------")
            print("Cidade:", local["name"])
            print("Estado:", local.get("admin1"))
            print("País:", local["country"])
            print("Latitude:", local["latitude"])
            print("Longitude:", local["longitude"])
            print("Fuso horário:", local.get("timezone"))
