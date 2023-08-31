#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#o nome com todas minusculas
#quantas letras no total, sem considerar espaços - split e soma(?) #DESAFIO
#quantas letras tem o primeiro nome. (aproveita os splits de cima)

nome_completo = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')


nome_upper = nome_completo.upper()
nome_lower = nome_completo.lower()


#---------------------------------------

espaços = int(nome_completo.count(' '))
letras = int(nome_completo.count(''))
res = letras-espaços-1 #Poderia usar len(nome_completo) - nome_completo.count(' '). Isso tiraria variavel e usaria menos
#linhas

n1 = nome_completo.split()
pn = int(n1[0].count(''))

respn = pn-1

print(f'O nome com todas as letras maiusculas fica {nome_upper}!')
print(f'O nome com todas as letras minusculas fica {nome_lower}!')
print(f'Seu nome completo tem {res} letras, e {respn} delas estão no seu primeiro nome! ({n1[0]})')
