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

## Execução

Para abrir a interface:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Selecione a fonte de informação e, para clima, uma cidade na barra lateral
ou informe Manaus, Belém ou Curitiba na pergunta. Exemplos:

- Como está o clima em Manaus?
- Quantos atendimentos estão pendentes?
- Qual é a previsão para Curitiba e quantos chamados estão pendentes?

No modo automático, o roteador identifica clima e atendimentos por palavras-chave;
perguntas sem essas palavras seguem para conhecimento geral do modelo.

Para usar o chat de terminal:

```powershell
.\.venv\Scripts\python.exe v13_chat_integrado.py
```

Digite `sair` para encerrar. Consultas meteorológicas precisam de acesso à internet;
a geração de respostas depende do serviço e do modelo Ollama disponíveis.

## Organização e limites

- `app.py`: interface Streamlit e histórico da conversa na sessão.
- `config.py`: configuração do endereço e modelo Ollama.
- `core/assistant.py`: coordenação das fontes e respostas.
- `core/source_router.py`: seleção de fontes por palavras-chave.
- `services/`: geocodificação, clima, atendimentos, modelo e ponto de integração RAG.
- `database/`: conexão SQLite e criação da tabela.
- `v01_*.py` a `v13_*.py`: exemplos progressivos e roteiros de consulta manual.

A opção Documentos (RAG) exige implementar `consultar_documentos` em
`services/rag_service.py`. Atualmente ela lança `RAGNotConfiguredError`;
a recuperação documental ainda não está conectada.

Os scripts com `teste` no nome são roteiros manuais e podem consultar serviços
externos ou depender do banco preparado. Eles não constituem uma suíte automatizada.

O `.gitignore` exclui ambientes virtuais, caches, bancos locais, segredos,
relatórios de cobertura, artefatos de build, logs e arquivos locais de editores.
Os exemplos `.env.example` e `.env.sample` podem ser versionados.
