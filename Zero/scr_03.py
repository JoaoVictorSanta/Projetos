#bibliotecas
import os
import mediapipe as mp
import cv2
from fer import FER as fer
import shutil as st

#módulos
from scr_99 import load_config, arquivos

#config
config = load_config()

#recebe infos de config
Jlog = (config['config']['jlog'])
    
#inicialização do mediapipe
mp_malha_facial = mp.solutions.face_mesh
malha_facial = mp_malha_facial.FaceMesh()

#---------------------------------------------------FUNÇÕES DE TREINAMENTO DE MODELO (MELHORAR)---------------------------------------------------
def olhando_baixo(landmarks, alt_img):
    olho_esq_y = (landmarks[33].y + landmarks[133].y) / 2 * alt_img
    olho_dir_y = (landmarks[362].y + landmarks[263].y) / 2 * alt_img
    nariz_y = landmarks[1].y * alt_img
        
    if nariz_y > olho_esq_y and nariz_y > olho_dir_y:
        return True
    return False

def olhando_lados(landmarks, lar_img):
    olho_esq_x = (landmarks[33].x + landmarks[133].y) / 2 * lar_img
    olho_dir_x = (landmarks[362].x + landmarks[263].y) / 2 * lar_img
    nariz_x = landmarks[1].x * lar_img
        
    if nariz_x < olho_esq_x:
        return "esquerda"
    elif nariz_x > olho_dir_x:
        return "direita"
    return "frente"

def conversando(landmarks, alt_img):
    top_boca_y = landmarks[13].y * alt_img
    bot_boca_y = landmarks[14].y * alt_img
        
    abrindo_boca = bot_boca_y - top_boca_y
    if abrindo_boca > 0.5 * alt_img:
        return True
    return False

def detectar_emocoes(img):
    detector_emocao = fer()
    emocoes = detector_emocao.detect_emotions(img)
    return emocoes

#------------------------------------------------------------------TERMINA AQUI------------------------------------------------------------------

#função para achar cada imagem e comparar
def diag(_dir):
    
    #tentativa, se não der pra executar, ele cria as pastas
    try:
        #variaveis dos diretorios
        ref_dir = f"{_dir}\\data\\ref"
        diag_dir = f"{_dir}\\data\\diag"
    
        #procura as imagens uma a uma
        for pasta in os.listdir(ref_dir):
            ref = os.path.join(ref_dir, pasta) 
        
            if os.path.isdir(ref):
                
                #seta as pastas de entrada e saida das imagens para verificação
                unv = f"{ref}\\01"
                ver = f"{ref}\\02"
            
                for image in os.listdir(unv):
                    
                    #verifica quantas imagens tem dentro da pasta de REF# - Se só tiver 1 ou menos (foto de referencia)
                    if len(os.listdir(ref)) <= 1:
                        
                        #exibe um log de que não há imagens para ver
                        if Jlog:
                            print("Não há imagens para verificar")
                            
                        return
                
                    #verifica se a imagem não é a referencia
                    if not image.startswith("REF#"):
                        image_dir = os.path.join(unv, image)
                    
                        #exibe um log de geração de diag do REF#
                        if Jlog:
                            print(f"Gerando diag de {pasta}...")

                        #analisa a imagem e gera o diga
                        analisar(pasta, image_dir, diag_dir, image)
                        
                        #copia a imgame da pasta unv (01) para a ver (02)
                        st.copy(image_dir, ver)
                        
                        #exclui a imagem da pasta unv(01)
                        os.remove(image_dir)
                        
                        #exibe um log de diag do REF# concluido
                        if Jlog:
                            print(f"Diag de {pasta} concluído")
                        
    #caso o try não funcione
    except:
        arquivos()
        return print("ERROR - Tente novamente")
          
#função que compara as imagens e gera diag no txt
def analisar(_nome, _image, _diag, _data):
    
    #lê a imagem de entrada
    img = cv2.imread(_image)
    
    #transforma em rgb
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    #puxa toda a malha facial da imagem
    imagem = malha_facial.process(rgb_img)
    
    #para cada ponto do rosto ele gera um shape e testa nas funções treinadas
    if imagem.multi_face_landmarks:
        for landmarks_facial in imagem.multi_face_landmarks:
            a, l, _ = img.shape
            landmarks = landmarks_facial.landmark
            
            #funções treinadas retornam para essas variaveis o resultado
            direção_face = olhando_lados(landmarks, l)
            face = "baixo" if olhando_baixo(landmarks, a) else "cima"
            falando = "falando" if conversando(landmarks, a) else "quieto"
            emocoes = detectar_emocoes(img)
            
            #escreve num arquivo com nome da REF# os resultados
            with open(f"{_diag}\\{_nome}.txt", "a") as diag:
                diag.write(f"\n{_data}:\nOlhando para {direção_face}\nA cabeça está para {face}\nEle está {falando}\n{emocoes}\n")