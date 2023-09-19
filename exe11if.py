# COMPRA DE MAÇÃS
# DEV: JORGE AUGUSTO
# DATA:13/09/2022

#As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze.
#Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

N = int(input("Digite a quantidade de maçãs: "))

if N >= 12:
    print(f"O valor total foi de {N*0.25:,.2f} reais!")
else:
    print(f"O valor total foi de {N*0.3:,.2f} reais!")

