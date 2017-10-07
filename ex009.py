# ------------ TEOREMA DE PITÁGORAS ------------ #

from math import hypot

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

hi = hypot(co, ca)

print ("O valor da hipotenusa e: {}".format(hi))