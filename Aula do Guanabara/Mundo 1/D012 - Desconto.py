#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input('Qual o valor do produto? '))
pd = p*0.95

print(f'Com 5% de desconto, o valor cai de R${p} para R${pd}!')