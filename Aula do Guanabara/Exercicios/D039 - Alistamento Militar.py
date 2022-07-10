#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se ja passou do tempo do alistamento.

#Seu programa tambem deverá mostrar o tempo que falta ou o tempo que passou do prazo.

print('\033[7m--------------ALISTAMENTO MILITAR--------------\033[m')
print('Vamos ver como está seu alistamento?')
nasc = int(input('Insira o ano que você nasceu: Ex: 1996. '))

idade = 2022-nasc

if idade < 18:
    dif = 18-idade
    print(f'Você tem {idade} anos, ainda faltam {dif} para o seu alistamento. ')

elif idade == 18:
    print(f'Fique atento, você precisa se alistar até o final desse ano. ')

else:
    dif = idade-18
    print(f'Atenção, seu alistamento deveria ter acontecido a {dif} anos. Regularize sua situação! ')


print('\033[7m--------------FIM--------------\033[m')