from typing import AnyStr
import ship_hub
import ascii_art
from usefulfunctions import typewriter_print, typewriter_input, clearScreen, next_page, paragraph_counter
import time
from rpg_variables import p
from threading import Thread


def wronginput():
    typewriter_print("Whoops invalid input...Please try again.")
    time.sleep(1)
    clearScreen()
def no_c():
    print("[THERE ARE NO CONTINUES]")

lives = 0
clock = 18
cell = ""

def new_life(func):
    global clock_time
    global lives
    global health 
    typewriter_print('\n\nAs your consciousness fades, your last thoughts are of your four legged companion.\n\n\n', 0.03)
    paragraph_counter(int(p))
    typewriter_print('YOUR HEALTH HAS REACHED 0', 0.05)
    if lives > 0:
        new_answer = typewriter_input(f"\n\nBut it's not the end, you have {lives} continue/s remaining. CONTINUE? [1 == YES || 2 == NO] ",0.03 )
        if new_answer == "1":
            clearScreen()
            typewriter_print("It's not over. ",0.03)
            paragraph_counter(int(p))
            typewriter_print("It can't be! ",0.03)
            paragraph_counter(int(p))
            typewriter_print("With your dying breath you scream out to the universe!\n\n", 0.03)
            paragraph_counter(int(p))
            paragraph_counter(int(p))
            typewriter_print("The universe responds!\n\n",0.03) 
            typewriter_print("Suddenly, something envelopes you just as everything goes dark.", 0.03)
            paragraph_counter(int(p))
            typewriter_print(" You wake up, dazed and confused...with no recollection of what happened yet something spurs you into action, \"It's time to get moving\", you think to yourself\n\n", 0.03)
            next_page()
            clearScreen()
            func()
            lives -=1 
            clock_time = 60
            #credits()
        else:
            ascii_art.game_over()
            credits()
            replay()
    else:
        ascii_art.game_over()
        credits()
        replay()

def ending_zone1():
    global lives
    global cell
    global clock
    typewriter_print("This is it. It all boils down to this.",0.03)
    typewriter_print(" The stakes are high and you will only have one shot to save Comet.\n\n[THERE ARE NO CONTINUES FROM NOW ON]",0.03)
    next_page()
    time.sleep(0.5)
    print(f"TIME - {clock}:10\nCELL - {cell}\n\n\n\n")
    typewriter_print("You brace yourself as you fly directly into ship into the Secret Pirate Base hangar bay.\n\n",0.03)
    time.sleep(0.5)
    typewriter_print("luckily you make it in undetected and there is no one around.\n\n",0.03)
    time.sleep(0.5)
    typewriter_print("You exit your ship with the items you collected, ready for the challenge ahead.",0.03)
    time.sleep(0.5)
    typewriter_print(" The hangar bay appears to be deserted. There are 4 doors on the far side of the hangar bay.\n\nSigns above the doors read - Defence Systems | Camera Room | Cell Block | Boss Room")
    time.sleep(0.5)
    typewriter_print("\n\nNext to the doors - Defense Systems, Camera Room and Cell Block. There are digital terminals.", 0.04)
    time.sleep(0.5)
    next_page()
    ending_room_choice()

defence_check = False
cam_check = False
cell_check = False
boss_check = False


