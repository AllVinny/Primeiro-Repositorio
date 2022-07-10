#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição do pagamento

#a vista dinheiro/cheque: 10% de desconto
#a vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros.

print('\033[7m--------------GERENCIADOR DE PAGAMENTOS--------------\033[m')
print('Insira o valor do produto, e depois qual o seu metodo de pagamento! ')

valor = float(input('Qual o valor do produto? R$ '))
metodo = str(input('Qual o metodo de pagamento? Dinheiro/Cheque/Cartão. ')).strip().lower()

if metodo == 'dinheiro' or metodo == 'cheque':
    print(f'Como vc escolheu pagar com {metodo.title()}, o valor ficou R$ {valor*0.9:,.2f}! (10% de desconto).')

elif metodo == 'cartão' or metodo == 'cartao':
    parcelas = int(input('Em quantas parcelas você quer pagar? Digite apenas o número! '))

    if parcelas == 1:
        print(f'Como você vai pagar em {parcelas}x no Cartão, o valor ficou em R$ {valor*0.95:,.2f}! (5% de desconto.')

    elif parcelas == 2:
        print(f'Como você vai pagar em {parcelas}x no Cartão, o valor se mantem R$ {valor:,.2f}. (Sem desconto). ')

    elif parcelas >= 3:
        print(f'Como você vai pagar em {parcelas}x no Cartão, o valor ficou em R$ {valor*1.20:,.2f}! (20% de juros).')

else:
    print(f'Não reconheci a forma de pagamento \033[7m"{metodo}"\033[m, só aceitamos Dinheiro, Cheque ou Cartão, reinicie o programa!!!')

print('\033[7m--------------FIM--------------\033[m')
