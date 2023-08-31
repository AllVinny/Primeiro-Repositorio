#Melhore o jogo do D028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
pc = random.randint(0,10)
cont = 1
print('Pensei em um número entre 0 e 10, consegue adivinhar qual? ')
us = int(input('Qual número eu pensei? '))

while us != pc: #O professor atibuiu uma variavel de ACERTOU = False, e quando us == pc, acertou = True. No while fica (while not acertou:), então cont iniciaria em 0, e us só entra depois do while
    if us > pc:
        print('Você errou, eu pensei em um número menor! ')
    if us < pc:
        print('Você errou, eu pensei em um número maior!')
    us = int(input('Qual número eu pensei? '))
    cont += 1

print(f'Você acertou com {cont} tentativas. Parabéns! ')
    
#----------------------------------------------------------#CÓDIGO DO PROFESSOR
pc = random.randint(0,10)
acertou = False
print('Pensei em um número entre 0 e 10, consegue adivinhar qual? ')
cont = 0
while not acertou:
    us = int(input('Qual número eu pensei? '))
    cont += 1
    if us == pc:
        acertou = True
    else:
        if us > pc:
            print('Você errou, eu pensei em um número menor! ')
        if us < pc:
            print('Você errou, eu pensei em um número maior!')
print(f'Você acertou com {cont} tentativas. Parabéns! ')