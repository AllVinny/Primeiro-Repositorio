#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e
#motre sua categoria, de acordo com a idade:

#Até 9 anos: Mirim
#Até 14 anos: Infantil
#até 19 anos: Junior
#até 20 anos: Senior
#20+: Master

print('\033[7m--------------CLASSIFICAÇÃO DE ATLETAS--------------\033[m')
print('Vamos descobrir em qual categoria seu atleta vai competir!')

idade = int(input('Qual a idade do atleta? '))

if idade <= 9:
    print(f'Atletas de {idade} anos, competem na categoria MIRIM! ')

elif idade < 14:
    print(f'Atletas de {idade} anos competem na categoria INFANTIL! ')

elif idade <= 19:
    print(f'Atletas de {idade} anos competem na categoria JUNIOR! ')

elif idade >= 20:
    print(f'Atletas de {idade} anos ou mais competem na categoria MASTER! ')



print('\033[7m--------------FIM--------------\033[m')