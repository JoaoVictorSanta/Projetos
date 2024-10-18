#Bibliotecas
from ftplib import FTP
import tkinter as tk
from tkinter import filedialog
import os
import sys
import json
from datetime import datetime

#função para verificar se o programa base está no sistema ou na pasta do .py
def base_path(_dir):
    
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, _dir)
    else:
        return os.path.join(os.path.abspath("."), _dir)
    
_base = base_path('base.json')

#função para gerar o cabeçalho
def gerar_cabecalho():
    with open(_base, 'r') as file:
        data = json.load(file)
    
    head_txt = data['head']

    c_data = datetime.now().strftime('%d-%m-%Y')
    c_hora = datetime.now().strftime('%H:%M:%S')

    return head_txt.replace('{data}', c_data).replace('{time}', c_hora)

#função para gerar o rodape
def gerar_rodape():
    with open(_base, 'r') as file:
        data = json.load(file)
    
    foot_txt = data['foot']
    
    return foot_txt

#função para a estrutura do tooldata
def gerar_txt(_linha, _data, _v1, _v2, _v3, _v4, _v5, _v6, _v7, _id):
    with open(_base, 'r') as file:
        data = json.load(file)
        
    frame = data[_data]
    
    linha_atual = _linha
    
    txt = f"{linha_atual}: ;\n"
    linha_atual += 1
    
    for linha in frame.splitlines():
        txt += f"{linha_atual}: {linha}\n"
        linha_atual += 1

    return txt.replace('{v1}', _v1).replace('{v2}', _v2).replace('{v3}', _v3).replace('{v4}', _v4).replace('{v5}', _v5).replace('{v6}', _v6).replace('{v7}', _v7).replace('{id}', _id), linha_atual

#função para encontrar a pasta que será usada
def select_pasta(tipo):
    root = tk.Tk()
    root.withdraw()

    if tipo == "pasta":
        result = filedialog.askdirectory()
        
    if tipo == "arq":
        result = filedialog.askopenfilename()
    
    return result

#função para encontrar os arquivos que serão lidos
def file(_dir):
    pasta = os.listdir(_dir)
    for arq in pasta:
        arq_dir = os.path.join(_dir, arq)
        if os.path.isfile(arq_dir):
            if arq.startswith("errall") or arq.startswith("ERRAL"):
                name = arq_dir
            if arq.startswith("sysframe") or arq.startswith("SYSFRAME"):
                frame = arq_dir
    return name, frame
    
#função para encontrar as informações dos arquivos
def get_data(_dir, n, t):
    
    found_name = 0
    count_frame = 0
    found_frame = 0
    txt = ""
    block = ""

    with open(_dir, "r") as f:
        linhas = f.readlines()
        
        for linha in linhas:
            
            if "Robot Name" in linha:
                palavras = linha.split()
                for palavra in palavras:
                    if found_name == 1:
                        return palavra
                    if palavra.startswith("Name"):
                        found_name = 1
                
            if t == "uframe":

                if "$MNUFRAMENUM" in linha:
                    found_frame = 0
                
                if found_frame == 1:
                    txt += "\n" +linha
                
                if "$MNUFRAME " in linha:
                    found_frame = 1
                    tipo = "userframe"
                    
            if t == "tframe":

                if "$MNUTOOLNUM" in linha:
                    found_frame = 0
                
                if found_frame == 1:
                    txt += "\n" +linha
                
                if "$MNUTOOL " in linha:
                    found_frame = 1
                    tipo = "toolframe"
                
        for linha in txt.splitlines():
            
            if f"[1,{n}]" in linha:
                count_frame += 1

            if not count_frame == 0 and count_frame < 9:
                block += "\n" + linha
                count_frame += 1
                
        return block, tipo
            
#função para extrair as informações
def get_info(txt):
    
    palavras = txt.split()
    
    _x = 0
    _y = 0
    _z = 0
    _w = 0
    _p = 0
    _r = 0
    
    for p in palavras:
        
        if "[" in p:
            _frame = p
            
        if _x == 1:
            _xx = p
            _x = 0
            
        if _y == 1:
            _yy = p
            _y = 0
            
        if _z == 1:
            _zz = p
            _z = 0
            
        if _w == 1:
            _ww = p
            _w = 0
            
        if _p == 1:
            _pp = p
            _p = 0
            
        if _r == 1:
            _rr = p
            _r = 0

        if "X:" in p:
            _x = 1
            
        if "Y:" in p:
            _y = 1
            
        if "Z:" in p:
            _z = 1
            
        if "W:" in p:
            _w = 1
            
        if "P:" in p:
            _p = 1
            
        if "R:" in p:
            _r = 1
    
    return _frame.replace("[1,", "").replace("]", ""), _xx, _yy, _zz, _ww, _pp, _rr
           
