import pygame
import os

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
jugador_d=pygame.image.load("jugador/perfil_1.png").convert_alpha()
fondo = pygame.image.load("sprites/fondo.jpg").convert_alpha()

#colores


#clase jugador
class jugador:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width = 37
        self.height = 44
        self.velocidad = 0.5
        self.image = pygame.image.load("jugador/perfil_2.png").convert_alpha()
    def draw(self):
        screen.blit(self.image, (self.x,self.y))


#clase planeta
#class planeta:
   # def __init__(self,x,y):
    #    self.x =x
     #   self.y=y
     #   self.width = 80
     #   self.heigt = 80
        
