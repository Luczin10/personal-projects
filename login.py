def login_banco():

    login=input("Digite seu email")
    senha=int(input("Digite sua senha numerica"))
    print("login feito com sucesso")
    print(f"Seu email de confirmação é {login}")

    print("Agora vamos para o cadastre")
    nome=input("Digite seu nome")
    idade=int(input("Digite sua idade"))
    cpf=int(input("Digite seu cpf"))
    rg=int(input("seu rg"))
    endereço=input("Digite sua rua, cidade")
    rg_dos_pais=int(input("cpf de seu responsavel"))
    cpf_dos_pais=int(input("cpf do responsavel"))
    documentos_dos_pais=[rg_dos_pais, cpf_dos_pais]

    usuario_social=[nome, idade]
    usuario_pessoal=(cpf, rg, endereço, documentos_dos_pais)


login_banco()


def quaisquer ():
    
