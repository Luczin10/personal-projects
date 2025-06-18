def primeira_vez():
    try:
        global nome
        nome=input("Digite seu nome\n")
        senha=int(input("Digite sua senha"))
        while True:
            senha2=int(input("digite novamente sua senha"))    
            if senha==senha2:
                print(f"Login feito %s"%(nome))
                break
            else:
                print("erro")
    except:
        print("Erro")
                
def escrever_usuario():
    try:   
        with open("projetos/ind4ex.txt","r") as fs1:
            usuario=fs1.read()
            print(usuario)
    except FileNotFoundError:
        primeira_vez()
        print("Arquivo não encontrado")

    
escrever_usuario()



        