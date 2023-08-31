#Faça um programa que leia um angulo qualquer, e mostre na tela o valor
#do seno, cosseno e tangente desse angulo.

#Dica: Carregar o módulo certo.

import math

angg = float(input('Digite o ângulo: '))

angr = math.radians(angg)

seno = math.sin(angr)
cos = math.cos(angr)
tan = math.tan(angr)

print(f'O seno de é {angg} é {seno:.2f}!')
print(f'O cosseno de é {angg} é {cos:.2f}!')
print(f'E a tangente de é {angg} é {tan:.2f}!')