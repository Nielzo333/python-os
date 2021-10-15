import os
from time import sleep

os.system('clear')
print('login')
print(

)

def login():
    os.system('clear')
    print('logged in successfully')
    system()

def logout():
    print('Wrong password')

def system():
    while True:
        system_name = username + '@python-os$ '
        command = str(input(system_name))
        if command == 'cd':
            sleep(0.2)
            print('error')
            sleep(0.5)
        elif command == 'exit':
            exit()
        else:
            os.system(command)

username = str(input('username : '))

if username == 'admin':
    login()
elif username == 'root':
    sleep(0.2)
    print('error')
    exit()
password = str(input('password : '))

if password == '123456789':
    login()
else:
    logout()
