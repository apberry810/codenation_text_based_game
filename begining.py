from time import sleep
from usefulfunctions import clearScreen, next_page, typewriter_print, typewriter_input, paragraph_counter, new_life
from rpg_variables import health, p, lives, race, INCORRECT_A
import ship_hub

def rpg_beg_1():
    typewriter_print(paragraph_0, 0.03)
    typewriter_print(paragraph_1, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_2, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_3, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_4, 0.03)
    paragraph_counter(int(p))
    rpg_beg_choice_1()

def rpg_beg_choice_1():
    global health
    answer = typewriter_input('Do you [1 = Use your palm print | 2 = Use the retinal scanner] ', 0.03)
    if answer == "1":
        health -= 10
        typewriter_print(paragraph_5,0.03)
        paragraph_counter(int(p))
        typewriter_print(paragraph_5a, 0.03)
        paragraph_counter(int(p))
        typewriter_print(paragraph_5ab, 0.03)
    elif answer == "2":
        typewriter_print(paragraph_5b,0.03)
        paragraph_counter(int(p))
    else:
        typewriter_print(INCORRECT_A, 0.03)
        rpg_beg_choice_1()
    rpg_beg_2()

def rpg_beg_2():
    typewriter_print(paragraph_6, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_6a, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_7, 0.03)
    paragraph_counter(int(p))
    answer = typewriter_input("Please input a destination? ",0.03)
    if answer == "":
        answer = "Nowhere"
    typewriter_print(f"\n\nDestination Locked - Preparing subspace drive jump to {answer}", 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_8, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_8a, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_9, 0.03)
    paragraph_counter(int(p))
    paragraph_counter(int(p))
    next_page()
    clearScreen()
    rpg_beg_3()

def rpg_beg_3():
    typewriter_print(paragraph_10, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_11, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_12, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_13, 0.03)
    paragraph_counter(int(p))
    rpg_beg_choice_2()

def rpg_beg_choice_2():
    global health
    answer = typewriter_input("\n\nWhat do you do? [1 = Shoot first | 2 = Question them] ",0.03)
    if answer == "1":
        health -= 10
        typewriter_print(paragraph_13a, 0.03)
        paragraph_counter(int(p))
        typewriter_print(paragraph_13aa, 0.03)
        paragraph_counter(int(p))
    elif answer == "2":
        typewriter_print('\n"Why have you boarded my ship!?", you scream', 0.03)
    else:
        typewriter_print(INCORRECT_A, 0.03)
        rpg_beg_3()
    typewriter_print(paragraph_13b, 0.03)
    typewriter_print(paragraph_13ba, 0.03)
    typewriter_print(paragraph_13bb, 0.03)
    typewriter_print(paragraph_13c, 0.03)
    typewriter_print(paragraph_13d, 0.03)
    paragraph_counter(int(p))
    typewriter_print(paragraph_14, 0.03)
    paragraph_counter(int(p))
    answer = typewriter_input(paragraph_14a, 0.03)
    if answer == "1":
        typewriter_print(paragraph_14b, 0.03)
        paragraph_counter(int(p))
        typewriter_print(paragraph_14ba, 0.03)
        new_life(rpg_beg_3)
    if answer == "2":
        typewriter_print(paragraph_14bc, 0.03)
        paragraph_counter(int(p))
        typewriter_print(paragraph_15, 0.03)
        paragraph_counter(int(p))
        typewriter_print(paragraph_15a, 0.03)
        paragraph_counter(int(p))
        typewriter_print(paragraph_15b, 0.03)
        paragraph_counter(int(p))
        typewriter_print(paragraph_15ba, 0.03)
        sleep(3)
        next_page()
        ship_hub.ship_hub("Mars")



