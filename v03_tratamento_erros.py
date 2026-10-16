
import httpx

URL = "https://geocoding-api.open-meteo.com/v1/search"


def buscar_cidade(nome):
    parametros = {
        "name": nome,
        "count": 5,
        "language": "pt",
        "countryCode": "BR"
    }

    try:
        resposta = httpx.get(
            URL,
            params=parametros,
            timeout=10.0
        )

        resposta.raise_for_status()

        dados = resposta.json()

        return dados.get("results", [])

    except httpx.TimeoutException:
        print("A API demorou para responder.")

    except httpx.HTTPStatusError as erro:
        print(
            "Erro HTTP:",
            erro.response.status_code
        )

    except httpx.RequestError as erro:
        print("Erro de conexão:", erro)

    except ValueError:
        print("A resposta não contém JSON válido.")

    return []


cidade = input("Informe a cidade: ").strip()

if len(cidade) < 2:
    print("Informe um nome válido.")
else:
    resultados = buscar_cidade(cidade)

    for local in resultados:
        print(
            local["name"],
            "-",
            local.get("admin1", "Sem estado"),
            "-",
            local["country"]
        )
