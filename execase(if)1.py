# Preço de Produtos (case 1)
# DEV: JORGE AUGUSTO
# DATA:18/09/2022

#Faça um programa que receba o preço, a categoria (1 – limpeza; 2 – alimentação; ou 3 – vestuário) e
#a situação (R – produtos que necessitam de refrigeração;
#e N – produtos que não necessitam de refrigeração). Calcule e mostre:

#O valor do aumento, usando as regras que se seguem.

#  PREÇO         CATEGORIA          PERCENTUAL DE AUMENTO
#  <=25              1                       5%
#  <=25              2                       8%
#  <=25              3                       10%
#  >25               1                       12%
#  >25               2                       15%
#  >25               3                       18%

#O valor do imposto, usando as regras a seguir.

#O produto que preencher pelo menos um dos seguintes requisitos pagará imposto equivalente a 5% do preço; caso contrário, pagará 8%. Os requisitos são:
#Categoria: 2
#Situação: R

#O novo preço, ou seja, o preço mais aumento menos imposto.
#A classificação, usando as regras a seguir.

#  NOVO PREÇO             CLASSIFICAÇÃO
# <= 50                      BARATO
# ENTRE 50 E 120             NORMAL
# > 120                      CARO

imposto = 0.08
preco = float(input("Digite o preço: "))
categoria = int(input("Digite a categoria:"))
situacao = str(input("Digite N para produtos não refrigerados ou R para produtos refrigerados: "))

if preco <= 25:
    if categoria == 1:
        precoaumento = preco * 1.05
        novopreco = precoaumento * (1 - imposto)  # preço sem imposto

        if novopreco <= 50:
            print("Produto Barato")
        elif novopreco > 50 and novopreco < 120:
            print("Produto Normal")
        else:
            print("Produto Caro")
    elif categoria == 2 or situacao == "R" or situacao == "r":
        precoaumento = preco * 1.08
        novopreco = precoaumento * (1 - 0.05)

        if novopreco <= 50:
            print("Produto Barato")
        elif novopreco > 50 and novopreco < 120:
            print("Produto Normal")
        else:
            print("Produto Caro")
    else:
        precoaumento = preco * 1.10
        novopreco = precoaumento * (1 - imposto)

        if novopreco <= 50:
            print("Produto Barato")
        elif novopreco > 50 and novopreco < 120:
            print("Produto Normal")
        else:
            print("Produto Caro")

elif preco > 25:

    if categoria == 1:
        precoaumento = preco * 1.12
        novopreco = precoaumento * (1 - imposto)

        if novopreco <= 50:
            print("Produto Barato")
        elif novopreco > 50 and novopreco < 120:
            print("Produto Normal")
        else:
            print("Produto Caro")

    elif categoria == 2 or situacao == "R" or situacao == "r":
        precoaumento = preco * 1.15
        novopreco = precoaumento * (1 - 0.05)
        if novopreco <= 50:
            print("Produto Barato")
        elif novopreco > 50 and novopreco < 120:
            print("Produto Normal")
        else:
            print("Produto Caro")
    else:
        precoaumento = preco * 1.18
        novopreco = precoaumento * (1 - imposto)
        if novopreco <= 50:
            print("Produto Barato")
        elif novopreco > 50 and novopreco < 120:
            print("Produto Normal")
        else:
            print("Produto Caro")

print("O valor do aumento é: RS ", round(precoaumento - preco, 2))
print("O valor do imposto é: RS ", round(precoaumento - novopreco, 2))
print("O novo preço sem imposto é: RS ", round(novopreco, 2))
