import pygame
from juego import *

class Programa:
    def __init__(self):
        # ventana
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Mujeres en la ciencia")
        self.running = True

        # interfaz mostrada en ventana
        self.interfaz = Juego()

        # nose
        self.clock = pygame.time.Clock()

    def ejecutar(self):
        while self.running:
            #eventos
            self.capturar_eventos()
            #actualizar
            self.interfaz.update()
            #dibujar
            self.interfaz.draw(self.screen)

            self.clock.tick(60)

    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.interfaz.manejar_evento(event)