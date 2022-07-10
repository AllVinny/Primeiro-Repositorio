#Exemplo 1
'''nome = str(input('Qual é seu nome? '))
if nome == 'Vinny':
    print('Que nome lindo você tem!!') #Esse bloco só vai aparecer se o nome for Vinny (nome == 'Vinny'.
else:
    print('Seu nome é bem normal!!')
print(f'Bom dia, {nome}!')'''

#Exemplo 2

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m >= 6.0:
    print(f'Sua média foi {m:,.2f}, você foi aprovado. PARABÉNS!!!')
else:
    print(f'Sua média foi {m:,.2f}, você foi reprovado :c')

