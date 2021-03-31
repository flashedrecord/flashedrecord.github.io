# imports
import os
import time
import random
from msvcrt import getch
import getpass, sys
import pw
#
# password hider
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
            if key == 13:
                sys.stdout.write('\n')
                return pwd
            if key == 8:
                if len(pwd) > 0:
                    sys.stdout.write('\b' + ' ' + '\b')
                    sys.stdout.flush()
                    pwd = pwd[:-1]
            else:
                char = chr(key)
                sys.stdout.write('*')
                sys.stdout.flush()  
                pwd = pwd + char
#
# login
def login():
    while True:
        username = input ("Enter Username: ")
        password = pyssword(prompt='Password: ')

        if username == pw.admin and password == pw.admin_pw:
            time.sleep(1)
            print ("Login successful!")
            print("")
            logged_in_admin()

        elif username == pw.user1 and password == pw.user1_pw:
            time.sleep(1)
            print ("Login successful!")
            print("")
            logged_in_user1()

        elif username == pw.user2 and password == pw.user2_pw:
            time.sleep(1)
            print ("Login successful!")
            print("")
            logged_in_user2()

        else:
            print ("Password did not match!")
            print("Try again!")

        break
#
# logged in
def logged_in_admin():
    print ("Welcome!")
    print(f"You are logged in as {pw.admin}.")
    return admin_return()

class admin_return:
    def __init__(self):
        self.logged_in = True
        self.user = "admin"

if admin_return().user == "admin":
    ar = admin_return()

def logged_in_user1():
    print ("Welcome!")
    print(f"You are logged in as {pw.user1}.")
    return user1_return()

class user1_return:
    def __init__(self):
        self.logged_in = True
        self.user = "user1"

if user1_return().user == "user1":
    u1 = user1_return()

def logged_in_user2():
    print ("Welcome!")
    print(f"You are logged in as {pw.user2}.")
    return user2_return()

class user2_return:
    def __init__(self):
        self.logged_in = True
        self.user = "user2"

if user2_return().user == "user2":
    u2 = user1_return()

# start
login()
if ar.user == "admin":
    print("you are an admin")

if u1.user == "user1":
    print("you are a user")

if u2.user == "user2":
    print("you are another user")
