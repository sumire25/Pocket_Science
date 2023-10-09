import pygame

class Interfaz(pygame.Surface):
    def __init__(self, mediator):
        super().__init__((1280,720))
        self.mediator = mediator
    def manejar_evento(self, event):
        pass
    def update(self):
        pass
    def draw(self):
        pass