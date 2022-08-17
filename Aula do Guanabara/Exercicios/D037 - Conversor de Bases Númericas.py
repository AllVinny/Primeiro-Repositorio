#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual sera a base de conversão:

#1 para binário
#2 para octal
#3 para hexadecimal

#Estudar base númericas.

print('\033[7m--------------CONVERSÃO DE BASES NÚMERICAS--------------\033[m')
print('Vamos converter um número para Binário, Octal ou Hexadecimal. ')

num = int(input('Digite um número inteiro: '))
print('Opções: ')
print('1 - Binário. ')
print('2 - Octal. ')
print('3 - Hexadecimal. ')
base = int(input('Qual a base para conversão? ' ))

if base == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num) [2:]}!')
elif base == 2:
    print(f'{num} convertido pra OCTAL é igual a {oct(num) [2:]}!')
elif base == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num) [2:]}!')
else:
    print('Opção inválida, tente novamente!!')


print('\033[7m--------------FIM--------------\033[m')