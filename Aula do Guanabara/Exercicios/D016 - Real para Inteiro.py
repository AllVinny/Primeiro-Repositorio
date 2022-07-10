#Crie um programa que leia um número real qualquer pelo teclado e mostre na sua tela a sua
#porção inteira. Ex: 6,127 "o numero 6.127 tem a parte inteira 6

#Dica: Funções do Módulo math

import math

num = float(input('Insira um número real: (ex: 1,2432) '))
#Inputando 1.123
num1 = math.modf(num)
#depois desse comando, num1 vira "0.123", "1.0"
#Só incluir [1] no print
#Na aula, o guanabara ensina a função trunc(num), q faz isso de forma automatica
#e tbm transformando o float em um int

print(num1)
print(num1[0])
print(num1[1])
print(f'O valor digitado foi {num}, e a sua porção inteira é {num1[0]}')