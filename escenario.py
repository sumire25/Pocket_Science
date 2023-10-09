from jugador import *

class Escenario(pygame.Surface):
    def __init__(self):
        super().__init__((1280, 720))
        self.mapa = pygame.image.load("sprites/fondo.jpg").convert()
        self.jugador = Jugador(100, 100)

        self.entidades = pygame.sprite.Group(self.jugador)
        
    def update(self):
        self.entidades.update()

    def draw(self):
        self.blit(self.mapa, (0, 0))
        self.entidades.draw(self)