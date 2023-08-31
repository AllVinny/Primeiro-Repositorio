#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possiveis sobre ele.

#Recebe a informação e imprime o que ela é

x = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(x),'!') #O resultado sempre vai ser str
print('Só tem espaços?', x.isspace())
print('Você digitou letras? ', x.isalpha())
print('Você digitou um número? ', x.isalnum())
print('A primeira letra é maiuscula?', x.isidentifier())
print('Está só com letras maiusculas?', x.isupper())
print('Está só com letras minusculas?', x.islower())
print('Está com apenas a primeira letra maiuscula? ', x.istitle()) #title = Capitalizada