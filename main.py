import pygame

#initializations
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Task Manager')
font = pygame.font.SysFont('Corbel', 36)
width = screen.get_width()
height = screen.get_height()
mouse = pygame.mouse.get_pos()

#Main program loops
while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
             if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
                pygame.quit()