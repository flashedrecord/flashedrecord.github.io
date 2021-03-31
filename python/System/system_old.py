import os
import time
import random
from msvcrt import getch
import getpass, sys

def pyssword(prompt='Password: '):
    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        pwd = ""        
        sys.stdout.write(prompt)
        sys.stdout.flush()        
        while True:
            key = ord(getch())
            if key == 13: #Return Key
                sys.stdout.write('\n')
                return pwd
            if key == 8: #Backspace key
                if len(pwd) > 0:
                    # Erases previous character.
                    sys.stdout.write('\b' + ' ' + '\b')                
                    sys.stdout.flush()
                    pwd = pwd[:-1]                    
            else:
                # Masks user input.
                char = chr(key)
                sys.stdout.write('*')
                sys.stdout.flush()                
                pwd = pwd + char

admin = "admin"
admin_pw = "verysecure123"

user1 = "berci"
user1_pw = "pass"

user2 = "joe"
user2_pw = "joemama"

def login():
    while True:
        username = input ("Enter Username: ")

        if username == "exit" or username == "cancel":
            print("Exiting...")
            time.sleep(1)
            break

        password = pyssword(prompt='Password: ')

        if username == admin and password == admin_pw:
            time.sleep(1)
            print ("Login successful!")
            logged_in_admin()

        elif username == user1 and password == user1_pw:
            time.sleep(1)
            print ("Login successful!")
            logged_in_user1()

        elif username == user2 and password == user2_pw:
            time.sleep(1)
            print ("Login successful!")
            logged_in_user2()

        else:
            print ("Password did not match!")

        break

class admin_return:
    def __init__(self):
        self.logged_in = True
        self.user = admin

def logged_in_admin():
    time.sleep(1)
    print ("Welcome!")
    print(f"You are logged in as {admin}.")
    return admin_return()

class user1_return:
    def __init__(self):
        self.logged_in = True
        self.user = user1

def logged_in_user1():
    time.sleep(1)
    print ("Welcome!")
    print(f"You are logged in as {user1}.")
    return user1_return()

class user2_return:
    def __init__(self):
        self.logged_in = True
        self.user = user2_return()

def logged_in_user2():
    time.sleep(1)
    print ("Welcome!")
    print(f"You are logged in as {user2}.")
    return

def rps():

    while True:
        my_answer = input("Choose: rock, paper or scissors: ")
        my_answer = my_answer.lower()

        if my_answer == "quit":
            break

        if my_answer != "rock" and my_answer != "paper"  and my_answer != "scissors":
            print("Choose a correct answer")
            continue

        computer_answer = random.choice(["rock", "paper", "scissors"])
        print(f"The computer chose: {computer_answer}")

        if computer_answer == my_answer:
            print("You tied!")
            continue

        elif my_answer == "paper" and computer_answer == "rock":
            print("You won!")
            break

        elif my_answer == "rock" and computer_answer == "scissors":
            print("You won!")
            break

        elif my_answer == "scissors" and computer_answer == "paper":
            print("You won!")
            break
        else:
            print("You lost. Try again!")
        break

def rps_loose():
    print("Rock Paper Scissors")
    user_answer = input("Choose: rock, paper or scissors! ")

    if user_answer == "rock":
        computer_answer = "paper"

    elif user_answer == "paper":
        computer_answer = "scissors"
    elif user_answer == "scissors":
        computer_answer = "rock"
    else:
        computer_answer = f"something that beats {user_answer}"


    print (f"You chose {user_answer}.")
    print (f"The computer chose {computer_answer}.")
    print ("You lost. Try again!")

login()
if logged_in_admin().logged_in == True or logged_in_user1().logged_in == True or logged_in_user2().logged_in == True:
    print("")
    print("What do you want to do")
    print("You can choose:")
    print("Rock paper scissors - type: rps")
    action = input("Choose one: ")
if action == "rps":
    if logged_in_user2().user == user2:
        rps_loose()
    else:
        rps()


