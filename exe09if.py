# IDADE PARA VOTO(CONSIDERANDO SOMENTE O ANO)
# DEV: JORGE AUGUSTO
# DATA: 13/09/2022

#Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

anoatual = int(input("Digite o ano atual com 4 digítos: "))
anonascimento = int(input("Digite o ano de nascimento com 4 digítos: "))
idade = anoatual - anonascimento

if idade >= 16:
    print(idade, "Anos,você já pode votar!")
else:
    print(idade, "Anos,você ainda não pode votar!")
