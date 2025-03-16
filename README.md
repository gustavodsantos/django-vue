# Django-Vue Project

Este projeto combina **Django** para o backend e **Vue.js** (com **Vuetify**) para o frontend, criando uma aplicação web moderna, escalável e de fácil manutenção. O projeto é configurado para ser executado em um ambiente **Docker**, com integração contínua via **GitHub Actions**.

---

## Tecnologias Utilizadas

### Backend
- **Django 5.1.7**: Framework web Python para desenvolvimento rápido e seguro.
- **Django REST Framework**: Para construção de APIs RESTful.
- **PostgreSQL**: Banco de dados relacional.
- **Gunicorn**: Servidor WSGI para produção.
- **Poetry**: Gerenciamento de dependências Python.

### Frontend
- **Vue.js 3**: Framework JavaScript progressivo para construção de interfaces de usuário.
- **Vuetify 3**: Biblioteca de componentes UI para Vue.js com Material Design.
- **Pinia**: Gerenciamento de estado para Vue.js.
- **Axios**: Cliente HTTP para consumir APIs.

### Ferramentas e Infraestrutura
- **Docker e Docker Compose**: Para conteinerização e orquestração de serviços.
- **GitHub Actions**: Para integração contínua (CI/CD).
- **Ruff**: Linting e formatação de código Python.
- **Pytest**: Framework de testes para Python.
- **Coverage**: Medição de cobertura de testes.

---

## Requisitos

- **Docker** e **Docker Compose** instalados.
- **Python 3.12** (para o backend).
- **Node.js 20** (para o frontend).

---

## Como Executar o Projeto

### 1. Configuração Inicial

Clone o repositório e navegue até o diretório do projeto:

```bash
git clone https://github.com/gustavodsantos/django-vue.git
cd django-vue
```

### 2. Configuração do Ambiente
Crie um arquivo `.env` na raiz do projeto, use `env-example` como exemplo para o arquivo.

### 3. Executando com Docker Compose
Suba os contêineres do backend, frontend e banco de dados:

```bash
docker-compose up -d --build
```

Após a inicialização, o projeto estará disponível em:

* http://localhost

* Em seguida crie um super usuário:

```bash
docker compose exec backend python manage.py createsuperuser
```
O **Adim do Django** estará disponivel em:

* http://localhost/admin

    
### 4. Executando Localmente (Sem Docker)

**Backend**
Instale as dependências do Poetry:

```bash
poetry install
```

Execute as migrações e inicie o servidor:

```bash
poetry run python manage.py migrate
poetry run python manage.py runserver
```

**Frontend**
Navegue até o diretório do frontend:

```bash
cd frontend/vuetify
```

Instale as dependências do Node.js:

```bash
npm install
```

Inicie o servidor de desenvolvimento:
```bash
npm run dev
```

**Testes e Linting**
O projeto utiliza `pytest` para testes e `ruff` para linting e formatação. Para executar os testes e verificar a qualidade do código:

```bash
poetry run task test  # Executa os testes com cobertura
poetry run task lint  # Verifica o linting
poetry run task format  # Formata o código
```

**Cobertura de Testes**
Após executar os testes, um relatório de cobertura será gerado em `htmlcov/`. Abra o arquivo `index.html` no navegador para visualizar o relatório.

**CI/CD**
O projeto está configurado com GitHub Actions para executar testes e linting automaticamente em cada push ou pull request para a branch `main`. 
O arquivo de configuração está em `.github/workflows/github_ci.yml.`

**Rotas da API**
O backend expõe as seguintes rotas da API:

* Listar Cursos: `GET /api/cursos/`

* Detalhes de um Curso: `GET /api/cursos/{id}/`

* Listar Usuários: `GET /api/users/`

* Admin do Django: `GET /admin/`

**Licença**
Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

**Desenvolvido por**
Gustavo Junior dos Santos

* Email: [gustavojuniordos@hotmail.com](mailto:gustavojuniordos@hotmail.com)

* LinkedIn: [gustavo junior dos santos](https://www.linkedin.com/in/gustavo-junior-dos-santos/)

* GitHub: [gustavodsantos](https://github.com/gustavodsantos/)

**Contribuições**
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
