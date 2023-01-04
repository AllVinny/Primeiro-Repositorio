#Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = 0
cont = 1
n = int(input('Qual o primeiro número? '))
maior = n
menor = n
soma += n
print('Deseja continuar? ')
continuar = str(input('S/N '))

if continuar == 's':
    while continuar == 's':
        n = int(input('Qual o proximo número? '))
        soma += n
        cont += 1
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        continuar = str(input('Deseja continuar? '))
    if continuar == 'n':
        media = soma/cont
        print(f'Você inseriu {cont} números;')
        print(f'O maior número foi {maior};')
        print(f'O menor número foi {menor};')
        print(f'A média entre os números foi {media}.')
else:
    print(f'Você digitou apenas o número {n}! ')

print('FIM')
