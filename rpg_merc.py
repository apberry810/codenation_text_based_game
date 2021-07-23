
import time
import random
import ship_hub
from usefulfunctions import clearScreen, typewriter_print, typewriter_input, paragraph_counter, new_life, next_page, health, lives
from ascii_art import game_over
from rpg_variables import p, health, ammo, race, INCORRECT_A



def random_encounter(enemy, win_1, win_2, lose):
    global health
    global ammo
    num = 0
    typewriter_print(f"\n\nThe enemy looks {enemy}\n\n", 0.03)
    if enemy == "weak": 
        num = random.randint(1,6)
    elif enemy == "strong": 
        num = random.randint(1,11)
    if num <= 4:
        win_1()
        if health <= 0:
            lose()
    elif num > 5:
        win_2()
        if health <= 0:
            lose()
    
ammo = 100


def choice_1_ammo():
    global ammo
    global paragraph_10
    ammo_c = typewriter_input('Do you want to take the spare ammo just in case? 1 = Yes || 2 = No  ', .029)
    if ammo_c == "1":
        paragraph_10 = paragraph_10a
    elif ammo_c == "2":
        paragraph_10 = paragraph_10b
        ammo = 0
    else:
        choice_1_ammo()
    typewriter_print(paragraph_10, 0.032)
   


def path_1_door():
    typewriter_print(paragraph_13a, 0.03)
    typewriter_print(paragraph_13c, 0.03)
    answer = typewriter_input("\n\nWould you like to hack the system to open the door? [1 = Yes | 2 = No] ", 0.035)
    if answer == "1":
        typewriter_print("\n\nWorking", 0.015)
        typewriter_print(".....",.8)
        typewriter_print("\n\nSUCCESS!\n\n", 0.015)
        paragraph_counter(int(p))
        typewriter_print(paragraph_13d, 0.03)
        choice_2_an()
    elif answer == "2":
        typewriter_print(paragraph_13aa, 0.03)
        new_life(choice_2_all())


def choice_2_an():
    global health
    answer = typewriter_input("\n\nDo you still want to hack the system? [1 = Yes | 2 = No] ", 0.035)
    if answer == ("1"):
        num = random.randint(1, 6)
        typewriter_print("\n\nWorking",0.015)
        typewriter_print("........",.8)
        if num <= 3:
            typewriter_print("\n\nSUCCESS!\n\n",0.015)
            typewriter_print(paragraph_14a, 0.03)
        else:
            health -= 20
            paragraph_counter(int(p))
            typewriter_print("\n\nFAILURE!!\n\n", 0.015)
            typewriter_print(paragraph_14b, 0.03)
            typewriter_print(paragraph_14ba, 0.03)
            typewriter_print(paragraph_14bb, 0.03)
            typewriter_print(paragraph_14bc, 0.03)
            
        paragraph_counter(int(p))
    if answer == ("2"):
        typewriter_print(paragraph_13aa, 0.03)
        typewriter_print(paragraph_13ab, 0.03)
        choice_2_all()

tries = 1
question_level = 0
def choice_2_all():
    global tries
    global question_level
    answer = typewriter_input("\n\nWhat would you like to do? 1 = Speak Password || 2 = Show Key || 3 = Speak Password and Show Key at the same time ", 0.035)   
    if answer == "2" and question_level == 0:
        typewriter_print(paragraph_15, 0.03)
        question_level = 1
        choice_2_all()
    elif answer != "2" and question_level == 0 and tries == 1:
        typewriter_print( paragraph_15a, 0.03)
        question_level = 0
        tries = 0
        choice_2_all()
    elif answer != "2" and question_level == 0 and tries == 0:
        typewriter_print(paragraph_15b, 0.03)
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        new_life(merc_pt_2)
    elif answer != "1" and question_level == 1 and tries == 1:
        typewriter_print(paragraph_15a,0.03)
        question_level = 0
        tries = 0
        choice_2_all()
    elif answer != "1" and question_level == 1 and tries == 0:
        typewriter_print(paragraph_15b,0.03)
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        new_life(merc_pt_2)
    else:
        typewriter_print(paragraph_16, 0.03)
        merc_pt_3()
l = 0
r = 0

def damage_0_low():
        global health
        typewriter_print("It seems like there are more of them then you first anticipated and the fight is a struggle with only 10 charges, but with your elite combat training you manage to defeat them all, if not without a few scrapes [-10 Health]",0.03)
        health -= 10
def damage_0_high():
        global health 
        typewriter_print("It seems like there are more of them then you first anticipated and the fight is a struggle with only 10 charges, even with your elite combat training and you barely manage to defeat them all and the damage you take is severe [-50 Health]",0.03)
        health -= 50
