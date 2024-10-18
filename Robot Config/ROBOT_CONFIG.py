#Bibliotecas
import PySimpleGUI as sg

#função da tela do programa
def tela():
    
    #vetores de lista e dados para gerar o arquivo
    lista = []
    data = []
    
    #tema do layout
    sg.theme('DarkGrey16')

    #função que cria o arquivo com os valores e nome do robo
    def salvar_arquivo(lista, nome):
        
        #cabeçalho e rodape
        cbc = 'FRCLRPR\nKCL SET VERIFY ON\n!\nPRINT "CONFIGURANDO ROBO..."\n!\n'
        rdp = 'PRINT "CONFIGURADO!"'

        #variavel que adiciona as informações
        txt = ""
        
        #cria um arquivo com o nome do robo
        with open(f'{nome}.cm', 'w') as f:
            
            for item in lista:
                
                var = item.split()
                
                #verifica os toolframes
                if var[0] == 'T':
                    txt += f"KCL SET VAR $MNUTOOL[1,{var[1]}].X = {var[2]}\nKCL SET VAR $MNUTOOL[1,{var[1]}].Y = {var[3]}\nKCL SET VAR $MNUTOOL[1,{var[1]}].Z = {var[4]}\nKCL SET VAR $MNUTOOL[1,{var[1]}].W = {var[5]}\nKCL SET VAR $MNUTOOL[1,{var[1]}].P = {var[6]}\nKCL SET VAR $MNUTOOL[1,{var[1]}].R = {var[7]}\n!\n"

                #verifica os userframes
                if var[0] == 'U':
                    txt += f"KCL SET VAR $MNUFRAME[1,{var[1]}].X = {var[2]}\nKCL SET VAR $MNUFRAME[1,{var[1]}].Y = {var[3]}\nKCL SET VAR $MNUFRAME[1,{var[1]}].Z = {var[4]}\nKCL SET VAR $MNUFRAME[1,{var[1]}].W = {var[5]}\nKCL SET VAR $MNUFRAME[1,{var[1]}].P = {var[6]}\nKCL SET VAR $MNUFRAME[1,{var[1]}].R = {var[7]}\n!\n"

                #verifica os payloads
                if var[0] == 'P':
                    txt += f"KCL SET VAR $PLST_GRP1[{var[1]}].$PAYLOAD = {var[2]}\nKCL SET VAR $PLST_GRP1[{var[1]}].$PAYLOAD_X = {var[3]}\nKCL SET VAR $PLST_GRP1[{var[1]}].$PAYLOAD_Y = {var[4]}\nKCL SET VAR $PLST_GRP1[{var[1]}].$PAYLOAD_Z = {var[5]}\nKCL SET VAR $PLST_GRP1[{var[1]}].$PAYLOAD_IX = {var[6]}\nKCL SET VAR $PLST_GRP1[{var[1]}].$PAYLOAD_IY = {var[7]}\nKCL SET VAR $PLST_GRP1[{var[1]}].$PAYLOAD_IZ = {var[8]}\n!\n"

                #verifica a posição de home
                if var[0] == 'H':
                    txt += f"KCL SET VAR $REFPOS1[1].$PERCHPOS[1] = {var[1]}\nKCL SET VAR $REFPOS1[1].$PERCHPOS[2] = {var[2]}\nKCL SET VAR $REFPOS1[1].$PERCHPOS[3] = {var[3]}\nKCL SET VAR $REFPOS1[1].$PERCHPOS[4] = {var[4]}\nKCL SET VAR $REFPOS1[1].$PERCHPOS[5] = {var[5]}\nKCL SET VAR $REFPOS1[1].$PERCHPOS[6] = {var[6]}\n!\n"

            #escreve o arquivo
            f.write(cbc + txt + rdp)
            
        #popup para dizer que foi criado o programa e zera a lista
        sg.popup('Salvo com sucesso!', f'As entradas foram salvas no arquivo {nome}.cm!')

