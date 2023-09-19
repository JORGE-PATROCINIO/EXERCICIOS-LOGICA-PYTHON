# GRATIFICAÇÃO DE NATAL
# DEV: JORGE AUGUSTO
# DATA: 30/08/2022

#Uma empresa decidiu dar uma gratificação de Natal a seus funcionários, 
#baseada no número de horas extras e no número de horas que o funcionário faltou ao trabalho.
#O valor do prêmio é obtido pela consulta à tabela que se segue, na qual:

# H = número de horas extras – (2/3 * ( número de horas falta ))         H (MINUTOS	PRÊMIO (R$)

#                      >= 2.401	                                             500,00
#                      1.801 até 2.400                                       400,00
#                      1.201 até 1.800                                       300,00
#                      600 até 1.200                                         200,00
#                      <600	                                                 100,00
rep = True
while rep:
    horaextra = int(input("Digite o número de horas extras: "))
    horafalta = int(input("Digite o número de faltas em horas:"))
    H = (horaextra - (2 / 3 * horafalta)) * 60
    if horaextra < 0 or horafalta < 0:
        print("Valor fora da faixa!")
    elif H < 600:
        print("O valor da gratificação é: R$ 100,00")
    elif H >= 600 and H <= 1200:
        print("O valor da gratificação é: R$ 200,00")
    elif 1200 < H <= 1800:
        print("O valor da gratificação é: R$ 300,00")
    elif H > 1800 and H <= 2400:
        print("O valor da gratificação é: R$ 400,00")
    else:
        print("O valor da gratificação é: R$ 500,00")
    x = int(input("Deseja repetir a operação? 1 para sim e 2 para não!\n"))
    if x == 1:
        rep = True
    elif x == 2:
        rep = False
    else:
        print("Erro")
        rep = False
