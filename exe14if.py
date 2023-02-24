# POLÍGONO
# DEV: JORGE AUGUSTO
# DATA: 13/12/2022

#Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).

#Calcular e imprimir o seguinte:

#Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área

#Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.

#Se o número de lados for igual a 5 escrever PENTÁGONO.

import math
nlados = int(input("Digite o número de lados: "))
if nlados > 2 and nlados < 5:
    vlados = float(input("Digite a medida do lado:"))
    if nlados == 3:
        raizq = math.sqrt(3)
        area = (vlados ** 2 * raizq) / 4
        print(f"É um triângulo de área igual á {area:,.2f} CM²")
    elif nlados == 4:
        area = (vlados ** 2)
        print(f"É um quadrado de área igual á {area:,.2f} CM²")
elif nlados == 5:
    print("É um pentágono!")

