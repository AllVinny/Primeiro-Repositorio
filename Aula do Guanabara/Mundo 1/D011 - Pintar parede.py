#Faça um programa que leia a largura e a altura de uma parede em metros, calcule
#a sua area, e a quantiade de tinta necessária para pinta-la, sabendo que cada litro de tinta
#pinta uma area de 2m².

l = float(input('Qual a largura da sua parade? (em metros) '))
a = float(input('Qual a altura da sua parade? (em metros) '))

p = l*a
lt = p/2

print(f'Para pintar a sua parede inteira, você vai precisar de {lt} litros de tinta')