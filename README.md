# Aplicação Web de Análise de Sentimento com Django

## Autor

- [*Gustavo Rodrigues Ribeiro*](https://github.com/GustavooRibas)

## Visão Geral

Este projeto é uma aplicação web simples desenvolvida utilizando o framework Django. O objetivo principal é permitir que usuários autenticados submetam blocos de texto para análise de sentimento. A aplicação processa o texto e retorna uma classificação (Positivo, Negativo ou Neutro) acompanhada de uma pontuação numérica de polaridade.

A análise de sentimento é realizada utilizando a biblioteca de Processamento de Linguagem Natural (PLN) **TextBlob**. O frontend foi construído com HTML, CSS (utilizando **Bootstrap 5.3** para estilização responsiva) e um pouco de JavaScript para interatividade básica.

Este projeto foi desenvolvido como parte de um processo seletivo para estágio na área de tecnologia.

## Funcionalidades Principais

*   **Autenticação de Usuários:** Sistema seguro de login e logout baseado no `django.contrib.auth`. Apenas usuários autenticados podem acessar a funcionalidade de análise.
*   **Submissão de Texto:** Interface com formulário para que o usuário insira o texto a ser analisado.
*   **Análise de Sentimento:**
    *   Utiliza a biblioteca `TextBlob` para calcular a polaridade do texto.
    *   Classifica o sentimento em:
        *   **Positivo:** Polaridade > 0.1
        *   **Negativo:** Polaridade < -0.1
        *   **Neutro:** Polaridade entre -0.1 e 0.1 (inclusive)
    *   Exibe a **pontuação de polaridade** numérica (variando de -1.0 a +1.0).
*   **Interface do Usuário:**
    *   Design limpo e responsivo utilizando **Bootstrap 5.3** (via CDN).
    *   Navegação clara com indicação do status de login do usuário.
    *   Exibição clara dos resultados da análise.

## Tecnologias Utilizadas

*   **Backend:**
    *   **Python:** Versão 3.8+
    *   **Django:** Framework Web (versão 4.x, ver `requirements.txt`)
    *   **TextBlob:** Biblioteca para PLN e Análise de Sentimento
    *   **Pillow:** Biblioteca de processamento de imagem (dependência comum)
*   **Frontend:**
    *   **HTML5:** Estrutura das páginas
    *   **CSS3:** Estilização (principalmente via Bootstrap)
    *   **Bootstrap:** Framework CSS/JS (versão 5.3, via CDN)
    *   **JavaScript:** Para funcionalidades do Bootstrap e pequenas interações
*   **Banco de Dados:**
    *   **SQLite3:** Banco de dados padrão do Django para desenvolvimento (simples, baseado em arquivo)
*   **Ambiente e Ferramentas:**
    *   **venv:** Gerenciamento de ambiente virtual (recomendado)
    *   **pip:** Gerenciador de pacotes Python

## Estrutura do Projeto

```
sentiment_analysis_project/
├── manage.py                   # Arquivo de gerenciamento
├── requirements.txt
├── venv/                       # Ambiente virtual (não mexa diretamente)
├── sentiment_project/          # Pasta de CONFIGURAÇÃO do projeto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Arquivo principal de configurações
│   ├── urls.py                 # Arquivo principal de URLs
│   └── wsgi.py
└── sentiment_app/              # Pasta do Aplicativo
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```


## Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados em seu sistema:

**Python 3.8 ou superior:** Verifique com `python --version` ou `python3 --version`.
**pip:** O gerenciador de pacotes do Python (geralmente vem com Python). Verifique com `pip --version`.
**Git:** (Opcional) Para clonar o repositório, se aplicável.

## Como Executar o Projeto

Siga estas etapas para configurar e executar o projeto localmente:

### 1. **Obtenha o Código Fonte:**

Clone o repositório (se disponível):

```bash
git clone <URL_DO_REPOSITORIO> sentiment_analysis_project
```

Ou descompacte o arquivo `.zip` fornecido em um local de sua escolha.

### 2. **Navegue até o Diretório do Projeto:**

Abra seu terminal ou prompt de comando e navegue até a pasta raiz do projeto (a pasta que contém o arquivo `manage.py`).

```bash
cd path/to/sentiment_analysis_project
```

### 3. **Crie um ambiente virtual (opcional, mas recomendado)**

*    No repositório do projeto:

Criando ambiente virtual:

```bash
python -m venv venv
```

*    Acessando ambiente virtual:

Em Sistemas Unix:

```bash
source venv/bin/activate
```

Em Sistemas Windows (CMD):

```bash
venv\Scripts\activate
```

### 4. **Instale as Dependências:**

Utilize o arquivo `requirements.txt` incluso:

```bash
pip install -r requirements.txt
```

### 5. **Baixe os Dados do TextBlob:**

Execute o seguinte comando para baixar os córpus linguísticos necessários para o TextBlob:

```bash
python -m textblob.download_corpora
```

Siga as instruções no terminal (geralmente, baixar "corpora" é suficiente).
*Observação:* Pode ser necessário executar como administrador/`sudo` se ocorrerem erros de permissão.

### 6. **Aplique as Migrações do Banco de Dados:**

Este comando cria as tabelas necessárias no banco de dados (arquivo `db.sqlite3`) para o Django (incluindo o sistema de autenticação).

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. **Crie um Superusuário (Administrador):**

Você precisará de um usuário para fazer login. Crie um superusuário:

```bash
python manage.py createsuperuser
```

Siga as instruções para definir um nome de usuário, e-mail (opcional) e senha.

### 8. **Execute a Aplicação**

1.  **Inicie o Servidor de Desenvolvimento:**
    *   Certifique-se de que seu ambiente virtual esteja ativo e que você esteja no diretório raiz do projeto.
    *   Execute o comando:
        ```bash
        python manage.py runserver
        ```

2.  **Acesse a Aplicação:**
    *   Abra seu navegador web e acesse o endereço: `http://127.0.0.1:8000/`
    *   O servidor local do Django estará rodando e servindo a aplicação.

3.  **Parando o Servidor:**
    *   Volte ao terminal onde o servidor está rodando e pressione `CTRL + C`.

## Como Usar a Aplicação

1.  Ao acessar `http://127.0.0.1:8000/`, você será redirecionado para a página de **Login**.
2.  Insira as credenciais (nome de usuário e senha) do **superuser** criado durante a instalação.
3.  Após o login bem-sucedido, você será direcionado para a página principal de **Análise de Sentimento**.
4.  Na caixa de texto "Texto para Análise", digite ou cole o texto que deseja analisar.
5.  Clique no botão **"Analisar Sentimento"**.
6.  A página será recarregada e, abaixo do formulário, um card exibirá:
    *   O texto original que foi analisado.
    *   O **Sentimento** classificado (Positivo, Negativo ou Neutro), destacado com uma cor correspondente (verde, vermelho ou cinza).
    *   A **Pontuação de Polaridade** numérica exata calculada pelo TextBlob.
7.  Para sair da aplicação, clique no botão **"Sair"** na barra de navegação superior. Você será redirecionado de volta para a página de Login.

## Possíveis Melhorias e Próximos Passos

Esta aplicação serve como uma base funcional. Diversas melhorias e expansões podem ser consideradas:

*   **Integração com LLM (API):** Substituir ou adicionar a opção de usar uma API de um Modelo de Linguagem Grande (como OpenAI GPT, Google Gemini) para análise de sentimento, potencialmente oferecendo resultados mais contextuais e nuances.
*   **Histórico de Análises:**
    *   Criar um modelo Django (`AnalysisHistory`) para armazenar cada análise (usuário, texto, resultado, data/hora) no banco de dados.
    *   Adicionar uma página onde os usuários logados possam visualizar seu histórico de análises.
*   **Processamento Assíncrono:** Para análises mais demoradas (especialmente com APIs externas), implementar tarefas em background usando Celery e um message broker (como Redis ou RabbitMQ) para não bloquear a interface do usuário.
*   **Interface Aprimorada:**
    *   Utilizar AJAX para submeter o formulário e exibir resultados sem recarregar a página inteira.
    *   Adicionar indicadores visuais (spinners) durante o processamento da análise.
    *   Visualização de dados (ex: gráficos simples mostrando a distribuição de sentimentos no histórico).
*   **Testes Automatizados:** Escrever testes unitários e de integração usando o framework de testes do Django ou `pytest` para garantir a robustez e facilitar futuras modificações.
*   **Cadastro de Usuários:** Implementar um fluxo para que novos usuários possam se registrar na aplicação, em vez de depender apenas do superusuário.
*   **Tratamento de Erros:** Melhorar o feedback ao usuário em caso de falhas na análise ou problemas de comunicação com APIs externas.
*   **Deploy:** Preparar a aplicação para ser hospedada em um servidor de produção (ex: Heroku, PythonAnywhere, AWS EC2, Google Cloud App Engine), configurando um servidor WSGI (Gunicorn), gerenciamento de arquivos estáticos (Whitenoise) e variáveis de ambiente seguras.

## Troubleshooting Comum

*   **`ModuleNotFoundError: No module named 'sentiment_app'`:**
    *   Verifique se você está no diretório raiz do projeto (`sentiment_analysis_project`) ao executar `manage.py`.
    *   Confirme se a pasta `sentiment_app` existe no local correto.
    *   Verifique se `sentiment_app` contém um arquivo `__init__.py` (pode ser vazio).
    *   Confirme se `'sentiment_app.apps.SentimentAppConfig'` está corretamente listado em `INSTALLED_APPS` no arquivo `settings.py`.
    *   Certifique-se de que o ambiente virtual (`venv`) está ativo.
*   **Erro ao baixar córpus do TextBlob:**
    *   Verifique sua conexão com a internet.
    *   Tente executar o comando `python -m textblob.download_corpora` como administrador (Windows) ou com `sudo` (macOS/Linux).
*   **Página não encontrada (404):**
    *   Verifique se as URLs estão corretamente definidas em `sentiment_project/urls.py` e `sentiment_app/urls.py`.
    *   Certifique-se de que o servidor de desenvolvimento (`python manage.py runserver`) está em execução.

## Contato

- E-mail: gustavooriibeiro.ofc@hotmail.com