def ending_room_choice():
    global lives
    global clock
    global defence_check
    global cam_check
    global cell_check
    global boss_check
    clearScreen()
    print(f"TIME - {clock}:12\nCELL - {cell}\n\n\n\n\n\n\n")
    answer= typewriter_input("Which door do you want to approach? [1 = Defence Systems | 2 = Camera Room | 3 = Prison Wing | 4 = Boss Room ",0.03)
    if answer=="1":
        typewriter_print("\n\nYou approach the Defence Systems Door\n\nThe terminal reads - Gaurd SHIFT CHANGES:\n\n23:45 - 00:00\n08:00 - 08:15\n18:00 - 18:15:", 0.03)
        answer= typewriter_input("\n\nDo you want to enter? [1 = Yes | 2 = No] ",0.03)
        if answer == "1" and clock != 18:
           typewriter_print("\nYou enter the room but it's full of gaurds. They raise the alarm letting everyone on the ship know you're here.", 0.03)
           time.sleep(0.5)
           typewriter_print("There is no escape.", 0.03)
           lives = 0
           new_life()
        if answer == "1" and clock == 18:
           defence_room_choice()
        elif answer == "2":
            ending_room_choice()
        elif answer=="1" and defence_check == True:
            typewriter_print("\nYou enter the room but it's full of gaurds. They raise the alarm letting everyone on the ship know you're here.", 0.03)
            time.sleep(0.5)
            typewriter_print("There is no escape.", 0.03)
            lives = 0
            new_life()
    if answer == "2":
        typewriter_print("\n\nYou approach the Camera Room Door\n\nThe terminal reads - Gaurd SHIFT TIMES:\n\n23:00 - 8:00\n9:15 - 19:00\n19:15 - 10:45:", 0.03)
        answer= typewriter_input("\n\nDo you want to enter? [1 = Yes | 2 = No] ",0.03)
        if answer == "1" and clock != 19:
           typewriter_print("\nYou enter the room but it's full of gaurds. They raise the alarm letting everyone on the ship know you're here.", 0.03)
           time.sleep(0.5)
           typewriter_print("There is no escape.", 0.03)
           lives = 0
           new_life()
        if answer == "1" and clock == 19:
           clock = 20
           cam_room_choice()
        elif answer == "2":
            ending_room_choice()
    if answer == "3":
        typewriter_print("\n\nYou approach the Prison Wing Door\n\nThe terminal reads - DIRECTORY OF PRINSORS. PLEASE INPUT PRISONER CELL FOR DIRECTIONS\n\n")
        answer= typewriter_input("Do you want to input? [1 = Yes | 2 = No] ",0.03)
        if answer == "1":
            cell_room_choice()
        elif answer == "2":
            ending_room_choice()
    if answer == "4":
        answer = typewriter_input("\n\nYou aproach the main boss room...are you ready? [1 = HELL YEAH! | 2 = NOT QUITE ")
        if answer == "1" and cell_check == True:
            boss_choice()
        if answer == "1" and cell_check != True:
            typewriter_print("You face the boss empty handed....and without your weapon...you die horribly")
            new_life()
        else:
            ending_room_choice()
    else:
            ending_room_choice()
    


 
tries = 1 
def cell_room_choice():
        global lives
        global tries
        global cell_check
        global clock   
        answer= typewriter_input("\nINPUT PRISONER BLOCK ",0.03)
        answer2=typewriter_input("\nINPUT PRISONER CELL ",0.03)
        answer3 = answer2+answer.upper()
        if answer3 == "428D":
            paragraph_counter(int(p))
            typewriter_print("\n\nSHOWING MAP TO PRISINOR \'COMET\'")
            paragraph_counter(int(p))
            typewriter_print("\n\nYou memerise the map and fly to Cell 428D")
            paragraph_counter(int(p))
            paragraph_counter(int(p))            
            typewriter_print("\n\nAs soon as you get there, you are elated to see that he is unharmed and the both of you are so excited to see one another.")
            typewriter_print("\n\nYou look at the bars keeping him captive and figure out they're made from a super heated metal material that can be broken using the THERMAL EXPANSION COEFFICIENT, luckily the bars are already HOT")
            answer = typewriter_input("\n\nDo you: [1 = Use the Maxion Metal | 2 = Use the Energy Bar | 3 = Use the Ice Crystal ")
            if answer == "3":
                typewriter_print("\n\nYou use the Ice Crystal to super cool the bars of the cell in a matter of milliseconds, causing them to shatter into tiny snowflakes.")            
                typewriter_print("\n\nBoth you and comet run up to each other and you spare a few seconds to pet him.\n\nSeeing your companion again gives a burst of energy and determination and you feel as if you can take on anything again")
                typewriter_print("\n\nBut now it's time for the showdown")
                clock = 20
                lives = 0
                cell_check = True
                next_page()
                ending_room_choice()
            elif answer == "1" or answer == "2":
                typewriter_print("\n\nIn a moment of madness you try to use one of the other bars to super cool the bars of the cell. The reaction causes you to be vaporised")   
                new_life() 
        if answer3 != "428D" and tries != 0:
            tries = 0
            typewriter_print("\n\nYou have one more try\n\n")
            cell_room_choice()
        elif answer3 != "428D" and tries == 0 :
            typewriter_print(f"You memerise the map and fly to Cell {answer3}.")
            paragraph_counter(int(p))
            typewriter_print(" Unfortunatley what you see in front of you is not Comet...you wander around aimlessly until you are found by the gaurds.\n\nIn your confusion you are quickly dealt with")
            new_life()
                
                
        



