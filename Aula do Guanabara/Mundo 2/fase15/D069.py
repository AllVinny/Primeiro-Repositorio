# Crie um programa que leia a idade e o sex de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuário quer ou não continuar. No final mostre:
# A - Quantas pessoas tem mais de 18 anos.
# B - Quantos homens foram cadastrados.
# C - Quantas mulheres tem menos de 20 anos.
count18 = countm = countm20 = 0
test = True
while test == True:
    print('CADASTRE UMA PESSOA! ')
    age = int(input('Idade: '))
    sex = str(input('Sexo: [M/F] ')).strip().capitalize()[0]
    while sex not in ['M', 'F']:
        sex = str(input('Sexo: [M/F] ')).strip().capitalize()[0]

    if age > 18:
        count18 += 1
    
    if sex == 'M':
        countm += 1
    
    if sex == 'F' and age < 20:
        countm20 += 1

    cont = str(input('Deseja continuar? [S/N] ')).strip().capitalize()[0]
    while cont not in ['N', 'S']:
        cont = str(input('Deseja continuar? [S/N] ')).strip().capitalize()
    if cont == 'N':
        test = False
print(f'Total de pessoas com mais de 18 anos: {count18}')
print(f'Ao todo temos {countm} homens cadastrados')
print(f'E temos {countm20} mulheres com menos de 20 anos')
    