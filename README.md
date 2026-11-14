# Empório Gralha Azul

Loja virtual fictícia de produtos artesanais e regionais do Paraná. Projeto de portfólio em desenvolvimento.

> **Aviso:** a loja, os produtos e os produtores são fictícios. Os pagamentos serão simulados.

## Sobre o projeto

O Empório Gralha Azul reúne produtos que carregam a identidade do estado, do pinhão aos Campos Gerais, das colônias imigrantes à culinária regional. O objetivo é construir uma loja completa e navegável, com catálogo, produtores parceiros, carrinho e pedidos, mostrando um front-end e um back-end organizados.

## Tecnologias

- **Back-end:** Python + FastAPI + SQLAlchemy + Alembic
- **Banco de dados:** PostgreSQL (Supabase)
- **Front-end (planejado):** React + Tailwind CSS

## Status

- [x] Planejamento: telas, catálogo e modelagem do banco
- [x] API inicial com FastAPI
- [x] Conexão com PostgreSQL no Supabase
- [x] Tabelas criadas com migrações (Alembic)
- [ ] Cadastro de categorias, produtores e produtos
- [ ] Rotas do catálogo
- [ ] Front-end
- [ ] Autenticação, carrinho e pedidos
- [ ] Deploy

## Documentação

- [Telas e navegação do site](docs/telas.md)
- [Modelagem do banco de dados](docs/modelagem.md)
- [Catálogo inicial de produtos](docs/catalogo-inicial.md)

## Como rodar o back-end

Requisitos: Python 3.13 ou superior e um banco PostgreSQL (o projeto usa o Supabase).

```bash
git clone https://github.com/dudatrento/emporio-gralha-azul.git
cd emporio-gralha-azul/backend

python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# edite o .env e preencha DATABASE_URL

alembic upgrade head
uvicorn main:app --reload
```

A API fica em `http://127.0.0.1:8000`, e a documentação automática em `http://127.0.0.1:8000/docs`.