import pygame, sys
from pygame.locals import *


pygame.init()


screen = pygame.display.set_mode((1280, 640))
screen.fill((255, 255, 255))




Forma = "Quadrado"



while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
        if evento.type == MOUSEBUTTONDOWN:
            x, y = evento.pos
            if Forma == "Quadrado":
                 pygame.draw.rect(screen, (255, 0, 0), Rect((x, y), (30, 30)))
            if Forma == "Retângulo":
                    pygame.draw.rect(screen, (0, 255, 0), Rect((x, y), (80, 30)))
            if Forma == "Circulo":
                 pygame.draw.circle(screen, (0, 0, 255), (x, y), 30)
                
    
    keys = pygame.key.get_pressed()
    
    if keys[K_r]:
        Forma = "Retângulo"
    if keys[K_q]:
        Forma = "Quadrado"
    if keys[K_c]:
        Forma = "Circulo"
    if keys[K_l]:
        screen.fill((255, 255, 255))

    
    pygame.display.update()