#Melhore o D061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele sisser que quer mostrar 0 termos.
'''
pt = int(input('Primeiro termo da PA: '))
rp = int(input('Razão da PA: '))
dt = pt + (10 - 1) * rp
atual = pt
while atual < dt+1:
    print(atual, end=' -> ')
    atual += rp
print('FIM')
'''
#Mudar programa para perguntar se quer continuar com um buleano, assim consigo ficar em apenas um while
pt = int(input('Primeiro termo da PA: '))
rp = int(input('Razão da PA: '))
dt = pt + (10 - 1) * rp

while pt < dt+1:
    print(pt, end=' -> ')
    pt += rp
t = int(input('\nQuantos termos a mais você quer mostrar? '))
if t != 0:
    dt = pt + (t - 1) * rp
    print(pt, end=' -> ')
    while pt < dt + 1:
        pt += rp
        print(pt, end=' -> ')
    t = int(input('\nQuantos termos a mais você quer mostrar? '))
else:
    print('Encerrando...')

