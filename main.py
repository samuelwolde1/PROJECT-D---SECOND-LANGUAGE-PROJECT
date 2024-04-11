import pygame

#initializations
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.font.init()
pygame.display.set_caption("Main Menu")
def getText(size):
    return pygame.font.SysFont('Corbel', size)
background = pygame.image.load("images/Background.png")

def linearSearch():
    pass
def binarySearch():
    pass
def bubleSort():
    pass
def insertionSort():
    pass
def selectionSort():
    pass
def main_menu():
    while True:
        screen.blit(background, (0,0))
        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = getText(100).render("Main Menu", True, "#a1dbe6")
        menu_rect = menu_text.get_rect(center = (400, 100))
        ls_text = getText(75).render("LS", True, "#ffffff")
        ls_rect = menu_text.get_rect(center = (300, 300))
        screen.blit(ls_text, ls_rect)
        screen.blit(menu_text, menu_rect)
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
            elif menu_mouse_pos in range(ls_rect.left, ls_rect.right):
                print('yes')
        pygame.display.update() 
main_menu()
    