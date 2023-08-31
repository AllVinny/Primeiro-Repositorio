#Faça um programa que leia um número qualquer e mostre seu fatorial.
#Ex: 5! = 5*4*3*2*1 = 120
#Vale a pena tentar com while e for
'''
cont = 1
r = 1
n = int(input('Digite um número para descobrir seu fatorial: '))

while cont <= n:
    r *= cont
    cont += 1
print(r)
'''
#----------------------------------------------------#

n = int(input('Fatorial: '))
#fatorial = n*n-1*n-2...n-n
cont = 1
fat = 1
while cont <= n:
    fat *= cont
    if cont == n:
        print(f'{cont}',end=' ')
    else:
        print(f'{cont} *',end=' ')
    cont += 1
print(f'= {fat}')
