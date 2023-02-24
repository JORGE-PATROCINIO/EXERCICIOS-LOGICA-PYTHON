# POLÍGONO COMPLEMENTO
# DEV: JORGE AUGUSTO
# DATA: 13/12/2022

#Acrescente as seguintes mensagens à solução da tarefa 14 conforme o caso.

#Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.

#Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
import math

nlados = int(input("Digite o número de lados: "))
if nlados > 2 and nlados < 5:
    vlados = float(input("Digite a medida do lado em CM:"))
    if nlados==3:
        raizq = math.sqrt(3)
        area = (vlados ** 2 * raizq) / 4
        print(f"É um triângulo de área igual á {area:,.2f}CM²")
    elif nlados == 4:
        area = (vlados ** 2)
        print(f"É um quadrado de área igual á {area:,.2f} CM²")
elif nlados == 5:
    print("É um pentágono!")
elif nlados > 5:
    print("Polígono não identificado!")
else:
    print("Não é um polígono!")
