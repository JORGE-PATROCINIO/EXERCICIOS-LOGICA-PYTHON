# RECEBER NOMES E SALÁRIOS
# DEV: JORGE AUGUSTO
# DATA: 12/09/2022

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
