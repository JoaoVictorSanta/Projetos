# FrameBKP

Este projeto fornece scripts e arquivos de configuração para definir e controlar as posições de ferramentas (toolframe), posições de usuários (userframe), cargas (payloads) e posições iniciais (homepos) em robôs industriais. Utilizando dados estruturados em JSON e scripts em Python, este projeto permite uma configuração flexível e rápida para o ambiente de automação.

## Estrutura do Projeto

### Arquivos Principais

- **`base.json`**: Arquivo de configuração JSON contendo templates e dados principais para as definições de:
  - **Toolframe**: Coordenadas e orientações da ferramenta.
  - **Userframe**: Posições do quadro do usuário.
  - **Payloads**: Dados de carga para diferentes ferramentas.
  - **Homepos**: Posição inicial padrão do robô.
  - **Cabeçalho e Metadados**: Informações sobre versão, prioridade de tarefas, etc.

- **`FrameBKP.py`**: Script Python que utiliza o arquivo JSON para configurar o robô, aplicando as definições de toolframe, userframe, payload e homepos. Este script inclui funções que leem o arquivo JSON e carregam as informações no ambiente de controle do robô.

## Estrutura do `base.json`

O arquivo `base.json` é composto de várias seções:

- **head**: Contém metadados do programa, como `OWNER`, `COMMENT`, e configurações de prioridade e tamanho da tarefa.
- **payload**: Define configurações de carga para cada ferramenta, com campos como `PAYLOAD`, `PAYLOAD_X`, `PAYLOAD_Y`, `PAYLOAD_Z`, `PAYLOAD_IX`, `PAYLOAD_IY`, e `PAYLOAD_IZ`.
- **toolframe**: Define a posição e orientação da ferramenta em relação ao robô, utilizando as variáveis `PR[1,1]` a `PR[1,6]`.
- **userframe**: Define posições do quadro de referência do usuário.
- **homepos**: Define a posição inicial do robô, que pode ser configurada para ser executada em um *cold start*.
- **comment**: Inclui comentários e instruções adicionais que descrevem o programa e sua função.
- **foot**: Marca o fim do arquivo com um delimitador `/END`.

### Exemplo de Configuração de Payload (`payload`)

```json
{
  "payload": "! ---PAYLOAD {id}--- ;\n$PLST_GRP1[{id}].$PAYLOAD = {v1} ;\n$PLST_GRP1[{id}].$PAYLOAD_X = {v2} ;\n$PLST_GRP1[{id}].$PAYLOAD_Y = {v3} ;\n..."
}
