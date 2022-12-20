#Refaça o D051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
pt = int(input('Qual o primeiro termo da sua P.A.? '))
rp = int(input('Qual a razão da sua P.A? '))
decimotermo = pt + (10 - 1) * rp #isso foi resolvido pela matematica.
for c in range(pt,decimotermo + rp,rp):
    print(c, end=' -> ')

print('FIM')
'''
pt = int(input('Primeiro termo da PA: '))
rp = int(input('Razão da PA: '))
dt = pt + (10 - 1) * rp
while pt < dt+1:
    print(pt, end=' -> ')
    pt += rp
print('FIM')