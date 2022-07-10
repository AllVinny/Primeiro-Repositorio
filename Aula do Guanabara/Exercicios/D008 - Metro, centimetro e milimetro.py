#Escreva um programa que leia um valor em metros, e o exiba convertido em centimetros e milimetros.

m = float(input('Quantos metros você precisa converter? '))
c = int(m*100)
mm = int(c*10)

print(f'Em {m}m, você tem {c} centimetros e {mm} milimetros!')