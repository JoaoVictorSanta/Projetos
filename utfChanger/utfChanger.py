#Bibliotecas
import os

#diretorio atual
dir_atual = os.getcwd()

#função para mudar tudo que tiver dentro da pasta de utf-8-X para utf-8
def encode(raiz):
    while True:
        
        #cria a pasta raiz
        if not os.path.exists(f"{dir_atual}\\raiz"):
            os.mkdir(f"{dir_atual}\\raiz")
            print("Pasta Raiz criada, coloque as pastas dos robos nela e reinicie o programa!")
            input("Aperte enter para prosseguir!")
            break
        
        #lê a pasta raiz, depois as dos robos e depois os programas dentro e altera elas
        for pastas in os.listdir(raiz):
            robo = os.path.join(raiz, pastas)
            for arq in os.listdir(robo):
                arq_dir = os.path.join(robo, arq)
                print(arq_dir)
                with open(arq_dir, "r", encoding="utf-8-sig") as f:
                    conteudo = f.read()
                    with open(arq_dir, "w", encoding="utf-8") as g:
                        g.write(conteudo)
                        print("foi")
        break
                
#main
encode(f"{dir_atual}\\raiz")