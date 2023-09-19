# ALTURA E SEXO
# DEV: JORGE AUGUSTO
# DATA: 13/09/2022

#Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1: feminino 2: masculino) de uma pessoa,
#construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:

#para homens: (72.7 * Altura) – 58
#para mulheres: (62.1 * Altura) – 44.7

sexo = int(input("Digite 1 para o sexo feminino ou 2 para sexo masculino: "))
if sexo == 1:
    altura = float(input("Digite a altura em cm: "))
    pesoideal = round((62.1 * (altura / 100) - 44.7), 2)
    print(pesoideal, "KG é o peso ideal!")
elif sexo == 2:
    altura = float(input("Digite a altura em cm: "))
    pesoideal = round((72.7 * (altura / 100) - 58), 2)
    print(pesoideal, "KG é o peso ideal!")
else:
    print("Opção inválida!")
