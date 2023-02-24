# TRIÂNGULOS
# DEV: JORGE AUGUSTO
# DATA: 13/09/2022

#Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isósceles ou Escaleno.

#Sendo que:

#Triângulo Equilátero: possui os 3 lados iguais.
#Triângulo Isóscele: possui 2 lados iguais.
#Triângulo Escaleno: possui 3 lados diferentes.

L1=float(input("Digite o primeiro lado: "))
L2=float(input("Digite o segundo lado: "))
L3=float(input("Digite o terceiro lado: "))

if L1 != L2 != L3:
    print("O triângulo é escaleno !")
elif L1 == L2 == L3:
    print("O triângulo é equilátero !")
else:
    print("O triângulo é isoscele !")
