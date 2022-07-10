#Manipular cadeias de texto e caracteres

#Cadeia de texto/caracteres - Strings ou frases.

frase='curso em vídeo python' #essa atribuição usa memória do pc para armazenar cada caracter separadamente, organizando
#por indice. Indice de 0 até o necessário. Nesse caso seria de 0 a 20, para 21 caracteres.

'''Fatiamento'''

#print(frase[9]) mostraria o décimo caracter.
#print(frase[9:13]) Mostraria de V até o E (Vide), pois ele não pega o que a gente deu de limite.
#print(frase[9:21]) Mostraria de V até o N, ja que ele não mostraria o 22o caracter.
#print(frase[9:21:2]) Segue a mesma regra acima, mas o ultimo numero mostra que de 2 a 2 ele pularia. (Vdo Pto)
#print(print[:5]) Sem o numero de inicio, ele começa do caracter 0, mesma coisa que 0:5 nesse caso.
#print(print[15:]) Sem o numero final, ele mostra de onde partir, ate o final da variavel.
#print(print[9::3]) Sem o numero do meio, vai ter um inicio, vai mostrar tudo até o final, pulando de 3 em 3 (VePh)

'''Análise'''
#len(frase) conta o número de caracteres
#frase.count('o') manda contar as letras O em minusculo, nesse caso, 3
#frase.count('o',0,13) igual acima, mas com o fatiamento de 0 a 13 (ultimo valor ignorado), nesse caso, 1
#frase.find('deo') conta ONDE ele encontra as letras DEO, no caso, posição 11 (ja que está na ordem).
#frase.find('Android') Se não existe algo do find na string solicitada, ele retorna o valor -1
#'curso' in frase - Podemos usar o comando IN para procurar algo dentro da string

'''Transformação'''
#frase.replace('Python', 'Android') - Substituiria direto na frase, tiraria python e colocaria android.
#frase.upper() colocaria a frase em caixa alta.
#frase.lower() colocaria a frase em caixa baixa.
#frase.capitalize() coloca tudo em minusculo, e coloca a primeira letra da string em maiusculo, no caso, apenas o C
#frase.title() quebra a string em palavras (usando como separação a barra de espaços), e coloca a inicial de cada
#palavra em maiusculo. Curso Em Video Python.

#agora trabalhando com:
frase='   Aprenda Python  ' #3 Espaços iniciais e 2 finais.
#frase.strip() retira os espaços do inicio e final. Os do meio se mantem.
#frase.rstrip() retira os espaços da direita (isso só de colocar o R, e pode ser usado em outros comandos)
#frase.lstrip() retira os espaços da esquerda apenas (L)

'''Divisão'''
#Trabalhando novamente com:
frase='Curso em Vídeo Python'
#frase.split() - estudar um pouco a mais. O split separa a frase com base nos espaços, mas pode ser reconfigurado
#o split gera uma lista com cada uma das palavras.
#'-'.join(frase) Nesse caso, eu juntei as palavras da lista anterior, com o separador entre aspas, no caso -
#Curso-em-Vídeo-Python

