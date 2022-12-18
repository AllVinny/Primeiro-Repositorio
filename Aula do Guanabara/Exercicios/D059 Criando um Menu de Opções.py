#Crie um programa que leia dois valores e mostre um menu na tela:
'''1- Somar
2- multiplicar
3- maior
4- novos números
5- sair do programa'''

#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
v1 = int(input('Insira o primeiro valor: '))
v2 = int(input('Insira o segundo valor: '))
menu = False

while menu == False:
    sleep (0.15)
    print('1 - Somar')
    sleep (0.15)
    print('2 - Multiplicar')
    sleep (0.15)
    print('3 - Mostrar o maior número')
    sleep (0.15)
    print('4 - Trocar números')
    sleep (0.15)
    print('5 - Sair do Programa')
    sleep (0.3)
    menu = int(input('Qual opção você quer seguir? '))
    if menu == 1:
        r = v1 + v2
        print(f'O resultado da soma de {v1} + {v2} é {r}! ')
        menu = False
        sleep (0.6)
    elif menu == 2:
        r = v1 * v2
        print(f'O resultado da multiplicação de {v1} * {v2} é {r}! ')
        menu = False
        sleep (0.6)
    elif menu == 3:
        maior = 0
        if v1 > v2:
            maior = v1
            print(f'O maior número é {maior}! ')
        elif v2 > v1:
            maior = v2
            print(f'O maior número é {maior}! ')
        else:
            print(f'Os dois números são iguais! ')
        menu = False
        sleep (0.6)
    elif menu == 4:
        v1 = int(input('Qual o novo primeiro valor? '))
        v2 = int(input('Qual o novo segundo valor? '))
        menu = False
        sleep (0.6)
    elif menu == 5:
        menu = True
        print('Finalizando ',end='')
        print('.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='\n')
    else:
        print('Opção inválida. Tente novamente!')
        sleep (0.6)
        menu = False
    print('=-=' * 10)
print('FIM!')
