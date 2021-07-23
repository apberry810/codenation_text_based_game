import time
import ship_hub
from ascii_art import print_skull_ascii, print_pluto_ascii
from usefulfunctions import clearScreen, typewriter_print, typewriter_input, health, lives, new_life

def pluto_zone1():   
    print_pluto_ascii()
    answer = typewriter_input("You have landed on the icy planet of Pluto. There is nothing around for miles. In the distance you spot a spire. Do you: 1-Go towards the spire? Or 2-Leave on your ship? ", 0.03)
    if answer=="2":
        typewriter_print("You climb back into your ship and set a new destination", 0.03) ########### go to ship after this
        time.sleep(0.5)
        typewriter_print("...",0.5)
        ship_hub.ship_hub("Pluto")
    elif answer=="1":
        typewriter_print("You look towards the icy spire and start to walk towards it... \n", 0.03)
        pluto_zone2()
    else:
        typewriter_print("Whoops invalid input...Please try again.", 0.03)
        time.sleep(1)
        clearScreen()
        pluto_zone1()

def pluto_zone2():
    time.sleep(1)
    clearScreen()
    answer=typewriter_input("After a couple hours trekking across the ice plains of Pluto, you see the spire grow larger and larger until you are in its shadow. \nThere is a door in the centre of the spire, but it is frozen shut. \nDo you: 1- Use your laser blaster to melt the ice and break open the door? 2- See if there is another way in? ", 0.03)
    if answer=="1":
        typewriter_print("You aim your blaster directly at the door and set it to maximum power. You pull the trigger and the blaster makes quick work of the door. You enter through the hole that you created... \n", 0.03)
        pluto_zone3()
    elif answer=="2":
        trap()
    else:
        typewriter_print("Whoops invalid input...Please try again.", 0.03)
        time.sleep(1)
        clearScreen()
        pluto_zone2()


def trap():
    global health
    global lives
    typewriter_print("You scout the outside of the spire and it seems to be some sort of temple. You are unsure of who the temple's god is but it makes you feel uneasy. You circle the entire spire but before you return to where you started you hear an ominous voice", 0.03)
    typewriter_print("\n\nYOU SHOULD NOT BE HERE\n\n", 0.05)
    typewriter_print("At that moment the ground opens up beneath you and you fall, hitting the solid groud with a thud [lose 40 health]", 0.03)
    health -= 40
    if health <= 0:
        health = 100
        lives -=1
        new_life(pluto_zone2)
    else:
        typewriter_print("\n\nYou manage to get to your feet and climb back up. You sustained some damage, but you can move", 0.03)
        pluto_zone2_1()

def pluto_zone2_1():
    answer=typewriter_input("\n\nYou found no other entrances. Do you 1- Use your laser blaster to melt the ice and break open the door? 2- Return to your ship? ", 0.03)
    if answer=="1":
        typewriter_print("You aim your blaster directly at the door and set it to maximum power. You pull the trigger and the blaster makes quick work of the door. \nYou enter through the hole that you created", 0.03)
        time.sleep(0.5)
        typewriter_print("...",0.5)
        clearScreen()
        pluto_zone3()
    elif answer=="2":           #################back to ship here
        typewriter_print("You begin your journey back to your ship....", 0.03)
        ship_hub.ship_hub("Pluto")
    else:
        typewriter_print("Whoops invalid input...Please try again.", 0.03)
        time.sleep(1)
        clearScreen()
        pluto_zone2_1()

def pluto_zone3():
    typewriter_print("You step through the broken door, but as soon as you do the wall collapses behind you, leaving you trapped. \nYou have no choice but to continue to go deeper into the temple... \n", 0.03)
    time.sleep(1)
    answer=typewriter_input("\nAs you make your way towards the centre of the temple, you come across a small plinth with an ice crystal perched on top. This could be what you were looking for! \nDo you: 1- Reach out and pick up the ice crystal? 2- Look around for any danger first? 3- Back away slowly? ", 0.03)
    if answer=="1":
        clearScreen()
        typewriter_print("You reach towards the ice crystal but suddenly you hear a voice from behind you. You turn around to see a floating skeleton skull staring at you! \n", 0.03)
        print_skull_ascii()
        time.sleep(2)
        pluto_zone4()
    elif answer=="2":
        clearScreen()
        typewriter_print("You scan your surroundings and as you turn to check behind you a floating skeleton skull has snuck up behind you! \n", 0.03)
        print_skull_ascii()
        time.sleep(2)
        pluto_zone4()
    elif answer=="3":
        clearScreen()
        typewriter_print("Thinking this is a trap, you start to back away slowly. However you only took a handful of steps before you feel an object press into your back. You spin around and see a floating skeleton skull watching you! \n", 0.03)
        print_skull_ascii()
        time.sleep(2)
        pluto_zone4()
    else:
        typewriter_print("Whoops invalid input...Please try again.", 0.03)
        time.sleep(1)
        clearScreen()
        pluto_zone3()

