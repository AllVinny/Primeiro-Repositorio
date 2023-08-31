#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#peso em kg, dividido pela altura ao quadrado, em metros
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 e 25: peso ideal
#25 até 30: sobrepeso
#De 30 até 40: obesidade
#Acima de 40: obesidade mórbida.

print('\033[7m--------------CALCULO DE IMC--------------\033[m')
print('Vamos descobrir qual o seu IMC? ')
p = float(input('Digite seu peso em Kg: '))
a = float(input('Digite sua altura em metros: '))
imc = p/(a**2)

if imc < 18.5:
    print(f'Seu IMC é {imc:,.2f}, você está abaixo do peso ideal! ')

elif imc >=18.5 and imc < 25:
    print(f'Seu IMC é {imc:,.2f}, você está no seu peso ideal! ')

elif imc >= 25 and imc < 30:
    print(f'Seu IMC é {imc:,.2f}, você está com sobrepeso! ')

elif imc >= 30 and imc < 40:
    print(f'CUIDADO!!! Seu IMC é {imc:,.2f}, você está obeso!')

elif imc >= 40:
    print(f'CUIDADO!!! Seu IMC é {imc:,.2f}, você está com obesidade morbida!')

print('\033[7m--------------FIM--------------\033[m')