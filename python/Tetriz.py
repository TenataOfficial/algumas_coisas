import pygame
import random
from pygame.locals import *


pygame.init()
pygame.font.init()

tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Jogo')

tempo = pygame.time.Clock()

def escrever(texto,color,local):
    minha_fonte = pygame.font.SysFont('Comic Sans MS', 30)
    texto_surface = minha_fonte.render(texto, False, color)
    if local == 0:
        local = [300,300]
    if local == 1:
        local = [450,50]
    else:
        local = [60,450]
    tela.blit(texto_surface,local)
    
def cor(c):
    if c == 'branco':
        c = (255,255,255)
    if c == 'azul':
        c = (0,0,255)
    if c == 'verde':
        c = (0,255,0)
    if c == 'vermelho':
        c = (255,0,0)
    return c

tela.fill((0,0,0))
escrever('oi',cor('branco'),0)
pygame.display.update()
