# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.

print('Calculo de aumento salarial.')
wage = float(input('Qual o salário atual? R$ '))

if wage > 1250:
    print(f'O salário vai ficar em R${wage*1.10:,.2f}')
else:
    print(f'O salário vai ficar em R${wage*1.15:,.2f}')



