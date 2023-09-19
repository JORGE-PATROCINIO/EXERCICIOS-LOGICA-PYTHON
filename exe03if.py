# EXERCÍCIO IDADE DO NADADOR
# DEV: JORGE AUGUSTO
# DATA: 29/08/2022

#Faça um programa que receba a idade de um nadador e mostre sua categoria, 
#usando as regras a seguir. Para idade inferior a 5, qual mensagem deveríamos mostrar?

#                      CATEGORIA                     IDADE
#                      INFANTIL                       5 A 7
#                      JUVENIL                        8 A 10
#                      ADOLESCENTE                    11 A 15
#                      ADULTO                         16 A 30
#                      SÊNIOR                         ACIMA DE 30

idade = 1

print("Digite idade=0 para finalizar!")

while idade != 0:

    idade = int(input("DIGITE A IDADE DO NADADOR: "))

    if idade == 0:
        print("FIM !")
    elif idade < 5 or idade > 80:
        print("IDADE INVÁLIDA!")
    elif idade >= 5 and idade <= 7:
        print("Categoria Infantil!")
    elif idade >= 8 and idade <= 10:
        print("Categoria Juvenil!")
    elif idade >= 11 and idade <= 15:
        print("Categoria Adolescente!")
    elif idade >= 16 and idade <= 30:
        print("Categoria Adulto!")
    else:
        print("Categoria Sênior!")
