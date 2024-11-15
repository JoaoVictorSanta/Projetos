# Documentação da API de Feitiços

Este repositório contém uma API simples baseada no Flask, que serve uma lista de feitiços do universo Harry Potter. A API expõe dois endpoints principais para retornar informações sobre feitiços em formato JSON.

## Estrutura do Projeto

O projeto contém os seguintes arquivos e diretórios:

```
Spells_API/
├── app.py          # Arquivo principal da API utilizando Flask
├── spells.json     # Arquivo JSON com a lista de feitiços e seus detalhes
└── teste_API.py    # Script para testar a API
```

### Explicação dos Arquivos

- **app.py**: Contém a lógica principal da API Flask, que carrega os dados dos feitiços a partir de um arquivo JSON e os expõe por meio de endpoints HTTP.
- **spells.json**: Arquivo JSON que armazena a lista de feitiços, cada um com um `id`, `nome`, `efeito` e `dificuldade`.
- **teste_API.py**: Script de teste que faz requisições GET à API para buscar todos os feitiços ou um feitiço específico pelo seu ID.

## Endpoints da API

### 1. `/spells` [GET]
Este endpoint retorna uma lista de todos os feitiços disponíveis no sistema.

#### Resposta:
- **Código de Status**: 200 OK
- **Content-Type**: `application/json; charset=utf-8`
- **Corpo**: Uma lista de feitiços, cada um com `id`, `nome`, `efeito` e `dificuldade`.

Exemplo de Resposta:
```json
[
    {
        "id": 1,
        "nome": "Accio",
        "efeito": "Atrai o objeto desejado",
        "dificuldade": "Fácil"
    },
    {
        "id": 2,
        "nome": "Bombarda",
        "efeito": "Causa uma explosão",
        "dificuldade": "Médio"
    }
]
```

### 2. `/spells/<int:id>` [GET]
Este endpoint retorna os detalhes de um feitiço específico pelo seu `id`.

#### Parâmetros:
- `id`: O ID do feitiço a ser buscado.

#### Resposta:
- **Código de Status**: 
  - 200 OK se o feitiço for encontrado.
  - 404 Not Found se o feitiço com o ID fornecido não existir.
- **Content-Type**: `application/json; charset=utf-8`
- **Corpo**: Os detalhes do feitiço com `id`, `nome`, `efeito` e `dificuldade`.

Exemplo de Resposta (Sucesso):
```json
{
    "id": 1,
    "nome": "Accio",
    "efeito": "Atrai o objeto desejado",
    "dificuldade": "Fácil"
}
```

Exemplo de Resposta (Erro):
```json
{
    "error": "Feitiço não encontrado"
}
```

## Como Executar a API

### Pré-requisitos
- Python 3.7 ou superior
- Flask (Instale utilizando `pip install Flask`)

### Passos para Executar:

1. Clone o repositório para a sua máquina local:
   ```bash
   git clone https://github.com/seunome/Spells_API.git
   cd Spells_API
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install Flask
   ```

3. Execute a aplicação Flask:
   ```bash
   python app.py
   ```

   Por padrão, a API estará disponível em `http://127.0.0.1:5000`.

### Testando a API

Você pode usar o script `teste_API.py` para testar a API localmente:

1. Execute o script para ver os resultados:
   ```bash
   python teste_API.py
   ```

2. O script irá imprimir os resultados das requisições GET para buscar todos os feitiços e um feitiço específico (com o ID 1).

## Licença

Este projeto é open source e está disponível sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

Sinta-se à vontade para modificar os dados do JSON ou adicionar recursos extras à API conforme necessário!
