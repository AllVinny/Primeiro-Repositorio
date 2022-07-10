#Faça um programa que leia um ano qualquer e mostre se ele é bissesxto.

#Regra: Divide por 4, se não sobrar resto, divide por 100. Se sobrar ele é bissexto

#print('Quer saber se um ano é bissexto? Vou dizer pra vc! ')
#ano = int(input('Qual o ano? '))

#Ao inves de dar a entrada primeiro e rodar o código, podemos criar a função e depois dar a entrada, e
#rodar a função.

print('Quer saber se um ano é bissexto? Vou dizer pra vc! ')
ano = int(input('Qual o ano? '))

def is_leap_year(year): #Sendo def = função, LeapYear o nome da função, e depois o parametro
    if (year%4) == 0:
        if (year%100) == 0:
            if (year%400) == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False

#Depois colocamos a entrada (igual antes)




print('-----FIM-----')



