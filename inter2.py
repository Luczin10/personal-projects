import login2
def verificação():
    while True:
       
        global nome 
        nome=input("Digite seu nome de login")
        for nomes in login2.Usuario:
            if nome==nomes:
                print("Bem vindo")  
                return
            else:
                print("Login não existente, tente novamente") 
                break
verificação()
saldo=1000.00
print("Olá %s oque deseja fazer?"%(nome))
extrato=""
while True:
    escolha=int(input("1-extrato    2-depositar 3-meu porquinho     4-sair      "))
    if escolha==4:
        print("\033[93m Obrigado pela escolha, espero que nosso serviço tenha te satisfeito :)\033[0m")
        break
    if escolha==1:
        print(f"\033[32m {extrato}Seu saldo é de saldo R$%-5.2f\033[0m"%(saldo))
    elif escolha==2:
        quem=input("Para quem você irá depositar?           ")
        quanto=float(input("Digite quanto você irá depositar          "))
        confirmação=input("Você confirma sua transação          ").lower()      
        if confirmação=="sim":
            if quanto<=saldo:
                saldo-=quanto
                extrato=("\033[38;5;10m você depositou R$%-5.2f para %s."% (quanto, quem,))
                print("\033[32m Transação aprovada\033[0m")
            else:
                print("\033[31m Você não tem esse dinheiro, pobre, você neste momento tem %f\033[0m"%(saldo))
        else:
            print("\033[31m Tranferencia cancelada\033[0m")
    elif escolha==3:
        pupanca=0.0
        print("Olá %s estamos muito felizes em saber que quer investir, seu saldo da conta poupança é de %-5.2f"% (nome,pupanca))
        deposito_pou=float(input("Quanto ira colocar na poupança?           "))
        confirmação_pou=input("Você %s confirma sua tranferencia de %-5.2f para a conta poupança?       "% (nome, deposito_pou)).lower()
        if confirmação_pou=="sim":
            if deposito_pou<=saldo:
                var3=saldo
                saldo-=deposito_pou
                deposito_pou=var3-saldo
                print("\033[32m Deposito feito\033[0m")
                print("\033[93m Nossas agências trabalham sempre com a verdade por isso nossa poupança rende 14,75'%'ao ano ")
                print("Um exemplo é que colocando R$1000.00 no porquinho por 5 meses daria R$3.500.00 sem juros compostos\033[0m")
                meses=int(input("Quantos meses ficará seu deposito de %-5.2f ?"%(deposito_pou)))
                rendimento=(deposito_pou*0.5)*meses + deposito_pou
                print("Seu rendimento final,sera de: %-5.2f"% (rendimento))
                saldo=rendimento
                
            else:
                print("\033[31m Erro \033[0m")
        else:
            print("\033[31m Tranferencia cancelada\033[0m")
    else:
        print("\033[31m Erro \033[0m")
    
            
