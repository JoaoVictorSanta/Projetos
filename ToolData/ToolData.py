#Bibliotecas
import os
import sys
import json
from datetime import datetime

#Verifica a base se está na pasta do sistema ou na pasta do programa
def base_path(_dir):
    
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, _dir)
    else:
        return os.path.join(os.path.abspath("."), _dir)
    
_base = base_path('base.json')

#função de gerar cabeçalho com hora e data atual
def gerar_cabecalho():
    with open(_base, 'r') as file:
        data = json.load(file)
    
    head_txt = data['head']

    c_data = datetime.now().strftime('%d-%m-%Y')
    c_hora = datetime.now().strftime('%H:%M:%S')

    return head_txt.replace('{data}', c_data).replace('{time}', c_hora)

#função de gerar rodape
def gerar_rodape():
    with open(_base, 'r') as file:
        data = json.load(file)
    
    foot_txt = data['foot']
    
    return foot_txt

#função de gerar as partes do texto de acordo com os valores
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

#armazena os valores de acordo com o tipo que quer ser inputado
def valores(tipo):
    if tipo == 1:
        _id = input("Numero do frame: ")
        v1 = input("X: ")
        v2 = input("Y: ")
        v3 = input("Z: ")
        v4 = input("W: ")
        v5 = input("P: ")
        v6 = input("R: ")    
        return v1, v2, v3, v4, v5, v6, _id
    
    if tipo == 2:
        _id = input("Numero do payload: ")
        v1 = input("Payload (Kg): ")
        v2 = input("CG X (cm): ")
        v3 = input("CG Y (cm): ")
        v4 = input("CG Z (cm): ")
        print("Os proximos valores, verifique se tem 6 casas antes")
        print("da virgula, caso não haja, multiplique o valor por 1000 primeiro!")
        v5 = input("Ixx (Kgf cm sec2): ")
        v6 = input("Iyy (Kgf cm sec2): ")
        v7 = input("Izz (Kgf cm sec2): ")    
        return v1, v2, v3, v4, v5, v6, v7, _id
    
    if tipo == 3:
        v1 = input("J1: ")
        if v1.startswith("-"):
            v1 = "(" + v1 + ")"
        v2 = input("J2: ")
        if v2.startswith("-"):
            v2 = "(" + v2 + ")"
        v3 = input("J3: ")
        if v3.startswith("-"):
            v3 = "(" + v3 + ")"
        v4 = input("J4: ")
        if v4.startswith("-"):
            v4 = "(" + v4 + ")"
        v5 = input("J5: ")
        if v5.startswith("-"):
            v5 = "(" + v5 + ")"
        v6 = input("J6: ")   
        if v6.startswith("-"):
            v6 = "(" + v6 + ")" 
        return v1, v2, v3, v4, v5, v6
    
#rotina main
def main():
    txt = ""
    linha = 1
    _end = 0

    #gera o texto e o numero das linhas
    top, linha = gerar_txt(linha, "comment", "", "", "", "", "" ,"" ,"", "")

    while True:
    
        if _end == 1:
            break

        #menu
        print("\nEscolha o que quer configurar:")
        print("1 - Tool Frame")
        print("2 - User Frame")
        print("3 - Payload")
    #    print("4 - Home Position") - Não funciona
        print("9 - Fechar")
        tipo = input("Digite o numero: ")

        #gera os textos a partir dos valores inputados
        if tipo == "1":
            v1, v2, v3, v4, v5, v6, _id = valores(1)
            body, linha = gerar_txt(linha, "toolframe", v1, v2, v3, v4, v5, v6, "", _id)
    
        if tipo == "2":
            v1, v2, v3, v4, v5, v6, _id = valores(1)
            body, linha = gerar_txt(linha, "userframe", v1, v2, v3, v4, v5, v6, "", _id)
    
        if tipo == "3":
            v1, v2, v3, v4, v5, v6, v7, _id = valores(2)
            body, linha = gerar_txt(linha, "payload", v1, v2, v3, v4, v5, v6, v7, _id)
    
    #    if tipo == "4": - Não funciona
    #        v1, v2, v3, v4, v5, v6 = valores(3)
    #        body, linha = gerar_txt(linha, "homepos", v1, v2, v3, v4, v5, v6, "", "")
        
        if tipo == "9":
            print("Fechando...")
            break
    
        txt += body
    
        while True:
            con = input("Deseja adicionar outro? (s/n) :")
        
            if con == "s":
                _end = 0
                break
        
            if con == "n":
                _end = 1
                break
        
            else:
                print("Não entendi a decisão!")

    #gera as partes do texto
    head = gerar_cabecalho()
    end = gerar_rodape()
    ini = head + top

    #junta tudo e escreve num .ls
    with open("tooldata.ls", "w") as td:
        td.write(ini + txt + end)

    print("tooldata.ls criado!")
    os.startfile("tooldata.ls")
    
#main
main()