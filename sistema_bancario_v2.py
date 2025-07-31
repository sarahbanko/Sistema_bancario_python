
def menu_opcoes():
    return input('''

============ Menu ============

Selecione uma opção abaixo:
                 
[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar novo usuário
[c] Criar conta corrente  
[l] Listar contas criadas                                       
[q] Sair

===============================

Obrigada por usar nosso sistema!


''')

def realizar_deposito(saldo, extrato, valores_d, /):
    valor_d = float(input("Insira o valor que deseja depositar: "))

    if valor_d > 0:
        saldo += valor_d
        extrato += f"Depósito: R$ {valor_d:.2f}\n"
        valores_d.append(valor_d)
        print("Depósito realizado com sucesso!")
    else:
        print("O valor informado é inválido!")

    return saldo, extrato, valores_d


def realizar_saque(*, saldo, extrato, valores_s, contador_saque, limite, LIMITE_SAQUES ):
    valor_s = float(input("Insira o valor que deseja sacar: "))
    excedeu_saldo = valor_s > saldo
    excedeu_limite = valor_s > limite
    excedeu_saques = contador_saque >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Saldo insuficiente!")
    elif excedeu_limite:
        print("Limite insuficiente!")
    elif excedeu_saques:
        print("Limite diário de saque excedido!")
    elif valor_s > 0:
        saldo -= valor_s
        contador_saque += 1
        extrato += f"Saque: R${valor_s:.2f}\n"
        print("Saque realizado com sucesso!")
        valores_s.append(valor_s)
    else:
        print("O valor informado é inválido!")

    return saldo, extrato, valores_s, contador_saque


def exibir_extrato(saldo, /, *, extrato):
    if (extrato != ""):
        print(f'''
--------- Extrato ----------
                  
{extrato}
                          
Saldo: R$ {saldo:.2f}
----------------------------
       
            ''')
            
    else:
            print(f'''
------------ Extrato -------------
                  
Não houve movimentações bancárias
                          
Saldo: R$ {saldo:.2f}
----------------------------------
       
            ''')

def novo_usuario(usuarios):

    cpf = input("Informe seu CPF (apenas números): ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado")
        return
    
    nome = input("Insira o nome completo: ").strip()
    nascimento = input("Informe a data de nascimento (dd-mm-aaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
   
    novo = {
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo)
    print("Usuário cadastrado com sucesso!")
    return usuarios

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(usuarios, contas, numero_conta):
    cpf = input("Insira o CPF (somente números): ").strip()
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print("CPF não encontrado. Cadastre um novo usuário!")
        return contas
    
    conta = {
        "agencia": "0001",
        "numero": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print(f"Conta número: {numero_conta} criada com sucesso para o usuário {usuario['nome']}.")
    return contas

def listar_contas(contas):
    print("Contas criadas: ")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número: {conta['numero']}, Titular: {conta['usuario']['nome']}")


def main():

    saldo = 0
    extrato = ""
    limite = 500
    LIMITE_SAQUES = 3
    contador_saque = 0
    valores_d = []
    valores_s = []
    usuarios = []
    contas = []
    numero_conta = 0


    while True:

        opcao = menu_opcoes()
        if opcao == "d":
            saldo, extrato, valores_d = realizar_deposito(saldo, extrato, valores_d)
        elif opcao == "s":
            saldo, extrato, valores_s, contador_saque = realizar_saque(saldo=saldo, extrato=extrato,valores_s=valores_s, contador_saque=contador_saque, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "u":
            usuarios = novo_usuario(usuarios)
        elif opcao == "c":
            contas = criar_conta(usuarios, contas, numero_conta)
            numero_conta += 1
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada!")

main()
