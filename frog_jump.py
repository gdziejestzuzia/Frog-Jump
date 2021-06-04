#!/usr/bin/python

import pygame, sys
from pygame.locals import *
import random


logo = pygame.image.load("icons/pepe.png")
pla = pygame.image.load("icons/simple_plat.png")
frog = pygame.image.load("icons/frog.png")
background = pygame.image.load("icons/background.jpg") #zmienić tło na jakieś lepsze
(width, height) = (500, 600)


class Plat:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(logo)
pygame.display.set_caption("Frog jump!")

font_small = pygame.font.SysFont(None, 30)
font_big = pygame.font.SysFont(None, 80)
font_large = pygame.font.SysFont(None, 120)

def make_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

    click = False

def menu():

    while True:

        screen.blit(background, (0,0))
        make_text('Frog jump!', font_large, (0, 255, 0), screen, 40, 50)
        make_text('main menu', font_big, (0, 128, 0), screen, 100, 150)
        make_text('play', font_small, (0, 0, 0), screen, 40, 240)
        make_text('game rules', font_small, (0, 0, 0), screen, 30, 310)
        make_text('author', font_small, (0, 0, 0), screen, 40, 380)
        make_text('exit', font_small, (0, 0, 0), screen, 375, 525)
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(150, 220, 200, 50) #game 
        button_2 = pygame.Rect(150, 290, 200, 50) #rules
        button_3 = pygame.Rect(150, 360, 200, 50) #author
        exit_button = pygame.Rect(350, 550, 100, 30) #exit
        
           
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                game_rules()
        if button_3.collidepoint((mx, my)):
            if click:
                author()
        if exit_button.collidepoint((mx, my)):
            if click:
                end()

        pygame.draw.rect(screen, (0, 128, 0), button_1)
        pygame.draw.rect(screen, (34,139,34), button_2)
        pygame.draw.rect(screen, (34,139,34), button_3)
        pygame.draw.rect(screen, (0, 128, 0), exit_button)

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

platforms = [Plat(random.randrange(0, width), random.randrange(0, height)) for i in range (15)]



def game():

    x = 100
    y = 100
    dy = 0.0
    h = 200
    running = True
    while running:
        screen.fill((0,0,128))
        screen.blit(pla,(0,0))
        for platform in platforms:
            screen.blit(pla, (platform.x, platform.y))
        
        dy += 0.2
        y += dy
        if y > height:
            dy = -10

        screen.blit(frog, (x,y))
        
        make_text('Frog jump!', font_big, (255, 255, 255), screen, 100, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()

def author():
    running = True
    while running:
        screen.fill((0,128,0))
        
        make_text('about author', font_small, (255, 255, 255), screen, 200, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
 
def game_rules():
    running = True
    while running:
        screen.fill((0,128,0))
 
        make_text('game rules', font_small, (0, 255, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()

def end():
    pygame.quit()
    sys.exit()

menu()