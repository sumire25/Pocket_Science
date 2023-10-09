import pygame

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
#jugador_d=pygame.image.load("jugador/perfil_1.png").convert_alpha()
#fondo = pygame.image.load("sprites/fondo.jpg").convert_alpha()

class Hud(pygame.sprite.Sprite):
  def __init__(self, text_list_5):
    super().__init__()
    temp_w = WIDTH-20
    temp_h = (HEIGHT/4)-20
    self.image = pygame.Surface((temp_w,temp_h))
    self.rect = self.image.get_rect()

    self.rect.width = WIDTH-20
    self.rect.height = (HEIGHT/4)-20
    self.image.fill((100,100,100))
    self.rect.center = (WIDTH/2, HEIGHT*7/8)

    # texto
    self.fuente = pygame.font.Font(None,48)
    self.texto = []
    for i in range (5):
      self.texto.append(self.fuente.render(text_list_5[i], True, (255, 255, 255)))
    #self.image_texto = self.image
    
  def draw(self):
    #self.image = self.texto
    screen.blit(self.image,self.rect)
    print("midbuttom: ", self.rect.midbottom)
    for i in range (5):
      screen.blit(self.texto[i],(self.rect.x + 10 , self.rect.y+10+30*i))



