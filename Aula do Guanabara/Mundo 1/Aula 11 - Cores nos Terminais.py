#Códigos ANSI são sempre começados em \ (contra-barra)
#\033[m, sendo que depois do couchete, usamos 0:33:44. Os números servem pra Estilo, Texto e Background

#O estilo pode ser 0,1,4 ou 7 (existem outros mais esses funcionam melhor pra python)
#Sendo Sem estilo, negrito, sublinhado, e negativo (inverte fundo e letra).

#o texto vai de 30 a 37, sendo cada um uma cor.

#mesma ordem de texto, mas de 40 a 47.

print('\033[0;30;41mOlá, mundo!\033[m')
print('\033[4;33;44mOlá, mundo!\033[m')
print('\033[1;35;43mOlá, mundo!\033[m')
print('\033[30;42mOlá, mundo!\033[m')
print('\033[mOlá, mundo!\033[m')
print('\033[7mOlá, mundo!\033[m')

nome = 'Vinny'
cores = {'limpa':'\033[m' ,
         'azul':'\033[34m' ,
         'amarelo' : '\033[33m',
         'invertida':'\033[7m'} #Lembrando: Listas são com {} na lista, e [] no format

print(f'{cores["invertida"]}-*{cores["limpa"]}'*20)
print(f'Oi, seu nome é {cores["azul"]}{nome}{cores["amarelo"]} !!!')
print(f'{cores["invertida"]}-*{cores["limpa"]}'*20)

print(f'{cores["limpa"]}-*'*20)
print(f'{cores["invertida"]}!!!FIM!!!{cores["limpa"]}')
print(f'{cores["limpa"]}-*'*20)