import pygame
import sys
ANCHO = 640
ALTO = 480

pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Pocket Science')
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()