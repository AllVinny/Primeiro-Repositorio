# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder. Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
c = 0
while True:
    pc = random.randint(0,10)
    user_number = int(input('Escolha um valor: '))
    user_choice = str(input('Par ou Impar? [P/I] ')).strip().capitalize()
    if user_choice not in ['p', 'P', 'I', 'i']:
        print(f'Você digitou {user_choice}, escolha Par ou Impar [P/I]! ')
        continue
    s = pc + user_number
    if s % 2 == 0:
        r1 = 'P'
        r2 = 'PAR'
    else:
        r1 = 'I'
        r2 = 'IMPAR'

    if user_choice == r1:
        print(f'Você jogou {user_number} e o computador {pc}. Total de {s}, DEU {r2}')
        print('Você VENCEU! ')
        print('Vamos jogar novamente... ')
        c += 1


    else:
        print(f'Você jogou {user_number} e o computador {pc}. Total de {s}, DEU {r2}')
        print('Você PERDEU! ')
        break
print(f'GAME OVER! Você venceu {c} vezes! ')
    







# MESMA LOGICA APLICADA AO PEDRA PAPEL E TESOURA!
# import random
# p = 0
# while True:
#     pc = random.randint(0,2)
#     user = int(input('''Digite sua escolha: 
#                     1 - Pedra
#                     2 - Papel
#                     3 - Tesoura
#                     '''))
    
#     if user == 1 and pc == 2 or user == 2 and pc == 3 or user == 3 and pc == 1:
#         print(f'Você perdeu essa, mas venceu as ultimas {p} partidas! ')
#         break
    
#     if user == pc:
#         print(f'Empatou! ')
#         continue

#     else:
#         print(f'Você ganhou!')
#         p += 1

#     if pc == 1:
#         pc2 = 'Pedra'
#     if pc == 2:
#         pc2 = 'Papel'
#     if pc == 3:
#         pc2 = 'Tesoura'


