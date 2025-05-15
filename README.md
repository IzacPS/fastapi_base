# FastAPI Base Project

🚀 **Base pronta para iniciar projetos com FastAPI, SQLAlchemy e Alembic.**  
Ideal para quem quer pular a configuração inicial e focar direto no desenvolvimento da aplicação.

---

## 🧱 Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/) — Web framework moderno e rápido
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM para banco de dados
- [Alembic](https://alembic.sqlalchemy.org/) — Migrações de banco de dados
- [Uvicorn](https://www.uvicorn.org/) — Servidor ASGI leve e rápido
- [Pydantic](https://docs.pydantic.dev/) — Validação de dados com Python moderno

---

## 📁 Estrutura do Projeto

```
fastapi_base/
├── app/
│ ├── api/ # Rotas da API
│ ├── core/ # Configurações principais (DB, settings)
│ ├── crud/ # Operações com o banco de dados
│ ├── db/ # Configurações do banco de dados
│ ├── models/ # Modelos SQLAlchemy
│ ├── schemas/ # Schemas Pydantic
│ ├── tests/ # Regras de negócio
│ ├── __init__.py
│ ├── main.py # Ponto de entrada da aplicação
├── migrations/ # Diretório de migrações
├── .gitignore
├── README.md
├── alembic.ini # Configuração do Alembic
├── requirements.txt # Dependências do projeto
```
---

## ▶️ Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/IzacPS/fastapi_base.git
cd fastapi_base
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\activate.ps1 ou .\venv\Scripts\activate.cmd
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Edite o arquivo *.env* ou defina as variáveis de ambiente:
```bash
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

### 5. Execute as migrações

```bash
alembic upgrade head
```

### 6. Inicie o servidor

```bash
uvicorn app:server --reload
```

## 🛠️ Funcionalidades prontas
- Configuração básica do projeto com FastAPI
- Conexão com banco de dados via SQLAlchemy
- Migração de schemas com Alembic
- Organização modular da aplicação
- Separação entre models, schemas e rotas

## 📄 Licença
Este projeto está licenciado sob os termos da Licença MIT.
