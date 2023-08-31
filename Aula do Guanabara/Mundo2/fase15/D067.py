# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valdigitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0
while True:
    t = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 1:
        break
    while t <= 10:
        print(f'{n} x {t} = {n*t}')
        t += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')