def damage_1_low():
        typewriter_print("It seems like there are more of them then you first anticpated, however, with the extra ammo you brought the fight is a breeze. \nYou manage to defeat them all without so much as a scratch",0.03)
def damage_1_high():
        global health
        health -= 10
        typewriter_print("It seems like there are more of them then you first anticpated and the fight is a struggle, however with the extra ammo you brought you manage to defeat them all, if without if not withot a few scrapes [-10 Health]", 0.03)        
def loss_():
        global r
        global l
        r = 0        
        l = 0
        typewriter_print("\n\nYou are victorious but it seems the damage you take was too much in the end. You collapse head first in the room", 0.03)
        new_life(merc_pt_3)
        
def choice_3_all(): 
    global ammo
    global l
    global r
    answer = typewriter_input('\n\nWhere would you like to go? [1 = Go L | 2 = Use Terminal | 3 = Go R] ', 0.03)
    while answer != "1" and answer != "2" and answer != "3":
        choice_3_all()
    if (l == 0) and answer == "2":
        typewriter_print(paragraph_20a, 0.03)
        choice_3_all()
    elif l == 1 and answer == "2":
        typewriter_print(paragraph_20ab,0.03)
        metal_input()
    if answer == "1" and l == 0:
        typewriter_print(paragraph_20b,0.03)
        l = 1
        choice_3_all()
    elif answer == "1" and l == 1: 
        typewriter_print(paragraph_20ba, 0.03)
        choice_3_all()
    if answer == "3" and r == 0:
        r = 1
        typewriter_print(paragraph_20c, 0.03)       
        typewriter_print(paragraph_20ca,0.03)
        paragraph_counter(int(p))
        typewriter_print(paragraph_20cb,0.03)
        if ammo == 0:
            random_encounter("strong", damage_0_low, damage_0_high,loss_)
        else:
            random_encounter("weak", damage_1_low, damage_1_high, loss_)
        typewriter_print(' but the fight is over. You look around and search for somethig useful to help you forge. It\'s difficult, due to the destruction from the fight, to find anything that can help.', 0.03)
        typewriter_print('\nIn the corner of the room, on the arm of the scavs chairs you see a notebook. It reads - \n\n', 0.03)
        notepad()
        typewriter_print('\n\n\nYou head back into the control room', 0.03)
        choice_3_all()
    elif answer == "3" and r == 1:
        typewriter_print('You have already grabbed the note pad, there is nothing left for you in this room', 0.03)
        answer = typewriter_input("\n\nWould you like to read the notes again? [1 == Yes | 2 == No | 3 = Hint] ", 0.03)
        if answer == "1":
            notepad()
            choice_3_all()
        elif answer == "3":
            typewriter_print("You turn the page of the notepad and you see a bunch of Metal Values half written\n\nN Values\n\nIRON = IRO, so I = 9, R = 18, O = 15, so IRO = 91815\nSTEEL = STE, so S = 19, T = 20, E = 5, so STE = 19205\nMAXION = MAX, so....\n\nThe rest isn't legable")
            choice_3_all()
        else:
            choice_3_all()        
def notepad():
    typewriter_print('Hey Dumb Dumb - Here is the formula to calculate the value of the Metals...seeing as you keep forgetting\n\n', 0.03)
    typewriter_print('Value of Metal = N  MULTIPLIED by C\n\nN = Alphabetical number value of first 3 letters in the Word\n\nC = Count of Letters in the Word\n\nEXAMPLE. A,C,E,F,G = 1,3,5,6,7 and ACEFG = 5. So 135 X 5 =  Value', 0.01)
        
  
def metal_input():
    answer = input("\nWhat would you like to do? [1 = Enter Value | 2 = Go Back] ")
    if answer == "1":
        answer2 = input("Enter Value -  ")
        if answer2 == "78744":
            merc_pt_end()
        else:
            typewriter_print("Unrecognised metal value given", 0.03)
            metal_input()
    elif answer == "2":
        choice_3_all()
    else:
        INCORRECT_A
        metal_input()
            
#Above is all 

def merc_pt_end():
    typewriter_print('The system spins into action.', 0.03)
    typewriter_print('The dome above begins to open and a burst of blindingly hot light streams into the smelting pot below as it begins to clunk and churn.\n\n', 0.03)
    paragraph_counter(int(p))
    typewriter_print('Within less than a minute it\'s over.', 0.03)
    paragraph_counter(int(p))
    typewriter_print('In the exit tray you see a bar of black metal so dark, it absords all visible light.', 0.03)
    typewriter_print('You pick it up and are surpirsed at how cold it is already. You head back to your ship with the bar safley tucked in your backpak', 0.03)

