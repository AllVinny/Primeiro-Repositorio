#Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = 0
cont = 0
continuar = True
conti = "S"
soma = 0
maior = 0
menor = 0

while continuar == True:
    n = int(input('Qual o seu número? '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    cont += 1
    conti = str(input('Deseja continuar? S/N '))
    if conti == 'S' or 's':
        continuar = True
    if conti == 'N' or 'n':
        continuar = False
media = soma/cont
print(f'Você digitou {cont} valores; ')
print(f'O maior valor foi {maior}; ')
print(f'O menor valor foi {menor};')
print(f'A média dos números inseridos é {media}')
