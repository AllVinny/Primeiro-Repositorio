frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

#Para printar textos longos:

print('''Texto longo
Cheio de linhas
com muita informação.''') #Utilizar 3 aspas no print.

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android')) #isso substitui apenas nessa frase. Para ser definitivo precisa ser como na linha 23
print(frase)

#frase = frase.replace('Python', 'Android') #Agora ficou definitivo.
#print(frase)

#frase = 'Curso em Vídeo Python'
print(frase.find('Vídeo')) #ele vai achar a frase vídeo, mas apenas da forma EXATA, se der find em video, não encontra

#frase = 'Curso em Vídeo Python'
#frase.split() vai separar a frase em varias palavras, eu posso atribuir a uma variavel e trabalhar a lista
dividido = frase.split()
print(dividido) #isso printa a LISTA
print(dividido[2]) #isso printa a terceira palavra
print(dividido[2] [3]) #isso printa a quarta palavra da terceira letra (palavra 3 letra 4)
