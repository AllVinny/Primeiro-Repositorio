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
'''
pt = int(input('Primeiro termo da PA: '))
rp = int(input('Razão da PA: '))
dt = pt + (10 - 1) * rp
encerrar = False
r = 0
print(pt, end = ' -> ')
while encerrar == False:
    while pt < (dt):
        pt += rp
        print(pt, end = ' -> ')
    t = int(input('\nQuantos termos mais você quer mostrar? '))
    if t != 0:
        while pt < dt + ( (t+r) * rp ):
            pt += rp
            print(pt, end=' -> ')
        encerrar = False
        r += t
    else:
        encerrar = True
print('Encerrando...')

'''

#teste2
cont = 0
pt = int(input('Primeiro termo da PA: '))
rp = int(input('Razão da PA: '))
parada = 10

while cont < parada:
    print(pt, end=' -> ')
    pt += rp
    cont += 1
    if cont == parada:
        rp2 = int(input('\nQuantos temos mais você quer mostrar? '))
        parada += rp2
print('FIM')