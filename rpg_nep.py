import random
import time
import ship_hub
from usefulfunctions import next_page, typewriter_print, typewriter_input, clearScreen, health, lives, new_life

red_open_state=False
blue_open_state=False
green_open_state=False

def neptune_zone_1(): ##done
    typewriter_print("The navigation screen pings and reads: 'You have reached your destination - Neptune'\n")    #print ("you have reached your destination ...")
    typewriter_print("However a beep from the computer lets you know that the magnetic field from the planet has disrupted the ships systems! \nThe ship now cannot take off without an external power source to reboot the computer. You are now stuck here on Neptune.")
    time.sleep(1.5)
    typewriter_print("...",1.5)
    typewriter_print("\n You decide to leave the ship, and you head for a small cave nearby...\n")
    time.sleep(3)
    clearScreen()
    typewriter_print("Inside the small cave there is a door with a screen and keyboard attached to it. \nAbove the door there is a sign which says 'Energy Stone Storage'. \nYou might be able to use the energy stones to start the ship and leave Neptune, but first you need to open this door. \n")
    typewriter_print("The door speaks - 'You must give the correct password to gain access.")
    typewriter_print("\n\nThe password is that which you seek'")
    time.sleep(1.5)
    typewriter_print("...",1.5)
    next_page()
    clearScreen()
    neptune_password()

def neptune_password(): ##done except for maybe a hint?
    password=typewriter_input("\nPlease enter the correct password: ")
    typewriter_print("You have entered: "+password+"\n")   
    password=password.lower() ##makes the input not case sensitive
    if password == "energystone":
        typewriter_print("You have entered the correct password")
        time.sleep(0.5)
        typewriter_print("....",0.5)
        clearScreen()
        neptune_zone_2()    
    elif len(password)!= 11:
        typewriter_print("The password you entered: '"+password+"' is not the right length. The correct password is 12 characters long.")
        neptune_password()
    elif len(password)==11 and password!="energystone":
        typewriter_print("The password you have entered is 11 characters long;")
        time.sleep(1)
        typewriter_print(" however, it was not recognised, please try again")
        time.sleep(0.5)
        typewriter_print("\nHint: The password contains two words with no spaces")
        time.sleep(0.5)
        typewriter_print("...",0.5)
        typewriter_print("\nThe door with the sign reading 'Energy Stone' Storage bellows once again:\n 'The password is that which you seek'")
        time.sleep(0.5)
        neptune_password()

def neptune_zone_2(): #done i think, don't think there are any bugs
    global red_open_state
    global blue_open_state
    global green_open_state
    global health
    global lives
    if red_open_state==False and blue_open_state==False and green_open_state==False: ###statements for all combinations
        typewriter_print("\nThe door swings open and reveals 3 differently coloured crates - red, blue and green\n")
    elif red_open_state==True and blue_open_state==False and green_open_state==False:
        typewriter_print("\nThere is a red, a blue and a green crate. \nYou already have the energy bar from the red crate.\n")
    elif red_open_state==False and blue_open_state==True and green_open_state==False:
        typewriter_print("\nThere is a red, a blue and a green crate. \nThe blue crate is already open and there is an alarm sounding.\n")
    elif red_open_state==False and blue_open_state==False and green_open_state==True:
        typewriter_print("\nThere is a red, a blue and a green crate. \nYou have already used the medical supplies from the green crate.\n")
    elif red_open_state==True and blue_open_state==True and green_open_state==False:
        typewriter_print("\nThere is a red, a blue and a green crate. \nYou already have the energy bar from the red crate and an alarm is sounding from the blue crate.\n")
    elif red_open_state==False and blue_open_state==True and green_open_state==True:
        typewriter_print("\nThere is a red, a blue and a green crate. \nYou have already used the medical supplies from the green crate and there is an alarm sounding from the blue crate.\n")
    elif red_open_state==True and blue_open_state==False and green_open_state==True:
        typewriter_print("\nThere is a red, a blue and a green crate. \nYou already have the energy bar from the red crate and used the medical supplies from the green crate.\n")
    elif red_open_state==True and blue_open_state==True and green_open_state==True:
        typewriter_print("\nAll the crates have been opened. \nYou have everything you need here so you return to your ship. \n")
        neptune_zone_ending()

    stonecolour=typewriter_input("Which crate will you open? ")
    stonecolour=stonecolour.lower()
    if stonecolour == "red": 
        if red_open_state==False:    
            red_open_state=True           
            typewriter_print("You open the red crate and find the energy bar.\n") #condition1
        elif red_open_state==True:
            typewriter_print("You already have retrieved the energy bar")
            time.sleep(0.5)
            typewriter_print("...",0.5)
        red_crate_opened()
    elif stonecolour == "blue":
        if blue_open_state==False:
            blue_open_state=True
            typewriter_print("You open the blue crate but there is no energy bar inside. \nAt the same time a loud alarm starts to ring out! This crate must be a trap! \nSure enough a group of aliens round the corner and start to attack you") #################COMBAT HERE
            health-=30
            if health<=0:
                typewriter_print("The aliens overpower you and start to loot your body. You have died")
                time.sleep(0.5)
                typewriter_print("...",0.5)
                health=100
                lives-=1
                new_life(neptune_zone_2)
            else:
                typewriter_print("The aliens are no match for you, though they did get some good hits in [lose 30 health].")
                neptune_zone_2()
        elif blue_open_state==True:
            typewriter_print("You've already opened this crate but the alarm is still ringing. \nIt hurts your ears to stand this close")
            time.sleep(0.5)
            typewriter_print("...",0.5)
            typewriter_print("\nYou return to the door.\n")
            neptune_zone_2()
    elif stonecolour == "green":
        if green_open_state==False:
            green_open_state=True
            typewriter_print("You open the green crate, but you don't see any energy bars. \nThere are however some medical supplies which you use to heal yourself [You heal yourself for 50 health]") #######################HEAL HERE
            health+=50
            neptune_zone_2()
        elif green_open_state==True:
            typewriter_print("You have already opened the green crate and used all the medical supplies within")
            time.sleep(0.5)
            typewriter_print("...",0.5)
            typewriter_print("\nYou return to the door. \n")
            neptune_zone_2()
    else:
        typewriter_print("Whoops invalid input...Please try again.")
        time.sleep(1)
        clearScreen()
        neptune_zone_2()

def red_crate_opened(): #done i think
    answer=typewriter_input("You are now able to reboot the ship's systems now you have retrieved an energy bar. \nDo you: 1- Want to stay and open the other crates? or 2- Leave and return to the ship? ")
    if answer=="1":
        neptune_zone_2()
    elif answer=="2":
        neptune_zone_ending()
    else:
        typewriter_print("Whoops invalid input...Please try again.")
        time.sleep(1)
        clearScreen()
        red_crate_opened()

def neptune_zone_ending(): #done
    typewriter_print("Back on your ship you connect the computer to the energy bar, and reboot the computer systems.\nOnce the reboot is finished, you disconnect the energy bar and put it away for later use")
    time.sleep(0.5)
    typewriter_print("...",0.5)
    ship_hub.neptune_complete_check=True
    ship_hub.ship_hub("Neptune")

def neptune_zone_1_complete(): #done
    typewriter_print("There is not much else to do here now you have the energy bar so you return to your ship to set a new destination")
    time.sleep(0.5)
    typewriter_print("...",0.5)
    ship_hub.ship_hub("Neptune")
