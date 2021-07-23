from usefulfunctions import typewriter_print, typewriter_input, clearScreen
import time
import rpg_merc
import rpg_nep   
import rpg_plu
import rpg_jup
import ending

mercury_complete_check=False
jupiter_complete_check=False
neptune_complete_check=False
pluto_complete_check=False

def mercury_completion_checker():
    clearScreen()
    global mercury_complete_check
    if mercury_complete_check:
        rpg_merc.merc_story_complete()
    else:
        rpg_merc.merc_story()

def jupiter_completion_checker():
    clearScreen()
    global jupiter_complete_check
    if jupiter_complete_check:
        rpg_jup.Jupiter_complete()
    else:
        rpg_jup.Jupiter_0()

def neptune_completion_checker():
    clearScreen()
    global neptune_complete_check
    if neptune_complete_check:
        rpg_nep.neptune_zone_1_complete()
    else:
        rpg_nep.neptune_zone_1()

def pluto_completion_checker():
    clearScreen()
    global pluto_complete_check
    if pluto_complete_check:
        rpg_plu.pluto_zone1_2()
    else:
        rpg_plu.pluto_zone1()

def wronginput(last_planet):
    typewriter_print("Whoops invalid input...Please try again.")
    time.sleep(1)
    clearScreen()
    ship_hub(last_planet)

