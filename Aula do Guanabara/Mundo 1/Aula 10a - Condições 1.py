'''Estruturas Condicionais Simples e compostas (Aula 1 apenas simples) + Condições simplificadas.

Até agora vimos programas que seguem estruturas sequenciais (De cima pra baixo, da esquerda pra direita). Quando usamos
condições, a parte 'inutil' do código nem é lida.

Estruturas condicionais trabalham com possibilidades. Igual um carro que tem varios caminhos a seguir pra chegar em um
mesmo lugar.

Condições = SE / IF

Condições simples: If
Condições Compostas: if/else

Se o carro for pra esquerda
se carro.esquerda()
    Bloco verde (verdadeiro)

Se não
    bloco vermelho (Falso)

Em comando vira

if carro.esquerda():
    bloco True

else:
    bloco False

Exemplo do carro:
    tempo = int(input('Quantos anos tem o seu carro? '))
    if tempo <=3:
        print('Seu carro é novo') #Identação é PRIMORDIAL EM PHYTON IF.
    else:
        print('Seu carro ja é velho')
    print('---FIM---')

Da pra simplificar um pouco:
    tempo = int(input('Quantos anos tem o seu carro? '))
    print('Carro novo' if tempo <=3 else 'carro velho') #todo o comando está dentro do if.
    print('---FIM---')






'''
