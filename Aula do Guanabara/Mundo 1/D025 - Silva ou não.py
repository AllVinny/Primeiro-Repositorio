#Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome

nome = input('Insira seu nome completo: ').strip()

n1 = nome.lower()
print(f'Seu nome tem Silva? {"silva" in n1}.')