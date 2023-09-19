# COMPRA DE PRODUTO(CASE2)
# DEV: JORGE AUGUSTO
# DATA: 19/09/2022

#Faça um programa que receba:

#O código do produto comprado; e
#A quantidade comprada do produto.
#Calcule e mostre:

#O preço unitário do produto comprado, seguindo a Tabela abaixo;
#O preço total da nota;
#O valor do desconto, seguindo a Tabela abaixo e aplicado sobre o preço total da nota; e
#O preço final da nota depois do desconto.

#   CÓDIGO         PREÇO          PREÇO TOTAL DA NOTA       % DESCONTO
#   1 A 10           10               ATÉ 250                    %5
#   11 A 20          15               ENTRE 250 E 500            %10
#   21 A 30          20               ACIMA DE 500               %15
#   31 A 40          30                                          

codigo=int(input("Digite o Código do Produto: "))
quantidade=int(input("Digite a quantidade de Produto: "))

if codigo >= 1  and codigo <= 10:
    PU=10   # PREÇO UNITÁRIO
    Nota = quantidade * PU
    if Nota <= 250:
        NotaDesc = Nota - (Nota * 0.05)
    else:
        NotaDesc=Nota
elif codigo >= 11 and codigo <= 20:
    PU=15
    Nota = quantidade * PU
    if Nota >= 250 and Nota <= 500:
        NotaDesc = Nota - (Nota * 0.1)
    else:
        NotaDesc = Nota
elif codigo >= 21  and codigo <= 30:
    PU=20
    Nota = quantidade * PU
    if Nota > 50:
        NotaDesc = Nota - (Nota * 0.15)
    else:
        NotaDesc=Nota
elif codigo >=31 and codigo <= 40:
    PU=30
    Nota = quantidade * 30
    NotaDesc=Nota

print("O Valor unitário do Produto é = R$ ", PU, ",00")
print("O Valor da nota é = R$ ", Nota, ",00")
print("O Valor do desconto é = R$ ", Nota-NotaDesc, ",00")
print("o Valor da nota com desconto é = R$ ", NotaDesc, ",00")