def pluto_zone4():
    answer=typewriter_input("You ready your blaster, but the skull does not react in any way. Do you: 1- Speak to the skull? 2- Shoot at the skull? ", 0.03)
    if answer=="1":
        typewriter_print("You ask the skull what it is doing here, and it replies: 'I am the guardian of this temple, only those who I deem worthy may leave here with what they seek! Answer my riddles three and only then I will let you leave with what you seek!' \n", 0.03)
        pluto_zone5()
    elif answer=="2":
        typewriter_print("You fire your blaster directly at the skull but it doesn't have any effect on the skull whatsoever. \n", 0.03)
        typewriter_print("'Ow, why would you do that?! Did no-one ever teach you diplomacy? It's a good thing I'm a floating skull or else that might've hurt! \nYou should be careful with that thing. If you put that thing away I'll let you have that ice crystal thing if you just answer 3 of my questions.' \n", 0.03)
        time.sleep(3)
        pluto_zone5()
    else:
        typewriter_print("Whoops invalid input...Please try again.", 0.03)
        time.sleep(1)
        clearScreen()
        pluto_zone4()

def pluto_zone5():
    typewriter_print("'Question 1: Where are more than half of your bones found?' \n", 0.03)
    time.sleep(1)
    answer=typewriter_input("'1-Legs and Arms? 2- Hands and Feet? 3- Ribs and Face?' ", 0.03)
    if answer=="1":
        typewriter_print("'That is incorrect! Try again' \n", 0.03)
        pluto_zone5()
    elif answer=="2":
        typewriter_print("'Well done that was correct!' \n", 0.03)
        pluto_zone6()
    elif answer=="3":
        typewriter_print("'That is incorrect! Try again' \n", 0.03)
        pluto_zone5()
    else:
        typewriter_print("Whoops invalid input...Please try again.", 0.03)
        time.sleep(1)
        clearScreen()
        pluto_zone5()

def pluto_zone6():
    typewriter_print("'Now for Question 2: Pluto's atmosphere is made of mostly what gaseous substance?' \n ", 0.03)
    time.sleep(1)
    answer=typewriter_input("'1- Nitrogen? 2- Carbon Dioxide? 3- Helium? 4- Request a Hint?' \n", 0.03)
    if answer=="1":
        typewriter_print("'Correct! You must have guessed on that one...' \n", 0.03)
        time.sleep(2)
        pluto_zone7()
    elif answer=="2":
        typewriter_print("'Wrong! Try again' \n", 0.03)
        pluto_zone6()
    elif answer=="3":
        typewriter_print("'Nope, try again' \n", 0.03)
        pluto_zone6()
    elif answer=="4":
        typewriter_print("'You want a hint? Ok then, the answer is an element in the periodic table. That should help a little' \n", 0.03)
        time.sleep(2)
        pluto_zone6()
    else:
        typewriter_print("Whoops invalid input...Please try again.", 0.03)
        time.sleep(1)
        clearScreen()
        pluto_zone6()

def pluto_zone7():
    typewriter_print("'You've done well to make it this far but you'll never get this one right. Now for my final question. \nQuestion 3: What is the circumference of Pluto?' \n", 0.03)
    time.sleep(1)
    answer=typewriter_input("'1- 16,157 km? 2- 7,232 km? 3- 23,894 km? 4- Request a Hint?' \n", 0.03)
    if answer=="1":
        typewriter_print("'Incorrect, try again' \n", 0.03)
        pluto_zone7()
    elif answer=="2":
        typewriter_print("'That's the right answer! Did you cheat? Oh well, I'm bored of you anyway so take that ice crystal and leave before I make you join my skeleton legion!' \n", 0.03)
        time.sleep(0.5)
        typewriter_print("The skeleton uses his magic to remove the debris from the broken doorway and allows you to leave with the ice crystal. Back on your ship you decide where to travel to next... \n", 0.03) ##################back to ship
        ship_hub.pluto_complete_check=True
        ship_hub.ship_hub("Pluto")
    elif answer=="3":
        typewriter_print("'Wrong try again.' \n", 0.03)
        pluto_zone7()
    elif answer=="4":
        typewriter_print("'A hint? I told you this one was hard. For reference Earth's circumference is 40,030 km' \n", 0.03)
        time.sleep(2)
        pluto_zone7()
    else:
        typewriter_print("Whoops invalid input...Please try again.", 0.03)
        time.sleep(1)
        clearScreen()
        pluto_zone7()

def pluto_zone1_2():       ##this zone if for when the pluto section is complete   
    print_pluto_ascii()
    answer = typewriter_input("You have landed on the icy planet of Pluto. \nThere is nothing around for miles except for the temple spire. \nThere is nothing else to do here. \nDo you: 1- Take in the scenery? 2- Get back on your ship? ", 0.03)
    if answer=="2":
        typewriter_print("You climb back into your ship to set a new destination \n", 0.03) ############### go to ship after this    
        time.sleep(2)    
        ship_hub.ship_hub("Pluto")
    elif answer=="1":
        typewriter_print("The view looks like a postcard, and yet all the directions you look are all extremely similar. \nIce plains for miles in all directions except for the lonely spire in the distance. \nAfter some time you get back in your ship to set a new course", 0.03) #############go to ship after this
        typewriter_print("...",0.5)
        time.sleep(2)
        ship_hub.ship_hub("Pluto")
    else:
        typewriter_print("Whoops invalid input...Please try again.", 0.03)
        time.sleep(1)
        clearScreen()
        pluto_zone1_2()
