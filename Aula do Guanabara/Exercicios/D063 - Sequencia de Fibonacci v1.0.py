#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
#ex: 1 - 1 - 2 - 3 - 5 - 8

n = int(input('Quantos números da serie de Fibonacci você precisa ver? '))
cont = 1
atual = 1
anterior = 0

print(atual)

while cont < n:
    v = atual + anterior
    anterior = atual
    atual = v
    cont += 1
    print(v)
print('FIM')