def ship_hub(last_planet): ##there is definitely a better way of doing this than all these if statements
    clearScreen()
    typewriter_print("You are back on your ship. You recline in your seat and look at all the available destinations. You have just left "+last_planet+".\n")
    time.sleep(1)
    if mercury_complete_check==True and jupiter_complete_check==True and neptune_complete_check==True and pluto_complete_check==True:
        answer=typewriter_input("The navigation screen blinks on and displays a 5th destination! \nIt seems that after collecting all the items you need the ship's computer has given you the coordinates to the Secret Pirate Base. \nIt reads: 'Your available destinations are 1- Mercury, 2- Jupiter, 3- Neptune, 4- Pluto, 5- Secret Pirate Base' ")
        if last_planet=="Mercury" or last_planet=="mercury":      
            if answer=="1":
                typewriter_print("You exit your ship and get back to exploring Mercury... \n")
                time.sleep(2)
                mercury_completion_checker()
            elif answer=="2":
                typewriter_print("You punch in the coordinates for Jupiter and set off... \n")
                time.sleep(2)
                jupiter_completion_checker()
            elif answer=="3":
                typewriter_print("You punch in the coordinates for Neptune and set off... \n")
                time.sleep(2)
                neptune_completion_checker()
            elif answer=="4":
                typewriter_print("You punch in the coordinates for Pluto and set off... \n")
                time.sleep(2)
                pluto_completion_checker()
            elif answer=="5":
                typewriter_print("You punch in the coordinates for the Secret Pirate Base and set off\n")
                time.sleep(0.5)
                typewriter_print("...",0.5)
                clearScreen()
                ending.ending_zone1()
            else:
                wronginput(last_planet)

        elif last_planet=="Jupiter" or last_planet=="jupiter":      
            if answer=="1":
                typewriter_print("You punch in the coordinates for Mercury and set off... \n")
                time.sleep(2)
                mercury_completion_checker()
            elif answer=="2":
                typewriter_print("You exit your ship and get back to exploring Jupiter... \n")
                time.sleep(2)
                jupiter_completion_checker()
            elif answer=="3":
                typewriter_print("You punch in the coordinates for Neptune and set off... \n")
                time.sleep(2)
                neptune_completion_checker()
            elif answer=="4":
                typewriter_print("You punch in the coordinates for Pluto and set off... \n")
                time.sleep(2)
                pluto_completion_checker()
            elif answer=="5":
                typewriter_print("You punch in the coordinates for the Secret Pirate Base and set off\n")
                time.sleep(0.5)
                typewriter_print("...",0.5)
                clearScreen()
                ending.ending_zone1()
            else:
                wronginput(last_planet)

        elif last_planet=="Neptune" or last_planet=="neptune":       
            if answer=="1":
                typewriter_print("You punch in the coordinates for Mercury and set off... \n")
                time.sleep(2)
                mercury_completion_checker()
            elif answer=="2":
                typewriter_print("You punch in the coordinates for Jupiter and set off... \n")
                time.sleep(2)
                jupiter_completion_checker()
            elif answer=="3":
                typewriter_print("You exit your ship and get back to exploring Neptune... \n")
                time.sleep(2)
                neptune_completion_checker()
            elif answer=="4":
                typewriter_print("You punch in the coordinates for Pluto and set off... \n")
                time.sleep(2)
                pluto_completion_checker()
            elif answer=="5":
                typewriter_print("You punch in the coordinates for the Secret Pirate Base and set off\n")
                time.sleep(0.5)
                typewriter_print("...",0.5)
                clearScreen()
                ending.ending_zone1()
            else:
                wronginput(last_planet)

        elif last_planet=="Pluto" or last_planet=="pluto":      
            if answer=="1":
                typewriter_print("You punch in the coordinates for Mercury and set off... \n")
                time.sleep(2)
                mercury_completion_checker()
            elif answer=="2":
                typewriter_print("You punch in the coordinates for Jupiter and set off... \n")
                time.sleep(2)
                jupiter_completion_checker()
            elif answer=="3":
                typewriter_print("You punch in the coordinates for Neptune and set off... \n")
                time.sleep(2)
                neptune_completion_checker()
            elif answer=="4":
                typewriter_print("You exit your ship and get back to exploring Pluto... \n")
                time.sleep(2)
                pluto_completion_checker()
            elif answer=="5":
                typewriter_print("You punch in the coordinates for the Secret Pirate Base and set off\n")
                time.sleep(0.5)
                typewriter_print("...",0.5)
                clearScreen()
                ending.ending_zone1()
            else:
                wronginput(last_planet)

        else:
            wronginput(last_planet)

    else:
        answer=typewriter_input("The navigation screen blinks on and reads: 'Your available destinations are 1- Mercury, 2- Jupiter, 3- Neptune, 4- Pluto' ")
        if last_planet=="Mars" or last_planet=="mars":
            if answer=="1":
                typewriter_print("You exit your ship and get back to exploring Mercury... \n")
                time.sleep(2)
                mercury_completion_checker()
            elif answer=="2":
                typewriter_print("You punch in the coordinates for Jupiter and set off... \n")
                time.sleep(2)
                jupiter_completion_checker()
            elif answer=="3":
                typewriter_print("You punch in the coordinates for Neptune and set off... \n")
                time.sleep(2)
                neptune_completion_checker()
            elif answer=="4":
                typewriter_print("You punch in the coordinates for Pluto and set off... \n")
                time.sleep(2)
                pluto_completion_checker()
            else:
                wronginput(last_planet)

        elif last_planet=="Mercury" or last_planet=="mercury":      
            if answer=="1":
                typewriter_print("You exit your ship and get back to exploring Mercury... \n")
                time.sleep(2)
                mercury_completion_checker()
            elif answer=="2":
                typewriter_print("You punch in the coordinates for Jupiter and set off... \n")
                time.sleep(2)
                jupiter_completion_checker()
            elif answer=="3":
                typewriter_print("You punch in the coordinates for Neptune and set off... \n")
                time.sleep(2)
                neptune_completion_checker()
            elif answer=="4":
                typewriter_print("You punch in the coordinates for Pluto and set off... \n")
                time.sleep(2)
                pluto_completion_checker()
            else:
                wronginput(last_planet)

        elif last_planet=="Jupiter" or last_planet=="jupiter":      
            if answer=="1":
                typewriter_print("You punch in the coordinates for Mercury and set off... \n")
                time.sleep(2)
                mercury_completion_checker()
            elif answer=="2":
                typewriter_print("You exit your ship and get back to exploring Jupiter... \n")
                time.sleep(2)
                jupiter_completion_checker()
            elif answer=="3":
                typewriter_print("You punch in the coordinates for Neptune and set off... \n")
                time.sleep(2)
                neptune_completion_checker()
            elif answer=="4":
                typewriter_print("You punch in the coordinates for Pluto and set off... \n")
                time.sleep(2)
                pluto_completion_checker()
            else:
                wronginput(last_planet)

        elif last_planet=="Neptune" or last_planet=="neptune":      
            if answer=="1":
                typewriter_print("You punch in the coordinates for Mercury and set off... \n")
                time.sleep(2)
                mercury_completion_checker()
            elif answer=="2":
                typewriter_print("You punch in the coordinates for Jupiter and set off... \n")
                time.sleep(2)
                jupiter_completion_checker()
            elif answer=="3":
                typewriter_print("You exit your ship and get back to exploring Neptune... \n")
                time.sleep(2)
                neptune_completion_checker()
            elif answer=="4":
                typewriter_print("You punch in the coordinates for Pluto and set off... \n")
                time.sleep(2)
                pluto_completion_checker()
            else:
                wronginput(last_planet)

        elif last_planet=="Pluto" or last_planet=="pluto":      
            if answer=="1":
                typewriter_print("You punch in the coordinates for Mercury and set off... \n")
                time.sleep(2)
                mercury_completion_checker()
            elif answer=="2":
                typewriter_print("You punch in the coordinates for Jupiter and set off... \n")
                time.sleep(2)
                jupiter_completion_checker()
            elif answer=="3":
                typewriter_print("You punch in the coordinates for Neptune and set off... \n")
                time.sleep(2)
                neptune_completion_checker()
            elif answer=="4":
                typewriter_print("You exit your ship and get back to exploring Pluto... \n")
                time.sleep(2)
                pluto_completion_checker()
            else:
                wronginput(last_planet)

        else:
            wronginput(last_planet)

def test_complete_checks():
    print("mercury:"+str(mercury_complete_check))
    print("jupiter:"+str(jupiter_complete_check))
    print("neptune:"+str(neptune_complete_check))
    print("pluto:"+str(pluto_complete_check))