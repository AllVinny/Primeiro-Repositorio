#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('Insira um número: '))


if (num%2) == 0: #Leia-se: se a variavel dividida por 2 tem resto 0
    print(f'O número {num} é par!')

else:
    print(f'O número {num} é impar')

print('---FIM---')
