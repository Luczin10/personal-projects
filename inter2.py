nome=input("Digite seu nome     ")
saldo=1000.00
print("Olá %s oque deseja fazer?"%(nome))
while True:
    escolha=int(input("1-extrato    2-depositar 3-meu porquinho     4-sair      "))
    if escolha==4:
        print("\033[93m Obrigado pela escolha, espero que nosso serviço tenha te satisfeito :)")
        break
    if escolha==1:
        print("Não ha depositos recentes mas seu saldo é de saldo R$%-5.2f"%(saldo))
    elif escolha==2:
        quem=input("Para quem você irá depositar?           ")
        quanto=int(input("Digite quanto você irá depositar          "))
        confirmação=input("Você confirma sua transação          ").lower
        if confirmação=="sim":
            print("parabéns você depositou R$%-5.2f para %s, agora você tem %f"% (quanto, quem, saldo))
        else:
            print("\033[31m Tranferencia cancelada\033[0m")
    elif escolha==3:
        pupanca=0.0
        print("Olá %s estamos muito felizes em saber que quer investir, seu saldo da conta poupança é de %-5.2"% (nome,pupanca))
    
    
        

