
import httpx
import json

URL = "https://httpbin.org/get"

resposta = httpx.get(URL, timeout=10.0)

print("Status HTTP:", resposta.status_code)

dados = resposta.json()

print(json.dumps(dados, indent=4, ensure_ascii=False))
