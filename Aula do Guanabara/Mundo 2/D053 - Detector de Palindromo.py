#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços. (Pode ler de frente pra tras ou invertido que da a mesma frase).
#A base do teto desaba.
#A mãe te ama

#p = entrada
#r = sem espaços
#i = invertida

#p = 'A mãe te ama'
p = input('Frase ou palavra: (digite sem acento) ').strip().lower() #testar depois

r = p.replace(' ','')
i = r[::-1]


if r == i:
    print('A frase que você escreveu é um palindromo! ')
else:
    print('A frase que você escreveu não é um palindromo! ')
