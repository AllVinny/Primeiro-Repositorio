#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pause de 1 segundo entre eles. Emoji de fogos estourando.

import emoji
from time import sleep


for contagem in range(11,1,-1):
    print(contagem-1)
    sleep(1)
print(emoji.emojize(':sparkler::fireworks: FELIZ ANO NOVO!!! :fireworks::sparkler:'))