#função para pegar os arquivos remotamente
def get_robo_data(ip):

    robot_ip = ip
    username = 'anonymous'
    password = ''
    
    try:
        ftp = FTP(robot_ip)
        ftp.login(user = username, passwd = password)
        print("\nConectado\n")
    except Exception:
        print(f"\nNão foi possivel conectar o IP: {ip}")
        
    try:
        with open("ERRALL.LS", 'wb') as f:
            ftp.retrbinary("RETR ERRALL.LS", f.write)
        
        with open("SYSFRAME.VA", 'wb') as f:
            ftp.retrbinary("RETR SYSFRAME.VA", f.write)
        
        ftp.quit()
        
    except Exception:
        print(f"Erro ao tentar pegar os frames do IP: {ip}")
    
#função para juntar a pega de dados e unir tudo em um unico texto
def rotina(p, _dir):
    pasta = p
    name_dir, frame_dir = file(pasta)
    name = get_data(name_dir, 0, "")
    
    print("\nFazendo backup dos frames...")
    
    linha = 1
    txt = ""

    top, linha = gerar_txt(linha, "comment", "", "", "", "", "" ,"" ,"", "")

    head = gerar_cabecalho()
    end = gerar_rodape()
    ini = head + top

    for i in range(1,10):

        block, tipo = get_data(frame_dir, i, "uframe")

        f, x, y, z, w, p, r = get_info(block)
        
        body, linha = gerar_txt(linha, tipo, x, y, z, w, p, r, "", f)
        
        txt += body
        
    for i in range(1,10):

        block, tipo = get_data(frame_dir, i, "tframe")

        f, x, y, z, w, p, r = get_info(block)
        
        body, linha = gerar_txt(linha, tipo, x, y, z, w, p, r, "", f)
        
        txt += body
        
    try:
        os.remove('ERRALL.LS')
        os.remove('SYSFRAME.VA')
    except:
        None
        
        print(_dir)

    if not os.path.exists(f"{_dir}\\Backups"):
        os.makedirs(f"{_dir}\\Backups")

    with open(f"Backups\\{name}_tooldata.ls", "w") as td:
        td.write(ini + txt + end)
        
    print("\nBackup finalizado!\n")
    
#função de menu para uso remoto do robo
def ip_config(_dir, d):
    
    while True:
        print("\n--ETHERNET--\n")
        print("0 - Fechar")
        print("1 - Inerir IPs via arquivo .txt")
        print("2 - Inserir manualmente")
        escolha = input("\nDigite o numero da escolha: ")
        
        if escolha == "0":
            print("Fechando...")
            break
        
        if escolha == "1":
            
            print("\nCrie um arquivo .txt com os ips do robo em lista")
            print("\nExemplo:")
            print("192.168.0.5")
            print("192.168.0.6")
            print("...")
            
            input("\nPressinoe Enter para selecionar o arquivo.txt...")
            
            arq = select_pasta("arq")
            print(arq)
            
            with open(arq, "r") as f:
                linhas = f.readlines()
                for linha in linhas:
                    palavras = linha.split()
                    for palavra in palavras:
                        try:
                            get_robo_data(palavra)
                            rotina(_dir, d)
                            break
                        except Exception:
                            print(f"Erro ao tentar pegar o bakcup do IP: {palavra}, tente novamente!")
                        break
                    
        if escolha == "2":
            ip = input("Digite o IP do robo: ")

            try:
                get_robo_data(ip)
                rotina(_dir, d)
                break
            except Exception:
                print(f"Erro ao tentar pegar o bakcup do IP: {ip}, tente novamente!")
                
        else:
            print("\nEscolha invalida\n")
            
#função main com os menus principais
def main():
    
    dir_atual = os.getcwd()

    while True:

        print("--MENU--\n")
        print("0 - Fechar")
        print("1 - Geral ToolData a partir de um backup")
        print("2 - Gerar ToolData via ethernet")
        escolha = input("\nDigite o numero: ")
        
        if escolha == "0":
            print("\nFechando...\n")
            break

        if escolha == "1":
            try:
                rotina(select_pasta("pasta"), dir_atual)
                break
            except Exception:
                print("Falha ao tentar pegar frames pelo backup")
        
        if escolha == "2":
            ip_config(dir_atual, dir_atual)
            break
            
        else:
            print("\nEscolha invalida\n")
        
main()
