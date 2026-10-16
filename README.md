# Assistente IA — Integrações externas

Prática de IA generativa com Python que reúne consultas meteorológicas da
Open-Meteo, atendimentos em SQLite e respostas de um modelo local via Ollama.
A interface principal usa Streamlit; os scripts `v01` a `v13` apresentam
exemplos progressivos para execução no terminal.

## Instalação no Windows

É necessário ter Python com suporte às dependências de `requirements.txt`
e Ollama instalado para gerar respostas. O ambiente local foi criado com Python 3.13.

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Os comandos usam diretamente o Python do ambiente e dispensam sua ativação.
