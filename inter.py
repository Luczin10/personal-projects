def inter():
    nome=input("digite seu nome ")
    print(f"Ola {nome} oque deseja fazer ") 
    resultado=int(input("1-extrato  2-depositar 3-acessar conta poupança"))
    conta_corrente=1000
    conta_poupança=500
    if resultado==1:
        print(f"Não ha depositos recentes, mas seu saldo é de {conta_corrente}")
    elif resultado==2:
        quem=input("para quem você ira depositar")
        quanto=int(input("Quanto você ira depositar"))
        confirmação=input("Você confirma    1-sim   2-não")
        if confirmação==1:
            print("parabens voce depositou {quanto} reais, seu saldo agr é de ",conta_corrente-quanto)  
        elif confirmação==2: 
            print("deposito cancelado")
        else:
            print("Erro")
    elif resultado==3:
        result=(f"seu saldo é de {conta_poupança}, deseja depositar 1-sim   2-não")  
        if result==1:
            Deposito=float(input("Digite seu deposito  "))
    if conta_corrente>=conta_poupança:
        data=int(input("Digite quantos meses sera feito sua poupança "))
        Rendimento=Deposito*(1.3/100)*data
        saldo=Rendimento+conta_corrente
        print(f"Seu rendimento é de {Rendimento} e seu saldo atual é de {saldo}")
    else:
        print("Você não tem este dinheiro ")
inter()