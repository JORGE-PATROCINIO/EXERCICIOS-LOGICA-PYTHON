# O MAIOR DE 3 VALORES
# DEV: JORGE AUGUSTO
# DATA: 13/09/2022

#Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário não informará valores iguais.

n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))
if n1 > n2 and n1 >n3:
    print(n1, "é o maior número!")
elif n2 > n1 and n2 > n3:
    print(n2, "é o maior número!")
elif n3 > n2 and n3 > n1:
    print(n3, "é o maior número!")
