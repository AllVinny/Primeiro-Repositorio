#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
#triangulo

#é um principio matemáticom tem que dar uma pesquisada.
#(n1+n2)>n3

n1 = int(input('Qual o tamanho da primeira reta? '))
n2 = int(input('Qual o tamanho do segunda reta? '))
n3 = int(input('Qual o tamanho do terceira reta? '))

if (n1+n2)>n3 and (n2+n3)>n1 and (n3+n1)>n2:
    print('As 3 retas que você inseriu, formam um triangulo! ')

else:
    print('As retas que você colocou não formam um triangulo! ')

print('-----FIM-----')