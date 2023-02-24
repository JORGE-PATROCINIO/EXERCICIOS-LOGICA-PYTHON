# NÚMERO MAIOR
# DEV: JORGE AUGUSTO
# DATA: 12/09/2022

#Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.

rep=True
while rep:
    N = float(input("Digite o primeiro número: "))
    N1 = float(input("Digite o segundo número: "))

    if N > N1:
        print(N, "É maior que: ", N1)
    else:
        print(N1, "É maior que: ", N)
    x=str(input("Deseja repetir a operação? S ou N?"))
    if x=="n" or x=="N":
        print("Até a próxima!!!")
        rep=False
    elif x=="s" or x=="S":
        rep=True
    else:
        print("ERRO !!!")
        
