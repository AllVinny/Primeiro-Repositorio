# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se se o usuário vai continuar. No final mostre:

# A- qual é o total gasto na compra.
# B - Quantos produtos custam mais de R$1000
# C - Qual é o nome do produto mais barato.

print('---LOJA SUPER BARATÃO---')

total = contm = maisbarato = 0

while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    

    total += preço

    if preço > 1000:
        contm += 1

    if maisbarato == 0 or maisbarato > preço:
        maisbarato = preço
        nomemaisbarato = produto
    
    cont = str(input('Quer continuar? [S/N] ')).strip().capitalize()
    while cont not in ['S', 'N']:
        cont = str(input('Quer continuar? [S/N] ')).strip().capitalize()
    if cont == 'N':
        break
    
print('\n---FIM DO PROGRAMA---')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {contm} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nomemaisbarato}, que custa R$ {maisbarato:.2f}')
