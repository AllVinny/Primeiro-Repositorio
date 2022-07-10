#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
#um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

import math

cop = float(input('Insira o tamanho do cateto oposto: '))
cad = float(input('Insira o tamanho do cateto adjacente: '))

r = math.hypot(cop, cad)

print(f'A hipotenusa é igual a {r}!')