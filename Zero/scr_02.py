#bibliotecas
import cv2
import mediapipe as mp
import os
from datetime import datetime, timedelta

#módulos
from scr_99 import load_config, arquivos, ativar_janela

#config
config = load_config()

#recebe infos de config
Jlog = (config['config']['jlog'])
margem = (config['config']['margem'])
detect_face = (config['config']['detect_face'])
tempo_foto = (config['config']['tempo_foto'])
mostrar_camera = (config['config']['mostrar_camera'])
cam = (config['config']['cam'])

#função de salvar a foto recortada do rosto
def capturar_foto(_dir, _frame, _detections):

    #puxa a hora em tempo real
    agora = datetime.now()

    #dita a forma que aparecerá a data e hora
    datastr = agora.strftime("%Y.%m.%d-%H.%M.%S")
        
    #variavel do contador para as fotos
    contador = 0
    
    #para salvar mais de uma, ele verifica quantos rostos tem na imagem
    for detection in _detections:
        
        #salva o ponto de onde está o rosto
        bboxC = detection.location_data.relative_bounding_box
        ih, iw, _ = _frame.shape
        x = int(bboxC.xmin * iw)
        y = int(bboxC.ymin * ih)
        w = int(bboxC.width * iw)
        h = int(bboxC.height * ih)
            
        #usa o ponto salvo do rosto e cria 4 pontos para um quadrado ao redor dele
        x_start = max(x - margem, 0)
        y_start = max(y - margem * 2, 0)
        x_end = min(x + w + margem, _frame.shape[1])
        y_end = min(y + h + margem, _frame.shape[0])
            
        #diz o tamando da imagem que será tirada e onde
        img_rosto = _frame[y_start : y_end, x_start : x_end]
        
        if not os.path.isdir(f"{_dir}\\cap"):
            arquivos()
            cv2.destroyAllWindows() 
            return print("ERROR - Tente novamente")#fecha tudo

        #gera o nome que será salvo a imagem, pela datahora e um contador das fotos
        img_nome = f"{_dir}\\cap\\F_{datastr}_#{contador}.jpg"
        
        #grava a imagem
        cv2.imwrite(img_nome, img_rosto)
                    
        #aumenta o contador para não ter imagens com nomes iguais
        contador += 1
        
        #exibe um log de imagem salva
        if Jlog:
            print(f"Foto salva em {img_nome}")

#função da camera em tempo real
def gravando(_dir):

    #abre a camera
    camera = cv2.VideoCapture(cam)
    
    #inicializa o mediapipe
    solucao_reconhecimento_rosto = mp.solutions.face_detection
    reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
    desenho = mp.solutions.drawing_utils
    
    #primeiro timer para primeira foto 5s (ajustar como necessário)
    tempo_proxima_foto = datetime.now() + timedelta(seconds = tempo_foto)
   
    #loop e detecção facial
    with solucao_reconhecimento_rosto.FaceDetection(min_detection_confidence = detect_face) as fd:
        while True:
            
            #verifica se a camera está aberta e funcionando
            verificador, frame = camera.read()
            if not verificador:
                break
            
            #converte a imagem para rgb
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            lista_rostos = reconhecedor_rostos.process(rgb_frame)
           
            #se o tempo zerar
            if datetime.now() >= tempo_proxima_foto:
                
                #verifica se tem rostos na tela
                if lista_rostos.detections:
                    
                    #captura imagem dos rostos
                    capturar_foto(_dir, frame, lista_rostos.detections)
                    
                    break
            
            #desenha pontos para a detecção do rosto na camera
            if Jlog:    
                if lista_rostos.detections:
                    for rosto in lista_rostos.detections:
                        desenho.draw_detection(frame, rosto)
         
            #mostra a camera numa janela
            if mostrar_camera:
                cv2.imshow("Detector de Rostos", frame)
                
                #ativa a janela
                ativar_janela("Detector de Rostos")
           
            #aperte esc para fechar a camera (ajuste conforme necessário)
            if cv2.waitKey(1) == 27:
                break
            
    #fecha tudo
    camera.release()
    cv2.destroyAllWindows()
