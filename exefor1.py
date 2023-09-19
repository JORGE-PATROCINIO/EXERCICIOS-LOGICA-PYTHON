# AUMENTO SALARIAL
# DEV: JORGE AUGUSTO
# DATA: 13/09/2022

# Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:

# a) esse funcionário foi contratado em 2000, com salário inicial de R$1.000,00;

# b) Em 2001, ele recebeu aumento de 1,5%, sobre o seu salário inicial;

# c) A partir de 2002 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.

# Faça um programa que determine o salário desse funcionário dos anos de 2000 à 2017. Apresente todos os valores.

SI = TAXA = SA = REAJ = 0

for ano in range(2000, 2018, 1):
    if ano == 2000:
        SI = 1000
        print("Ano", ano, "SI: R$", round(SI, 2), "taxa: %", TAXA, "Reajuste:R$", round(REAJ, 2), "SA: R$", round(SA, 2))
    elif ano == 2001:
        TAXA = 0.00015
        REAJ = SI * TAXA
        SA = SI + REAJ
        print("Ano", ano, "SI: R$", round(SI, 2), "taxa: %", TAXA, "Reajuste:R$", round(REAJ, 2), "SA: R$", round(SA, 2))
    else:
        print("Ano", ano, "SA: R$", round(SA, 2))
        REAJ = SA * TAXA
        SA = SA + REAJ
        print("Ano", ano, "Reajuste:R$", round(REAJ, 2), "SA: R$", round(SA, 2))
    TAXA *= 2
