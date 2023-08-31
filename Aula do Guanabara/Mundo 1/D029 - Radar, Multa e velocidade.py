#Escreva um programa que leia a velocidade de um carro.

#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada Km acima do limite.

v1 = float(input('Qual a velocidade do seu carro em Km/h? '))

if v1>80:
    m = (v1-80)*7
    print(f'Você foi multado em R$ {m:,.2f} por estar {v1-80:,.2f} km/h acima do limite. ')

else:
    print(f'Muito bem, você respeita o limite de velocidade!')

print('-----FIM-----')
