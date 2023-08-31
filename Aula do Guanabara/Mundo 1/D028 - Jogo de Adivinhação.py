#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador.

#O programa deverá escrever na tela se o usuário venceu ou perdeu.

#import time - Não consegui fazer esse import, mas deveria funcionar com o comando sleep(x), sendo 5 os segundos de delay
import random

num1 = random.randint(0, 5)
print('Pensei em um número entre 0 e 5, você consegue adivinhar qual? ')
num2 = int(input('Qual o número que eu pensei?: ')) #Ele só vai aceitar entrada de número, se digitar letra ele quebra.

print('Será que você acertou? ')

#sleep(3)

if  num1 == num2:
    print(f'Você acertou! Eu pensei no número {num1}!')
    print('---FIM---')

elif num2>5:
    print(f'Você digitou um número maior que 5!')
    print('Tente novamente!')

elif num2<0:
    print(f'Você digitou um número menor que 0!')
    print('Tente novamente!')

else:
    print(f'Você errou! O número que eu pensei foi o {num1}, e não o {num2}.')
    print('---FIM---')


