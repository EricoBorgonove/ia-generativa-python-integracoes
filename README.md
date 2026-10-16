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

## Modelo local

Com o Ollama instalado, obtenha o modelo padrão:

```powershell
ollama pull llama3.1:8b
```

Mantenha o serviço Ollama ativo. Se ele não estiver em execução, inicie-o com
`ollama serve` em outro terminal.

`config.py` lê as variáveis de ambiente `OLLAMA_MODEL` e `OLLAMA_HOST`.
Os padrões são `llama3.1:8b` e `http://localhost:11434`.
Para alterá-los na sessão atual do PowerShell:

```powershell
$env:OLLAMA_MODEL = "llama3.1:8b"
$env:OLLAMA_HOST = "http://localhost:11434"
```

O projeto não carrega arquivos `.env` automaticamente.

## Banco de atendimentos

Para criar a tabela e inserir oito atendimentos demonstrativos em um banco vazio:

```powershell
.\.venv\Scripts\python.exe v08_criar_banco.py
```

O banco fica em `data/atendimentos.db`. O script preserva registros existentes
quando a tabela já contém dados. O serviço de consultas também cria a tabela
quando necessário, mas não insere os exemplos automaticamente.

Os arquivos SQLite e seus auxiliares são ignorados pelo Git e permanecem locais.
