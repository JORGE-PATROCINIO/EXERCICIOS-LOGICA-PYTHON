# CONJUNTO DE VALORES
# DEV: JORGE AUGUSTO
# DATA: 12/09/2022

#Faça um programa que leia um conjunto não determinado de valores e mostre o valor lido, seu quadrado, seu cubo e sua raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

import math
valor=1
print("Digite um número negativo ou 0 para encerrar a aplicação!")
while valor > 0:
    valor = float(input("Digite um valor: "))
    if valor <= 0:
        print("Obrigado, volte sempre!")
    else:
        quadrado = valor*valor
        cubo = valor**3
        raizq = math.sqrt(valor)
        print(f"O quadrado de {valor},é igual á: {quadrado:,.1f}!")
        print(f"O cubo de {valor},é igual á: {cubo:,.1f}!")
        print(f"A raíz quadrada de {valor},é igual á: {raizq:,.1f}!")

