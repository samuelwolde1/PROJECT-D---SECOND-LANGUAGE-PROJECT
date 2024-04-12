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
    while True:
        screen.fill('#FFFFFF')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            pygame.display.update()
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
        ls_rect = ls_text.get_rect(center = (100, 250))
        bs_text = getText(75).render("BS", True, "#eb4034")
        bs_rect = bs_text.get_rect(center = (250, 250))
        bubu_text = getText(75).render("bubu", True, "#26ff00")
        bubu_rect = bs_text.get_rect(center = (400, 250))
        screen.blit(bubu_text, bubu_rect)
        screen.blit(bs_text, bs_rect)
        screen.blit(ls_text, ls_rect)
        screen.blit(menu_text, menu_rect)
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
            elif ls_rect.collidepoint(menu_mouse_pos):
                linearSearch()
            elif bs_rect.collidepoint(menu_mouse_pos):
                binarySearch()
            elif bubu_rect.collidepoint(menu_mouse_pos):
                bubleSort()
                
        pygame.display.update() 
main_menu()
    