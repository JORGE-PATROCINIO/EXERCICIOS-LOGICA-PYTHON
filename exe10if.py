# VALIDAR SENHA
# DEV: JORGE AUGUSTO
# DATA:12/09/2022

# Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234.
#Devem ser impressas as seguintes mensagens: ACESSO PERMITIDO caso a senha seja válida e  ACESSO NEGADO caso a senha seja inválida.

senha = 1234
for i in range(0,3,1):
    x =int(input("Digite a senha: "))
    if x != senha:
        if i == 2:
            print("Acesso negado !")
            print("Bloqueado, procure a agência mais próxima!")
            break
        print("Acesso negado !")
        print(f"Faltam {2 - i:,.0f} tentativas!")
    else:
        print("Acesso liberado!")
        break
