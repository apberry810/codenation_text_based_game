import random
import time
import ship_hub
from rpg_variables import INCORRECT_A,ammo, p
from usefulfunctions import typewriter_input, typewriter_print, new_life, next_page, game_over, clearScreen, paragraph_counter, health, lives

def Jupiter_0():
    typewriter_print("You have reached your destination...", 0.03)
    paragraph_counter(int(p))
    typewriter_print("Jupiter.\n\n", 0.030)
    paragraph_counter(int(p))
    typewriter_print("Now...", 0.030)
    typewriter_print("Your task if you chose to complete it, is to find the magical Ring, this Ring is a very important piece of the weapon.", 0.030)
    typewriter_print("\n\nYou open your spaceship door, you take a moment to look all around and see what you can see",0.03)
    typewriter_print('...', 0.6)
    paragraph_counter(int(p))
    typewriter_print("but all you see is sheer desert.",0.03)
    Jupiter_1()

def Jupiter_1():
    typewriter_print("\n\nYou come to a clearing with 3 open paths.", 0.03)
    typewriter_print("\n\nA sign in the sand reads - ", 0.03)
    typewriter_print("Left = (100 - 99) | Centre = (8 on it's side) | Right = (10 / 5)", 0.03)
    answer = typewriter_input("\n\nWhich path will you chose? [ 1 = Left | 2 = Centre | 3 = Right] ", 0.03)
    path = str(answer)
    while path != "1" and path != "2" and path !="3":
        Jupiter_1()
    if answer == ("1"):
            typewriter_print("\nYou turn left and start walking into the vast desert, ",0.03)
            paragraph_counter(int(p))
            typewriter_print("then all a sudden...you come to beautiful oasis with what looks like fresh green trees, and fresh clear running water",0.03)
            answer = typewriter_input("\n\nDo you fill your bottle of water, or carry on? [ 1 = fill water bottle | 2 = Carry on): ",0.03)
            if answer == "2":
                typewriter_print("\n\nYou try to continue but you do not survive without water and begin to fade.",0.03)
                new_life(Jupiter_1)
            elif answer == "1":
                typewriter_print("\nYou fill your water bottle and continue on your quest.", 0.03)
                paragraph_counter(int(p))    
                typewriter_print("\n\nYou start to feel the strangest sensation, as if you're fading, so you stop to take a drink from your water bottle, to see if that helps.",0.03)
                typewriter_print(" It does. ", 0.03)
                paragraph_counter(int(p))
                typewriter_print("Soon you realise that you haven't got a lot of water left, so start taking small sips.",0.03)
                paragraph_counter(int(p))
                typewriter_print("\n\nAs you carry on down this path you begin to fade even faster. As you take another small sip, you start to wonder if the water will last, or if you can even complete your quest.",0.03)
                paragraph_counter(int(p))
                typewriter_print("\n\nLuckily and just in your grasp, you see another oasis. You sigh in relief. ",0.03)
                paragraph_counter(int(p))
                typewriter_print("You fill your water bottle again but this time you head back to your spaceship so you can carry on your search",0.03)
                Jupiter_2()
            else:
                typewriter_print(INCORRECT_A, 0.03)
                new_life(Jupiter_1)
    else:
            typewriter_print("You take two steps before you begin to vaporize into millions of dust particles", 0.03)
            new_life(Jupiter_1)

def Jupiter_2():
    global health
    answer = typewriter_input("\n\nWhich path will you chose? [ 1 = Left | 2 = Centre | 3 = Right] ", 0.03)
    path = str(answer)
    while path != "1" and path != "2" and path !="3":
        Jupiter_2()
    if answer == ("3"):
        typewriter_print("\n\nYou turn right and all of a sudden you see a huge ball coming towards you, as it comes nearer it starts to take shape.",0.03)
        paragraph_counter(int(p))
        typewriter_print(" The shape soon morphs into that of a huge andriod, at least 10 feet tall.",0.03)
        paragraph_counter(int(p))
        typewriter_print(" You look up and see it has a face like a big evil wasp, with huge wings",0.03)
        paragraph_counter(int(p))
        typewriter_print("\n\nYou gasp in horror as you decide what action to take",0.03)
        paragraph_counter(int(p))
        answer = typewriter_input("\n\nDo you fight, or flee? [1 = Fight | 2 = Flee]: ",0.03)
        if answer == "1":
            health -= 30
            typewriter_print("\n\nYour first attack lands, weakening the wasp slightly. But now it looks angry and lunges in for the attack [Lose - 30 Health]",0.03)
            answer = typewriter_input("\n\nDo you carry on fighting? [1 = Fight | 2 = Flee]: ",0.03)
            if answer == "1":
                typewriter_print("\nYou shoot with the precision of a sniper, and with this second attack you sheer the wasps wings and bring it too it's knees",0.03)
                answer = typewriter_input("\n\nFinish it? [1 = Fight | 2 = Show Mercy]: ",0.03)
                if answer == "1":
                    typewriter_print("\n\nYou shoot a decisive third shot, peircing it's head and killing the big, evil, wasp andriod",0.03)      
                    typewriter_print("\n\nCongratulations you have WON",0.03)
                    typewriter_print("\n\nYou claim the RING as your prize from the corpse of the andriod",0.03)
                    Jupiter_3()
                elif answer == "2":
                    typewriter_input('You try to display some kindness to the andriod and leave, but Andriods do not understand mercy.', 0.03)
                    typewriter_print("Before you can even begin to turn, the Andriod shoots you with a sonic ray", 0.03)
                    new_life(Jupiter_2)
            else:
                typewriter_print("Before you can even begin to turn and flee, the Andriod shoots you with a sonic ray", 0.03)
                new_life(Jupiter_2)
        else:
                typewriter_print("Before you can even begin to turn and flee, the Andriod shoots you with a sonic ray", 0.03)
                new_life(Jupiter_2)
    else:
        typewriter_print("You take two steps before you begin to vaporize into millions of dust particles", 0.03)
        new_life(Jupiter_1)

def Jupiter_3():
    typewriter_print('\n\nWith the ring in hand you head back to your ship', 0.03)
    time.sleep(0.5)
    typewriter_print("...",0.5)
    next_page()
    clearScreen()
    ship_hub.jupiter_complete_check=True
    ship_hub.ship_hub("Jupiter")

def Jupiter_complete():
    typewriter_print("Having already got the ring, there's not much else for you to do here so you get back aboard your ship")
    time.sleep(0.5)
    typewriter_print("...",0.5)
    ship_hub.ship_hub("Jupiter")