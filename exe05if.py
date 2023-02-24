# SALÁRIO DE 10 FUNCIONÁRIOS
# DEV: JORGE AUGUSTO
# DATA:11/09/2022

#Uma empresa possui dez funcionários com as seguintes características: código, número de horas trabalhadas no mês, turno de trabalho (M – matutino; V – vespertino; N – noturno), categoria (O – operário; ou G – gerente), valor da hora trabalhada.

#Sabendo-se que essa empresa deseja informatizar sua folha de pagamento, faça um programa que: a) Leia as informações dos funcionários, exceto o valor da hora trabalhada, não permitindo que sejam informações dos turnos e nem categorias inexistentes. Trabalhe sempre com a digitação de letras maiúsculas; b) Calcule o valor da hora trabalhada, conforme a tabela 1. Adote o valor de R$450,00 para o salário mínimo; c) Calcule o salário inicial dos funcionários com base no valor da hora trabalhada e no número de horas trabalhadas; d) Calcule o valor do auxílio alimentação recebido pelo funcionário de acordo com seu salário inicial, conforme a tabela 2; e) Mostre o código, número de horas trabalhadas, valor da hora trabalhada, salário inicial, auxílio alimentação e salário final (salário inicial + auxílio alimentação).

#       CATEGORIA                TURNO                 VALOR DA HORA TRABALHADA
#           G                      N                    18% DO SALÁRIO MÍNIMO
#           G                   M OU V                  15% DO SALÁRIO MÍNIMO
#           O                      N                    13% DO SALÁRIO MÍNIMO
#           O                   M OU V                  10% DO SALÁRIO MÍNIMO

#      SALÁRIO INICIAL                                  AUXILÍO ALIMENTAÇÃO
#      ATÉ R$300,00                                     20% DO SALÁRIO INICIAL
#      ENTRE R$300,00 E R$600,00                        15% DO SALÁRIO INICIAL
#      ACIMA DE R$600,00                                 5% DO SALÁRIO INICIAL


NF: int = 1
C = True

while NF <= 10:
    SalarioMinimo = 450  # ESSAS VARIAVEIS NÃO PODEM SER CRIADAS FORA DO LAÇO WHILE!!!!
    AuxilioAlimentacao = 0
    SalarioInicial = 0
    SalarioFinal = 0

    codigo = int(input("Digite o Codigo: "))                             # CÓDIGO DO FUNCIONÁRIO
    NHoratrabalhada = int(input("Digite o Número de Horas trabalhadas: "))

    while C:
        categoria = (input("Digite a categoria: "))
        if categoria == "O" or categoria == "o" or categoria == "G" or categoria == "g":
            C = False
        else:
            print("Digite uma categoria válida ( G ou O) !")
    C = True
    while C:
        turno = (input("Digite o turno: "))
        if turno == "N" or turno == "n" or turno == "M" or turno == "m" or turno == "v" or turno == "V":
            C = False
        else:
            print("Digite um turno válido: ( M, V ou N) !")

    if categoria == "G" or categoria == "g" and turno == "N" or categoria == "n":
        VHtrabalhada = SalarioMinimo * 0.18
        SalarioInicial = NHoratrabalhada * VHtrabalhada

        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    if categoria == "G" or categoria == "g" and turno == "M" or turno == "m" or turno == "V" or turno == "v":
        VHtrabalhada = SalarioMinimo * 0.15
        SalarioInicial = NHoratrabalhada * VHtrabalhada

        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    if categoria == "O" or categoria == "o" and turno == "N" or turno == "n":
        VHtrabalhada = SalarioMinimo * 0.13
        SalarioInicial = NHoratrabalhada * VHtrabalhada

        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    if categoria == "O" or categoria == "o" and turno == "M" or turno == "m" or turno == "V" or turno == "v":
        VHtrabalhada = SalarioMinimo * 0.10
        SalarioInicial = NHoratrabalhada * VHtrabalhada

        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.10
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    print("Código: ", codigo)
    print("Categoria:", categoria)
    print("Turno:", turno)
    print("Números de Horas Trabalhadas: ", NHoratrabalhada)
    print("Valor da hora trabalhada:R$", VHtrabalhada)
    print("Salário Inicial:R$ ", SalarioInicial)
    print("Salário Final:R$ ", SalarioFinal)
    print("Auxilio Alimentação:R$ ", AuxilioAlimentacao)
    print("Números de Funcionários: ", NF)

    NF = NF + 1
    C = True
print("FIM !")
