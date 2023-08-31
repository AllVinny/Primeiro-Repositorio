#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcula o preço da passagem, cobrando R$ 0,50 por km para viagens até 200Km
#e R$ 0,45 para viagens mais longas.

dist = float(input('Qual a distância da sua viagem em km? '))

if dist<=200:
    v = dist*0.5
    print(f'Sua viagem de {dist:,.0f} Km vai custar R$ {v:,.2f}. (R$ 0,50 por km)')

else:
    v2 = dist*0.45
    print(f'Sua viagem de {dist:,.0f} km vai custar R$ {v2:,.2f}. (R$ 0,45 por km)')

#Eu poderia ter colocado apenas v, e usar um unico print, visto que o valor de V ja depende da distancia.

print('-----FIM-----')
    
