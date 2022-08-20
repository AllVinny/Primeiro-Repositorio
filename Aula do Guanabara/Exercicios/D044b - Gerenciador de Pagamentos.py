#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição do pagamento

#a vista dinheiro/cheque: 10% de desconto
#a vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros.

#Na correção do exercicio, as formas de pagamento foram passadas antes
#Preço das compras: xxxx
#[1] A vista dinheiro/cheque
#[2] A vista cartão
#[3] 2x no cartão
#[4] 3x ou mais no cartão - Quantas parcelas? xx. {calculo}

#Sua compra será parcelada em xxx de {valor da parcela} COM JUROS (ou sem juros).
#Sua compra de xxxx vai custar xxxx(com juros).

#Dessa forma o programa fica mais intuitivo, mas reduz a possibilidade de parcelamento.

#Tentar fazer um meio termo, como 44b.

print('\033[7m--------------GERENCIADOR DE PAGAMENTOS--------------\033[m')
valor = float(input('Preço das Compras: R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
metodo = int(input('Qual é a opção? '))

if metodo == 1:
    print(f'Sua compra será À VISTA, em DINHEIRO ou CHEQUE, e o valor passa de R${valor:,.2f} para R${valor*0.9:,.2f}')

elif metodo == 2:
    print(f'Sua compra será À VISTA no CARTÃO, e o valor passa de R${valor:,.2f} para R${valor*0.95:,.2f}')

elif metodo == 3:
    print(f'Sua compra será parcelada em 2x de R${valor/2:,.2f} SEM JUROS. Totalizando R${valor:,.2f}!')

elif metodo == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R$ {(valor*1.2)/parcelas:,.2f} COM JUROS.')
    print(f'Sua compra de R${valor:,.2f} passa a custar R${valor*1.2:,.2f}.')

else:
    print('Opção Inválida. Tente novamente!')

print('\033[7m--------------FIM--------------\033[m')