#bibliotecas
import os
import json
import win32gui
import win32con

#puxa o diretorio do programa
dir_atual = os.getcwd()

#configurações padrão
default_config = {
  "config": {
    "jlog": True,
    "margem": 40,
    "detect_face": 0.2,
    "key_foto": "f",
    "tempo_foto_inicial": 5,
    "tempo_foto": 5
  }
}

#gera as configurações padrão caso não exista o arquivo
def gerar_deafult_config():
    
    #variavel do diretorio do arquivo
    config = f"{dir_atual}\\config.json"
    
    #caso não exista
    if not os.path.exists(config):
        
        #cria o arquivo com base nas configurações padroes
        with open(config, "w") as arquivo_config:
            json.dump(default_config, arquivo_config, indent = 4)
            
        #exibe log dizendo que foi criado o arquivo
        print("arquivo config.json criado")
   
        #função de carregar as configurações
def load_config():
    
    #tenta rodar num loop
    while True:
        try:
            
            #abre e lê as informações do config
            with open(f"{dir_atual}\\config.json", "r") as config_json:
                config = json.load(config_json)
                
            #retorna tudo que está no arquivo
            return config
        
        #caso não dê, ele gera novamente o arquivo
        except:
            gerar_deafult_config()

#config
config = load_config()

#recebe Jlog de config
Jlog = config['config']['jlog']

#função para criar as pastas caso não exisam (inicialização)
def arquivos():
            
    #cria as pasta necessarias
    if not os.path.exists(f"{dir_atual}\\cap"):
        os.makedirs(f"{dir_atual}\\cap")        
    if not os.path.exists(f"{dir_atual}\\data"):
        os.mkdir(f"{dir_atual}\\data")
    if not os.path.exists(f"{dir_atual}\\data\\ref"):
        os.mkdir(f"{dir_atual}\\data\\ref")
    if not os.path.exists(f"{dir_atual}\\data\\diag"):
        os.mkdir(f"{dir_atual}\\data\\diag")
            
        #exibe um log de pastas criadas
        if Jlog:
            print(f"Todas as pastas estão ok")
         
    #cria o arquivo data
    with open(f"{dir_atual}\\data\\data.txt", "a") as data:
        data.write("DATA\n\nCADASTRADOS\n\n")
        
#ativa a janela na tela baseado no nome
def ativar_janela(_nome):
    try:
        
        #encontra a janela pelo nome
        janela = win32gui.FindWindow(None, _nome)
        
        #se ela existir, ativa na tela e maximiza
        if janela:
            win32gui.ShowWindow(janela, win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(janela)
            
    #se erro, mostra o erro
    except Exception as e:
        if Jlog:
            print(f"Erro ao ativar a janela: {e}")
            
def autoconfig():
    config = load_config()
    Jlog = (config['config']['jlog'])
    margem = (config['config']['margem'])
    detect_face = (config['config']['detect_face'])
    key_foto = (config['config']['key_foto'])
    tempo_foto = (config['config']['tempo_foto'])
    tempo_rotina = (config['config']['tempo_rotina'])
    fim_rotina = (config['config']['fim_rotina'])
    mostrar_camera = (config['config']['mostrar_camera'])