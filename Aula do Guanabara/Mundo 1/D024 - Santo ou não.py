#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo

cidade = input('Digite o nome de uma cidade qualquer: ').strip()
nome = cidade.lower()
prm = nome.split()
print(f'A cidade começa com santo? {prm[0] == "santo"}')
