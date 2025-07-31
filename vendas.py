vendas={"batata":1200,"abacaxi":200,"Salada de grão-de-bico":50,"Lasanha de berinjela":10,"Feijão tropeiro vegetariano":10}
valores={"batata":12,"abacaxi":10,"Salada de grão-de-bico":10,"Lasanha de berinjela":17,"Feijão tropeiro vegetariano":13}
logins=["Lucas","Lazaro","Ricardo"]
def mostrar():
    for podruto,estoque in vendas.items():
        print("%30s | %5d restantes "%(podruto,estoque))


def vendinhas():

    while True:
        resposta= int(input("Olá %s Oque deseja fazer? \n 1-ver estoque 2-ver valores 3-sair \t"%(usuario)))
        match resposta:
            case 1:
                mostrar()
                print("\n")
            case 2:
                mostrar_valores()
                print("\n")
            case _:
                break


def mostrar_valores():
    for prodrutos, grana in valores.items():
        print("%30s  | $%-5.2d "%(prodrutos,grana))


def primeiro_visita():
    contador=0
    while contador <4:
    
        print("seja bem vindo, aqui sera feito seu login")
        login=input("Digite como sera seu login \t")
        certeza=input("Digite novamente \t")
        if login==certeza:
            print("login feito com sucesso")
            logins.append(login)
        else:
            print("deu errado")
            contador+=1

        




def loginzin():
    global usuario
    tentativas = 0
    while tentativas < 4:
        usuario =input("Digite seu login \t")
        if usuario in logins:
            print("seja bem vindo")
            return vendinhas()
        else:
            print("erro")
            tentativas += 1
    novo=input("Você é novo por aqui? Quer fazer seu primeiro cadastro? \t").lower()
    if novo=="sim":    
        return primeiro_visita()
loginzin()
