# ----------- SENO, COSSENO E TANGENTE DE UM ANGULO ---------- #

from math import sin, cos, tan, radians

ang = float(input("Digite o angulo: "))

s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))

print("O angulo de {} tem o seno de: {:.2f} \n"
      "O angulo de {} tem o cosseno de: {:.2f} \n"
      "O angulo de {} tem a tangente de: {:.2f}".format(ang, s, ang, c, ang, t))