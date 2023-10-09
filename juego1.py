import pygame, sys
from interfaz import *
from boton import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 620))
pygame.display.set_caption("Menu")

rosa =(255, 192, 203)
verde=(0, 157, 113)

BG = pygame.image.load("sprites/Fondo_1.1.png")

class Menu(Interfaz):
    def __init__(self):
        pass

def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("fuentes/Julee-Regular.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(50).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 280))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(60), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(40).render("This is the OPTIONS screen.", True, rosa)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color=rosa, hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(90).render("Mujeres al mando ", True,verde)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 185))

        PLAY_BUTTON = Button(image=pygame.image.load("sprites/iniciosinletra.png"), pos=(640, 350), 
                            text_input="inicio", font=get_font(45), base_color=rosa, hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("sprites/opcionessinletra.png"), pos=(640, 450), 
                            text_input="opciones", font=get_font(45), base_color=rosa, hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("sprites/cerrarsinletra.png"), pos=(640, 550), 
                            text_input="cerrar", font=get_font(35), base_color=rosa, hovering_color="White")

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
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
        