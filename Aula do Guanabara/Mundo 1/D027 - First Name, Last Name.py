#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
#ultimo nome separadamente.

#Ex: Ana Maria de Souza
#Primeiro = Ana
#Ultimo = Souza

n1 = input('Digite seu nome completo: ').strip.title().split()

print(f'''Seu primeiro nome é {n1[0]}.
Seu último nome é {n1[-1]}.''')
#Isso se chama indexação negativa, e usamos quando queremos começar a contar do ultimo item da lista
