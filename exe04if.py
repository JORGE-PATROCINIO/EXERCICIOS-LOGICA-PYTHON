# Salário Bruto
# Dev: Jorge Augusto
# 30/08/2022

#Faça um programa que receba o salário bruto de um funcionário e, usando a tabela a seguir, calcule e mostre o valor a receber. Sabe-se que este é composto pelo salário bruto acrescido de gratificação e descontado o imposto de 7% sobre o salário.

#         SALÁRIO                          GRATIFICAÇÃO
#       ATÉ R$ 350,00                        R$ 100,00
#       ATÉ R$ 351,00 ATÉ R$600,00           R$ 75,00
#       ATÉ R$ 601,00 ATÉ R$900,00           R$ 50,00
#       ACIMA R$ 900,00                      R$ 35,00

imposto = 0.07
salario = 1
rep = True
print("Digite salário = 0 para finalizar o programa!")
while rep:
    salario = float(input("Digite o salário do funcionário: "))
    if salario < 0:
        print("Salário inválido!")
    elif salario <= 350 and salario != 0:
        salarioareceber = salario - salario * 0.07 + 100
        print("O salário a receber é: R$", salarioareceber, " reais !")
    elif salario > 350 and salario <= 600:
        salarioareceber = salario - salario * 0.07 + 75
        print("O salário a receber é: R$ ", salarioareceber, " reais !")
    elif salario > 600 and salario <= 900:
        salarioareceber = salario - salario * 0.07 + 50
        print("O salário a receber é: R$", salarioareceber, " reais !")
    elif salario > 900:
        salarioareceber = salario - salario * 0.07 + 35
        print("O salário a receber é: R$", salarioareceber, " reais !")
    else:
        rep = False
