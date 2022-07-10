#Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:

#Equilátero: todos os lados iguais
#Isosceles: dois lados iguais
#Escaleno: Todos os lados diferentes

print('\033[7m--------------ANALISE DE TRIANGULOS 2.0--------------\033[m')
print('Insira as medidas das retas, que eu vou te dizer se formam um triangulo, e qual seria o tipo de triangulo!! ')
n1 = float(input('Qual o tamanho da primeira reta? '))
n2 = float(input('Qual o tamanho da segunda reta? '))
n3 = float(input('Qual o tamanho da terceira reta? '))

if (n1+n2)>n3 and (n2+n3)>n1 and (n3+n1)>n2:
    print('As 3 retas que você inseriu, formam um triangulo! ')
    if n1 == n2 and n1 == n3:
        print('E seria um triângulo equilátero! (3 arestas de mesmo tamanho) ')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('E seria um triangulo isosceles! (2 arestas de mesmo tamanho)')
    else:
        print('E seria um triangulo escaleno! (Todos os lados de tamanhos diferentes)')

else:
    print('As medidas que você colocou não formam um triangulo :c ')

print('\033[7m--------------FIM--------------\033[m')