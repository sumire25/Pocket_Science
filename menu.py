from interfaz import *
from boton import *

class Menu(Interfaz):
    def __init__(self, mediator):
        super().__init__(mediator)
        self.MENU_TEXT = get_font(90).render("Scully Pocket", True, verde)
        self.MENU_RECT = self.MENU_TEXT.get_rect(center=(640, 185))
        self.PLAY_BUTTON = Button(image=pygame.image.load("sprites/iniciosinletra.png"), pos=(640, 350),
                             text_input="Inicio", font=get_font(45), base_color=rosa, hovering_color=(255, 255, 255))
        self.OPTIONS_BUTTON = Button(image=pygame.image.load("sprites/opcionessinletra.png"), pos=(640, 450),
                                text_input="Opciones", font=get_font(35), base_color=rosa, hovering_color=(255, 255, 255))
        self.QUIT_BUTTON = Button(image=pygame.image.load("sprites/cerrarsinletra.png"), pos=(640, 550),
                             text_input="Cerrar", font=get_font(45), base_color=rosa, hovering_color=(255, 255, 255))
        self.blit(BG, (0,0))
        self.blit(self.MENU_TEXT, self.MENU_RECT)
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        #self.hud

    def manejar_evento(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.PLAY_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                self.mediator.notify("play")
                ''''play = Play()
                play.run()'''
            if self.OPTIONS_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                self.mediator.notify("options")
                '''options = self.OptionsScreen(self)
                options.run()'''
            if self.QUIT_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                self.mediator.notify("exit")
                '''pygame.quit()
                sys.exit()'''

    def update(self):
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()

    def draw(self):
        self.blit(BG, (0,0))
        self.blit(self.MENU_TEXT, self.MENU_RECT)
        for button in [self.PLAY_BUTTON, self.OPTIONS_BUTTON, self.QUIT_BUTTON]:
            button.changeColor(self.MENU_MOUSE_POS)
            button.update(self)