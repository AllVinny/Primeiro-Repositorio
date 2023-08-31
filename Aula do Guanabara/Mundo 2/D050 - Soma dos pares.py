#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

from time import sleep

print('Digite 6 números, que vou somar apenas os pares! ')
soma = 0
cont = 0
contp = 0

sleep(0.3)
for c in range(1,7):
    num = int(input(f'Digite {c}ª valor: '))
    if num%2==0:
        soma += num
        contp += 1

    cont += 1
print(f'Você informou {cont} números, {contp} eram pares, e a soma dos pares resulta em {soma}! ')


