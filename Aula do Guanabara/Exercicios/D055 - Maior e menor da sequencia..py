#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
for c in range(1,6):
    peso = float(input(f'Insira o {c}º peso em kg: '))
    if c == 1: #se é pra comparar entre o que o usuário inserir, o primeiro vira uma régua... assim você não precisa estabelecer o limite.
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        elif peso > maior:
            maior = peso
print(f'O maior peso por de {maior}kg; ')
print(f'E o menor peso foi {menor}kg. ')
print('FIM')
