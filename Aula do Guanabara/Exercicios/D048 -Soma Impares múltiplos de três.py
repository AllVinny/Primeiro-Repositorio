#Faça um programa que calcule a soma entre todos os números impares que são multiplos de 3 e que se encontram no intervalo de 1 até 500.

'''somar todos os numeros //2 que quando dividido por 3 resta 0'''
s=0
cont = 0
for c in range(1,501,2):
    if c%3 ==0:
        cont = cont + 1 #ou cont += 1
        s += c
print(f'A soma dos {cont} valores solicitador é {s}.')
print('Fim')