paragraph_0 = ("You wake up, dazed and confused...with no recollection of what happened, yet something spurs you into action. \"It's time to get moving\", you think to yourself")
paragraph_1 = ("\n\nYou take a moment to adjust to your surroundings. In the distance you see what looks like a giant wave on land.\n\n")
paragraph_2 = ("But it’s getting closer.\n\n")
paragraph_3 = ("At that moment you come to realize 2 things...1: that isn't a wave at all, it’s a martian sandstorm, and 2: You are locked outside of your spaceship..")
paragraph_4 = ("\n\nYou rush to the door of your spaceship to gain access. Your ship's AI speaks to you - “BIOMETRIC AUTHENTICATION REQUIRED”.\n\n")
paragraph_5 = ("\n\nYou attempt to use your palm print as it’s usually the quickest method...however, in the panic your hands are sweating and it doesn’t take the first two times.")
paragraph_5a = ("\n\nA piece of debris from the storm passes by your ship's door and you aren’t able to get inside in time.")
paragraph_5ab = ('\n\nIt catches you on the shoulder [lose - 10 Health]')
paragraph_5b = ('\n\nYou flash your eye against the scanner and it picks up your retinal ID immediately. You gain access in plenty of time before the main body of the storm starts to engulf your ship.')
paragraph_6 = ('\n\nOnce inside you are greeted by your canine travel companion Comet.\n\nHe wags his tail in excitement at first but then immediately recognises your urgency, and runs to his bed to wait patiently.')
paragraph_6a = ("\n\nYou flash him a quick wink to say “good dog”.")
paragraph_7 = ("\n\nThe storm is thicker now. You need to get off this planet before the both of you are toast.\n")
paragraph_8 = ("\n\nYou clip Comet into the canine harness, and strap yourself into the cockpit as the engines fire at full throttle.\n\nThe ship accelerates hard and the cockpit shakes as the heart of the sandstorm batters your ship.")
paragraph_8a = ("\n\nYou manage to break the atmosphere but the damage to your subspace drive, by the storm, means Earth is the only destination you’ll be able to reach now.")
paragraph_9 = ("\n\nYou settle in for the long journey ahead. Even with modern day tech, without a subspace drive it still takes about 3 weeks from mars to earth.")
paragraph_10 = ('[19 DAYS LATER]\n\n\n\nYou are roused from your sleep by Comet growling ever so slightly. You look at him through half shut eyes, “shhh, go to sleep”, you whisper. \nYou try to close your eyes to go back to sleep, but before your eyelids can meet an alarm rings through your entire ship. \n“INTRUDER ALERT” your AI screams at you. “Pirates have boarded!"')
paragraph_11 = ("\n\nYou fly out of bed to your locker. You armour yourself, grab your blaster and load it. You stash Comet in a secret safe room.")
paragraph_12 = ("\n\nYou decide the best course of action is to sprint to the bulkhead and meet them at a choke point.")
paragraph_13 = ('\n\nWhen you get there you see the landing party is massive...too big for a raid on a vessel like this...this is pre-planned, you realise.')
paragraph_13a = ('You waste no time trying to deal with the invaders. Your aim is precise and catching them at the bulkhead was the smart choice. \nYou deal with more than most could, but unfortunately you run out of ammo before they run out of bodies.')
paragraph_13aa = ('\n\nYou prepare yourself for death as you take a shot to the shoulder [lose - 10 Health]...but they cease fire.')
paragraph_13b = ('\n\n"We have not come here to fight. We know you’re creating a weapon. We want it”, one of them says.') 
paragraph_13ba = ('\n\n“How do they know?”, you think to yourself.\n“I have no idea about any weapon”, you say back.')
paragraph_13bb = ('\n\nGesturing to one of the other pirates, he then speaks to you again “Think very carefully about your next answer”. \nWhat you see next creates feelings of intense anger and painful regret...Comet! He is bound by a muzzle and attached to a long pole!')
paragraph_13c = ('\n\nYou are speechless and frozen in anger.')
paragraph_13d = (' The chatty one talks again, “You have seven days to bring us the weapon. Your animal will survive if you comply”.')
paragraph_14 = ("\n\nThey leave")
paragraph_14a = ('\n\nAs soon they do. You sprint to the cockpit [Do you give chase 1 = Yes | 2 = No] ')
paragraph_14b = ('\nYou\'re not thinking straight. All you know is you can’t leave Comet behind. \nYou fly as quick as possible but with the damage to your ship, and the fuel you have left, you don’t get very far.')
paragraph_14ba = ('Eventually your ship stops dead.\n\nYou drift alone in space until all systems shut down...including life support.') 
paragraph_14bc = ('\nDespite almost every fibre of your being screaming at you to give chase, with a damaged ship, no fuel and no ammo, you’ll be less than useless.')
paragraph_15 = ('\n\nYou carry on your journey to Earth...if they want a weapon, that’s exactly what they’ll get.')
paragraph_15a = ('\n\nYou reach Earth and debrief your Captain on everything that happened and explain your plan to use the weapon against the pirates to save Comet.')
paragraph_15b = ('\n\nShe agrees with your course of action and briefs you on the location of the remaining items required to complete the weapon.\n\n“Jupiter to create the ring of power”, “Mercury to forge the special metal Maxion”, “Neptune to collect the bar of energy”, “Pluto to find the Ice crystal”. She then green lights the fast track repair and refueling of your ship.')
paragraph_15ba = ('\n\nThe work is done incredibly fast and before you know you’re walking back to your ship to select a destination.')

rpg_beg_1()
