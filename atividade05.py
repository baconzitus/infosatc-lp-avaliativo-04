nome = [ ] 
cpf  = [ ]
senha =[ ]
doador=[ ]

apto = None

for x in range(5):
        nome.append("nome exemplo")
        cpf.append(100) 
        senha.append(100) 
        doador.append(True)



def verificar():
    global apto 
    print("\nverificao para doacao de sangue: ")
    idade = int(input("\ninsira a idade:"))
    peso  = int(input("insira o peso:"))
    durmio = int(input("insira a quantidade de horas durmidas nas ultimas 24horas:"))

    c_durmio=True
    c_idade=True
    c_peso=True

    if idade<16 or idade>69:
       c_idade = False
    if peso<50:
        c_peso = False
    if durmio<6 or durmio>24:
        c_durmio = False

    if c_idade==False or c_durmio==False or c_peso==False:
        print("\nvoce não foi aceito porque:")
        if c_durmio==False:
            print("horas de sono insufientes ou exedidas")
        if c_idade==False:
            print("idade abaixo ou acima da aceita")
        if c_peso==False:
            print("peso abaixo do desejado")
        apto = False
        return
    else:
        print("\nvoce foi aceito para a doação")
        apto= True
        return

def cadastrar():
    global apto
    #se ele n tiver nada cadastrado no lugar ele vai para a pergunta se quer fazer o teste
    if apto==None:
        while(True):
            confirma=input("\nvoce gostaria de saber se vc esta apto para doar sangue, se vc n realizar o teste voce ficara como nao apto s ou n: ")
            if confirma.lower()=="s":
                verificar()
                break
            elif confirma.lower()=="n":
                apto =False
                break
            else:
                print("comando nao indentificado")

    #se n so salva se ele eh ou n    
    if apto==True:
        doador.append(True)
    else:
        doador.append(False)
    print("\ncadastro:")
    nome.append(input("nome completo:"))
    cpf.append (int((input("cpf:"))))
    senha.append(int(input("senha:")))
    
    #fazer um loop na tela de cadastro
    cont = input("deseja cadastrar mais alguem s ou n: ")
    if cont.lower()=="n":
        return
    elif cont.lower()=="s":
        apto=None
        cadastrar()
    else:
        print("comando n indentificado")


def printar():  

    geral = [nome,cpf,senha,doador]
    print("\nLista de pessoas cadastradas aptas e nao aptas:")
    for x in range(len(nome)):
        print("\nlugar:",x)
        print("nome:",geral[0][x])
        print("cpf:",geral[1][x])
        print("senha:",geral[2][x])
        print("pode doar:",geral[3][x])
    SystemExit(1)
        
while(True):
    print("\no que voce gostaria de fazer")
    print("1- ver quem esta cadastrado")
    print("2- se cadastrar")
    print("3- sair")
    menu_v = (int(input(">"))) 
    if menu_v ==1:
        printar()
    elif menu_v ==2:
        apto=None
        cadastrar()
    elif menu_v ==3:
        break
    else:
        print("caracterer n aceito")