#----------------------------------------------------------------------------------LAYOUTS----------------------------------------------------------------------------------

    tframe = [
        [sg.Text('Nº', s=(2,1)), sg.InputText(key='-T1-', s=2)],
        [sg.Text('X:', s=(2,1)), sg.InputText(key='-T2-',expand_x=True)],
        [sg.Text('Y:', s=(2,1)), sg.InputText(key='-T3-',expand_x=True)],
        [sg.Text('Z:', s=(2,1)), sg.InputText(key='-T4-',expand_x=True)],
        [sg.Text('W:', s=(2,1)), sg.InputText(key='-T5-',expand_x=True)],
        [sg.Text('P:', s=(2,1)), sg.InputText(key='-T6-',expand_x=True)],
        [sg.Text('S:', s=(2,1)), sg.InputText(key='-T7-',expand_x=True)],
        [sg.Button('Inserir', expand_x=True)]
        ]
    
    uframe = [
        [sg.Text('Nº', s=(2,1)), sg.InputText(key='-U1-', s=2)],
        [sg.Text('X:', s=(2,1)), sg.InputText(key='-U2-', expand_x=True)],
        [sg.Text('Y:', s=(2,1)), sg.InputText(key='-U3-', expand_x=True)],
        [sg.Text('Z:', s=(2,1)), sg.InputText(key='-U4-', expand_x=True)],
        [sg.Text('W:', s=(2,1)), sg.InputText(key='-U5-', expand_x=True)],
        [sg.Text('P:', s=(2,1)), sg.InputText(key='-U6-', expand_x=True)],
        [sg.Text('S:', s=(2,1)), sg.InputText(key='-U7-', expand_x=True)],
        [sg.Button('Inserir', expand_x=True)]
        ]

    payload = [
        [sg.Text('Nº', s=(2,1)), sg.InputText(key='-P1-', s=2), sg.Text('Kg:', s=(2,1)), sg.InputText(key='-P2-', expand_x=True)],
        [sg.Text('CG X:', s=(4,1)), sg.InputText(key='-P3-', expand_x=True)],
        [sg.Text('CG Y:', s=(4,1)), sg.InputText(key='-P4-', expand_x=True)],
        [sg.Text('CG Z:', s=(4,1)), sg.InputText(key='-P5-', expand_x=True)],
        [sg.Text('Ixx:', s=(4,1)), sg.InputText(key='-P6-', expand_x=True)],
        [sg.Text('Iyy:', s=(4,1)), sg.InputText(key='-P7-', expand_x=True)],
        [sg.Text('Izz:', s=(4,1)), sg.InputText(key='-P8-', expand_x=True)],
        [sg.Button('Inserir', expand_x=True)]
        ]
    
    homepos = [
        [sg.Text('Home Position')],
        [sg.Text('J1:', s=(3,1)), sg.InputText(key='-H1-', expand_x=True)],
        [sg.Text('J2:', s=(3,1)), sg.InputText(key='-H2-', expand_x=True)],
        [sg.Text('J3:', s=(3,1)), sg.InputText(key='-H3-', expand_x=True)],
        [sg.Text('J4:', s=(3,1)), sg.InputText(key='-H4-', expand_x=True)],
        [sg.Text('J5:', s=(3,1)), sg.InputText(key='-H5-', expand_x=True)],
        [sg.Text('J6:', s=(3,1)), sg.InputText(key='-H6-', expand_x=True)],
        [sg.Button('Inserir', expand_x=True)]
        ]
    
    config = [
        [sg.Text('Nome do Robo')],
        [sg.InputText(key='-ROBO-', expand_x=True)],
        [sg.Text()],
        [sg.Text()],
        [sg.Text()],
        [sg.Text()],
        [sg.Text()],
        [sg.Button('Inserir', expand_x=True)]
        ]

    layout_l = [
        [sg.TabGroup([
            [sg.Tab('TFrame', tframe), sg.Tab('UFrame', uframe), sg.Tab('Payload', payload), sg.Tab('HomePos', homepos), sg.Tab('Robo', config)]
            ], key='-TAB-')]
        ]
    
    layout_r = [
        [sg.Listbox(values=lista, no_scrollbar=True, s=(17,11), key='-LISTA-')],
        [sg.Button('Excluir', s=(6,1)), sg.Button('Criar', s=(6,1))]
        ]

    layout = [
        [sg.Menu([['Janela', ['Minimizar', 'Fechar']], ['Arquivo', ['Local', 'Ajuda']]], background_color='White', text_color='Black')],
        [sg.Col(layout_l, p=0), sg.Col(layout_r, p=0)]
        ]

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Define a tela com o layout
    tela = sg.Window('Robot Config', layout)

    #abre e mantem a tela aberta
    while True:
        
        event, values = tela.read()
        
        #verifica o botao inserir, acrescenta na lista e nos dados os valores de toolframe
        if event == "Inserir":
            if values['-T1-'] != '' and values['-T2-'] != '' and values['-T3-'] != '' and values['-T4-'] != '' and values['-T5-'] != '' and values['-T6-'] != '' and values['-T7-'] != '':
                novo_item = f"Tool Frame {values['-T1-']}"
                nova_data = f"T {values['-T1-']} {values['-T2-']} {values['-T3-']} {values['-T4-']} {values['-T5-']} {values['-T6-']} {values['-T7-']}"
                lista.append(novo_item)
                data.append(nova_data)
                tela['-T1-'].update("")
                tela['-T2-'].update("")
                tela['-T3-'].update("")
                tela['-T4-'].update("")
                tela['-T5-'].update("")
                tela['-T6-'].update("")
                tela['-T7-'].update("")
                tela['-LISTA-'].update(lista)
                
        #verifica o botao inserir, acrescenta na lista e nos dados os valores de userframe
        if event == "Inserir0":
            if values['-U1-'] != '' and values['-U2-'] != '' and values['-U3-'] != '' and values['-U4-'] != '' and values['-U5-'] != '' and values['-U6-'] != '' and values['-U7-'] != '':
                novo_item = f"User Frame {values['-U1-']}"
                nova_data = f"U {values['-U1-']} {values['-U2-']} {values['-U3-']} {values['-U4-']} {values['-U5-']} {values['-U6-']} {values['-U7-']}"
                lista.append(novo_item)
                data.append(nova_data)
                tela['-U1-'].update("")
                tela['-U2-'].update("")
                tela['-U3-'].update("")
                tela['-U4-'].update("")
                tela['-U5-'].update("")
                tela['-U6-'].update("")
                tela['-U7-'].update("")
                tela['-LISTA-'].update(lista)
        
        #verifica o botao inserir, acrescenta na lista e nos dados os valores de payload
        if event == "Inserir1":
            if values['-P1-'] != '' and values['-P2-'] != '' and values['-P3-'] != '' and values['-P4-'] != '' and values['-P5-'] != '' and values['-P6-'] != '' and values['-P7-'] != '' and values['-P8-'] != '':
                novo_item = f"Payload {values['-P1-']}"
                nova_data = f"P {values['-P1-']} {values['-P2-']} {values['-P3-']} {values['-P4-']} {values['-P5-']} {values['-P6-']} {values['-P7-']} {values['-P8-']}"
                lista.append(novo_item)
                data.append(nova_data)
                tela['-P1-'].update("")
                tela['-P2-'].update("")
                tela['-P3-'].update("")
                tela['-P4-'].update("")
                tela['-P5-'].update("")
                tela['-P6-'].update("")
                tela['-P7-'].update("")
                tela['-P8-'].update("")
                tela['-LISTA-'].update(lista)
          
        #verifica o botao inserir, acrescenta na lista e nos dados os valores de homeposition        
        if event == "Inserir2":
            if values['-H1-'] != '' and values['-H2-'] != '' and values['-H3-'] != '' and values['-H4-'] != '' and values['-H5-'] != '' and values['-H6-'] != '':
                nova_data = f"H {values['-H1-']} {values['-H2-']} {values['-H3-']} {values['-H4-']} {values['-H5-']} {values['-H6-']}"
                novo_item = "Home Pos"
                lista.append(novo_item)
                data.append(nova_data)
                tela['-H1-'].update("")
                tela['-H2-'].update("")
                tela['-H3-'].update("")
                tela['-H4-'].update("")
                tela['-H5-'].update("")
                tela['-H6-'].update("")
                tela['-LISTA-'].update(lista)
                
        #verifica o botao inserir, acrescenta na lista e nos dados os valores do config do robo (até agora nome apenas)
        if event == "Inserir3":
            if values['-ROBO-'] != '':
                novo_item = "Robo Config"
                nova_data = f"R {values['-ROBO-']}"
                nome = values['-ROBO-']
                lista.append(novo_item)
                data.append(nova_data)
                tela['-ROBO-'].update("")
                tela['-LISTA-'].update(lista)

        #exclui os dados da lista e dos dados
        if event == "Excluir":
            item = values['-LISTA-']
            if item:
                index = lista.index(item[0])
                lista.remove(item[0])
                data.pop(index)
                tela['-LISTA-'].update(lista)

        #gera o .cm
        if event == "Criar":
            salvar_arquivo(data, nome)

        #minimiza a tela
        if event == 'Minimizar':
            tela.minimize()

        #fecha a tela
        if event == sg.WIN_CLOSED or event == 'Fechar':
            break

    tela.close()

#main
tela()
