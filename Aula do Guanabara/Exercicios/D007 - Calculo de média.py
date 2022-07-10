#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

aluno = input('Qual o nome do aluno? ')
n1 = float(input(f'Qual a primeira nota do {aluno}? '))
n2 = float(input(f'Qual a segunda nota do {aluno}? '))

ma = ((n1+n2)/2)

print(f'A média do {aluno} foi de {ma}!')