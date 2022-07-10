# Faça um programa que leia um ano qualquer e mostre se ele é bissesxto.

# Regra: Divide por 4, se não sobrar resto, divide por 100. Se sobrar ele é bissexto

#o python consegue saber o ano que está no seu pc, com a biblioteca datetime, comando date. Não está funcionando o import
#no note, por isso não consegui testar.
#Poderiamos colocar pra inserir 0 no ano a analisar, e colocar as linhas comentadas. (12 e 13).

print('Quer saber se um ano é bissexto? Vou dizer pra vc! ')
ano = int(input('Qual o ano? '))

'''if ano == 0
    ano = date.today().year'''

if (ano % 4) == 0:
    if (ano % 100) == 0:
        if (ano % 400) == 0:
            print('true')
        else:
            print('false')
    else:
        print('true')

else:
    print(f'O ano que você inseriu não é bissexto!')

print('-----FIM-----')
