# ----------- ALUGUEL DE CARROS ------------- #

dia = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
total = (60 * dia) + (0.15 * km)
print("O preco a pagar ficou: {} reais".format(total))