def cam_room_choice():
    global cam_check
    global cell
    answer = typewriter_input("\nYou enter the room to find it empty. No gaurds are around. The room has a number of computers, atop tables and chairs, dotted around the room. All the computers have no power.\n\nYou try turning one on but it has no effect.\n\nThere is an open chamber in one of the walls with an empty slot inside. It looks like both your Maxium metal and the Energy Bar might fit! [Do you: [1 = Insert the Energy Bar | 2 = Insert the Maxium Metal?  ")
    if answer=="1":
        typewriter_print("\nYou push the energy bar into the slot and the computers in the room light up!")
        time.sleep(0.5)
        typewriter_print(" One of the computers now diplays all of cells in the Cell block.\n\nYou see Comet inside cell 428, cell block D\n\n")
        time.sleep(0.5)
        typewriter_print("You don't think there is anything else to do here so you leave back to the hanger")
        cell = "428D"
        cam_check = True
        next_page()
        ending_room_choice()
    elif answer=="2":
        typewriter_print("\nYou place the Maxion Metal inside the chamber expecting the room to spring to life.\n",0.03)
        time.sleep(1)
        typewriter_print("Instead the Metal causes a short circuit reaction that cascades through the ship, causing the ship's core to explode.\n",0.03)
        typewriter_print("No one makes it out.\n",0.03)
        new_life(cam_room_choice)
        


def defence_room_choice():
    global defence_check
    global clock
    answer = typewriter_input("\nYou enter the room to find it empty. No gaurds are around. The room has a number of computers, atop tables and chairs, dotted around the room.\n\nOne computer reads -  TURRETS ONLINE\n\nThere is an open chamber in one of the walls. Inside there is a bright light, so bright, you can't look directly at it. Above it a sign reads \"TURRET POWER COUPLING\".\n\nIt looks like both your Maxium metal and the Energy bar might fit! [Do you: [1 = Insert the Energy Bar | 2 = Insert the Maxium Metal?  ")
    if answer=="2":
        typewriter_print("\nYou push the Maxion metal into the slot. It pulses as it draws all of the light from the chamber into it, until the chamber is dark!")
        typewriter_print("\n\nThe computers now reads - TURRETS OFFLINE")
        time.sleep(0.5)
        typewriter_print("\n\nYou don't think there is anything else to do here so you leave back to the hanger")
        defence_check = True
        clock = 19
        next_page()
        ending_room_choice()
    elif answer=="1":
        typewriter_print("\nYou place the Energy bar inside the chamber expecting the turrets to shut down.\n",0.03)
        time.sleep(1)
        typewriter_print("\nInstead the Energy from the bar causes a massive reaction that cascades through the ship, causing the ship's core to explode.\n",0.03)
        typewriter_print("\nNo one makes it out.\n",0.03)
        next_page()
        new_life(ending_room_choice)
    else:
      wronginput() 
      defence_room_choice()

   
clock_time = 60
end_answer = ""


    


def countdown():
    global end_answer
    global clock_time
    end_answer = end_answer.upper()
    while clock_time > 0:
        time.sleep(1)
        clock_time -= 1
        if clock_time == 0:
            # print("You ran out of time, \n\n")
            clearScreen()
            choice_test()
            
        elif end_answer == "USE POWER RING" or end_answer == "POWER RING" or end_answer == "RING" or end_answer == "USE RING":
            break
        
    



def attack_boss():
    global clock_time
    global end_answer
    end_answer = input("\n\nWhat do you do? ")
    end_answer = end_answer.upper()
    if end_answer == "USE POWER RING" or end_answer == "POWER RING" or end_answer == "RING" or end_answer == "USE RING":
        choice_test() 
    while end_answer != "USE POWER RING" and end_answer != "POWER RING" and end_answer != "RING" and end_answer != "USE RING"  and clock_time > 0:
            clearScreen()
            print(f"WRONG ANSWER\n\nThe Head Pirate takes aim\n\n{clock_time} seconds remaing")
            attack_boss()
            #if clock_time == 0:
    # elif end_answer != "USE POWER RING" or end_answer != "POWER RING" or end_answer != "RING" or end_answer != "USE RING"  and clock_time > 0:
    #     clearScreen()
    #     print(f"WRONG ANSWER\n\nThe Head Pirate takes aim\n\n{clock_time} seconds remaing")
    #     attack_boss()
    

