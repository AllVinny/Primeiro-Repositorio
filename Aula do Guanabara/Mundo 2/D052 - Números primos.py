#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. (primo = divisivel só por 1 ou ele mesmo).
#Ele só é divisivel duas vezes
tot = 0
n = int(input("Digite seu número: "))

for c in range(1,n+1):
    r = n/c
    if n%c == 0:
        tot += 1
        print(f'\033[7m{c:,.0f}\033[m', end=' ')
    else:
        print(f'{c}',end=' ')

print(f'\nO número {n} foi divido {tot} vezes ')

if tot <= 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')

print('Fim')