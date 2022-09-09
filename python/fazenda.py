import pygame
from pygame.locals import *
import random
import time

pygame.init()
width = 600
tela = pygame.display.set_mode((width,600))
pygame.display.set_caption('FAZENDA')
tamanho = 100
clock = pygame.time.Clock()

snake = [[10,10]]
snake_color = pygame.Surface((tamanho,tamanho))
snake_color.fill((0,255,0))
x = 0
y = 0
while True:
    
    clock.tick(30)
    tela.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                x -=tamanho
            elif event.key == K_d:
                x += tamanho
            elif event.key == K_w:
               y -= tamanho
            elif event.key == K_s:
                y+= tamanho
                
        snake[0] = [x,y]
        
        #print(snake[0])
    for ix in snake:
        tela.blit(snake_color,(ix[0],ix[1]))
    
    while snake[0][1] < width/tamanho * 10:
        print('passou')
        y = y + tamanho
    
    i = 0
    while i <= width/tamanho:
        pygame.draw.line(tela, (255,255,255), [0,i * tamanho],[600, i * tamanho], 1)
        pygame.draw.line(tela, (255,255,255), [i * tamanho, 0], [i * tamanho, 600])
        i += 1
    
    pygame.display.update()
