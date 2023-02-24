# AUMENTO SALARIAL
# DEV: JORGE AUGUSTO
# DATA: 13/09/2022

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