paragraph_1 = ("As you drop out of subspace and begin your descent to the surface, you look out of your cockpit at the dull, grey planet. \nThere is nothing around besides a bunch of craters and if it wasn’t for the giant ball of light in the near distance, you could swear you’re about to land on the moon.\n\n")
paragraph_2 = ("You shift into focus because you have a mission to do, and Comet is waiting.")
paragraph_3 = (" Time to gear up.")
section_1 = [paragraph_1, paragraph_2]
paragraph_4 = ("\n\nYou key into your locker to check your space suit and backpack.\n\n")
paragraph_5 = ("You suit up, and activate the internal cooling system. Your HUD reads - CURRENT TEMP = 28C'.")
paragraph_6 = ("")
paragraph_6a = ('\n\n"28 still feels crazy warm in this suit...but it’s better than 428oC”, you think to yourself')
paragraph_6b = ('\n\n"Walking around in this suit always feels odd, but it\'s not like this metal body can withstand extreme temps”, you think to yourself.')
paragraph_7 = ('\n\nNext you check your backpack. You definitely need to take the key to the vault and the Ingot needed to mix with the Mercronium to make Maxion. \nThere isn\'t much space left, but you think you can fit one more item in. \nYou grab your blaster and load it with 10 charges - “enough to deal with a small group of scavs, but not much else”, you say to yourself as you sling it over your shoulder.')
paragraph_8 = ("\n\nNext you look over at the spare ammo.")
paragraph_9 = ("\n\nYou remember the commander saying that the forge should have long since been abandoned from the end of the early space age, but there could be a few bandits about.\n")
paragraph_10 = ("")
paragraph_10a = ("\nYou decide it’s best to take the ammo, just in case, “better to have it and not need it” after all.")
paragraph_10b = ("\nYou decide it’s best to leave the ammo to save on weight.")
paragraph_11 = ("\n\nYou touch down at the designated LZ about a mile away from the vault. You wonder why you were advised not to get closer, but it’s an easy enough walk in 0.38g.")
paragraph_12 = ("\n\nYou step out of the airlock and begin walking (well, hopping) to the Vault until you come across a large, tinted, lattice like dome. \nAbout 100 meters to the right there is a relatively small, windowless building with a red sensor above a blast door.\n")
paragraph_13 = ('You approach the door and it speaks.')
paragraph_13aa = (' “Waarschuwing, toon de SLEUTEL dan spreek de WACHTWOORD, of DOOD. Je hebt 2 pogingen”')
paragraph_13a = ('\n\nIt\'s a language neither you, nor your translator understand, but with your superior intelligence you deduce that, as this is a Human facility, it\'s most likely an earth language.\n\nYou then use your suit\'s rudimentary computer system to remotely connect to your ship and use a quantum cypher to do a quick check on Earth languages.\n\nYou get a hit from “Dutch” and begin to download the library, unfortunately a solar wind interferes with your connection and the file only partly downloads, leaving only the last half of the sentence deciphered. It reads - “then speak the PASSWORD, or DIE. 2 attempts”.')
paragraph_13ab = ('The last half reads - “then speak the PASSWORD, or DIE. 2 attempts”.')
paragraph_13c = ('\n\nYou can also use your suit to hack into this system.')
paragraph_13d = ('Upon gaining access, and looking over the programming, you can see that there are 4 laser turrets hidden behind panels on either side of the door, and while you are confident you can open the door, because the two programmes are intrinsically linked, there is a small chance that opening the door will trigger the “Turret Defence” programme to execute.')
paragraph_14a = ('\n\nYou manage to hack the door. The system wurrs and the doors creak, before slowly sliding open. You see no sign of the turrets, looks like you didn’t trip the programme. You enter to see a large elevator and a panel on the wall with two arrows pointing up and down, you press down and the elevator starts to move. ')
paragraph_14b = ('You manage to hack the door, and it begins to creak and slide open slowly. You start to walk, but no sooner do you put one foot in front of the other, do the panels slide open.')
paragraph_14ba = ('\n\nYou sprint for the open door. Running in this gravity is clumsy and awkward, but you adjust remarkably quickly. You jump and dive through the door just as the turrets spring to action.')
paragraph_14bb = ('You make it, barely, and not without a bit of damage to your leg and suit [-10HP]. That outcome may have been very different.') 
paragraph_14bc = ('\n\nStanding, you realise you’re inside a large elevator. On the wall is a panel with two arrows pointing up and down, you press down and the elevator starts to move.')
paragraph_15 = ('\n\nThe sensor glows red. The door is silent.')
paragraph_15a = ('\n\nThe sensor glows red. The door speaks again, but this time in English - “Warning, This is your last attempt"')
paragraph_15b = ('\nThe sensor glows red and the system wurrs. Suddenly, 4 panels slide open on either side of the door revealing laser turrets which spring into action. You turn to try and flee, but it’s no use, from this distance you would need a miracle to surive. The piercing lasers begin to dematerialise you.\n\n\n')
paragraph_15ba = ('YOU ARE DEAD.')
paragraph_16 = ('The sensor glows red. The system wurrs and the doors creak, before sliding open slowly to reveal a large elevator. On the wall is a panel with two arrows pointing up and down, you press down and the elevator starts to move.')
paragraph_17 = ('As you sink incredibly slowly for what feels like an hour, you realise that gravity is starting to normalise...no, wait, it’s actually getting stronger. \n“Artificial gravity!”, you come to realise. \nYou finally reach the bottom of the elevator and a blast door opens leading to a long hallway, you walk down and hit another blast door that automatically starts to open “Thank the maker there isn’t another sensor” you whisper to yourself. ')
paragraph_18 = ('\n\nYou exit the elevator to stand in what looks like a control room with a terminal in the centre and a door to the left and right. \nLooking out over the terminal you see a large, circular room. It’s ceiling stretches all the way to the surface, and you surmise that you’re directly below the large dome. \nIn the centre of the room you see a giant smelting pot below about the same size as your ship, and next to it is a pile of Mercronium.')
paragraph_19 = ('\n\nBelow the terminal in front of you is a sign “L = Forge || R = Crew quarters.')
paragraph_20a = ('\n\nYou check the terminal display and it has a message which reads - “The Smelting Pot is Empty - no metal can be forged”')
paragraph_20ab = ('\n\nYou check the terminal display and it has a message which reads - “AUTOMATED FORGING IS   ONLINE - Please enter the Value of the metal you wish to forge”')
paragraph_20b = ('\n\nYou walk down a long arching staircase to the left of the control room and arrive at the forge. \nYou look up through the long tunnel and see what looks like countless refracting lenses and prisms aligned all the way to the top. \nYou were right, you are under the dome. You place the Ingot and the Mercronium in a small hatch on the side of the smelting pot then go back up the stairs to the control room. \nIt\'s time to forge some Maxium. ')
paragraph_20ba = ('\n\nYou have already placed the materials in the forge, why go back down? ')
paragraph_20c = ('You open the door to the crew quarters expecting to find an empty room, what you find instead are several heavily armed bandits, dressed in thick, scaly armor.')
paragraph_20ca = ('\nThey\'re bickering intensely about something, and haven\'t actually noticed you yet.') 
paragraph_20cb = ('\nYou ready your weapon and before they even turn to face you, you fire a volley of shots')

