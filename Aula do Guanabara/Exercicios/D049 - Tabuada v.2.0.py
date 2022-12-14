#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Qual a tabuada que você quer ver agora? '))

m=0
for tab in range(0,10):
    m = tab+1
    r = n * m

    if m == 10:
        print(f'{n} vezes {m} é {r}. ')
    else:
        print(f'{n} vezes {m} é {r}; ')
print(f'Essa é a tabuada do {n}! ')