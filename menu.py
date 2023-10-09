from interfaz import *
from escenario import *

class Menu(Interfaz):
    def __init__(self, mediator):
        super().__init__(mediator)
        self.pausa = False
        self.scene = Escenario()
        #self.hud
        self.clock = pygame.time.Clock()

    def manejar_evento(self, event):
        if not self.pausa:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.mediator.notify("juego")
                    #self.jugador.accionar()
                    print("Espacio presionado")
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #self.hud.accionar()
                    print("Espacio presionado")
        
    def update(self):
        if not self.pausa:
            self.scene.update()
        #self.hud.update()

    def draw(self):
        self.scene.draw()
        self.blit(self.scene, (0, 0))