#!/usr/bin/python

import pygame, sys
from pygame.locals import *
import random
import os



logo = pygame.image.load("icons/pepe.png")
pla = pygame.image.load("icons/simple_plat.png")
frog = pygame.image.load("icons/frog.png")
background = pygame.image.load("icons/background.png")
go_background = pygame.image.load("icons/go.png")

(width, height) = (500, 600)


class Plat:
    def __init__(self, x, y):
        self.x = x
        self.y = y


pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(logo)
pygame.display.set_caption("Frog jump!")


font_small = pygame.font.SysFont(None, 30)
font_big = pygame.font.SysFont(None, 80)
font_large = pygame.font.SysFont(None, 100)

jump = pygame.mixer.Sound("sounds/jump.wav")
frogsound = pygame.mixer.Sound("sounds/frogsound.mp3")
gameover = pygame.mixer.Sound("sounds/game_over.wav")
hurt = pygame.mixer.Sound("sounds/hurt.wav")

def make_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def highscore():
    with open('./highscore.txt',"w") as f:
        try:
            high_score = int(f.read()) 
        except: 
            high_score = 0  

def menu():
    click = False
    while True:

        screen.blit(background, (0,0))
        make_text('Frog jump!', font_large, (50,205,50), screen, 70, 50)
        make_text('main menu', font_big, (34,139,34), screen, 100, 190)
        make_text('play', font_small, (34,139,34), screen, 55, 275)
        make_text('game rules', font_small, (34,139,34), screen, 25, 345)
        make_text('author', font_small, (34,139,34), screen, 40, 415)
        make_text('exit', font_small, (34,139,34), screen, 375, 525)
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(150, 260, 200, 50) #game 
        button_2 = pygame.Rect(150, 330, 200, 50) #rules
        button_3 = pygame.Rect(150, 400, 200, 50) #author
        exit_button = pygame.Rect(350, 550, 100, 30) #exit
        
           
        if button_1.collidepoint((mx, my)):
            if click:
                frogsound.play()
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                frogsound.play()
                game_rules()
        if button_3.collidepoint((mx, my)):
            if click:
                frogsound.play()
                author()
        if exit_button.collidepoint((mx, my)):
            if click:
                frogsound.play()
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
    score = 0
    life = 3
    running = True
    while running:
        clock.tick(90)
        screen.blit(background, (0,0))

        for platform in platforms:
            screen.blit(pla, (platform.x, platform.y))

        if y < h:
            y = h
            for platform in platforms:
                platform.y = platform.y - dy
                if platform.y > height:
                    platform.y = 0
                    platform.x = random.randrange(0, width)
                    jump.play()
                    score +=1
        make_text('Score: ' + str(score), font_small, (128,128,0), screen, 20, 25)

        screen.blit(frog, (x,y))

        dy += 0.2
        y += dy

        
        if y > height:
            hurt.play()
            life = life - 1
            dy = -10

        if life == 0:
            gameover.play()
            game_over()

        make_text('Lifes: ' + str(life), font_small, (255, 0, 0), screen, 20, 50)
        if x > width:
            x = 0
        if x < 0:
            x = width

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 4
        if keys[pygame.K_RIGHT]:
            x += 4

        for plat in platforms: 
            if (x + 50 >plat.x) and (x+20 < plat.x + 68) and (y +70 > plat.y) and (y +70 < plat.y + 14) and dy > 0:
                dy = - 10
        
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
        screen.blit(background, (0,0))
        
        make_text('about author', font_small, (144, 238, 144), screen, 200, 20)
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
        screen.blit(background, (0,0))
        make_text('game rules', font_small, (0, 255, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()

def game_over():
    
    running = True
    while running:
        screen.blit(go_background, (0,0))
        #make_text('Your score: ' + str(score), font_small, (255, 255, 255), screen, 390, 20)
        #make_text('Best score: ' + str(score), font_small, (255, 255, 255), screen, 390, 20)
        make_text('Your score: ', font_small, (34,139,34), screen, 20, 20)
        make_text('Back to menu: press Esc', font_small, (34,139,34), screen, 20, 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu()
        
        pygame.display.update()

def end():
    pygame.quit()
    sys.exit()

menu()