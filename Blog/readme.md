# Blog em Django

O **Blog em Django** é uma aplicação simples de blog desenvolvida com o framework Django e Python. Ele permite a criação, edição e visualização de postagens de blog, com uma interface administrativa que facilita o gerenciamento do conteúdo. A aplicação utiliza um banco de dados SQLite e foi projetada para ser simples e fácil de usar.

## Funcionalidades

- **Cadastro de Postagens**: Criação, edição e exclusão de posts através do painel de administração.
- **Exibição de Posts**: A página inicial lista os posts publicados, com links para acessar cada post individualmente.
- **Visualização Detalhada**: Cada post tem uma página dedicada exibindo o título, autor, data de publicação e conteúdo completo.
- **Interface de Administração**: O painel de administração do Django permite a gestão eficiente dos posts e usuários.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para o desenvolvimento da aplicação.
- **Python**: Linguagem de programação principal do projeto.
- **SQLite**: Banco de dados utilizado para armazenar os posts.
- **HTML/CSS**: Estrutura e estilização da interface do blog.
- **JavaScript** (opcional): Para funcionalidades interativas no front-end.

## Como Rodar o Projeto

1. Clone este repositório:
    ```bash
    git clone https://github.com/JoaoVictorSanta/Projetos/tree/main/Blog
    cd Blog
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

4. Crie um superusuário para acessar o painel de administração:
    ```bash
    python manage.py createsuperuser
    ```

5. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

6. Acesse o blog em seu navegador:
    - Página inicial: `http://127.0.0.1:8000/`
    - Admin: `http://127.0.0.1:8000/admin/`

## Objetivo do Projeto

O objetivo deste projeto é fornecer uma plataforma simples e eficaz para publicação e gerenciamento de conteúdo em um blog, com uma interface administrativa fácil de usar, que permite controle total sobre o conteúdo.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
