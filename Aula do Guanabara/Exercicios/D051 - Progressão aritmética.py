#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão aritmética. Mostre os 10 primeiros termos dessa progressão.

pt = int(input('Qual o primeiro termo da sua P.A.? '))
rp = int(input('Qual a razão da sua P.A? '))
decimotermo = pt + (10 - 1) * rp #isso foi resolvido pela matematica.
for c in range(pt,decimotermo + rp,rp):
    print(c, end=' -> ')

print('FIM')