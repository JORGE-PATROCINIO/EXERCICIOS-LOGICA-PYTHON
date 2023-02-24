# Ângulos do triângulo
# Dev: Jorge Augusto
# Data: 13/09/2022

#Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo.

#Sendo que:

#Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
#Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90º)
#TriânguloAcutângulo: possui três ângulos agudos. (menor que 90º

A1=float(input("Digite o primeiro ângulo do triângulo: "))
A2=float(input("Digite o segundo ângulo do triângulo: "))
A3=float(input("Digite o terceiro ângulo do triângulo: "))
soma=A1+A2+A3
if soma != 180:
    print("Valores inválidos !")
elif A1 == 90 or A2 == 90 or A3 == 90:
    print("É um triângulo reto !")
elif A1 > 90 or A2 > 90 or A3 > 90:
    print("É um triângulo obtusângulo!")
elif A1 < 90 and A2 < 90 and A3 < 90:
    print("É um triângulo acutângulo !")
