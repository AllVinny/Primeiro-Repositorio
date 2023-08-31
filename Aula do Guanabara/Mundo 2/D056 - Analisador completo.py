#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
soma = 0
mmv = 0
imv = 0
for p in range (1,5):
    print(f'Dados da {p}ª pessoa:')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade
    if sexo == 'M': #Nome do Homem mais velho
        if idade > imv:
            imv = idade
            nmv = nome
    if sexo == 'F': #Quantidade de mulheres com menos de 20 anos.
        if idade < 20:
            mmv += 1
mi = soma/4 #Média de idade
print(f'A média de idade do grupo é de {mi} anos;')
print(f'O homem mais velho do grupo é o {nmv}, com {imv} anos de idade;')
print(f'No grupo, {mmv} mulheres tem menos de 20 anos! ')
print('FIM')
