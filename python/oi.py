import pygame
import random
from pygame.locals import *


pygame.init()
pygame.font.init()

width = 600
heigth = 600

tela = pygame.display.set_mode((width,heigth))
pygame.display.set_caption('Jogo')

tempo = pygame.time.Clock()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

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
    
tela.fill((0,0,0))
i = 0

p = []
p_corpo = pygame.Surface((100,100))

jogo = []


    

limite = 0
tamanho = 50

while len(jogo) - 1 <= tamanho:
    jogo.append([])

while len(jogo[0]) < tamanho:
    i = len(jogo) - 1
    print(i)
    while i <= tamanho:
        while len(jogo[i]) <= tamanho:
            jogo[i].append(random.randint(0,2))
        i-= 1        
    

while True:
    tempo.tick(30)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
                
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                limite += 1

    tile = 0
    for tiles in jogo:
        n = 0
        for num in tiles:
            p_corpo = pygame.Surface((tamanho,tamanho))
            if num == 1:
                p_corpo.fill(BLUE)
            elif num == 2:
                p_corpo.fill(RED)
            tela.blit(p_corpo,(n*tamanho,tile * tamanho))
            n +=1    
        tile += 1
    
    i = 0
    while i <= width/tamanho:
        pygame.draw.line(tela, WHITE, [0,i * tamanho],[600, i * tamanho], 1)
        pygame.draw.line(tela, WHITE, [i * tamanho, 0], [i * tamanho, 600])
        i += 1
    
                    
    escrever('oi',WHITE,1)
    pygame.display.update()
