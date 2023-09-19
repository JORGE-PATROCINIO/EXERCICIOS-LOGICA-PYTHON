# RECEBER NOMES E SALÁRIOS
# DEV: JORGE AUGUSTO
# DATA: 12/09/2022

#Faça um programa que receba o salário de um funcionário chamado Carlos.
#Sabe-se que outro funcionário, João, tem salário equivalente a um terço do salário de Carlos.
#Carlos aplicará seu salário integralmente na caderneta de poupança, que rende 2% ao mês,
#e João aplicará seu salário integralmente no fundo de renda fixa, que rende 5% ao mês. 
#O programa deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale
#ou ultrapasse o valor pertencente a Carlos.

Meses = 0
RendaPoupanca = 1.02
RendaFundo = 1.05

Salario = float(input("Qual o salário: "))
ValorPoupanca = Salario * RendaPoupanca
print(ValorPoupanca)
Salario = Salario / 3
ValorFundoRendaFixa = Salario * RendaFundo
print(ValorFundoRendaFixa)

while ValorFundoRendaFixa < ValorPoupanca:
    Meses += 1
    print(f"O valor de investimentos do João é: , {ValorFundoRendaFixa:,.2f}, mês", Meses)
    if ValorFundoRendaFixa < ValorPoupanca:
        ValorPoupanca = ValorPoupanca * RendaPoupanca
        ValorFundoRendaFixa = ValorFundoRendaFixa * RendaFundo
        continue
    else:
        break
