# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1

print('---BANCO CEV---')

valor = int(input('Que valor você quer sacar? R$ '))
valornotas = resto = cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0
resultadofinal = []
while valornotas != valor:
    if valor >= 50:
        cedulas50 += 1
        valor -= 50
        resultado50 = f'Total de {cedulas50} de R$ 50,00'
        continue
    if valor >= 20:
        cedulas20 += 1
        valor -= 20
        resultado20 = f'Total de {cedulas20} de R$ 20,00'
        continue
    if valor >= 10:
        cedulas10 += 1
        valor -= 10
        resultado10 = f'Total de {cedulas10} de R$ 10,00'
        continue
    if valor >= 1:
        cedulas1 += 1
        valor -= 1
        resultado1 = f'Total de {cedulas1} de R$ 1,00'
        continue
    
if cedulas50 > 0:
    resultadofinal.append(resultado50)
if cedulas20 > 0:
    resultadofinal.append(resultado20)
if cedulas10 > 0:
    resultadofinal.append(resultado10)   
if cedulas1 > 0:
    resultadofinal.append(resultado1) 
    
print(resultadofinal)
print('Volte sempre ao BANCO CEV! Tenha um ótimo dia!')