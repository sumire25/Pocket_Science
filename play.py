from interfaz import *
from boton import *

class Play(Interfaz):
    def __init__(self, mediator):
        super().__init__(mediator)
        self.play_mouse_pos = pygame.mouse.get_pos()

        self.play_text = get_font(50).render(".", True, (255, 255, 255))
        self.play_rect = self.play_text.get_rect(center=(1280, 620))

        self.play_back = Button(image=None, pos=(1220, 600),
                            text_input = "regresar", font=get_font(20), base_color=(255, 255, 255), hovering_color=(0, 255, 0))
        self.play_astro = Button(image=None, pos = (480, 380),
                            text_input="ASTRONOMIA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        self.play_bio = Button(image=None, pos = (800, 400),
                            text_input="BIOLOGIA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        self.play_fis = Button(image=None, pos = (1080, 300),
                            text_input="FISICA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        self.play_quim = Button(image=None, pos = (830, 110),
                            text_input="QUIMICA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        self.play_geo = Button(image=None, pos = (560, 80),
                            text_input="GEOLOGIA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))
        self.play_eco = Button(image=None, pos = (280, 120),
                            text_input="ECOLOGIA", font=get_font(40), base_color=(0,0,0), hovering_color=(0, 255, 0))

    def manejar_evento(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_back.checkForInput(self.play_mouse_pos):
                self.mediator.notify("menu")
            elif self.play_astro.checkForInput(self.play_mouse_pos):
                    self.mediator.notify("juego")
            elif self.play_bio.checkForInput(self.play_mouse_pos):
                pass



    def update(self):
        self.play_mouse_pos = pygame.mouse.get_pos()

    def draw(self):
        self.blit(panta1, (0, 0))
        self.blit(self.play_text, self.play_rect)

        self.play_back.changeColor(self.play_mouse_pos)
        self.play_back.update(self)
        
        self.play_astro.changeColor(self.play_mouse_pos)
        self.play_astro.update(self)
                    
        self.play_bio.changeColor(self.play_mouse_pos)
        self.play_bio.update(self)
     
        
        self.play_fis.changeColor(self.play_mouse_pos)
        self.play_fis.update(self)
 
        self.play_quim.changeColor(self.play_mouse_pos)
        self.play_quim.update(self)
        
        self.play_geo.changeColor(self.play_mouse_pos)
        self.play_geo.update(self)
        
        self.play_eco.changeColor(self.play_mouse_pos)
        self.play_eco.update(self)