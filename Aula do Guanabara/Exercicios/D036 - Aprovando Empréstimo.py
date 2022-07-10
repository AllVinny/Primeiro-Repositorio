#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

print('\033[7m--------------Aprovando Empréstimo--------------\033[m')
print('Vamos ver se seu empréstimo será aprovado?')

casa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o seu salário mensal? R$ '))
ano = float(input('Em quantos anos você pretende pagar? ')) #Precisa transformar anos em meses.

meses = (ano*12) #agora sei o resultado em meses, preciso ver a mensalidade da casa

parcela = casa/meses

if parcela > (sal*0.3):
    print(f'Seu empréstimo foi recusado! A parcela ficaria maior que 30% do seu salário!')

else:
    print(f'Seu empréstimo foi aprovado, seu pagamento fica {meses:,.0f} parcelas de R$ {parcela:,.2f}! PARABENS!')