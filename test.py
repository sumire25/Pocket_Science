import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("jugador/perfil_2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = 37
        self.height = 44
        self.velocidad = 5  # Ajusta la velocidad según tus necesidades

    def update(self):
        # Captura los eventos de teclado
        keys = pygame.key.get_pressed()

        # Actualiza la posición del jugador en función de las teclas presionadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidad

# Ejemplo de uso:
pygame.init()
screen = pygame.display.set_mode((800, 600))
jugador = Jugador(100, 100)
jugadores = pygame.sprite.Group(jugador)  # Grupo de jugadores
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    jugadores.update()  # Llama al método update de los jugadores

    screen.fill((255, 255, 255))
    jugadores.draw(screen)  # Dibuja el jugador en la pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
