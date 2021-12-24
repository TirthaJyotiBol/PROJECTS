"""

Bruteforce Attack of Password Cracker 

pyautogui is being used for GUI input ----> pip install pyautogui

"""

import random
import pyautogui

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+abcdefghijklmnopqrstuvwxyz0123456789"
char_list = list(chars)

password = pyautogui.password("Enter Your Password")

guess_number = ""

while(guess_number != password):
    guess_number = random.choices(char_list, k=len(password))
    print("<********"+str(guess_number)+"*********>\n")
    if(guess_number == list(password)):
        print("Your password is "+"".join(guess_number))
        break
