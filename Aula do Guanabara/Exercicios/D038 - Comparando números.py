#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais.
print('\033[7m--------------COMPARADOR DE NÚMEROS--------------\033[m')
print('Insira 2 números, e vou te dizer qual é o maior.')

num1 = int(input('Digite o primeiro númmero: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro número é maior! {num1} é maior que {num2}!')

elif num2 > num1:
    print(f'O segundo número é maior! {num2} é maior que {num1}!')

else:
    print('Nenhum dos números é maior, os dois são iguais.')

