#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Insira um número: '))
    if n != 999:
        cont += 1
        soma += n
print(f'Você inseriu {cont} números, e a soma deles resulta em {soma}. ')
