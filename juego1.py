import pygame
import sys
from boton import Button  # Assuming 'Button' is a custom class from 'boton' module

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN = pygame.display.set_mode((1280, 650))
pygame.display.set_caption("Mujeres en la ciencia")
rosa = (255, 192, 203)
verde = (0, 157, 113)

# Load images
BG = pygame.image.load("D:/python/archi/imagenes/Fondo_1.1.png")
panta1 = pygame.image.load("D:/python/archi/imagenes/fondo3.png")

# Function to get fonts
def get_font(size):
    return pygame.font.Font("D:/python/archi/fuente/JUA.ttf", size)

class Play:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 620))
        self.clock = pygame.time.Clock()
        self.running = True
        self.astro = astro.draw(self)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    #def astronomia(self):
        

    def update(self):
        pass 

    def draw(self):
        play_mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(panta1, (0, 0))

        play_text = get_font(50).render(".", True, (255, 255, 255))
        play_rect = play_text.get_rect(center=(1280, 620))
        self.screen.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(1220, 600),
                            text_input = "regresar", font=get_font(20), base_color=(255, 255, 255), hovering_color=(0, 255, 0))
        play_back.changeColor(play_mouse_pos)
        play_back.update(self.screen)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.astro
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(play_mouse_pos):
                    self.running = False
        
        play_astro = Button(image=None, pos = (480, 380),
                            text_input="ASTROLOGIA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        play_astro.changeColor(play_mouse_pos)
        play_astro.update(self.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main_menu()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_astro.checkForInput(play_mouse_pos):
                    self.running = False
                    
        play_bio = Button(image=None, pos = (800, 400),
                            text_input="BIOLOGIA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        play_bio.changeColor(play_mouse_pos)
        play_bio.update(self.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main_menu()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_bio.checkForInput(play_mouse_pos):
                    self.running = False
                    
        play_fis = Button(image=None, pos = (1080, 300),
                            text_input="FISICA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        play_fis.changeColor(play_mouse_pos)
        play_fis.update(self.screen)
 
        play_quim = Button(image=None, pos = (830, 110),
                            text_input="QUIMICA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        play_quim.changeColor(play_mouse_pos)
        play_quim.update(self.screen)
        
        play_geo = Button(image=None, pos = (560, 80),
                            text_input="GEOLOGIA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        play_geo.changeColor(play_mouse_pos)
        play_geo.update(self.screen)
        
        play_eco = Button(image=None, pos = (280, 120),
                            text_input="ECOLOGIA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        play_eco.changeColor(play_mouse_pos)
        play_eco.update(self.screen)
       
        

    def main_menu(self):
        pass  # Implement the functionality to return to the main menu

class astro:
    
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 620))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    #def astronomia(self):

    def update(self):
        pass 

    def draw(self):
        astro_mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(panta1, (0, 0))

        astro_back = Button(image=None, pos=(1220, 600),
                            text_input = "regresar", font=get_font(20), base_color=(255, 255, 255), hovering_color=(0, 255, 0))
        astro_back.changeColor(astro_mouse_pos)
        astro_back.update(self.screen)
        

class OptionsScreen:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.rosa = (255, 0, 127)

    def run(self):
        while self.running:
            self.update()

    def update(self):
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        self.screen.fill((255, 255, 255))

        OPTIONS_TEXT = self.get_font(40).render("opciones de la pantalla.", True, self.rosa)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=self.get_font(75), base_color=self.rosa, hovering_color=(0, 255, 0))

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(self.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    self.running = False

        pygame.display.update()

    def get_font(self, size):
        return pygame.font.Font("D:/python/archi/fuente/JUA.ttf", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(90).render("Mujeres al Mando", True, verde)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 185))

        PLAY_BUTTON = Button(image=pygame.image.load("D:/python/archi/imagenes/iniciosinletra.png"), pos=(640, 350),
                             text_input="Inicio", font=get_font(45), base_color=rosa, hovering_color=(255, 255, 255))
        OPTIONS_BUTTON = Button(image=pygame.image.load("D:/python/archi/imagenes/opcionessinletra.png"), pos=(640, 450),
                                text_input="Opciones", font=get_font(35), base_color=rosa, hovering_color=(255, 255, 255))
        QUIT_BUTTON = Button(image=pygame.image.load("D:/python/archi/imagenes/cerrarsinletra.png"), pos=(640, 550),
                             text_input="Cerrar", font=get_font(45), base_color=rosa, hovering_color=(255, 255, 255))

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play = Play()
                    play.run()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options = OptionsScreen(SCREEN)
                    options.run()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()

        