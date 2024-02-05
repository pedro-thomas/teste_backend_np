# Gestão de Propriedades - NICEPLANET

## Sobre o Projeto

Este projeto é um sistema de gestão de propriedades desenvolvido com Django e Django Rest Framework, focado no monitoramento ambiental de propriedades rurais. Ele permite o cadastro e gerenciamento de propriedades, produtores e o registro de histórico de buscas de propriedades pelo número do CAR (Cadastro Ambiental Rural).

### Principais Funcionalidades

- Visualização e edição de propriedades.
- Listagem de propriedades com opção de detalhamento.
- Listagem de produtores.
- Registro e listagem de histórico de buscas por número do CAR.
- Autenticação de usuários com sistema de login e logout.

## Tecnologias Utilizadas

- **Backend**: Django e Django Rest Framework
- **Frontend**: Bootstrap para o design das páginas
- **Banco de Dados**: MySQL
- **Autenticação**: Sistema de autenticação do Django com suporte a JWT para APIs

## Configuração do Ambiente

### Pré-requisitos

- Python 3.10 ou superior
- Pip (Gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)
- MySQL Server

### Instalação

1. Clone o repositório do projeto:
   git clone <url-do-repositorio>

2. Crie um ambiente virtual e ative-o:
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

3. Instale as dependências do projeto:
pip install -r requirements.txt

4. Configure o banco de dados MySQL no settings.py do projeto (teste_backend):

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_usuario',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Execute as migrações para criar as tabelas no banco de dados:
python manage.py migrate

6. Crie um superusuário para acessar o painel administrativo:
python manage.py createsuperuser

7. Inicie o servidor de desenvolvimento:
python manage.py runserver
Acesse o projeto em http://127.0.0.1:8000/.

README criado por Pedro Thomas para o projeto Gestão de Propriedades - NICEPLANET.