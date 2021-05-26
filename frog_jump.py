import pygame

logo = pygame.image.load("icons/pepe.png")
background = pygame.image.load("icons/background.jpg") 
(width, height) = (500, 600)

game = pygame.display.set_mode((width, height))
pygame.display.set_icon(logo)
pygame.display.set_caption("Frog jump!")

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            
    game.blit(background, (0,0))
    pygame.display.update()
