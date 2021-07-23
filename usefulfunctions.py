import sys
import time
import os
from ascii_art import game_over
import rpg_variables

lives = rpg_variables.lives
health = rpg_variables.health

def clearScreen():  ##this function clears the console, works on windows mac and linux
    ##for windows
    if os.name=="nt":
        _ = os.system("cls")    
    ##for mac and linux
    else:
        _ = os.system("clear")

def typewriter_print(text, speed=0.03):##text must be a string. this function simply types out the text you input
    for chars in text:
        sys.stdout.write(chars)
        sys.stdout.flush()
        time.sleep(speed)


def typewriter_input(text,speed=0.03):##text must be a string. this function is the same as above except it also returns a user input
    for chars in text:
        sys.stdout.write(chars)
        sys.stdout.flush()
        time.sleep(speed)
    answer = input()
    return answer
    
p=1
def paragraph_counter(p):
	while p:
		time.sleep(1)
		p -= 1      

def next_page():
    input("\n\n\n\nPRESS ENTER TO CONTINUE ")
    clearScreen()

def new_life(func):
    global lives
    global health 
    typewriter_print('\n\nAs your consciousness fades, your last thoughts are of your four legged companion.\n\n\n', 0.03)
    paragraph_counter(int(p))
    typewriter_print('YOUR HEALTH HAS REACHED 0', 0.05)
    if lives > 0:
        answer = typewriter_input(f"\n\nBut it's not the end, you have {lives} continue/s remaining. CONTINUE? [1 == YES || 2 == NO] ",0.03 )
        if answer == "1":
            clearScreen()
            typewriter_print("It's not over. ",0.03)
            paragraph_counter(int(p))
            typewriter_print("It can't be! ",0.03)
            paragraph_counter(int(p))
            typewriter_print("With your dying breath you scream out to the universe!\n\n", 0.03)
            paragraph_counter(int(p))
            paragraph_counter(int(p))
            typewriter_print("The universe responds!\n\n",0.03) 
            typewriter_print("Suddenly, something envelops you just as everything goes dark.", 0.03)
            paragraph_counter(int(p))
            typewriter_print("\nYou wake up, dazed and confused...with no recollection of what happened yet something spurs you into action, \n\"It's time to get moving\", you think to yourself\n\n", 0.03)
            next_page()
            lives -= 1
            clearScreen()
            func()
        else:
            game_over()
    else:
        game_over() 