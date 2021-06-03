import pygame, sys
from pygame.locals import *


logo = pygame.image.load("icons/pepe.png")
background = pygame.image.load("icons/background.jpg") #zmienić tło na jakieś lepsze
(width, height) = (500, 600)


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(logo)
pygame.display.set_caption("Frog jump!")

font_small = pygame.font.SysFont(None, 30)
font_big = pygame.font.SysFont(None, 80)

def make_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def menu():
    while True:
        screen.blit(background, (0,0))
        make_text('main menu', font_big, (0, 128, 0), screen, 100, 150)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(150, 220, 200, 50)
        button_2 = pygame.Rect(150, 290, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (0, 128, 0), button_1)
        pygame.draw.rect(screen, (34,139,34), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
 
def game():
    running = True
    while running:
        screen.fill((0,128,0))
        
        make_text('game', font_small, (255, 255, 255), screen, 220, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
 
def options():
    running = True
    while running:
        screen.fill((0,128,0))
 
        make_text('options', font_small, (0, 255, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()

"""run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            
    screen.blit(background, (0,0))
    pygame.display.update()"""

menu()