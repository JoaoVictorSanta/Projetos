# Projetos
Aqui estão todos os projetos que desenvolvi.

# Backup e Geração de ToolData para Robôs Fanuc - FrameBKP (Finalizado)
Este projeto realiza backups de dados de frames (Tool Frame e User Frame) de robôs Fanuc via FTP ou arquivos locais. Os backups geram arquivos de texto organizados com cabeçalho e rodapé personalizados.

# Upload de Programas via FTP para Robôs Fanuc - OfflineDownload (Finalizado)
Este projeto realiza o upload de programas para robôs Fanuc via FTP, utilizando um arquivo Excel com os IPs e nomes dos robôs e uma pasta ZIP contendo os programas correspondentes.

# Interface de Configuração de Robôs Fanuc com PySimpleGUI - RobotConfig (Finalizado)
Este projeto cria uma interface gráfica usando PySimpleGUI para configurar parâmetros de robôs Fanuc. A interface permite inserir valores de Tool Frames, User Frames, Payloads e Posições de Home, que são organizados em uma lista e podem ser exportados para um arquivo .cm com cabeçalhos e rodapés predefinidos. O programa também permite editar e excluir itens da lista antes de gerar o arquivo de configuração.

# Gerador de Arquivos de Configuração de Tool Frame, User Frame e Payload - Tooldata (Finalizado)
Este script em Python gera arquivos de configuração .ls para robôs Fanuc, permitindo a configuração de Tool Frame, User Frame e Payload a partir de entradas fornecidas pelo usuário. Ele personaliza as saídas com cabeçalhos e rodapés e estrutura os dados com base em um arquivo JSON predefinido. Com um menu interativo, o usuário pode configurar diferentes tipos de frames e payloads, gerando um arquivo final com todas as informações. Este código é o antecessor de uma versão mais avançada, focada na melhoria do processo de backup e manipulação remota dos dados via FTP, conforme o novo projeto do usuário. Esta é a versão anterior do programa citado acima.

# Sistema de Monitoramento e Análise Comportamental em Sala de Aula - Zero
Aplicação Python que utiliza visão computacional para monitorar alunos em tempo real e gerar relatórios detalhados sobre o engajamento e o comportamento em sala de aula.

# Conversor de Codificação de Arquivos para UTF-8 - utfChanger (Finalizado)
Este script em Python converte a codificação de todos os arquivos em subpastas localizadas dentro de uma pasta chamada "raiz" para UTF-8. O usuário deve criar a pasta "raiz" e adicionar as pastas dos robôs com os programas a serem convertidos. O programa lê os arquivos existentes com a codificação UTF-8-SIG, ajusta sua codificação para UTF-8 e salva as alterações. O objetivo é padronizar a codificação dos arquivos para garantir compatibilidade e facilitar a manipulação dos dados.