def boss_choice():
    typewriter_print("\n\nYou know that you wont make it out alive unles you deal with the Head Pirate")
    paragraph_counter(int(p))         
    typewriter_print("\n\nWith Comet in tow. You tear through the ship, defeating pirate after pirate, until you reach a large, oval room....this must be the bridge.")
    paragraph_counter(int(p))    
    typewriter_print("\n\nThe Head Pirate is sat in a throne at the far end")
    paragraph_counter(int(p))    
    typewriter_print("\n\nAs he turns his chair to face you. You see he is huge, easily 10ft in height.")
    typewriter_print("\n\n\"Welldone\",", 0.06)
    typewriter_print(" he says. His voice filling the room with a low rumble.\n\n") 
    paragraph_counter(int(p))    
    typewriter_print(" \"You kmade it this far, but what do you intend to 'USE' now\".")         
    typewriter_print("\n\n\"I can see you have no Ammo left after dealing with my minions, and you have brought no super weapon either\"")
    typewriter_print("\n\n\"You have lost\"", 0.05)
    typewriter_print("\n\nHe stands up and begins walking across the large room as he prepares his weapon to kill you")
    typewriter_print("\n\nYou look over at Comet and he looks back at you. Then sits, opens his mouth, and waits paitiently.....")
    typewriter_print("\n\nThere is only SIMPLE action left to take")
    Thread(target = countdown).start()
    attack_boss()


    
def choice_test():
    global end_answer
    end_answer = end_answer.upper()
    if end_answer == "USE POWER RING" or end_answer == "POWER RING" or end_answer == "RING" or end_answer == "USE RING":
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        typewriter_print("\n\nYou look at the pirate and smile")
        paragraph_counter(int(p))
        typewriter_print("\n\nI didn't bring the weapon?, you ask rhetorically. You're right.")
        typewriter_print("\n\nYou throw the RING OF POWER into Comet's mouth, to the bewilderment of the giant pirate standing before you")
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        typewriter_print("\n\nComent starts to glow")
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        typewriter_print('\n\nSuddley his body begins to release an immense amount of steam as he begins to dramatically increase in size.\n\nThe steam is so thick you can\'t see.')
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        typewriter_print("\n\nEventually the steam clears and what stands before you is Comet.")
        paragraph_counter(int(p))
        typewriter_print("20 feet tall, with 3 heads, and a body tougher than the strogest Maxion")
        typewriter_print("\n\n\"That's because you had it with you the whole time\", you say")
        typewriter_print("\n\nComet let's out a deafening roar as he charges the pirate")
        typewriter_print("\n\nThe pirate fires his whole clip in defence but thet bullets ricochet of Comet's metal frame")
        typewriter_print("\n\nWhat happens to te pirate is beyond gruesome...but revenge is sweet")
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        typewriter_print("\n\nComet returns back to normal and you both head back to your ship. ") 
        paragraph_counter(int(p))
        typewriter_print("\n\nThe other pirates give you little trouble on the way back. Most have heard about the destruction on the bridge, and those that haven't are few, and easily dealt with")
        paragraph_counter(int(p))
        typewriter_print("\n\nYou set a course for Earth and start the engines.")
        paragraph_counter(int(p))
        typewriter_print("\n\nNow you can ttake the time to properly welcome Comet with a nice meal and some tlc, before you both hit the bed for some well deserved R&R")
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        typewriter_print("Just as your eyelids close and you slip into sleep, you hear and ominous voice")
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        typewriter_print("\n\n\n\"IT\'S TIME TO GET MOVINNG\"\n\n",0.1)
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        ascii_art.the_end()
        paragraph_counter(int(p))
        paragraph_counter(int(p))
        credits()     
    elif clock_time == 0:
        typewriter_print("You fail to do what is needed.")
        typewriter_print(" The prirate takes aim at you and smiles.")
        typewriter_print("\n\n\"You should have just followed orders\" he says as he pulls the trigger to end your life")
        new_life()
    

def credits():
    typewriter_print("This game was made by: \n",0.03)
    time.sleep(0.2)
    ascii_art.credit_names() #luke, daniel, rebecca and alex
    time.sleep(2)
    typewriter_print("We hope you enjoyed playing! \n\n",0.03)
    time.sleep(2)


# def replay():
#     answer = typewriter_input("Would you like to play again? Y/N ")
#     answer = answer.upper()
#     # if answer == "Y":
#     #    sci_fi_rpg_story.rpg_beg_1()
#     # if answer == "N":
#     #     print("")

