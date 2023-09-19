# CLASSIFICAÇÃO DE RISCO POR PESO E IDADE
# DEV: JORGE AUGUSTO
# DATA: 05/09/2022

# Faça um programa que receba a idade e o peso de uma pessoa. 
# De acordo com a tabela a seguir, verifique e mostre em qual grupo de risco essa pessoa se encaixa.

#        IDADE               ATÉ 60KG          ENTRE 60 E 90KG                 ACIMA DE 90KG
#        <20                    9                     8                              7
#        ENTRE 20 E 50          6                     5                              4
#        >50                    3                     2                              1


rep = True
while rep:
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    if idade <= 0 or peso <= 0:
        print("Dados inválidos!")
    elif idade < 20 and peso <= 60:
        print("Grupo de risco 9!")
    elif idade < 20 and peso > 60 and peso <= 90:
        print('Grupo de risco 8!')
    elif idade < 20 and peso > 90:
        print("Grupo de risco 7!")
    elif idade >= 20 and idade <= 50 and peso <= 60:
        print("Grupo de risco 6!")
    elif idade >= 20 and idade <= 50 and peso > 60 and peso <= 90:
        print("Grupo de risco 5!")
    elif idade >= 20 and idade <= 50 and peso > 90:
        print("Grupo de risco 4!")
    elif idade > 50 and peso <= 60:
        print("Grupo de risco 3!")
    elif idade > 50 and peso > 60 and peso <= 90:
        print("Grupo de risco 2!")
    elif idade > 50 and peso > 90:
        print("Grupo de risco 1!")
    print("******************************************")

    x = input("Deseja repetir a operação? S /N?\n")

    if x == 'S' or x == 's':
        rep = True
    elif x == 'N' or x == 'n':
        rep = False
    else:
        print("ERRO")
        rep = False
    print("******************************************")
