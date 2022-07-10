#Faça um programa em python que abra e reproduza o audio de um arquivo MP3

#Dica: Usando módulos. QUALQUER UM.

#Na pesquisa, encontrei o pacote pygame

import pygame
pygame.mixer.init() #comando para iniciar o pygame
pygame.mixer.music.load('D021.mp3') #controlando o mixer.
pygame.mixer.music.play() #iniciando o mixer
input() #esse comando foi uma sugestão do chat para fazer funcionar.
pygame.event.wait()
