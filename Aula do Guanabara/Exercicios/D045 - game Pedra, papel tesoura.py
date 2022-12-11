#Crie um programa que faça o computador jogar jokenpo com vc.
import random
import time

#alteração simples

print('\033[7m--------------PEDRA, PAPEL, TESOURA--------------\033[m')
print('Vamos jogar Pedra, Papel ou Tesoura?!')
time.sleep(0.5)
pc = random.randint(0,2)
user = str(input('Digite sua escolha: ')).strip().title()

if pc == 0:
    pc2 = 'Pedra'
if pc == 1:
    pc2 = 'Papel'
if pc == 2:
    pc2 = 'Tesoura'
time.sleep(0.3)
print('JO')
time.sleep(0.3)
print('KEN')
time.sleep(0.3)
print('PO')
time.sleep(0.5)

if pc2 == user:
    print(f'Empatou, nós dois escolhemos {pc2}')
elif pc2 == 'Pedra' and user == 'Tesoura':#PC ganha
    print(f'Eu escolhi {pc2}, GANHEI! ')
elif pc2 == 'Pedra' and user == 'Papel': #USER ganha
    print(f'Eu escolhi {pc2}, VOCÊ GANHOU! ')
elif pc2 == 'Papel' and user == 'Pedra': #PC ganha
    print(f'Eu escolhi {pc2}, GANHEI! ')
elif pc2 == 'Papel' and user == 'Tesoura': #USER ganha
    print(f'Eu escolhi {pc2}, VOCÊ GANHOU! ')
elif pc2 == 'Tesoura' and user == 'Pedra': #USER ganha
    print(f'Eu escolhi {pc2}, VOCÊ GANHOU! ')
elif pc2 == 'Tesoura' and user == 'Papel': #PC ganha
    print(f'Eu escolhi {pc2}, GANHEI! ')

elif user != 'Pedra' and user != 'Papel' and user != 'Tesoura':
    print('Você não sabe jogar! Digite Pedra, Papel ou Tesoura! ')

time.sleep(0.5)
print('\033[7m--------------FIM--------------\033[m')
print('Quer tentar de novo??? ')
