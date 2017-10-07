# ----------- ANALISADOR DE TEXTOS ------------ #

nome = str(input("Digite seu nome: "))

print ("Seu nome em letra maiuscula e {}".format(nome.upper()))
print ("Seu nome em letra minuscula e {}".format(nome.lower()))
print ("Seu nome tem ao todo {} letras".format(nome.__len__() - nome.count(' ')))
print ("Seu primeiro nome tem {} letras".format(nome.find(" ")))

