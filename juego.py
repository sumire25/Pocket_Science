import pygame
import sys
from personaje import *


pygame.init()


jugador = jugador(0,550)

pygame.display.set_caption("Mujeres en la ciencia")
        
# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(fondo, [0,0])
    #llamr personaje
    jugador.draw()
    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    
    # Mover al jugador
    
    if keys[pygame.K_LEFT] and jugador.x - jugador.velocidad > 0:
        jugador.x -= jugador.velocidad
    if keys[pygame.K_RIGHT] and jugador.x + jugador.velocidad < WIDTH - jugador.width:
        jugador.x += jugador.velocidad
    if keys[pygame.K_UP] and jugador.y - jugador.velocidad > 0:
        jugador.y -= jugador.velocidad
    if keys[pygame.K_DOWN] and jugador.y + jugador.velocidad < HEIGHT - jugador.height:
        jugador.y += jugador.velocidad
        
    pygame.display.update()
"""
    #limite
        if jugador.x < 0:
            jugador.x = 0
        if jugador.x - jugador.width > WIDTH:
            jugador.x = WIDTH - jugador.width
        if jugador.y < 0 :
            jugador.y = 0
        if jugador.y + jugador.height > HEIGHT:
            jugador.y = HEIGHT - jugador.height
            
"""
    
       
pygame.quit()
sys.exit()

