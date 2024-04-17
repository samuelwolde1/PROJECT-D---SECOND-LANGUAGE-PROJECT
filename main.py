# import pygame

# #initializations
# size = (800, 600)
# screen = pygame.display.set_mode(size)
# pygame.font.init()
# pygame.display.set_caption("Main Menu")
# def getText(size):
#     return pygame.font.SysFont('Corbel', size)
# background = pygame.image.load("images/Background.png")

# def linearSearch():
#     while True:
#         screen.fill('#FFFFFF')
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             pygame.display.update()
# def binarySearch():
#     pass
# def bubleSort():
#     pass
# def insertionSort():
#     pass
# def selectionSort():
#     pass
# def main_menu():
#     while True:
#         screen.blit(background, (0,0))
#         menu_mouse_pos = pygame.mouse.get_pos()
#         menu_text = getText(100).render("Main Menu", True, "#a1dbe6")
#         menu_rect = menu_text.get_rect(center = (400, 100))
#         linear_search_text = getText(75).render("LS", True, "#ffffff")
#         linear_search_rect = linear_search_text.get_rect(center = (100, 250))
#         binary_search_text = getText(75).render("BS", True, "#eb4034")
#         binary_search_rect = binary_search_text.get_rect(center = (250, 250))
#         buble_sort_text = getText(75).render("bubu", True, "#26ff00")
#         buble_sort_rect = binary_search_text.get_rect(center = (400, 250))
#         screen.blit(buble_sort_text, buble_sort_rect)
#         screen.blit(binary_search_text, binary_search_rect)
#         screen.blit(linear_search_text, linear_search_rect)
#         screen.blit(menu_text, menu_rect)
#         for event in pygame.event.get(): # User did something
#             if event.type == pygame.QUIT: # If user clicked close
#                 pygame.quit()
#             elif linear_search_rect.collidepoint(menu_mouse_pos):
#                 linearSearch()
#             elif binary_search_rect.collidepoint(menu_mouse_pos):
#                 binarySearch()
#             elif buble_sort_rect.collidepoint(menu_mouse_pos):
#                 bubleSort()
                
#         pygame.display.update() 
# main_menu()
    

import hashlib

def signup():
    email = input('Enter email address:')
    password = input('Enter password')
    confirm_password = input('Confirm password')
    if confirm_password == password:
        enc = confirm_password.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open('credentials.txt', 'w') as file:
            file.write(email + '\n')
            file.write(hash1)
            file.close
            print('You registsered')
    else:
        print('Password is not same as above \n')

def login():
     email = input('Enter email:')
     pwd = input('Enter password:')
     auth = pwd.encode()
     auth_hash = hashlib.md5(auth).hexdigest()
     with open('credentials.txt', 'r') as f:
         stored_email, stored_pwd = f.read().split('\n')
     f.close()
     if email == stored_email and auth_hash == stored_pwd:
         print('Logged in Successfully!')
     else:
         print('Login failed! \n')

while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        signup()
    elif choice == 2:
        login()
    elif choice == 3:
        break
    else:
        print("Wrong Choice!")