clearScreen()
def merc_pt_1():
    typewriter_print(paragraph_1, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_2, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_3, 0.07)
    paragraph_counter(int(p))
    typewriter_print(paragraph_4, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_5, 0.03)
    paragraph_counter(int(p))
    if race == "Android":
        paragraph_6 = paragraph_6b
        typewriter_print(paragraph_6, 0.03)
    elif race != "Android":
        paragraph_6 = paragraph_6a
        typewriter_print(paragraph_6, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_7, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_8, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_9, 0.03)
    paragraph_counter(int(p))
    choice_1_ammo()

def merc_pt_2():
    paragraph_counter(int(p))
    typewriter_print(paragraph_11, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_12, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_13, 0.03)
    typewriter_print(paragraph_13aa, 0.04)
    paragraph_counter(int(p))
    path_1_door()
    paragraph_counter(int(p))

def merc_pt_3():     
    paragraph_counter(int(p))
    typewriter_print(paragraph_17, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_18, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_19, 0.03)
    choice_3_all()
    merc_pt_end()
    ship_hub.mercury_complete_check=True
    ship_hub.ship_hub("Mercury")

def merc_story():
    merc_pt_1()
    next_page()
    clearScreen()
    merc_pt_2()
    next_page()
    clearScreen()
    merc_pt_3()

def merc_story_complete():
    typewriter_print(paragraph_1, 0.03)
    typewriter_print("There is nothing else to do here so you return to your ship", 0.03)
    time.sleep(0.5)
    typewriter_print("...",0.5)
    ship_hub.ship_hub("Mercury")