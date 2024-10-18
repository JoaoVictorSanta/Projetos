#bibliotecas
import os
import shutil as st
from deepface import DeepFace as df
from datetime import datetime, timedelta

#modulos
from scr_01 import cadastro
from scr_02 import gravando
from scr_03 import diag
from scr_99 import load_config, arquivos

#armazena o diretório atual
dir_atual = os.getcwd()

#config
config = load_config()

#recebe Jlog de config
Jlog = (config['config']['jlog'])
tempo_rotina = (config['config']['tempo_rotina'])

#função para separar as imagens (colocado na main por bugs)
def separar():
    
    #salva as pastas usadas no code
    capturas = f"{dir_atual}\\cap"
    pessoas = f"{dir_atual}\\data\\ref"

    #tentativa, se não der pra executar, ele cria as pastas
    try:

        #loop para verificar todas as fotos dentro das capturas
        for foto in os.listdir(capturas):
            dir_captura = os.path.join(capturas, foto)
        
            #verifica se é uma imagem
            if dir_captura.endswith(".jpg"):
            
                #exibe um log do diretorio da imagem lida
                if Jlog:
                    print(dir_captura)
            
                #verifica as pastas de referencias nas pastas
                for pessoa in os.listdir(pessoas):
                    dir_pessoa = os.path.join(pessoas, pessoa)
                
                    #verifica as imagens de referencias nas pastas de referencias
                    if os.path.isdir(dir_pessoa):
                    
                        #verifica o caminho das imagens
                        for nome_img in os.listdir(dir_pessoa):
                        
                            #verifica se é uma imagem
                            if nome_img.endswith(".jpg"):
                                ref_pessoa = os.path.join(dir_pessoa, nome_img)
                            
                                #tenta fazer a verificação das imagens com as referencias
                                try:
                                
                                    #verificação
                                    resultado = df.verify(dir_captura, ref_pessoa)
                                
                                    #verifica o resultado
                                    if resultado["verified"]:
                                    
                                        #copia a imagem para a pasta da referencia
                                        st.copy(dir_captura, f"{dir_pessoa}\\01")
                                    
                                        #exibe log de copiada
                                        if Jlog:
                                            print(f"{dir_captura} Copiado!")
                                    
                                        #apaga a imagem da pasta de captura
                                        os.remove(dir_captura)
                                    
                                        #exibe log de apagado
                                        if Jlog:
                                            print(f"{dir_captura} Apagado!")
                                        
                                        break
                                
                                #se erro, mostra o erro
                                except Exception as e:
                                    print(f"Erro ao verificar imagem: {e}")
    
    #caso o try não funcione
    except:
        arquivos()
        return print("ERROR - Tente novamente")

#automain
def auto_main():
    
    #inicialização
    
    arquivos()
    
    #inicio do temporizador
    temporizador = datetime.now()

    #loop de rotina
    while True:
        
        #le config em tempo real
        config = load_config()
        Jlog = (config['config']['jlog'])
        margem = (config['config']['margem'])
        detect_face = (config['config']['detect_face'])
        key_foto = (config['config']['key_foto'])
        tempo_foto = (config['config']['tempo_foto'])
        tempo_rotina = (config['config']['tempo_rotina'])
        fim_rotina = (config['config']['fim_rotina'])
        mostrar_camera = (config['config']['mostrar_camera'])
        
        #verifica o temporizador
        if datetime.now() >= temporizador:
            
            #exibe mensagem de inicio de rotina
            if Jlog:
                print("inicio da rotina")
            
            #rotinas
            gravando(dir_atual)
            separar()
            diag(dir_atual)
            
            #verifica se a config fim de rotina está ligada
            if fim_rotina:
            
                #exibe mensagem de fim da rotina
                if Jlog:
                    print("finalizando rotina automatica")

                break
            
            #exibe mensagem que a rotina esperará para começar novamente
            if Jlog:
                print(f"inicio do contador em segundos: {tempo_rotina}")
                
            #temporizador de turno da rotina
            temporizador = datetime.now() + timedelta(seconds = tempo_rotina)
            
        

#main
def main():
    
    #inicialização
    
    arquivos()

    #-------AREA DE TESTE-------



    #-------------X-------------

    #loop da main
    while True:
        
        #menu de escolhas
        print("\nMenu:")
        print("0. Sair")
        print("1. Cadastrar")
        print("2. Gravar")
        print("3. Separar")
        print("4. Gerar diagnóstico das imagens")
        print("5. Automatico")
        escolha = input("Escolha uma opção: ").strip()
        
        #verifica as escolhas
        
        #cadastro - 1
        if escolha == '1':
            cadastro(dir_atual)

        #camera - 2
        if escolha == '2':
            gravando(dir_atual)
            
        #organizador - 3
        if escolha == '3':
            separar()
            
        #diagnostico - 4
        if escolha == '4':
            diag(dir_atual)
            
        #automatico - 5
        if escolha == '5':
            auto_main()
            
        #fechar - 0
        elif escolha == '0':
            print("Fechando.")
            break
        
        #caso não tenha escolha valida
        else:
            print("Opção inválida. Tente novamente.")

#rotina
main()