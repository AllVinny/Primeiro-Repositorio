#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

#Tentar montar como string ou com matemática, qualquer um dos 2 vale.

#num = input('Digite um número de 0 a 9999: ')

#print(f'''Milhar: {num[-4]};
#Centena: {num[-3]};
#Dezena: {num[-2]};
#Unidade: {num[-1]}.''')

num = int(input('Digite um número de 0 a 9999: '))

print((f'Analisando o número {num}'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'''Milhar: {m};
#Centena: {c};
#Dezena: {d};
#Unidade: {u}.''')