import pygame
import random
from pygame.locals import *


pygame.init()
pygame.font.init()

tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Jogo do Dinossauro')

dinossauro = [200,200]
dinossauro_pele = pygame.Surface((30,30))
dinossauro_pele.fill((255,255,255))
dinossauro_velocidade = 0

enimigo = [[500,570]]
enimigo_pele = pygame.Surface((30,30))
enimigo_pele.fill((255,0,0))

pausa = pygame.time.Clock()
velocidade = 5
pontos = 0
passou = True


def escrever(texto,cor,local):
    minha_fonte = pygame.font.SysFont('Comic Sans MS', 30)
    texto_surface = minha_fonte.render(texto, False, cor)
    tela.blit(texto_surface,local)

def main():
    global dinossauro_velocidade, velocidade, pontos, passou
    while True:
        pausa.tick(30)
        tela.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_SPACE and dinossauro[1] >= (600 - 30):
                    dinossauro_velocidade = -10
                    
        tela.blit(dinossauro_pele,dinossauro)
        
        for pos in enimigo:
            if pos[0] <= -20:
                x = 0
                i = 0
                if len(enimigo) <= 1:
                    x = random.randint(1,3)
                while i < x:
                    if i > 0:
                        enimigo.append([600 + (30*i) + 10 + (10 * i),570])
                        if len(enimigo)>= 3:
                            enimigo[len(enimigo) - 1][0] = enimigo[len(enimigo) - 1][0] - 5
                            print('passou')
                        
                    else:
                        enimigo.append([600,570])
                    i += 1
                enimigo.pop(0)
            else:
                enimigo[enimigo.index(pos)] = (pos[0] -1 * velocidade, pos[1])
                #print(str(enimigo))
            tela.blit(enimigo_pele,pos)
            
            if dinossauro[0] + 25 >= pos[0] and dinossauro[0] + 15 <= pos[0] + 30:
                if dinossauro[1] + 15 >= pos[1]:
                    escrever('Você Perdeu',(255,255,255), (100,200))
                    pygame.display.update()
                    return 0
            if dinossauro[0] - 120 == pos[0] and dinossauro[1] >= 560:
                pontos += 1
                    
        escrever('Seus pontos: ' + str(pontos), (255,255,255),(380,30))    
        if dinossauro[1] < (600 - 30) or dinossauro_velocidade < 0:
            dinossauro[1] += (1 * dinossauro_velocidade)
            dinossauro_velocidade += 0.5
        elif dinossauro[1] >= (600 - 30):
            dinossauro_velocidade = 0
        escrever(str(dinossauro),(255,255,255),(30,30))
        pygame.display.update()
        
main()
