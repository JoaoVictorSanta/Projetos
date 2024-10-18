#Bibliotecas
from ftplib import FTP
from tkinter import filedialog
import pandas as pd
import tkinter as tk
import zipfile

#fun��o para selecionar pastas
def select_data():
    root = tk.Tk()
    root.withdraw()
    
    return filedialog.askopenfilename()

#escolher os arquivos e pasta

print("Selecione o arquivo excel com os ips e nomes dos robos!")
input("Aperte enter para prosseguir!")
_arq = select_data()

print("Selecione a pasta com a pasta onde est�o os programas relacionados a cada robo!")
input("Aperte enter para prosseguir!")
_pasta = select_data()

#le o excel
data = pd.read_excel(_arq)

#verifica quantos ips tem no excel
qtd_linhas = data['IP DO ROBO'].count()

#compara o ip do robo e o nome e verifica a pasta com o nome do robo
for linha in range(qtd_linhas):
    
    _ip = data.iloc[linha]['IP DO ROBO'].strip()
    _nome = data.iloc[linha]['NOME DA PASTA']
    print(f"{_ip} / {_nome}")

    #conecta via FTP
    ftp = FTP(_ip)
    ftp.login(user="anonymous", passwd="")
    print(f"Robo: {_ip} conectado!")
    
    #inseri via FTP os programas no robo
    with zipfile.ZipFile(_pasta, 'r') as zip_ref:
        for arq_info in zip_ref.infolist():
            if _nome in arq_info.filename:
                if arq_info.filename.endswith('.LS'):
                    _ls = arq_info.filename
                    with zip_ref.open(_ls) as arquivo:
                        print(_ls)
                        print(arquivo)
                        ftp.storbinary(f"STOR {_ls}", arquivo)
    
