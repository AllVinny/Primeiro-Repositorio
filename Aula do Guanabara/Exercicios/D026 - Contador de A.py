#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

v1 = input('Insira sua frase: ').lower().strip()
a1 = v1.count('a') #Quantas vezes aparece a letra A.
fa = v1.find('a')
la = v1.rfind('a')
print(f'A frase tem {a1} letras A') #Aqui mostra quantas Letras A foram achadas na frase
print(f'A primeira letra A aparece na posição {fa+1}') #Acha a primeira letra A. Precisa trabalhar o find+1 pra compensar o zero.
print(f'A última letra A aparece na posição {la+1} ')

