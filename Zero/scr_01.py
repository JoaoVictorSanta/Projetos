#bibliotecas
import os
import cv2
import mediapipe as mp

#módulos
from scr_99 import load_config, arquivos, ativar_janela

#config
config = load_config()

#recebe infos de config
Jlog = (config['config']['jlog'])
margem = (config['config']['margem'])
detect_face = (config['config']['detect_face'])
key_foto = (config['config']['key_foto'])
cam = (config['config']['cam'])

#abre o arquivo .txt e para escrever as informações
def data(_dir, _nome, _email, _ref):
    
    with open(f"{_dir}\\diag\\{_ref}.txt", "a") as diag:
        diag.write(f"DIAG\n\n{_ref}\n")
    
    #abre o arquivo
    with open(f"{_dir}\\data.txt", "a") as data:
        
        #escreve no arquivo
        data.write(f"{_ref}\nNome: {_nome}\nEmail: {_email}\n\n")
         
#gera o numero de referencia do cadastro 
def code(_dir):
    
    #incio de referencia 0
    n = 0

    while True:
        
        #lista os arquivos de referencia (mudar para listar baseado no .txt)
        pastas = os.listdir(_dir)
        
        #se não tiver nenhuma referencia, usa a 0
        if not pastas:
            return(f"REF#{n}")

        #se já existir referencia, vai acrescentando 1 a 1 até bater a certa
        for pasta in pastas:
            dir_foto = os.path.join(_dir, pasta)
            if dir_foto.endswith(f"REF#{n}"):
                n += 1
            else:
                return(f"REF#{n}")
      
#tirar a foto (melhorar precisão e ajustar para uma imagem de referencia)
def foto(_dir, _nome):
    
    #abre a camera
    camera = cv2.VideoCapture(cam)
    
    #inicialização do mediapipe
    solucao_reconhecimento_rosto = mp.solutions.face_detection
    reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
    desenho = mp.solutions.drawing_utils
    
    #loop e detecção facial
    with solucao_reconhecimento_rosto.FaceDetection(min_detection_confidence = detect_face) as fd:
        while True:
        
            #verifica se a camera está aberta e funcionando
            ver, frame = camera.read()
            if not ver:
                break
            
            #converte a imagem para rgb
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            lista_rostos = reconhecedor_rostos.process(rgb_frame)
        
            #tira a foto apertando f
            if cv2.waitKey(1) == ord(key_foto):
                
                #para cada rosto detectado
                for rosto in lista_rostos.detections:
                    
                    #salva o ponto de onde está o rosto
                    bboxC = rosto.location_data.relative_bounding_box
                    ih, iw, _ = frame.shape
                    x = int(bboxC.xmin * iw)
                    y = int(bboxC.ymin * ih)
                    w = int(bboxC.width * iw)
                    h = int(bboxC.height * ih)
                    
                    #usa o ponto salvo do rosto e cria 4 pontos para um quadrado ao redor dele
                    x_start = max(x - margem, 0)
                    y_start = max(y - margem * 2, 0)
                    x_end = min(x + w + margem, frame.shape[1])
                    y_end = min(y + h + margem, frame.shape[0])

                    #diz o tamando da imagem que será tirada e onde
                    img_rosto = frame[y_start : y_end, x_start : x_end]
                    
                    #cria a pastas de referencia, de imagens sem verificar e de verificadas
                    if not os.path.exists(f"{_dir}\\{_nome}"):
                        os.mkdir(f"{_dir}\\{_nome}")
                    if not os.path.exists(f"{_dir}\\{_nome}\\01"):
                        os.mkdir(f"{_dir}\\{_nome}\\01")
                    if not os.path.exists(f"{_dir}\\{_nome}\\02"):
                        os.mkdir(f"{_dir}\\{_nome}\\02")
            
                        #exibe um log de pastas criadas
                        if Jlog:
                            print(f"pasta {_dir}\\{_nome} criada com 01 e 02")

                    #grava a imagem
                    cv2.imwrite(f"{_dir}\\{_nome}\\{_nome}.jpg", img_rosto)
                    
                    #exibe um log se a foto foi tirada
                    if Jlog:
                        print("Foto tirada!")
                break
                
            #desenha pontos para a detecção do rosto na camera
            if lista_rostos.detections:
                for rosto in lista_rostos.detections:
                    desenho.draw_detection(frame, rosto)
        
            #mostra a camera numa janela
            cv2.imshow("Camera",frame)
        
            #ativa ela na tela
            ativar_janela("Camera")
        
        #fecha tudo
        camera.release()
        cv2.destroyAllWindows()

#função de cadastro
def cadastro(_dir):

    while True:
 
        #cadastrando o nome e o email   
        nome = input("Digite o nome da pessoa: ").strip()
        email = input("Digite o email da pessoa: ").strip()
    
        #tentativa, se não der pra executar, ele cria as pastas
        try:
            
            #gera o codigo de referencia
            ref = code(f"{_dir}\\data\\ref")
        
            #abre a camera pra foto do cadastro
            foto(f"{_dir}\\data\\ref", ref)
    
            #salva as escolhas num .txt
            data(f"{_dir}\\data", nome, email, ref)
            
        #caso o try não funcione
        except:
            arquivos()
            return print("ERROR - Tente novamente")
        
        # pergunta se deseja cadastrar outra pessoa
        continuar = input("Deseja cadastrar outra pessoa? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saindo do cadastro.")
            break
