menu = ''''


============ Menu ============

Selecione uma opção abaixo:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

===============================

Obrigada por usar nosso sistema!


'''

saldo = 0
extrato = ""
limite = 500
LIMITE_SAQUES = 3
contador_saque = 1
valores_d = []
valores_s = []

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_d = float(input("Insira o valor que deseja depositar: "))

        if valor_d > 0:
            saldo += valor_d
            extrato += f"Depósito: R$ {valor_d:.2f}\n"
            print("Depósito realizado com sucesso!")
           
        else:
            print("O valor informado é inválido!")
        
    elif opcao == "s":
        valor_s = float(input("Insira o valor que deseja sacar: "))
        excedeu_saldo = valor_s > saldo
        excedeu_limite = valor_s > limite
        excedeu_saques = contador_saque > LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Valor maior do que o limite permitido")
        
        elif excedeu_saques:
            print("Limite diário de saque excedido!")

        elif (valor_s > 0):
            saldo -= valor_s
            contador_saque += 1
            extrato += f"Saque: R$ {valor_s:.2f}\n"
            print("Saque realizado com sucesso!")

        else:
            print("O valor informado é inválido!")

    elif opcao == "e":

        if (extrato != ""):

            print(f'''
--------- Extrato ----------
                  
{extrato}
                          
Saldo: R$ {saldo:.2f}
----------------------------
       
            '''
            )
            
        else:
            print(f'''
------------ Extrato -------------
                  
Não houve movimentações bancárias
                          
Saldo: R$ {saldo:.2f}
----------------------------------
       
            '''
            )
            
    elif opcao == "q":
        break   

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")
