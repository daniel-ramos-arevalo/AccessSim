# AccessSim

> **README**
> Use este documento como guia inicial para configurar e executar o projeto.

## Objetivo do projeto

Este projeto foi criado com o intuito de divulgar os serviços da empresa AccessSim, proporcionando informações sobre seu trabalho e soluções para a arquitetura contemporânea.

Este projeto atinge este objetivo fornecendo um site single page contando em detalhes sobre como a empresa opera e proporcionando um formulário para a captura de leads.

## Funcionalidades
- Descrição em blocos de diversos aspectos da AccessSim.
- Navegação automatizada através de componentes HTML.
- Formulário para captura de leads.
- Gerenciamento de tabelas através de página admin.

## Como configurar o projeto pela primeira vez

### 1. Instalar dependências

Recomenda-se usar um ambiente virtual (venv) Python.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Definir variáveis de ambiente no arquivo `.env`

Crie um arquivo `.env` na raiz do projeto (`AccessSim/.env`) e configure as variáveis do banco de dados.

```env
DB_NAME=nome_do_banco
DB_USER=usuario_do_banco
DB_PASSWORD=senha_do_banco
DB_HOST=localhost
DB_PORT=5432
DJANGO_KEY=sua_chave
```

O arquivo `AccessSim/main/settings.py` usa essas variáveis para conectar ao PostgreSQL.

Recomenda-se o uso do pgAdmin4 para gerenciar o banco de dados.

### 3. Aplicar migrações do Django

Dentro da pasta `AccessSim`, execute:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Estes comandos irão criar as tabelas dentro do PostgreSQL.

### 4. Criar superusuário

Crie um superusuário para acessar o Django Admin:

```bash
python3 manage.py createsuperuser
```
Após isto, digite as informações solicitadas no terminal para criar o superusuário.

Essas informações erão usadas para o login na página admin do Django, sendo acessada pela rota /admin.

### 5. Executar o seed de dados iniciais

O script `seed_origins.py` insere valores base na tabela `origin`.

```bash
python3 seed_origins.py
```
Estes valores são opcionais e podem ser alterados mais tarde através da página admin ou manipulação direta do SQL com o pgAdmin4.

### 6. Executar o projeto

Vá até a pasta principal do Django e inicie o servidor:

```bash
cd AccessSim
python3 manage.py runserver
```

Acesse `http://127.0.0.1:8000/` no navegador.
A página padrão está definida como `http://127.0.0.1:8000/home`

### 7. Acesse a API ou Admin

Para conseguir acesso ao gerenciamento de todas as tabelas com uma interface interativa, acesse `http://127.0.0.1:8000/admin` com as credenciais feitas ao utilizar o comando `python3 manage.py createsuperuser`

As páginas de requisição da API podem ser acessadas apenas após o login como admin:
- `http://127.0.0.1:8000/api` - root da API
- `http://127.0.0.1:8000/api/schema` - schema completo como arquivo
- `http://127.0.0.1:8000/api/docs` - documentação da API 

Apenas requisições GET são permitidas nesta interface. A inserção de dados está reservada unicamente para o formulário e painel admin do Django.

## Ações para fazer o projeto funcionar em qualquer computador

1. Fazer fork do repositório no GitHub.
2. Clonar o fork localmente.
3. Entrar na pasta do projeto.
4. Criar e ativar um ambiente virtual.
5. Instalar dependências com `pip install -r requirements.txt`.
6. Configurar PostgreSQL localmente.
7. Criar o banco de dados e o usuário PostgreSQL compatíveis com o `.env`.
8. Criar o arquivo `.env` com as variáveis de conexão.
9. Executar `python3 manage.py migrate`.
10. Criar o superusuário com `python3 manage.py createsuperuser`.
11. Executar `python3 seed_origins.py`.
12. Iniciar o servidor Django com `python3 manage.py runserver`.

## Erros comuns

- `psycopg2` não encontrado: verifique se o ambiente virtual está ativado e `pip install -r requirements.txt` foi executado.
- Erro de conexão com o banco: confira as variáveis `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` e `DB_PORT` no `.env`.
- `django.core.exceptions.ImproperlyConfigured`: o arquivo `.env` pode não estar sendo carregado ou a variável está faltando.
- `Permission denied` ao rodar `manage.py`: verifique permissões e se o comando está sendo executado com o Python correto.
- Falha em criar superusuário: use um e-mail e senha válidos e certifique-se de que as migrações foram aplicadas.
- Erro `module 'django' has no attribute ...`: o ambiente virtual pode estar desativado ou o Django instalado está na versão errada.

## Observações

- O projeto usa PostgreSQL como banco de dados.
- Se necessário, adapte a configuração para outro banco alterando `main/settings.py`.
- Mantenha o `.env` fora do controle de versão para proteger credenciais.

## Créditos

### Desenvolvedores:
- Daniel Ramos Arévalo
Criação da API; Criação do HTML e CSS; Implementação do Django; Implementação de API; Conexão com Postgres.

- Ângelo Vieira de Souza
Criação do Banco de Dados; Implementação do Banco de Dados; Criação do Backlog do Produto; Teste final do produto;

- Daniela Regina Santos Oliveira 
Criação do Banco de Dados; Implementação do Banco de Dados; Teste final do produto.

- Rafaela Palácios da Silva Chaves
Criação dos Wireframes; Definição do CSS; Implementação de Responsividade.
 

### Orientador(es)
- Catuxe Varjão
- Cristiane Oliveira de Santana
- Josiane de Nazaré
