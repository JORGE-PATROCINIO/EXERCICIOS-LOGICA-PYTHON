# VALIDAR SENHA
# DEV: JORGE AUGUSTO
# DATA:12/09/2022

# Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234.
#Devem ser impressas as seguintes mensagens: ACESSO PERMITIDO caso a senha seja válida e  ACESSO NEGADO caso a senha seja inválida.


senha = 1234
x = int(input("Digite a senha: "))
if x != senha:
    print("Acesso negado !")
else:
    print("Acesso liberado!")

