import hashlib

def signup():
    username = input('Enter username: ')
    password = input('Enter password: ')
    confirm_password = input('Confirm password: ')
    if confirm_password == password:
        with open('credentials.txt', 'a+') as file:
            file.write(username + ',' + confirm_password + '\n')
            file.close
            print('You registsered')
    else:
        print('Password is not same as above \n')

def login():
     username = input('Enter username: ')
     password = input('Enter password: ')
     with open('credentials.txt', 'r') as file:
         stored_username, stored_password = file.read().split(',')
     file.close()
     if username == stored_username and password == stored_password:
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