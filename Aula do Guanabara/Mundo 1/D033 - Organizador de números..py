#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Digite 3 números, que eu vou colocar em ordem: ')

n1 = int(input('Insira seu primeiro número: '))
n2 = int(input('Insira seu segundo número: '))
n3 = int(input('Insira seu terceiro número: '))

if n1>n2 and n1>n3:
    if n2>n3:
        print(f'A ordem dos números é: {n1}, {n2}, {n3}!')
    else:
        print(f'A ordem dos números é: {n1}, {n3}, {n2}!')
if n2>n1 and n2>n3:
    if n1>n3:
        print(f'A ordem dos números é: {n2}, {n1} e {n3}!')
    else:
        print(f'A ordem dos números é: {n2}, {n3} e {n2}!')
if n3>n1 and n3>n2:
    if n1>n2:
        print(f'A ordem dos números é: {n3}, {n1} e {n2}!')
    else:
        print(f'A ordem dos números é: {n3}, {n2} e {n1}!')

print('-----FIM-----')