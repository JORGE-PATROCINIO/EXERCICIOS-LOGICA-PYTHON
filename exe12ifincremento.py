# VALORES EM ORDEM
# DEV: JORGE AUGUSTO
# DATA: 13/09/2022

#Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

rep = True
while rep:

    n1 = int(input("Entre com o primeiro número: "))
    n2 = int(input("Entre com  o segundo número: "))
    n3 = int(input("Entre com o terceiro número: "))

    if n1==n2 or n1==n3 or n2==n3:
        print("Não podem ser iguais, tente novamente!")
    else:
        if n1 > n2 and n1 > n3:
            maior = n1
            if n2 > n3:
                intermediario = n2
                menor = n3
            else:
                intermediario = n3
                menor = n2
        elif n2 > n1 and n2 > n3:
            maior = n2
            if n1 > n3:
                intermediario = n1
                menor = n3
            else:
                intermediario = n3
                menor = n1
        elif n3 > n1 and n3 > n2:
            maior = n3
            if n2 > n1:
                intermediario = n2
                menor = n1
            else:
                intermediario = n1
                menor = n2
        print("A ordem correta dos números digitados é: ", menor, intermediario, maior)
        ret = str(input("Deseja repetir a operação? S ou N?"))

        if ret == "s" or ret == "S":
            rep = True
        elif ret == "n" or ret == "N":
            print("Agradecemos a sua visita!!!")
            rep = False
        else:
            print("Comando incorreto!")
            rep = False
