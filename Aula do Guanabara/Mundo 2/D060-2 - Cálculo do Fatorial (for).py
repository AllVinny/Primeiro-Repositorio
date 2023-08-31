#Faça um programa que leia um número qualquer e mostre seu fatorial.
#Ex: 5! = 5*4*3*2*1 = 120
#Escrever com for

n = int(input('Digite o número do seu fatorial: '))
c = n
f = 1

for c in range (c,0,-1):
    print(c, end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c-= 1
print(f)
