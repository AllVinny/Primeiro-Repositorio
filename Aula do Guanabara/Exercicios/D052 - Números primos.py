#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. (primo = divisivel só por 1 ou ele mesmo).
#Ele só é divisivel duas vezes
#criar if para programa divisivel por 2 (n%2==0: não primo)
#

test = 0
n = int(input("Digite seu número: "))

for c in range(1,n+1):
    r = n/c
    if n%c == 0:
        test += 1
        print(f'\033[7m{c:,.0f}\033[m', end=', ')
    else:
        print(f'{c}',end=', ')

print(f'O número {n} foi divido {test} vezes ')


if test <= 2:
    print('E por isso ele É primo')
else:
    print('E por isso ele NÃO é primo')

print('Fim')