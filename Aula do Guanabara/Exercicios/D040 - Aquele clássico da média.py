#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#Média abaixo de 5.0: Reprovado
#Média entre 5.0 e 6.9: Recuperação
#Média 7 ou superior: Aprovado.

print('\033[7m--------------MÉDIA DE ALUNOS--------------\033[m')
print('Vamos calcular a média dos alunos!')

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Aluno REPROVADO. Média {media:,.2f}!')

elif media >= 5 and media < 6.99:
    print(f'Aluno em RECUPERAÇÃO. Média {media:,.2f}!')

else:
    print(f'Aluno APROVADO. Média {media:,.2f}!')

print('\033[7m--------------FIM--------------\033[m')