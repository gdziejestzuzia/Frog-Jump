#!/usr/bin/python

import pygame, sys
from pygame.locals import *
import random

logo = pygame.image.load("icons/pepe.png")
pla = pygame.image.load("icons/simple_plat.png")
frog = pygame.image.load("icons/frog.png")
background = pygame.image.load("icons/background.png")
go_background = pygame.image.load("icons/go.png")

(width, height) = (500, 600)

class Plat:
    """
    class to represent platform
    Attributes
    ----------
    x : float
        first coordinate of the random position
    y : folat
        the second coordinate of the random position
    """
    def __init__(self, x, y):
        """
        Constructs all the necessary attributes for the platform object
         Parameters
        ----------
         x : float
        first coordinate of the random position
         y : folat
        the second coordinate of the random position
        """
        self.x = x
        self.y = y

SCORE = 0
#main
pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(logo)
pygame.display.set_caption("Frog jump!")

#text size
font_small = pygame.font.SysFont(None, 30)
font_big = pygame.font.SysFont(None, 80)
font_large = pygame.font.SysFont(None, 100)

#sounds
jump = pygame.mixer.Sound("sounds/jump.wav")
frogsound = pygame.mixer.Sound("sounds/frogsound.mp3")
gameover = pygame.mixer.Sound("sounds/game_over.wav")
hurt = pygame.mixer.Sound("sounds/hurt.wav")

def make_text(text, font, color, surface, x, y):
    """
    function that creates text with a given font, color and position

     @param text: (str) the text you want to display on the screen

     @param font: the type and size of the font(large, big, small)

     @param color: rgb text color

     @param surface: the surface where the text will be displayed

     @param x,y: (int): coordinates of the text position

    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def get_highscore(score):
    """
    the function reads the highest result or, if it has been beaten, changes its value
    """
    new_score = score
    with open("highscore.txt", "r") as f:
        stored_val = f.read()
        high_score = int(stored_val) if stored_val else 0

    with open("highscore.txt", "w") as f:
        if new_score > int(high_score):
            f.write(str(new_score))
            return new_score
        else:
            return high_score



def menu():
    """
    the main page of the game with all the buttons you need
    """
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
    """
the whole mechanism of the game
    
    """
    x = 100
    y = 100
    dy = 0.0
    h = 200
    
    life = 3
    running = True
    while running:
        clock.tick(90)
        screen.blit(background, (0,0))

        for platform in platforms:
            screen.blit(pla, (platform.x, platform.y))

        #getting score
        if y < h:
            y = h
            for platform in platforms:
                platform.y = platform.y - dy
                if platform.y > height:
                    platform.y = 0
                    platform.x = random.randrange(0, width)
                    jump.play()
                    global SCORE
                    SCORE +=1
                    get_highscore(SCORE)
        make_text('Score: ' + str(SCORE), font_small, (128,128,0), screen, 10, 10)
        make_text('Back to menu: press esc', font_small, (34,139,34), screen, 10, 570)
        
        
        #frog
        screen.blit(frog, (x,y))
        dy += 0.2
        y += dy

        #lose life
        if y > height:
            hurt.play()
            life = life - 1
            dy = -10

        if life == 0:
            gameover.play()
            game_over()

        make_text('Lifes: ' + str(life), font_small, (255, 0, 0), screen, 10, 30)
        if x > width:
            x = 0
        if x < 0:
            x = width
        #right/left move
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 4
        if keys[pygame.K_RIGHT]:
            x += 4

        #jump
        for plat in platforms: 
            if (x + 50 >plat.x) and (x+20 < plat.x + 68) and (y +70 > plat.y) and (y +70 < plat.y + 14) and dy > 0:
                dy = - 10
        #exit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()

def author():
    """
    a short text about the author
    
    """
    running = True
    while running:
        screen.blit(background, (0,0))
        
        make_text('About author', font_big, (34,139,34), screen, 70, 50)
        make_text('Hello! My name is Zuzia and I am studying  ', font_small, (34,139,34), screen, 10, 200)
        make_text('Applied Mathematics  at the Wrocław', font_small, (34,139,34), screen, 10, 230)
        make_text('University of Technology. This game is my', font_small, (34,139,34), screen, 10, 260)
        make_text('project for my programming course.', font_small, (34,139,34), screen, 10, 290)
        make_text('I wish you a nice game.', font_small, (34,139,34), screen, 10, 320)
        make_text('Back to menu: press esc', font_small, (34,139,34), screen, 10, 570)

        #exit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
 
def game_rules():
    """
    short game rules
    
    """
    running = True
    while running:
        screen.blit(background, (0,0))
        make_text('Game rules', font_big, (34,139,34), screen, 70, 50)
        make_text('The rules are very simple. Press left / right', font_small, (34,139,34), screen, 10, 200)
        make_text('keys to move and jump as high as possible.', font_small, (34,139,34), screen, 10, 230)
        make_text('The higher you jump, the more points you get.', font_small, (34,139,34), screen, 10, 260)
        make_text('You have three lives, you will lose one ', font_small, (34,139,34), screen, 10, 290)
        make_text('if you fall. That’s all, have fan!', font_small, (34,139,34), screen, 10, 320)
        make_text('Back to menu: press esc', font_small, (34,139,34), screen, 10, 570)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()

def game_over():
    """
    the function displays the screen ending the game
    
    """
    
    running = True
    while running:
        screen.blit(go_background, (0,0))
        #make_text('Your score: ' + str(score), font_small, (255, 255, 255), screen, 390, 20)
        #make_text('Best score: ' + str(get_highscore(f.read())), font_small, (255, 255, 255), screen, 390, 20)
        make_text('Your score: ' + str(SCORE), font_small, (34,139,34), screen, 150, 300)
        make_text('play again: press space', font_small, (34,139,34), screen, 20, 10)
        make_text('Back to menu: press esc', font_small, (34,139,34), screen, 10, 570)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu()
                if event.key == K_SPACE:
                    game()
        
        pygame.display.update()

def end():
    """
    the function closes the program
    
    """
    pygame.quit()
    sys.exit()

menu()