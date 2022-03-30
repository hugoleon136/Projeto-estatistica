with open ('pesquisa.txt', 'w') as arquivo:
    listnome = []
    listasexo = []
    listaltura = []
    listpeso = []
    listcordapele = []
    listidade= []
    listfilhos = []
    listrenda = []
    listescolaridade = []
    listresidencia = []
    listec = []
    for i in range (1, 21, 1):
        nome = input('Digite o nome do funcionário: ').upper()
        listnome.append(nome)
        sexo = input('Sexo: ').upper()
        listasexo.append(sexo)
        altura = float(input('Digite a altura: '))
        listaltura.append(altura)
        peso = float(input('Digite o seu peso: '))
        listpeso.append(peso)
        cordapele = input('Digite a cor da sua pele: ').upper()
        listcordapele.append(cordapele)
        idade = int(input('Digite a sua idade: '))
        listidade.append(idade)
        filhos = int(input('Quantos filhos ele(a) tem: '))
        listfilhos.append(filhos)
        renda = float(input('Digite a renda: '))
        listrenda.append(renda)
        escolaridade = str(input('Qual o nível de escolaridade: \n[I] Nível Fundamental \n[II] Nível Médio \n[III] Nível Superior \n[IV]Pós-Graduação \n[V] Nenhum \nResposta: ')).upper()
        listescolaridade.append(escolaridade)
        residencia = str(input('Moradia: \n[I] Alugada \n[II] Própria \n[III]Outro \nResposta: ')).upper()
        listresidencia.append(residencia)
        ec = str(input('Estado civil: \n[I] Casado(a) \n[II] Solteiro(a) \n[III] Outros \nResposta: ')).upper()
        listec.append(ec)
    print('NOME, SEXO, ALTURA, PESO, AUTODECLARAÇÃO ÉTNICO-RACIAL, IDADE, Nº DE FILHOS, RENDA, ESCOLARIDADE, MORADIA, ESTADO CIVIL', file=arquivo)
    print(f'{listnome[0]},{listasexo[0]},{listaltura[0]},{listpeso[0]},{listcordapele[0]},{listidade[0]},{listfilhos[0]},{listrenda[0]},{listescolaridade[0]},{listresidencia[0]},{listec[0]}', file=arquivo)
    print(f'{listnome[1]},{listasexo[1]},{listaltura[1]},{listpeso[1]},{listcordapele[1]},{listidade[1]},{listfilhos[1]},{listrenda[1]},{listescolaridade[1]},{listresidencia[1]},{listec[1]}', file=arquivo)
    print(f'{listnome[2]},{listasexo[2]},{listaltura[2]},{listpeso[2]},{listcordapele[2]},{listidade[2]},{listfilhos[2]},{listrenda[2]},{listescolaridade[2]},{listresidencia[2]},{listec[2]}', file=arquivo)
    print(f'{listnome[3]},{listasexo[3]},{listaltura[3]},{listpeso[3]},{listcordapele[3]},{listidade[3]},{listfilhos[3]},{listrenda[3]},{listescolaridade[3]},{listresidencia[3]},{listec[3]}', file=arquivo)
    print(f'{listnome[4]},{listasexo[4]},{listaltura[4]},{listpeso[4]},{listcordapele[4]},{listidade[4]},{listfilhos[4]},{listrenda[4]},{listescolaridade[4]},{listresidencia[4]},{listec[4]}', file=arquivo)
    print(f'{listnome[5]},{listasexo[5]},{listaltura[5]},{listpeso[5]},{listcordapele[5]},{listidade[5]},{listfilhos[5]},{listrenda[5]},{listescolaridade[5]},{listresidencia[5]},{listec[5]}', file=arquivo)
    print(f'{listnome[6]},{listasexo[6]},{listaltura[6]},{listpeso[6]},{listcordapele[6]},{listidade[6]},{listfilhos[6]},{listrenda[6]},{listescolaridade[6]},{listresidencia[6]},{listec[6]}', file=arquivo)
    print(f'{listnome[7]},{listasexo[7]},{listaltura[7]},{listpeso[7]},{listcordapele[7]},{listidade[7]},{listfilhos[7]},{listrenda[7]},{listescolaridade[7]},{listresidencia[7]},{listec[7]}', file=arquivo)
    print(f'{listnome[8]},{listasexo[8]},{listaltura[8]},{listpeso[8]},{listcordapele[8]},{listidade[8]},{listfilhos[8]},{listrenda[8]},{listescolaridade[8]},{listresidencia[8]},{listec[8]}', file=arquivo)
    print(f'{listnome[9]},{listasexo[9]},{listaltura[9]},{listpeso[9]},{listcordapele[9]},{listidade[9]},{listfilhos[9]},{listrenda[9]},{listescolaridade[9]},{listresidencia[9]},{listec[9]}', file=arquivo)
    print(f'{listnome[10]},{listasexo[10]},{listaltura[10]},{listpeso[10]},{listcordapele[10]},{listidade[10]},{listfilhos[10]},{listrenda[10]},{listescolaridade[10]},{listresidencia[10]},{listec[10]}', file=arquivo)
    print(f'{listnome[11]},{listasexo[11]},{listaltura[11]},{listpeso[11]},{listcordapele[11]},{listidade[11]},{listfilhos[11]},{listrenda[11]},{listescolaridade[11]},{listresidencia[11]},{listec[11]}', file=arquivo)
    print(f'{listnome[12]},{listasexo[12]},{listaltura[12]},{listpeso[12]},{listcordapele[12]},{listidade[12]},{listfilhos[12]},{listrenda[12]},{listescolaridade[12]},{listresidencia[12]},{listec[12]}', file=arquivo)
    print(f'{listnome[13]},{listasexo[13]},{listaltura[13]},{listpeso[13]},{listcordapele[13]},{listidade[13]},{listfilhos[13]},{listrenda[13]},{listescolaridade[13]},{listresidencia[13]},{listec[13]}', file=arquivo)
    print(f'{listnome[14]},{listasexo[14]},{listaltura[14]},{listpeso[14]},{listcordapele[14]},{listidade[14]},{listfilhos[14]},{listrenda[14]},{listescolaridade[14]},{listresidencia[14]},{listec[14]}', file=arquivo)
    print(f'{listnome[15]},{listasexo[15]},{listaltura[15]},{listpeso[15]},{listcordapele[15]},{listidade[15]},{listfilhos[15]},{listrenda[15]},{listescolaridade[15]},{listresidencia[15]},{listec[15]}', file=arquivo)
    print(f'{listnome[16]},{listasexo[16]},{listaltura[16]},{listpeso[16]},{listcordapele[16]},{listidade[16]},{listfilhos[16]},{listrenda[16]},{listescolaridade[16]},{listresidencia[16]},{listec[16]}', file=arquivo)
    print(f'{listnome[17]},{listasexo[17]},{listaltura[17]},{listpeso[17]},{listcordapele[17]},{listidade[17]},{listfilhos[17]},{listrenda[17]},{listescolaridade[17]},{listresidencia[17]},{listec[17]}', file=arquivo)
    print(f'{listnome[18]},{listasexo[18]},{listaltura[18]},{listpeso[18]},{listcordapele[18]},{listidade[18]},{listfilhos[18]},{listrenda[18]},{listescolaridade[18]},{listresidencia[18]},{listec[18]}', file=arquivo)
    print(f'{listnome[19]},{listasexo[19]},{listaltura[19]},{listpeso[19]},{listcordapele[19]},{listidade[19]},{listfilhos[19]},{listrenda[19]},{listescolaridade[19]},{listresidencia[19]},{listec[19]}', file=arquivo)
    
