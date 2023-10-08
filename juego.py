from interfaz import *
from jugador import *

class Juego(Interfaz):
    def __init__(self):
        self.mapa = pygame.image.load("sprites/fondo.jpg").convert()
        self.jugador = Jugador(100, 100)
        self.entidades = pygame.sprite.Group(self.jugador)
        #self.hud
        self.clock = pygame.time.Clock()

    def manejar_evento(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #self.jugador.accionar()
                print("Espacio presionado")
        
    def update(self):
        self.entidades.update()

    def draw(self, screen):
        screen.blit(self.mapa, (0, 0))
        self.entidades.draw(screen)
        pygame.display.flip()