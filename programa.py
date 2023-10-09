import pygame
from juego import *
from menu import *
from play import *

class Programa:
    def __init__(self):
        # ventana
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Mujeres en la ciencia")
        self.running = True

        # interfaz mostrada en ventana
        self.interfaz = Juego(self)

        # nose
        self.clock = pygame.time.Clock()

    def ejecutar(self):
        while self.running:
            #eventos
            self.capturar_eventos()
            #actualizar
            self.interfaz.update()
            #dibujar
            self.interfaz.draw()
            self.screen.blit(self.interfaz,(0,0))

            pygame.display.flip()
            self.clock.tick(60)

    def capturar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.interfaz.manejar_evento(event)
    def notify(self, str):
        if str == "menu":
            print("modo menu")
            self.interfaz = Menu(self)
        elif str == "juego":
            print("modo juego")
            self.interfaz = Juego(self)
        elif str == "play":
            self.interfaz = Play(self)
        elif str == "options":
            self.interfaz = Juego(self)
        elif str == "exit":
            self.running = False