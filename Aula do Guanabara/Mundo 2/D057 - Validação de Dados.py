#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
from time import sleep
sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0] #O zero no final da linha é para pegar apenas a primeira letra. Ex: Digite masculino.

while sexo not in 'MmFf':
    sleep(0.2)
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()
    sleep(0.2)
print(f'Sexo {sexo} registrado com sucesso! ')
