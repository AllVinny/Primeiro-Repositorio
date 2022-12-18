#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores. Maioridade = 21 anos.

maior = 0
menor = 0
for ano in range (1,8):
    nasc = int(input(f'Qual o ano de nascimento da {ano}ª pessoa? '))
    if nasc >= 2001:
        maior += 1
    else:
        menor += 1
print(f'Desse grupo de 6 pessoas, {maior} atingiram a maioridade, e {menor} ainda não atingiram! ')
