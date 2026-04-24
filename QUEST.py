"""
    QUEST game
    Author: Joe Scott

    NOTES: To get the program to work, you must install utils from your console!
"""

from time import sleep
import utils
import os
from random import randint

# Menu
os.system('cls')
print(utils.title(" QUEST "))
sleep(3)

# ----- VARIABLES ----- #
# Weapons
sword = 0
Scary_axe = 0

# Trinkets/Items
has_map = 0
Magic_Meal = 0
Stick = 0
Torch = 0
Neck_Cloth = 1 # Spend it to make a torch when you have a stick
rations = 0
shield = 0

# Allies/Hires
Rogue = 0
Chef = 0
Werewolf = False
# Do not change the initial string of Ally
# Ally is responsible for the name of your hired companion
Ally = "To be decided"

# Event Variables
Focus = False
chance = 0
lives = 3
lives_max = 3
if shield == 1:
    lives = 5
    lives_max = 5
enemy_health = 0
# PathChoices keeps track of which paths were correct in the cave IF you have the rogue.
# Combo is Right, Straight, Left, Left
PathChoices = ["Unknown", "Unknown", "Unknown", "Unknown"]

Player_Name = "Knight Guy"

# ---------------- DEBUGGING ---------------- #
DEBUG = False
if DEBUG == True:
    sec = 0
else:
    sec = 3
# ------------------------------------------- #

# ----- CHANCE FUNCTIONS ----- #
# 50%
def chance_50():
    random = randint(1, 2)
    return random

# 75%
def chance_75():
    random = randint(1, 4)
    return random
# ---------------------------- #

# ===================== AREAS/PLACES/MAIN GAME ===================== #
# Start/Setup
def drab_town():
    global sword, has_map, rations, Rogue, Chef, Ally, Player_Name, sec, lives

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    # Cross-platform clear screen (Thanks ChatGPT!)
    os.system('cls' if os.name == 'nt' else 'clear')

    print(utils.UnderLN("Drab Town"))
    sleep(sec)
    print("You wander your way into a quaint little town after taking on a quest\n"
          "issued from the castle by the village smithy, Ivar, to rescue his beloved\n"
          "daughter.")
    sleep(sec)
    print("\nYou are making your way to his hut to talk about the details of the quest.\n"
          "You approach his house and step through his door.")
    sleep(sec)
    print("\nYou can see him drowning away his sorrows at his workbench with fine mead.\n"
          "A bit much, actually. He notices his new visitor, you, gawking and straightens\n"
          "up swiftly.")
    sleep(sec)
    print("\nIVAR: Oh, erm, the mercenary! Pay me no mind, you likely know how a fath'r is\n"
          "without 'is good ol daughter.")
    sleep(sec)
    print("\nIVAR: I don't want to waste any of ye time, or my little lady's time, so we'll get straight\n"
          "to business...")
    sleep(sec)
    Player_Name = input("\nIVAR: First off, what's yer name, lad!:\n\nYour name?: ")
    print(f"\nIVAR: Haha, ye look like a {Player_Name}!")
    sleep(sec)
    print("Enough jesting, I tell the details now...\n")
    sleep(sec)
    print("\nIVAR: Me daught'r has been taken! Flown off with an evil figure I couldn't get a good look at, "
          "dare I say beast!\n"
          "I can tell ye that the jerk flew off towards those strange ruins, in case ye need directions.\n"
          "I'd go chasin' after 'er but years of poundin' metal are rough on a body...")
    sleep(sec)
    print("\nIVAR: You strange-folk and young'uns are after the thrill o' life anyway, so better give\n"
          "the next generation a fightin' chance!")
    sleep(sec)
    print("Alright, no mo' nice words! Get out and save me lass!")
    sleep(sec)
    print("\nYou jump out of your seat eagerly and clank your way out of the door. Time for adventure!\n")
    sleep(sec)

    input("Press any key to proceed: ")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("You make it to the town square and look around. There are shops all around you filled with\n"
          "different odds and ends, and some places that pique your interest; The armory.")
    sleep(sec)
    print("\nBesides the armory, you see a cartography shop (maps), a butcher’s stand, and a nearby pub that\n"
          "other adventurers flood to. You check your pockets... You got enough coin to visit two of\n"
          "these places.")
    sleep(sec)

    shop_stops = 2
    while shop_stops != 0:
        print(f"\nYou have {shop_stops} shop stops left.")
        choice1 = input("\nSo where to? [1. Armory,  2. Cartographer,  3. Butcher,  4. Pub]: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        # ---------- ARMORY ---------- #
        if choice1 == "1":
            if sword == 1:
                print("You know what's better than one sword? Two swords!")
                sleep(sec)
                print("You jog back to the armory and tug on the apron of the smith guy. The armory clerk turns to you and squats down to your level.\n")
                sleep(sec)
                print("\nARMORY CLERK: Little one, even if I did have an extra sword, you would not be able to carry it reasonably... Check out the other places lad!")
                sleep(sec)
                continue

            print("\nYou jog over to the armory and stare at the humongous blade displayed neatly over\n"
                  "the fireplace. You think you might need that sword...")
            sleep(sec)
            print("The smith guy sees you staring at it with childlike wonder and comes up to\n"
                  "you.")
            armory = input("\nARMORY CLERK: Didja want it, son? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
            if armory == "y":
                print("\nARMORY CLERK: Tis yours now! Thank ye for the gold!")
                sleep(sec)
                print("\nYou got the BIG SWORD!")
                sword = 1
                shop_stops -= 1
            else:
                print("\nARMORY CLERK: All good, son! Does plenty good lookin’ pretty for me business!")
            sleep(sec)
            os.system('cls' if os.name == 'nt' else 'clear')

        # ---------- CARTOGRAPHER ---------- #
        elif choice1 == "2":
            if has_map == 1:
                print("\nCARTOGRAPHER: I already gave you my best map! What more do you want?")
                sleep(sec)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            print("\nYou make your way over to the fancy place of scrolls and maps and walk through\n"
                  "the ornate door.")
            sleep(sec)
            print("\nYou go to the counter and ring the little service bell. A skinny bearded man shuffles\n"
                  "towards you.")
            sleep(sec)
            print("\nCARTOGRAPHER: Uh, oh! Hey little guy! What'cha lookin' for?")
            sleep(sec)
            Cartography = input("\nDo you want the ruins map? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
            if Cartography == "y":
                print("\nCARTOGRAPHER: Ah, yes! A great map, but why would you go to the ruins?")
                sleep(sec)
                print("\nCARTOGRAPHER: —uh, pay that question no mind! Here is the map, and I wish you the best of luck!")
                has_map = 1
                shop_stops -= 1
                sleep(sec)
                print("\nYou got the MAP!\n")
            else:
                print("\nCARTOGRAPHER: You sure? You think you can find the way just fine? Well, alright little man! Cya later!")
            sleep(sec)
            os.system('cls' if os.name == 'nt' else 'clear')

        # ---------- BUTCHER ---------- #
        elif choice1 == "3":
            if rations > 0:
                print("\nYou already have enough rations for your trip.")
                sleep(sec)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            print("\nYou wander over to the butcher shop, lured by the scent of cured ham. A gruff man\n"
                  "slaves away at his stand, focused as ever on perfecting his slices.")
            sleep(sec)
            print("\nBUTCHER GUY: Yo, small metal man, lookin' for quality cuts for the journey? No one gets far\n"
                  "without a proper meal!")
            sleep(sec)
            butcher = input("\nDo you want rations? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
            if butcher == "y":
                print("\nBUTCHER GUY: Wise choice, mate! No starving out there, little man!")
                rations = 3
                shop_stops -= 1
                print("\nYou got the RATIONS! [Three uses]")
            else:
                print("\nBUTCHER GUY: If you plan to hunt with your current weapons, I wish you luck!")
            sleep(sec)

        # ---------- PUB ---------- #
        elif choice1 == "4":
            if Rogue == 1 or Chef == 1:
                print(f"\n{Ally}: Seriously? I think I'm enough, don't go back in there...")
                sleep(sec)
                continue

            print("\nYou end up getting stuck in the crowd of the pub. After you find some space, two individuals pique\n"
                  "your interest.")
            sleep(sec)
            print("\nYou can see a hooded figure leaning against the far wall, and a short, noisy chef trying\n"
                  "to convince a group to hire him.")
            sleep(sec)

            hire = input("\nWho do you wanna talk to? [1. Chef,  2. Rogue,  3. Leave]: ")

            # Chef path
            if hire == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nYou shout at the top of your lungs to get the short guys attention. He jumps off a table and pleads to you.")
                sleep(sec)
                print("\n???: O' please, sir knight! I'va been lookin' for someone to take me in! How do people not need a good cook in their quest!?")
                sleep(sec)
                cook = input("\nTake him into your party? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
                if cook == "y":
                    Chef = 1
                    Ally = "TONIO"
                    print(f"\n{Ally}: Many thanks to you, sir knight! If you have any meals you wish to prep, make great use of my culinary abilities!")
                    sleep(sec)
                    print(f"\n{Ally}: And your name is... {Player_Name}? Wonderfully picked! I'ma still call you sir knight though... I Hope you don't mind!")
                    sleep(sec)
                    print(f"\nYou hired {Ally} the Chef!")
                    shop_stops -= 1
                else:
                    print("\nCHEF: Good grief! I gotta change my approach!")
                sleep(sec)
                

            # Rogue path
            elif hire == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nYou swim through the sea of people and make it to the hooded figure in the corner. The voice of a woman breaks the silence...")
                sleep(sec)
                print("???: ... Hey... Did you need something?")
                rogue = input("\nHire the rogue? [y/any key] [WILL EXHAUST A SHOP STOP]: ").lower()
                if rogue == "y":
                    Rogue = 1
                    Ally = "KANRA"
                    print(f"\n???: You want me for a quest? I've been looking for something to do... Thanks.")
                    sleep(sec)
                    print(f"\n???: Someone told me your name is {Player_Name}. Yeah, gotta say it suits you. Let's get going.")
                    print(f"{Ally}: My name is {Ally}, by the way. Nothing more, nothing less.")
                    print(f"\nYou hired {Ally} the Rogue!")
                    shop_stops -= 1
                else:
                    print("\n???: ...You seem to trust yourself, or maybe you lack trust in me. Shouldn’t be surprised...")
                sleep(sec)
            else:
                print("\nYou changed your mind. The crowd here is kind of strange.")
                sleep(sec)
        else:
            print("\nThat’s not a valid choice.")

    # ---------- POST-SHOP DECISION ---------- #
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n---\nAfter getting what you would call the necessities, you notice the sun begins to sink below the horizon. Since you see that the road\n"
          "ahead leads to Wood Woods, You think to yourself...\n")
    sleep(sec)
    sleep_or_embark = input("Should I embark or rest until morning? [1. REST,  2. EMBARK]: ")

    if sleep_or_embark == "1":
        print("\nYou decide that it's probably best to tackle the forest in the daylight. You stay in the nearby inn.")
        if Ally != "To be decided":
            print(f"\nAfter the sun rises, you wake up {Ally} and pack up your little camp on the outskirts of town. Your adventure truly begins!")
        else:
            print(f"\nAfter the sun rises over the horizon, you awaken, pack up, and begin your quest!")
        input("Press any key to proceed: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        wood_woods_day_choice()
    else:
        print("\nThe blacksmith's princess cannot wait! We must make haste! This darkness is nothing!")
        if Rogue == 1 or Chef == 1:
            print(f"\nYou and {Ally} make your way into the forest. Your silhouettes slowly sink into the darkness...")
        else:
            print("\nYou summon your courage and press on into the dark of the woods alone.")
            sleep(sec)
        input("Press any key to proceed: ")
        wood_woods_night()

    # Return necessary variables (May be redundant now)
    if Ally != "To be decided":
        if Rogue == 1:
            return Rogue, sword, has_map, rations
        elif Chef == 1:
            return Chef, sword, has_map, rations
    else:
        return sword, has_map, rations

# ========== WOOD WOODS [DAY] ========== #
# Make choice Map/Trail
def wood_woods_day_choice():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    # Title
    print(utils.UnderLN("\nWood Woods"))
    sleep(sec)
    # If you have a map, this gets to run.
    if has_map == 1:
        print("\nYou pull out the map that you got from the cartographer and think to yourself...")
        choice = int(input("Use your map or follow trail?: [1: Map / 2: Off Trail]: "))
        if choice == 1:
            print("\nYou decide that it would be foolish to even consider going outside the map's directions and follow it's directions.")
            sleep(sec)
            input("\nPress anything to proceed: ")
            wood_woods_day_has_map()
        elif choice == 2:
            print("You decide to see where the off-roads take you.")
            sleep(sec)
            input("\nPress anything to proceed: ")
            wood_woods_day_trail()
    else:
        # This runs if you don't have a map.
        print("\nSince there was no obvious path and you have no map, you decided to just keep moving into the forest blindly...")
        sleep(sec)
        input("\nPress anything to proceed: ")
        wood_woods_day_trail()
    
# Starting Wood Woods with a map
def wood_woods_day_has_map():
    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")
    
    print("\nBecause of your wise purchase of a map, you're able to know where the bad areas of the forest are and the direct path to the"
          " cave is. Just as things seem to go well, a tall knight in a black surcoat stands on a bridge, staring off into the distance.")
    sleep(sec)
    print("At his feet lies those who apparently fell before him. You wonder how he did such a thing, as this knight is missing an arm"
          " and a leg...")
    sleep(sec)
    print("You attempt to pass him, but he hops in your way with his one leg.")
    sleep(sec)
    print("\n???: NONE SHALL PASS...")
    sleep(sec)
    print("\nYou stare at the man confuzzled. Who is he to tell you what to do with only two limbs?")
    sleep(sec)
    # This choice is intentional!
    input("What do you do? [1: Push him over / 2: Push him over]: ")
    print("This man is clearly not gonna move. You point out a bird in the sky and he turns around.")
    sleep(sec)
    print("\n???: Where!?")
    sleep(sec)
    print("\nYou walk up to him and simply topple him over. He cannot pick himself up.")
    sleep(sec)
    print("\n???: Ah, DANG IT! I'm invincible I'll have you know! We'll meet again!")
    sleep(sec)
    print("\nYou walk off feeling a little guilty about what you've done, but your quest waits for no one!")
    sleep(sec)
    print("\nYou make it to the mouth of the cave. With all the strangeness of the forest you've been told of, you feel"
          " like you got through this very well. The map follows into the mouth of the cave, so you summon your courage and disappear"
          " into the darkness of the path ahead...")
    sleep(sec)
    input("\nPress enter to proceed: ")
    cave()

# Start of Wood Woods
def wood_woods_day_trail():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    print("As you walk amongst the forest aimlessly, you find a nice looking stick and think about"
          " how you may need a torch if it gets dark out.\n You found some space for it in your pack and"
          " kept on your merry way.")
    # You got a stick!
    Stick = 1
    sleep(sec)
    print("\nHours have passed, none you have kept track of, but suddenly, stifling the peace is a growl"
          " of a large creature...")
    sleep(sec)
    input("Press enter to proceed: ")
    wood_woods_lumberjack() 

# Initiate the lumberjack
def wood_woods_lumberjack():
    global sword, has_map, rations, Rogue, Chef, Ally, lives, Player_Name, sec, Stick, Neck_Cloth
    os.system('cls' if os.name == 'nt' else 'clear')

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    # If you have the rogue:
    if Rogue == 1:
        print(f"\n{Ally}: Hey, {Player_Name}, that isn't a monster behind those shrubs... It's a man. I'll let you decide how we play this out.")

    sleep(sec)
    choice = int(input("\nWhatever it is, it hasn't noticed you... How should you proceed? [1. Investigate / 2. Sneak away / 3. Throw your stick at it]: "))
    # Investigate the noise.
    if choice == 1:
        print("\nYou decide that you need to see what this is. Your armor should hold you up fine if it comes down to a fight.")
        sleep(sec)
        print("You breathe in... and then out, and swipe the brush away, and...")
        sleep(sec)
        print("\nCRASH!")
        sleep(sec)
        print("\nThe tree ahead hammers the earth right in front of you. The grunting is from no beast, but rather a hulking man in plaid;"
              " A lumber jack!")
        sleep(sec)
        print("\nLUMBERJACK: Stubborn pine! took ye long enough to come down!")
        sleep(sec)
        print("\nHe turns around to fell the next pine and sees your small frame, fixated on the fallen tree.")
        sleep(sec)
        wood_woods_lumberjack_intro()
        
    # Sneak by the creature.
    if choice == 2:
        if Rogue == 1:
            print("\nYou decide not to draw attention to yourself. Who knows if this guy is truly trustworthy. Let's just not bother...")
            sleep(sec)
            input("Press enter to proceed: ")
            cave()
        else:
            print("\nYou decide it's best not to play with fire. No need to make any silly decisions when your full focus should be to your quest.")
            sleep(sec)
            input("Press enter to proceed: ")
            cave()
    
    # Throw your stick at the sound!
    if choice == 3:
        print("\nYour intrusive thoughts get the better of you. You take out the stick from your pack and stare at it for a moment.")
        sleep(sec)
        print("You throw it straight past the bush and you hear a momentarily satisfying thunk. [-1 STICK]")
        Stick -= 1
        sleep(sec)
        print("\n???: OW! the hell!?")
        sleep(sec)
        print("\nA huge, plaid, burly man jumps out of the bush on all-fours. He looks very irritated.")
        sleep(sec)
        print("\nYou begin to panick. In the breif moment of thought that you have, you...\n")
        sleep(sec)
        # Menu Loop
        while True:
            choice4 = input("\n [1.           Run ]\n [2. Beg for mercy ]\n [3.         Fight ]\nWhat will you do: ")
            # Draw your sword
            if choice4 == "3":
                enemy_health = 2
                print("\nYou reach for your blade in a hurry and try to find a stance to fight.")
                sleep(sec)
                print("Without a chance to think, he swings his axe sideways!")
                sleep(sec)
                while True:
                    chance = chance_50()
                    if chance == 1:
                        print("He swings at you and...")
                        sleep(sec)
                        print("\nYou manage to duck quickly and strike the hulking man in the temple with the pommel of your sword.")
                        sleep(sec)
                        enemy_health -= 1
                        if enemy_health > 0:
                            print("\nHe's not done! The man turns back around and barrels toward you!")
                            sleep(sec)
                            continue
                    else:
                        print("\nWHACK!")
                        lives -= 1
                        sleep(sec)
                        print(f"\nHe struck you in the side for a chunk of your life! You hit the ground hard, wheezing.")
                        print(f"HEALTH REMAINING: {lives}/3")
                        sleep(sec)
                        if lives <= 0:
                            print("\nYou were struck too many times... You tried to reach for your sword in with your last breath, but you felt a strong grip grab the back of your armor.")
                            sleep(sec)
                            print("\nBefore you could stop the brute, a strong punch bent through your armor and...\neverything went black...")
                            sleep(sec)
                            input("Press enter to proceed")
                            game_over()
                            break
                        else:
                            print("As you attempt to get up, he bounds toward you again!")
                            sleep(sec)
                    if enemy_health <= 0:
                        print("\nHe slides against the forest floor five feet behind you, out cold. You breathe a sigh of relief.")
                        sleep(sec)
                        # if Chef is in your party
                        try:
                            if Chef == 1:
                                print(f"\n{Ally}: Scary fight, sir knight, {Player_Name}, glad you made it in one piece...")
                                sleep(sec)
                                print(f"\n{Ally}: Take this real quick! It's a salve, something my mama came up with!")
                                if lives < 3:
                                    lives += 1
                                sleep(sec)
                                print("\nIt's a hastily put together first-aid kit. Very convenient!")
                                sleep(sec)
                                print(f"HEALTH: {lives}/3")
                                sleep(sec)
                        except:
                            pass
                        # if Rogue is in your party
                        try:
                            if Rogue == 1:
                                print(f"\n{Ally}: Good fighting, {Player_Name}. As well as you did, I think this could have gone better...")
                                sleep(sec)
                                print(f"{Ally}: As much as I loathe talking or trusting people, even I would try talking your way out sometimes.")
                                sleep(sec)
                                print("You feel silly, but at least you've got something of a friend to give suggestions to.")
                                sleep(sec)
                        except:
                            pass
                        
                        
                        choice5 = input("\nAfter your adrenaline finally settles, you see that he dropped his axe... Take it? [1. Yes / 2. No]: ")
                        if choice5 == "1":
                            print("\nIt looks quite strong... Given your quest, you're sure something out there will forgive you for taking it.")
                            sleep(sec)
                            Scary_axe = 1
                            print("\nYou got the SCARY AXE!")
                            sleep(sec)
                        else:
                            print("\nYou don't take what you don't absolutely need. You don't need this axe, he does.")
                            sleep(sec)
                            print("Maybe you can make ammends after this is all over.")
                            sleep(sec)
                        
                        print("\nYou brush yourself off, stretch, and keep moving forward despite the ever approaching night.")
                        sleep(sec)
                        input("Press enter to continue: ")
                        wood_woods_night()
                        break

            # Run away
            if choice4 == "1":
                print("\nFear seizes your heart and without a thought, you run in any direction that is away from the monster man.")
                print("\nAfter running for until you couldn't hear his swearing anymore, you finally stop to breathe and recover from that sprint.")
                print("\nYou then turn your head up and see that the cave is right before your eyes. You've heard that, although perilous, this"
                    " is one of the better ways to get to the ruins. Why waste this opportunity perfectly placed in front of you?")
                cave()
                break

            # Beg for mercy
            elif choice4 == "2":
                print("\nYou fall to the floor and curl up into a ball. You cry out to the man not to hurt you!")
                print("\nLUMBERJACK: Oh geez, sorry about that! Ahem-")
                wood_woods_lumberjack_intro()
                break
            
            # Exception Handling
            else:
                print("\n! Please choose a number from 1 to 3 !\n")
                continue
    return lives

# Meet the lumberjack
def wood_woods_lumberjack_intro():
    global sword, has_map, rations, Rogue, Chef, Ally, Player_Name, sec, Stick, Neck_Cloth
    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")
    
    print("\nLUMBERJACK: Hey little guy! What are you doing out here? Nobody comes through here for a frolick besids the foolish!")
    sleep(sec)
    choice2 = int(input("\nHow do you answer? [1. I'm out to save the blacksmith's daughter! / 2. None of your business!]: "))
    # I'm saving Ivar's Daughter!
    if choice2 == 1:
        print("\nLUMBERJACK: You mean old man Ivar? You could have used his name! He and I go way back. He used to bug me all the"
                " time about lumber and charcoal for his forge!")
        sleep(sec)
        print("\nLUMBERJACK: Besides that, his daughter isn't safe? I find that hard to believe... She's a fighter with a good noggin"
                " on her shoulders, she wouldn't just be kidnapped, there's gotta be something more to this.")
        sleep(sec)
        print("\nLUMBERJACK: My best tip for you, lad is to also think rationally. You may not have to resort to fighting with good chattin'"
                " skills.")
        sleep(sec)
    # I'm keeping my secrets!
    else:
        print("\nLUMBERJACK: All good buddy! When it's just you and man-eating creatures out here, a good word from a stranger is"
                " entertaining!")
        sleep(sec)
    if has_map == 1:
        print("Say little man, you need any pointers for these parts? I do live here.")
        sleep(sec)
        choice3 = int(input("\n[1. Yeah, can you read my map! / 2. I'm ok, thanks!]"))
        if choice3 == 1:
            print("\nLUMBERJACK: Yeah, give it here!")
            sleep(sec)
            print("\nHe takes the map from you and squats down so you can see where he is pointing to. It's all making sense now!")
            sleep(sec)
            print("\nLUMBERJACK: Thanks for giving ol' redbeard a chance to help! Hope we meet again some other day, if nothing bad happens!")
            sleep(sec)
            print("\nYou leave with a clear image in your head of the path you must take! No take the wrong turns for this guy!")
            sleep(sec)
            input("\nEnter any button to continue: ")
            # You travel to the ruins this way, skipping the cave!
            ruins()
        if choice3 == 2:
            print("\nLUMBERJACK: I like your confidence, metal man! A good spirit will take you far!")
            sleep(sec)
            print("\nLUMBERJACK: Take care, don't get yourself hurt!")
            sleep(sec)
            print("\nYou are not sure how you feel about being so protective of your quest, but you can rest well knowing you will not"
                    " likely not be followed.")
            sleep(sec)
            print("\nAs night begins to fall, you approach the foot of a cave. Supposedly, this cave is the best way to the ruins and you have"
                " no better choice than to trust this.")
            sleep(sec)
            input("\nEnter any button to continue: ")
            # Enter the cave
            cave()

    print("\nLUMBERJACK: It's good to meet friendly faces once in a while, you take care little guy!")
    sleep(sec)
    print("\nYou wave back at him and keep following the path, knowing you made a good friend today.")
    sleep(sec)
    print("\nYou approach the cave after a nice walk through the woods and meet the ominous mouth of the cave. It seems to be the only way to"
          " the ruins, so without wasting any more time, you summon your courage and disappear into the darkness forward.")
    sleep(sec)
    input("\nPress any button to continue: ")
    cave()

# ========== WOOD WOODS [NIGHT] ========== #
# Start Wood Woods at Night
def wood_woods_night():
    global sword, has_map, rations, Rogue, Chef, Ally, Player_Name, sec, Stick, Neck_Cloth
    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    os.system('cls' if os.name == 'nt' else 'clear')
    print(utils.UnderLN("\nWood Woods Night"))
    sleep(sec)
    print("It's dark out. Very dark out, but nonetheless your spirits remain high. As far as you can see, it's just tall trees\n"
          "and ever-spanning hills. One of these directions leads to the cave you heard about. Supposedly, through the cave is the\n"
          "way to the ruins. You've got no choice but to follow that tip for right now, since anything could happen to Ivar's daughter.\n")
    sleep(sec)
    if has_map == 1:
        print("\nUnfortuantely, you can't see the contents of your map... If only you had some kind of light.")
    else:
        print("\nEven if you had a map, it's too dark to see it.")
    sleep(sec)
    if Stick != 1:
        print("Amidst your walking, you stumble upon a nice stick. You manage to find room in\n"
              "your bag for it and stash it away.")
    sleep(sec)
    print("\nGiven it's night, it might not be a bad idea to light a torch. You could use your neck scarf\n"
          "to add kindling to the stick... but you would lose it.")
    # Make a torch spending your only neck scarf
    choice = input("\nMake and set a torch alight? [1. Yes / 2. No ][ Uses Neck Scarf]: ")
    if choice == "y" or choice == "1":
        # TORCH ROUTE
        Neck_Cloth = 0
        Stick -= 1
        print("\nNot being able to see would hinder your ability to navigate. Why try to get through this\n"
              "darkness when you have this opportunity?")
        sleep(sec)
        input("\nPress anything to proceed: ")
        wood_woods_night_torch()
    else:
        # DARK ROUTE
        print("\nYou trust your gut. You believe that you can navigate through these woods with your internal\n"
              "compass. You steady yourself and then press forward.")
        sleep(sec)
        input("\nPress anything to proceed: ")
        wood_woods_night_dark()

# Torch Route
def wood_woods_night_torch():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The trail goes ever on. You try to count the time that's passed since you embarked from camp but with\n"
          "the sun down, there's no point in trying.")
    sleep(sec)
    print("As long as you keep moving, you know you're making progress.")

    # === DIALOGUE PORTION === #
    if Ally != "To be decided":
        print("You begin to stare at your feet, like your head was getting heavy. You're tired from what seems to be\n" 
              "'hiker's hypnosis'.\n")
        sleep(sec)
        print(f"Just before you begin to sleep-walk, {Ally} taps on your helmet.")
        # ========== Dialogue Time! =========== #
        if Rogue == 1:
            print(f"{Ally}: Hey, keep your head up man. You're awfully relaxed in these woods, do you not know what's\n"
                  "out there?\n")
            sleep(sec)
            print(f"{Ally}: Whether you do or not, stay alert. Would it helped you if we talked about something?\n")
            choice = input("How do you respond? [1. Yes / 2. No]: ")
            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nYou heave your head up and nod weakly.")
                sleep(sec)
                print(f"\n{Ally}: Hmm, ok... How about... I ask you a question first, and then you ask me something?")
                sleep(sec)
                print(f"{Ally}: I probably should have asked this sooner, but who really are you?")
                sleep(sec)
                print("\nYou pause for a moment... who exactly are you? You had not thought about that much. Regardless, you\n"
                      "try to explain to her...")
                sleep(sec)
                input("Press Enter to proceed: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                # PLAYER CHARACTER INTRODUCTION
                print(f"\nYou tell her that you are {Player_Name} heiled from the Kingdom of Wynveld. You were a former\n"
                      "member of the kings direct guards, but after seeing the injustice of the monarchy and the crimes\n"
                      "they let fly in favor of petty matters, you left to become a mercenary for the people and live a\n"
                      "transient life on the road, wherever the road takes you.")
                sleep(sec)
                print("\nYou also mention to her that you like a nicely seasoned steak, playing chess, and long walks on\n"
                "the beach.")
                sleep(sec)
                print(f"\n{Ally}: What a life, man. I respect the decision to help other people and take charge of things\n"
                      "that bother you.")
                sleep(sec)
                print(f"{Ally}: Oh, and, do you take off the helmet ever? Can I see your face?")
                sleep(sec)
                print("You promptly shake your head no. The helmet never comes off.")
                sleep(sec)
                print(f"\n{Ally}: OK! ok... I won't ask again... Now I'm a rogue of my word, ask me something, {Player_Name}.")
                sleep(sec)
                while True:
                    choice2 = input("\n[1. Who are you? ]\n[2. What do you like? ]\n[3. Do you know the blacksmith's daughter?]\n"
                                    "How do you respond:")
                    # Who are you?
                    if choice2 == "1":
                        print(f"\n{Ally}: You already know my name is Kanra. Besides that, I ended up getting separated from my family\n"
                              "in a skirmish with the Kolutz raiders with no idea how my family faired. I was only 8 years old... I learned\n"
                              "everything I know for the rogue path from previous adventures and others who made all the mistakes before me.\n")
                        sleep(sec)
                        print(f"{Ally}: I can't think of anything else I want to add... and no, I don't want to talk about those damn Kolutz scum...")
                        break
                    # What do you like?
                    elif choice2 == "2":
                        print(f"\n{Ally}: Silly question, but it's fair you ask.")
                        sleep(sec)
                        print(f"\n{Ally}: I like to hunt, I love animals, and I adore adventure. I'm not proud to admit it, but I also have a habit\n"
                              "of being a pickpocket from time to time. No worries, it's just the wealthy I take from. It's not just for me though,\n"
                              "Many others would find better use of their coin and trinkets than they would have the patience to find for themselves")
                        sleep(sec)
                        print(f"\n{Ally}: Now, being a pickpocket is a theif thing, not a rogue thing, let me get that straight... Although,\n"
                              "I suppose that makes me a theif. Ehh, whatever.")
                        break
                    # Do you know the blacksmith's daughter
                    elif choice2 == "3":
                        print(f"\n{Ally}: Old Ivar's daughter? Not super well, but I can remember one of the rare times that man used her actual name.\n"
                              "I believe it was Gwyndolin? I doubt that will be useful to you, but whatever.")
                        sleep(sec)
                        print(f"\n{Ally}: Before she disappeared, I can remember a time she threw a hose at Ivar and he panicked like he had a snake on\n"
                              "his shoulders. Couldn't forget that.")
                        break
                    # Handle incorrect input
                    else:
                        print(f"\n{Ally}: Uh... Could you repeat that?")
                        sleep(sec)
                        continue
                
                print(f"\n{Ally}: I know this whole chat we had was to keep your sleepy head awake, but I enjoyed myself... Thanks...")
 
            else:
                print(f"{Ally}: No pressure... just be alert then. I know you didn't hire me to babysit you.")

        if Chef == 1:
            print(f"{Ally}: Mr. Knight! Don't doze off, are you mad!? I can't fend for myself out here if you fall asleep!")
            sleep(sec)
            print(f"{Ally}: Oh, I got a solution for you! Let's chat. That'll keep you on your feet. I haven't even asked who you\n"
                  "are. You should introduce yourself. Now!")
            sleep(sec)
            print("\nYou pause for a moment... who exactly are you? You had not thought about that much.")
            sleep(sec)
            input("Press Enter to proceed: ")
            # PLAYER CHARACTER INTRODUCTION
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nYou tell him that you are {Player_Name} heiled from the Kingdom of Wynveld. You were a former\n"
                   "member of the kings direct guards, but after seeing the injustice of the monarchy and the crimes\n"
                   "they let fly in favor of petty matters, you left to become a mercenary for the people and live a\n"
                   "transient life on the road, wherever the road takes you.")
            sleep(sec)
            print("\nYou also mention to him that you like a nicely seasoned steak, playing chess, and long walks on\n"
                  "the beach.")
            sleep(sec)
            print(f"\n{Ally}: Good greif, What a hard lifestyle to give up! I can tell you this, it's so much livelier on\n"
                  "an adventure. So much to learn and do, but most importantly, nothing like completing a quest and relaxing\n"
                  "on the earnings! I'd argue it keeps ya humble!")
            sleep(sec)
            print(f"\n{Ally}: Also, is it fate that a steak lover teams up with a cook? I'd like to think so, ho-ho!")
            sleep(sec)
            print(f"\n{Ally}: Ok, I've asked the questions, surely your burning for an answer too! Ask me something Sir Knight!")
            sleep(sec)
            while True:
                choice = input("\n[1. Who are you? ]\n[2. Why the chef life? ]\n[3. What's your favourite food? ]\nWhat do you ask him?: ")
                # Who are you?
                if choice == "1":
                    print(f"\n{Ally}: I've already told you my name is Tonio, but if you need to hear my exquisite background, Let me\n"
                          "start with this;")
                    sleep(sec)
                    print(f"\n{Ally}: I've been a cook for Drab Town as long as I can remember, but I was done working with potatos,\n"
                          "Veggies and commoner food... I wanted to find richer things... Things that perfect even the blandest thing...\n"
                          "By traveling with you, I have hope of finding the 'All-Seasoning'... One seasoning to rule them all and in\n"
                          "consumerism bind them. I never want to taste dubious meals again!")
                    sleep(sec)
                    print(f"\n{Ally}: I've found two of the seasonings desired so far... Namely, Grinded up garlic, salt, and one more\n"
                          "ingredient I shan't name, because a good chef never reveals his secret!")
                    sleep(sec)
                    break
                # Why the chef life?
                elif choice == "2":
                    print(f"\n{Ally}: I come from a far land where a manhood was deemed worthy if said man could cook better than the others.\n"
                          "The place I call home is known as the Caiman Peninsula. I still miss the taste of salt on a spit roasted sea bass...")
                    sleep(sec)
                    print(f"\n{Ally}: I'm after the all seasoning... I have two of the necessary ingredients for it but I missing just one more...\n")
                    sleep(sec)
                    print(f"\n{Ally}: What? No, I can't tell you what it is! A good chef keeps his secret ingredient a secret!")
                    break
                # What's your favourite food?
                elif choice == "3":
                    print(f"\n{Ally}: Are you kidding me? I couldn't decide what my favourite food is! I love it all!")
                    sleep(sec)
                    print(f"\n{Ally}: However, there is one thing I wouldn't mind having again. I think that would be the giant buffet kebab I had\n"
                          "before I left home for spices, herbs, seasoning, and whatnot...")
                    sleep(sec)
                    break
                # Handle exception
                else:
                    print(f"\n{Ally}: What was that, Mr. Sir Knight Guy?")
                    continue
            
            print(f"\n{Ally}: Good chat, Sir {Player_Name}! I'll never hesitate to talk about the finest thing in life... Food!")

    print("\nAs time progressed, you began to notice that there was more leaves crunching than there should be when you walked.\n"
          "Everytime you stopped to check for it, there was no more sound. You felt a chill run down your spine.")
    sleep(sec)
    if Rogue == 1:
        print(f"\n{Ally}: I hear it too... I'm almost positive we are being stalked, but I have no idea who or what it could be...\n"
              "Proceed carefully...")
    while True:
        choice = input("You can't ignore it anymore. How do you act?: [1. Investigate the noise / 2. Keep moving quietly ]: ")
        # Investigate
        if choice == "1":
            print("If it's kept track of you thus far, you might as well stand your ground. You clench your fists and force\n"
                  "yourself forward.")
            sleep(sec)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("...")
            sleep(sec)
            print("...")
            sleep(sec)
            print("... Suddenly, you notice a silhouette grow over your torch light...")
            sleep(sec)
            print("You turn slowly, and your heart sinks to your gut...")
            sleep(sec)
            print("From behind, a werewolf towers over you, right in front of where your standing. Waiting for sudden movement.")
            sleep(sec)
            input("Press Enter to proceed: ")
            wood_woods_wolf()
            break

        # Keep moving
        elif choice == "2":
            print("You think you should just keep moving... the more miles we move the further we are from the potential threat.")
            sleep(sec)
            print("After ages on the road, you finally make it to the cave. It's truly incredible you managed to get through the\n"
                  "night unscathed.")
            sleep(sec)
            if rations != 0:
                print("You check your pack, but notice that your rations are gone. Maybe that weird sound took it. Whatever the\n"
                "circumstance is, you're glad that it's the rations that are gone and not yourself.")
                sleep(sec)
            cave()
            break
        else:
            print("\nThat's not a choice!\n")
            continue

# Fight method
def wood_woods_wolf():
    global sword, Scary_axe, rations, Rogue, Chef, Ally, Player_Name, lives, sec, Stick, Werewolf

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    while True:
        # Menus/Actions
        # ================ You have weapon/or Stick ================ #
        if sword == 1 or Scary_axe == 1 and Stick > 0:
            # Menu
            choice = input(
                "\n[1. Run ]"
                "\n[2. Plead ]"
                "\n[3. Fight ]"
                "\n[4. Throw Stick ]"
                "\nTension is high. what do you do: ")

            # Actions
            if choice == "1":
                print("\nWithout wasting a second, you bolt past the beast and attempt to run away.")
                sleep(sec)
                print("Unfortunately, what was once stalking you is now bounding towards you. It gaining on you!")
                sleep(sec)
                chance = chance_75()
                if chance == 1:
                    print("\nIn your mad dash for survival, you notice the cave just ahead, across a cliff. With no better way\n"
                          "out of this predicament, you summon your courage...")
                    sleep(sec)
                    print("\nYou leap forward, tuck, and roll back onto your feet on the other side!")
                    sleep(sec)
                    print("\nThe beast stops dead in it's tracks... It looks down at the pit, and back at you mournfully as it\n"
                          "turns back into the woods.")
                    sleep(sec)
                    print("Good god, your alive!")
                    sleep(sec)
                    print("\nWhen you regain your breath, you turn to face the cave. Your destination! It even has a road sign\n"
                          "that says it leads to the ruins!")
                    if Ally != "To be decided":
                        print(f"{Ally}: There it is, {Player_Name}! There's the cave!")
                    sleep(sec)
                    input("\nPress Enter to proceed: ")
                    cave()
                else:
                    print("\nCRUNCH!!!")
                    lives -= 1
                    sleep(sec)
                    print(f"\nHEALTH REMAINING: {lives}/3")

                    # If you ran out of lives (Death)
                    if lives == 0:
                        sleep(sec)
                        print("\nYou no longer have the strength to pry the beast off of you. As you begin lose consciousness, the monster\n"
                        "drags your fading body away into the woods...")
                        sleep(sec)
                        input("\nPress Enter: ")
                        game_over()
                    
                    # You survive the strike
                    print("\nThe monster bit into your side! You smack the wolf in the nose and it reels back. You take\n"
                          "your chance to stand back up!")
                    sleep(sec)
                    input("\nPress Enter:")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            elif choice == "2":
                print("\nFear gripped too tightly in your chest and all you could think of doing was curling up and\n"
                "pleading for your safety.")
                sleep(sec)
                print("\nInstead of being shown mercy, you were promptly returned to the food chain for your lack of will\n"
                "to defend yourself...")
                input("\nPress Enter: ")
                game_over()
            elif choice == "3":
                print("\nYou instinctivly draw your weapon and swing hastily!")
                sleep(sec)
                chance = chance_50()
                if chance == 1:
                    print("\nYou slice the beast in the gut and it reels back and runs into the forest. Clearly, it made\n"
                    "a mistake picking a fight with you!")
                    sleep(sec)
                    print("\nYou look around. Dazed after the fight and notice that the skirmish of battle has brought you to the cave.")
                    sleep(sec)
                    if Rogue == 1:
                        print(f"\n{Ally}: Geez! Are you ok!? Remember when I said do you know what's out there? Be careful!")
                        sleep(sec)
                        print(f"\n{Ally}: Well, besides all that, look! It's the cave!")
                        sleep(sec)
                    input("\nPress Enter to proceed: ")
                    cave()
                else:
                    print("\nYou missed! The werewolf shoves you down to the ground. You can hardly breathe.")
                    lives -= 1
                    sleep(sec)

                    # If you run out of lives
                    if lives == 0:
                        print("\nYou no longer have the strength to pry the beast off of you. As you begin lose consciousness, the monster\n"
                        "drags your fading body away into the woods...")
                        sleep(sec)
                        input("\nPress Enter: ")
                        game_over()

                    # If you survived
                    print("You roll back to your feet and face the beast again!")
                    sleep(sec)
                    continue
            elif choice == "4":
                print("\nYou take the stick out of your bag slowly, raise it above your head, and then throw it.")
                sleep(sec)
                print("\nThe beast is instantly distracted and bounds after the stick. That was easy.")
                sleep(sec)
                print("Just as you begin to walk away, the werewolf brings the stick back. Oh no.")
                sleep(sec)
                print("\n   The Werewolf joins your party\n")
                Werewolf = True
                sleep(sec)
                input("Press Enter to proceed: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("After tossing the stick a few times, the beast urges you to follow it. You can't convince it\n"
                "to leave you alone, so you follow it.")
                sleep(sec)
                print("\n... What do you know!? It's the cave! The werewolf took you to the cave you searched for! Let's waste\n"
                      "no time, let's keep going!")
                sleep(sec)
                if Rogue == 1:
                    print(f"\n{Ally}: What the hell!? No one is going to believe this...")
                    sleep(sec)
                input("Press Enter to proceed: ")
                cave()
            else:
                print("\nWrong number input... try that again!\n")
                continue
        # ==================== You have sword/axe =================== #
        elif Scary_axe or sword == 1:
            # Menu
            choice = input(
                "\n[1. Run ]"
                "\n[2. Plead ]"
                "\n[3. Fight ]"
                "\nTension is high. what do you do: ")
            
            # Actions
            if choice == "1":
                print("\nWithout wasting a second, you bolt past the beast and attempt to run away.")
                sleep(sec)
                print("Unfortunately, what was once stalking you is now bounding towards you. It gaining on you!")
                sleep(sec)
                chance = chance_75()
                if chance == 1:
                    print("\nIn your mad dash for survival, you notice the cave just ahead, across a cliff. With no better way\n"
                          "out of this predicament, you summon your courage...")
                    sleep(sec)
                    print("\nYou leap forward, tuck, and roll back onto your feet on the other side!")
                    sleep(sec)
                    print("\nThe beast stops dead in it's tracks... It looks down at the pit, and back at you mournfully as it\n"
                          "turns back into the woods.")
                    sleep(sec)
                    print("Good god, your alive!")
                    sleep(sec)
                    print("\nWhen you regain your breath, you turn to face the cave. Your destination! It even has a road sign\n"
                          "that says it leads to the ruins!")
                    if Ally != "To be decided":
                        print(f"{Ally}: There it is, {Player_Name}! There's the cave!")
                    sleep()
                    input("\nPress Enter to proceed: ")
                    cave()
                else:
                    print("\nCRUNCH!!!")
                    lives -= 1
                    sleep(sec)
                    print(f"\nHEALTH REMAINING: {lives}/3")

                    # If you ran out of lives (Death)
                    if lives == 0:
                        sleep(sec)
                        print("\nYou no longer have the strength to pry the beast off of you. As you begin lose consciousness, the monster\n"
                        "drags your fading body away into the woods...")
                        sleep(sec)
                        input("\nPress Enter: ")
                        game_over()
                    
                    # You survive the strike
                    print("\nThe monster bit into your side! You smack the wolf in the nose and it reels back. You take\n"
                          "your chance to stand back up!")
                    sleep(sec)
                    input("\nPress Enter:")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue

                pass
            elif choice == "2":
                print("\nFear gripped too tightly in your chest and all you could think of doing was curling up and\n"
                "pleading for your safety.")
                sleep(sec)
                print("\nInstead of being shown mercy, you were promptly returned to the food chain for your lack of will\n"
                "to defend yourself...")
                input("\nPress Enter: ")
                game_over()
            elif choice == "3":
                print("\nYou instinctivly draw your weapon and swing hastily!")
                sleep(sec)
                chance = chance_50()
                if chance == 1:
                    print("\nYou slice the beast in the gut and it reels back and runs into the forest. Clearly, it made\n"
                    "a mistake picking a fight with you!")
                    sleep(sec)
                    print("\nYou look around. Dazed after the fight and notice that the skirmish of battle has brought you to the cave.")
                    sleep(sec)
                    if Rogue == 1:
                        print(f"\n{Ally}: Geez! Are you ok!? Remember when I said do you know what's out there? Be careful!")
                        sleep(sec)
                        print(f"\n{Ally}: Well, besides all that, look! It's the cave!")
                        sleep(sec)
                    input("\nPress Enter to proceed: ")
                    cave()
                else:
                    print("\nYou missed! The werewolf shoves you down to the ground. You can hardly breathe.")
                    lives -= 1
                    sleep(sec)

                    # If you run out of lives
                    if lives == 0:
                        print("\nYou no longer have the strength to pry the beast off of you. As you begin lose consciousness, the monster\n"
                        "drags your fading body away into the woods...")
                        sleep(sec)
                        input("\nPress Enter: ")
                        game_over()

                    # If you survived
                    print("You roll back to your feet and face the beast again!")
                    sleep(sec)
                    continue
            else:
                print("\nWrong number input... try that again!\n")
                continue
        # ===================== You have rations ===================== #
        elif Stick != 0:
            # Menu
            choice = input(
                "\n[1. Run ]"
                "\n[2. Plead]"
                "\n[3. Throw Stick ]"
                "\nTension is high. what do you do: ")
            
            # Actions
            if choice == "1":
                print("\nWithout wasting a second, you bolt past the beast and attempt to run away.")
                sleep(sec)
                print("Unfortunately, what was once stalking you is now bounding towards you. It gaining on you!")
                sleep(sec)
                chance = chance_75()
                if chance == 1:
                    print("\nIn your mad dash for survival, you notice the cave just ahead, across a cliff. With no better way\n"
                          "out of this predicament, you summon your courage...")
                    sleep(sec)
                    print("\nYou leap forward, tuck, and roll back onto your feet on the other side!")
                    sleep(sec)
                    print("\nThe beast stops dead in it's tracks... It looks down at the pit, and back at you mournfully as it\n"
                          "turns back into the woods.")
                    sleep(sec)
                    print("Good god, your alive!")
                    sleep(sec)
                    print("\nWhen you regain your breath, you turn to face the cave. Your destination! It even has a road sign\n"
                          "that says it leads to the ruins!")
                    if Ally != "To be decided":
                        print(f"\n{Ally}: There it is, {Player_Name}! There's the cave!")
                    sleep(sec)
                    input("\nPress Enter to proceed: ")
                    cave()
                else:
                    print("\nCRUNCH!!!")
                    lives -= 1
                    sleep(sec)
                    print(f"\nHEALTH REMAINING: {lives}/3")

                    # If you ran out of lives (Death)
                    if lives == 0:
                        sleep(sec)
                        print("\nYou no longer have the strength to pry the beast off of you. As you begin lose consciousness, the monster\n"
                        "drags your fading body away into the woods...")
                        sleep(sec)
                        input("Press Enter: ")
                        game_over()
                    
                    # You survive the strike
                    print("\nThe monster bit into your side! You smack the wolf in the nose and it reels back. You take\n"
                          "your chance to stand back up!")
                    sleep(sec)
                    input("\nPress Enter:")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            elif choice == "2":
                print("\nFear gripped too tightly in your chest and all you could think of doing was curling up and\n"
                "pleading for your safety.")
                sleep(sec)
                print("\nInstead of being shown mercy, you were promptly returned to the food chain for your lack of will\n"
                "to defend yourself...")
                input("\nPress Enter: ")
                game_over()
            elif choice == "3":
                print("\nYou take the stick out of your bag slowly, raise it above your head, and then throw it.")
                sleep(sec)
                print("\nThe beast is instantly distracted and bounds after the stick. That was easy.")
                sleep(sec)
                print("Just as you begin to walk away, the werewolf brings the stick back. Oh no.")
                sleep(sec)
                print("\n   The Werewolf joins your party\n")
                Werewolf = True
                sleep(sec)
                input("Press Enter to proceed: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("After tossing the stick a few times, the beast urges you to follow it. You can't convince it\n"
                "to leave you alone, so you follow it.")
                sleep(sec)
                print("\n... What do you know!? It's the cave! The werewolf took you to the cave you searched for! Let's waste\n"
                      "no time, let's keep going!")
                sleep(sec)
                if Rogue == 1:
                    print(f"\n{Ally}: What the hell!? No one is going to believe this...")
                    sleep(sec)
                input("Press Enter to proceed: ")
                cave()
            else:
                print("\nWrong number input... try that again!\n")
                continue
        # =============== You don't have special items =============== #
        else:
            # Menu
            choice = input(
                "\n[1. Run ]"
                "\n[2. Plead]"
                "\nTension is high. what do you do: ")
            
            # Actions
            if choice == "1":
                print("\nWithout wasting a second, you bolt past the beast and attempt to run away.")
                sleep(sec)
                print("Unfortunately, what was once stalking you is now bounding towards you. It gaining on you!")
                sleep(sec)
                chance = chance_75()
                if chance == 1:
                    print("\nIn your mad dash for survival, you notice the cave just ahead, across a cliff. With no better way\n"
                          "out of this predicament, you summon your courage...")
                    sleep(sec)
                    print("\nYou leap forward, tuck, and roll back onto your feet on the other side!")
                    sleep(sec)
                    print("\nThe beast stops dead in it's tracks... It looks down at the pit, and back at you mournfully as it\n"
                          "turns back into the woods.")
                    sleep(sec)
                    print("Good god, your alive!")
                    sleep(sec)
                    print("\nWhen you regain your breath, you turn to face the cave. Your destination! It even has a road sign\n"
                          "that says it leads to the ruins!")
                    if Ally != "To be decided":
                        print(f"{Ally}: There it is, {Player_Name}! There's the cave!")
                    sleep(sec)
                    input("\nPress Enter to proceed: ")
                    cave()
                else:
                    print("\nCRUNCH!!!")
                    lives -= 1
                    sleep(sec)
                    print(f"\nHEALTH REMAINING: {lives}/3")

                    # If you ran out of lives (Death)
                    if lives == 0:
                        sleep(sec)
                        print("\nYou no longer have the strength to pry the beast off of you. As you begin lose consciousness, the monster\n"
                        "drags your fading body away into the woods...")
                        sleep(sec)
                        input("\nPress Enter: ")
                        game_over()
                    
                    # You survive the strike
                    print("\nThe monster bit into your side! You smack the wolf in the nose and it reels back. You take\n"
                          "your chance to stand back up!")
                    sleep(sec)
                    input("\nPress Enter:")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            elif choice == "2":
                print("\nFear gripped too tightly in your chest and all you could think of doing was curling up and\n"
                "pleading for your safety.")
                sleep(sec)
                print("\nInstead of being shown mercy, you were promptly returned to the food chain for your lack of will\n"
                "to defend yourself...")
                input("\nPress Enter: ")
                game_over()
            else:
                print("\nWrong number input... try that again!\n")
                continue
        return lives, Scary_axe, Stick

# Night Route
def wood_woods_night_dark():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")
    
    print("The trail goes ever on. You try to count the time that's passed since you embarked from camp but with\n"
          "the sun down, there's no point in trying.")
    sleep(sec)
    print("As long as you keep moving, you know you're making progress.")
    # === DIALOGUE PORTION === #
    if Ally != "To be decided":
        print("You begin to stare at your feet, like your head was getting heavy. You're tired from what seems to be\n" 
              "'hiker's hypnosis'.\n")
        sleep(sec)
        print(f"Just before you begin to sleep-walk, {Ally} taps on your helmet.")
        # ========== Dialogue Time! =========== #
        if Rogue == 1:
            print(f"{Ally}: Hey, keep your head up man. You're awfully relaxed in these woods, do you not know what's\n"
                  "out there?\n")
            sleep(sec)
            print(f"{Ally}: Whether you do or not, stay alert. Would it helped you if we talked about something?\n")
            choice = input("How do you respond? [1. Yes / 2. No]: ")
            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nYou heave your head up and nod weakly.")
                sleep(sec)
                print(f"\n{Ally}: Hmm, ok... How about... I ask you a question first, and then you ask me something?")
                sleep(sec)
                print(f"{Ally}: I probably should have asked this sooner, but who really are you?")
                sleep(sec)
                print("\nYou pause for a moment... who exactly are you? You had not thought about that much. Regardless, you\n"
                      "try to explain to her...")
                sleep(sec)
                input("Press Enter to proceed: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                # PLAYER CHARACTER INTRODUCTION
                print(f"\nYou tell her that you are {Player_Name} heiled from the Kingdom of Wynveld. You were a former\n"
                      "member of the kings direct guards, but after seeing the injustice of the monarchy and the crimes\n"
                      "they let fly in favor of petty matters, you left to become a mercenary for the people and live a\n"
                      "transient life on the road, wherever the road takes you.")
                sleep(sec)
                print("\nYou also mention to her that you like a nicely seasoned steak, playing chess, and long walks on\n"
                "the beach.")
                sleep(sec)
                print(f"\n{Ally}: What a life, man. I respect the decision to help other people and take charge of things\n"
                      "that bother you.")
                sleep(sec)
                print(f"{Ally}: Oh, and, do you take off the helmet ever? Can I see your face?")
                sleep(sec)
                print("You promptly shake your head no. The helmet never comes off.")
                sleep(sec)
                print(f"\n{Ally}: OK! ok... I won't ask again... Now I'm a rogue of my word, ask me something, {Player_Name}.")
                sleep(sec)
                while True:
                    choice2 = input("\n[1. Who are you? ]\n[2. What do you like? ]\n[3. Do you know the blacksmith's daughter?]\n"
                                    "How do you respond:")
                    # Who are you?
                    if choice2 == "1":
                        print(f"\n{Ally}: You already know my name is Kanra. Besides that, I ended up getting separated from my family\n"
                              "in a skirmish with the Kolutz raiders with no idea how my family faired. I was only 8 years old... I learned\n"
                              "everything I know for the rogue path from previous adventures and others who made all the mistakes before me.\n")
                        sleep(sec)
                        print(f"{Ally}: I can't think of anything else I want to add... and no, I don't want to talk about those damn Kolutz scum...")
                        break
                    # What do you like?
                    elif choice2 == "2":
                        print(f"\n{Ally}: Silly question, but it's fair you ask.")
                        sleep(sec)
                        print(f"\n{Ally}: I like to hunt, I love animals, and I adore adventure. I'm not proud to admit it, but I also have a habit\n"
                              "of being a pickpocket from time to time. No worries, it's just the wealthy I take from. It's not just for me though,\n"
                              "Many others would find better use of their coin and trinkets than they would have the patience to find for themselves")
                        sleep(sec)
                        print(f"\n{Ally}: Now, being a pickpocket is a theif thing, not a rogue thing, let me get that straight... Although,\n"
                              "I suppose that makes me a theif. Ehh, whatever.")
                        break
                    # Do you know the blacksmith's daughter
                    elif choice2 == "3":
                        print(f"\n{Ally}: Old Ivar's daughter? Not super well, but I can remember one of the rare times that man used her actual name.\n"
                              "I believe it was Gwyndolin? I doubt that will be useful to you, but whatever.")
                        sleep(sec)
                        print(f"\n{Ally}: Before she disappeared, I can remember a time she threw a hose at Ivar and he panicked like he had a snake on\n"
                              "his shoulders. Couldn't forget that.")
                        break
                    # Handle incorrect input
                    else:
                        print(f"\n{Ally}: Uh... Could you repeat that?")
                        sleep(sec)
                        continue
                
                print(f"\n{Ally}: I know this whole chat we had was to keep your sleepy head awake, but I enjoyed myself... Thanks...")
 
            else:
                print(f"{Ally}: No pressure... just be alert then. I know you didn't hire me to babysit you.")
        if Chef == 1:
            print(f"{Ally}: Mr. Knight! Don't doze off, are you mad!? I can't fend for myself out here if you fall asleep!")
            sleep(sec)
            print(f"{Ally}: Oh, I got a solution for you! Let's chat. That'll keep you on your feet. I haven't even asked who you\n"
                  "are. You should introduce yourself. Now!")
            sleep(sec)
            print("\nYou pause for a moment... who exactly are you? You had not thought about that much.")
            sleep(sec)
            input("Press Enter to proceed: ")
            # PLAYER CHARACTER INTRODUCTION
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nYou tell him that you are {Player_Name} heiled from the Kingdom of Wynveld. You were a former\n"
                   "member of the kings direct guards, but after seeing the injustice of the monarchy and the crimes\n"
                   "they let fly in favor of petty matters, you left to become a mercenary for the people and live a\n"
                   "transient life on the road, wherever the road takes you.")
            sleep(sec)
            print("\nYou also mention to him that you like a nicely seasoned steak, playing chess, and long walks on\n"
                  "the beach.")
            sleep(sec)
            print(f"\n{Ally}: Good greif, What a hard lifestyle to give up! I can tell you this, it's so much livelier on\n"
                  "an adventure. So much to learn and do, but most importantly, nothing like completing a quest and relaxing\n"
                  "on the earnings! I'd argue it keeps ya humble!")
            sleep(sec)
            print(f"\n{Ally}: Also, is it fate that a steak lover teams up with a cook? I'd like to think so, ho-ho!")
            sleep(sec)
            print(f"\n{Ally}: Ok, I've asked the questions, surely your burning for an answer too! Ask me something Sir Knight!")
            sleep(sec)
            while True:
                choice = input("\n[1. Who are you? ]\n[2. Why the chef life? ]\n[3. What's your favourite food? ]\nWhat do you ask him?: ")
                # Who are you?
                if choice == "1":
                    print(f"\n{Ally}: I've already told you my name is Tonio, but if you need to hear my exquisite background, Let me\n"
                          "start with this;")
                    sleep(sec)
                    print(f"\n{Ally}: I've been a cook for Drab Town as long as I can remember, but I was done working with potatos,\n"
                          "Veggies and commoner food... I wanted to find richer things... Things that perfect even the blandest thing...\n"
                          "By traveling with you, I have hope of finding the 'All-Seasoning'... One seasoning to rule them all and in\n"
                          "consumerism bind them. I never want to taste dubious meals again!")
                    sleep(sec)
                    print(f"\n{Ally}: I've found two of the seasonings desired so far... Namely, Grinded up garlic, salt, and one more\n"
                          "ingredient I shan't name, because a good chef never reveals his secret!")
                    sleep(sec)
                    break
                # Why the chef life?
                elif choice == "2":
                    print(f"\n{Ally}: I come from a far land where a manhood was deemed worthy if said man could cook better than the others.\n"
                          "The place I call home is known as the Caiman Peninsula. I still miss the taste of salt on a spit roasted sea bass...")
                    sleep(sec)
                    print(f"\n{Ally}: I'm after the all seasoning... I have two of the necessary ingredients for it but I missing just one more...\n")
                    sleep(sec)
                    print(f"\n{Ally}: What? No, I can't tell you what it is! A good chef keeps his secret ingredient a secret!")
                    break
                # What's your favourite food?
                elif choice == "3":
                    print(f"\n{Ally}: Are you kidding me? I couldn't decide what my favourite food is! I love it all!")
                    sleep(sec)
                    print(f"\n{Ally}: However, there is one thing I wouldn't mind having again. I think that would be the giant buffet kebab I had\n"
                          "before I left home for spices, herbs, seasoning, and whatnot...")
                    sleep(sec)
                    break
                # Handle exception
                else:
                    print(f"\n{Ally}: What was that, Mr. Sir Knight Guy?")
                    continue
            
            print(f"\n{Ally}: Good chat, Sir {Player_Name}! I'll never hesitate to talk about the finest thing in life... Food!")
            sleep(sec)
            print("Through the peace of night, you made it to the cave with no incident.")
            sleep(sec)
            input("Press enter to proceed: ")
            cave()

# ========== CAVE ========== #
# Cave
def cave():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    print(utils.UnderLN("The Cave"))
    sleep(sec)
    print("\nThe darkness in front of you grows, the light from behind recedes. At this point in the quest, the path is a mystery.")
    sleep(sec)
    if has_map == 1:
        print("The path on the map leads to the ruins, but unfortunately does not list the cave directions, only that you go through here.")
        sleep(sec)
        print("Not very helpful...")
        sleep(sec)
    else:
        print("Whatever way you go, from here it's about trusting your gut.")
        sleep(sec)
    print("\nAfter walking some distance in the cave, you've arrive at a three way fork, unfortunately. Initially, there are no giveaways for\n"
          "which trail leads to the other sides...")
    sleep(sec)
    print("\nLooks like we are going to have to guess the right path.")
    sleep(sec)
    if Rogue == 1:
        print(f"\nKANRA: Hey, not sure if I'll be too much help now, but I will try to keep tabs on the path we take as we move. Best thing to do\n"
              "for now is pick a path and find the way from there.")
        sleep(sec)
    input("\nPress enter to proceed: ")
    cave1()

# Cave fight
def caveFight():
    global sword, rations, Chef, Ally, Player_Name, sec, Stick, lives, Neck_Cloth, enemy_health
    os.system('cls' if os.name == 'nt' else 'clear')

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")
    
    print("...")
    sleep(sec)
    print("\nSomething is wrong... You're being followed.")
    sleep(sec)
    print("\nYou turn around and to your surprise, it's a skeleton brandishing a curved sword!")
    sleep(sec)
    print("\n???: FoOLIsH kNiGhT, HaVe ThEE cOmE tO ExPaNd oUR StAsH oF wEAlTh? HAnd iT OvEr!")
    sleep(sec)
    if Werewolf == True:
        print("\nThe beast you tamed from the forest walks to your side, determined to prove to you it's power.\n"
        "Looks like you're not fighting alone!")
        sleep(sec)
    input("Press Enter to proceed: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n- = [ FIGHT ] = -")
    enemy_health = 2
    # ========== FIGHT LOOP ============ #
    while True:
        # ===== YOUR TURN ===== #
        # If you have a neck scarf and a stick
        if Neck_Cloth > 0 and Stick > 0:
            action = input("\n    [1. Attack   ]\n    [2. Run      ]\n    [3. Light Torch]\nWhat will you do?: ")
            # Attack
            if action == "1":
                if sword == 1 or Scary_axe == 1:
                    crit = chance_75()
                    if crit == 4:
                        print("\nYou draw your blade calmly. As the skeleton jumps at you for a lethal blow...")
                        sleep(sec)
                        print("\n CLANG!")
                        enemy_health = 0
                        sleep(sec)
                        print("\nYou parry the sword of the evil being away from its hand and return a fierce, shattering strike that\n"
                              "pulverizes it instantly.")
                        sleep(sec)
                        print("\nAnd just like that, the battle is over.")
                        sleep(sec)
                        print("\n- = [ YOU WIN ] = -")
                        input("Press enter to proceed: ")
                        break
                    elif crit > 1:
                        print("\nYou swipe your weapon vigorously at the monster!")
                        sleep(sec)
                        enemy_health -= 1
                        print("\nYou struck it in the rib!")
                        sleep(sec)
                        if enemy_health > 0:
                            print(f"\nSKELETON HEALTH: {enemy_health}")
                            sleep(sec)
                            print("\nThe skeleton still stands!")
                            sleep(sec)
                        else:
                            print("\nThe figure takes a few steps back...")
                            sleep(sec)
                            print("Suddenly, it begins to turn to dust.")
                            sleep(sec)
                            print("\n???: GnnNNnngh... dOn't tHInk tHIs Is OVer, kNIGht! tHEre ArE mORe oF ME!")
                            sleep(sec)
                            print("\n- = [ YOU WIN ] = -")
                            input("Press enter to proceed: ")
                            break
                    else:
                        print("\nYou swing your weapon vigorously at the monster!")
                        sleep(sec)
                        print("\nYou... Missed!")
                        sleep(sec)
                else:
                    attack = chance_75()
                    if attack > 1:
                        print("You throw a punch vigorously at the monster!")
                        sleep(sec)
                        print("\nYou struck it in the skull!")
                        enemy_health -= 1
                        sleep(sec)
                        if enemy_health > 0:
                            print(f"\nSKELETON HEALTH: {enemy_health}")
                            sleep(sec)
                            print("\nThe skeleton still stands!")
                            sleep(sec)
                        else:
                            print("\nThe figure takes a few steps back...")
                            sleep(sec)
                            print("Suddenly, it begins to turn to dust.")
                            sleep(sec)
                            print("\n???: GnnNNnngh... dOn't tHInk tHIs Is OVer, kNIGht! tHEre ArE mORe oF ME!")
                            sleep(sec)
                            print("\n- = [ YOU WIN ] = -")
                            input("Press enter to proceed: ")
                            break
                    else:
                        print("You swing your arm vigorously at the monster!")
                        sleep(sec)
                        print("You... Missed!")
                        sleep(sec)
            # Run
            elif action == "2":
                print(f"You do NOT want to mess around with that scimitar. You attempt to flee...")
                sleep(sec)
                chance = chance_50()
                if chance == 1:
                    print("\nYou struggle against the dark cave walls, but manage to lose the skeleton!\n"
                    "You can still hear his greedy taunts as you disappear into the dark.")
                    break
                else:
                    print("\nBut you run into a wall. You seem to struggle to find the way out in this darkness.")
                    sleep(sec)
            # Torch attack
            elif action == "3":
                print("\nYou're not sure how this will work, but you frantically light your torch.")
                Neck_Cloth -= 1
                Stick -= 1
                sleep(sec)
                print("\nImmediately, the skeleton reels back from the light, dragging itself along the walls in search of shade.")
                sleep(sec)
                print("\n???: AUGH! nOt tHE lIGHt! cURSe yOu, cRAFtY mEtAl cAN!")
                sleep(sec)
            # Misinput
            else:
                print("\n ! That's not an action !\n")
                continue
        # No special items
        else:
            action = input("\n    [1. Attack   ]\n    [2. Run      ]\nWhat will you do?: ")
            # Attack
            if action == "1":
                if sword == 1 or Scary_axe == 1:
                    crit = chance_75()
                    if crit == 4:
                        print("\nYou draw your blade calmly. As the skeleton jumps at you for a lethal blow...")
                        sleep(sec)
                        print("\n CLANG!")
                        enemy_health = 0
                        sleep(sec)
                        print("\nYou parry the sword of the evil being away from its hand and return a fierce, shattering strike that\n"
                              "pulverizes it instantly.")
                        sleep(sec)
                        print("\nAnd just like that, the battle is over.")
                        sleep(sec)
                        print("\n- = [ YOU WIN ] = -")
                        input("Press enter to proceed: ")
                        break
                    elif crit > 1:
                        print("\nYou swipe your weapon vigorously at the monster!")
                        sleep(sec)
                        print("\nYou struck it in the rib!")
                        enemy_health -= 1
                        sleep(sec)
                        if enemy_health > 0:
                            print(f"\nSKELETON HEALTH: {enemy_health}")
                            sleep(sec)
                            print("\nThe skeleton still stands!")
                            sleep(sec)
                        else:
                            print("\nThe figure takes a few steps back...")
                            sleep(sec)
                            print("\nSuddenly, it begins to turn to dust.")
                            sleep(sec)
                            print("\n???: GnnNNnngh... dOn't tHInk tHIs Is OVer, kNIGht! tHEre ArE mORe oF ME!")
                            sleep(sec)
                            print("\n- = [ YOU WIN ] = -")
                            input("Press enter to proceed: ")
                            break
                    else:
                        print("\nYou swing your weapon vigorously at the monster!")
                        sleep(sec)
                        print("\nYou... Missed!")
                        sleep(sec)
                else:
                    attack = chance_75()
                    if attack > 1:
                        print("You throw a punch vigorously at the monster!")
                        sleep(sec)
                        print("\nYou struck it in the skull!")
                        enemy_health -= 1
                        sleep(sec)
                        if enemy_health > 0:
                            print(f"\nSKELETON HEALTH: {enemy_health}")
                            sleep(sec)
                            print("\nThe skeleton still stands!")
                            sleep(sec)
                        else:
                            print("\nThe figure takes a few steps back...")
                            sleep(sec)
                            print("Suddenly, it begins to turn to dust.")
                            sleep(sec)
                            print("\n???: GnnNNnngh... dOn't tHInk tHIs Is OVer, kNIGht! tHEre ArE mORe oF ME!")
                            sleep(sec)
                            print("\n- = [ YOU WIN ] = -")
                            input("Press enter to proceed: ")
                            break
                    else:
                        print("You swing your arm vigorously at the monster!")
                        sleep(sec)
                        print("You... Missed!")
                        sleep(sec)
            # Run
            elif action == "2":
                print(f"\nYou do NOT want to mess around with that scimitar. You attempt to flee...")
                sleep(sec)
                chance = chance_50()
                if chance == 1:
                    print("\nYou struggle against the dark cave walls, but manage to lose the skeleton!\n"
                    "You can still hear his greedy taunts as you disappear into the dark.")
                    break
                else:
                    print("\nBut you run into a wall. You seem to struggle to find the way out in this darkness.")
                    sleep(sec)
            # Misinput
            else:
                print("\n ! That's not an action !\n")
                continue

        # ===== ENEMY TURN ===== #
        print("The greedy figure grips the shaft of his blade with two hands and dances with it towards you!")
        sleep(sec)
        chance = chance_50()
        if chance == 1:
            print("\nCHINK!")
            sleep(sec)
            if lives > 0:
                lives -= 1
                print(f"\nThe bastard nicked you in several places! [HEALTH REMAINING: {lives}/3]")
                sleep(sec)
            elif lives <= 0:
                print("\nTwo many cuts... You struggle to keep yourself upright.")
                sleep(sec)
                print("\nWhen you meet the evil creatures eye sockets, he glares back and smirks, no remorse in what he's about to do.")
                sleep(sec)
                print("\nA heavy blow to the side of the head knocks you out cold, Now lost to the darkness...")
                sleep(sec)
                game_over()
        else:
            print("\nSwift reflexes bring your sword up to meet the blade of the skeleton. You block the attack!")
            sleep(sec)

        # ===== WEREWOLF'S TURN ===== #
        if Werewolf == True:
            print("\nThe werewolf bares it's fangs and lunges at the skeleton!")
            sleep(sec)
            chance = chance_75()
            if chance > 1:
                print("\nThe wolf tears through the skeleton easily. Given that this opponent is free advertising for bones, you're not\n"
                      "really that surprised.")
                enemy_health = 0
                sleep(sec)
                print("\nYou walk over to its head and pat it, asking it whose a good boy.")
                sleep(sec)
                print("\n- = [ YOU WON ] = -")
                input("Press enter to proceed: ")
                break
            else:
                print("\nThe skeleton is able to barely dive away from the giant wolf.")
                sleep(sec)
                print("The being is still fixated on you!")
                sleep(sec)
    # Heal if you took damage
    if rations > 0 and lives < 3:
        if Chef == 1:
            print(f"\nTONIO: Good god what a ghastly sight! Sir Knight {Player_Name}! I can already see that you took\n"
                  "a good hit from that wicked blade, let me help you my good sir!")
            sleep(sec)
            rations -= 1
            print(f"\nUsing your ration [{rations}/3 rations] he creates a healing stew. You're not sure how, but anything is better\n"
            "than bleeding out. You are thankful.")
            sleep(sec)
            lives = 3
            print(f"\nYOUR HEALTH: {lives}/3")
            sleep(sec)
        else:
            print(f"\nYou do what you can to make your rations heal you. You feel a bit better filling your stomach up after a\n" \
                f"long journey. [{rations}/3 rations]")
            sleep(sec)
            lives += 1
            print(f"\nYOUR HEALTH: {lives}/3")
            sleep(sec)
            rations -= 1
        input("\nPress enter to continue: ")
    return Stick, Neck_Cloth, lives, enemy_health, rations    

# Cave wrong way
def caveWrong():
    global PathChoices
    os.system('cls' if os.name == 'nt' else 'clear')
    print("...")
    sleep(sec)
    print("\nOh no... You've been here before.")
    sleep(sec)
    print("\nIt's the start of the cave. You'll need to take a different path than that one to find the way out.")
    sleep(sec)
    if Rogue == 1 and "Right" in PathChoices:
        print(f"\nKANRA: Hey {Player_Name}, I've been keeping track of what seems to bring us closer to the exit. So far,\n"
              f"{PathChoices} seems to be the route of progress.")
    else:
        pass
    cave1()
    return PathChoices

def cave1():
    global PathChoices
    choice = input("\n    [1. Left    ]\n    [2. Straight]\n    [3. Right   ]\nSo which way forward?: ")
    while True:
        if choice == "1" or choice == "2":
            chance = chance_75()
            if chance == 4:
                caveFight()
                caveWrong()
                return
            else:
                caveWrong()
                return
        if choice == "3":
            PathChoices[0] = "Right"
            chance = chance_75()
            if chance == 4:
                caveFight()
            else:
                pass
            break
        else:
            print("\nThat's not a direction!")
            sleep(sec)
            continue
    cave2()
    return PathChoices

def cave2():
    global PathChoices
    os.system('cls' if os.name == 'nt' else 'clear')
    print("...")
    sleep(sec)
    print("\nYou feel like you've made progress.")
    sleep(sec)
    print("\nYou think you might be hearing a stream and the air rushing through the cave, but you can't pin\n"
    "where it's from.")
    sleep(sec)
    
    choice = input("\n    [1. Left    ]\n    [2. Straight]\n    [3. Right   ]\nSo which way forward?: ")
    while True:
        if choice == "1" or choice == "3":
            chance = chance_75()
            if chance == 4:
                caveFight()
                caveWrong()
                return
            else:
                caveWrong()
                return
        if choice == "2":
            PathChoices[1] = "Straight"
            chance = chance_75()
            if chance == 4:
                caveFight()
            else:
                pass
            break
        else:
            print("\nThat's not a direction!")
            sleep(sec)
            continue
    cave3()
    return PathChoices

def cave3():
    global PathChoices
    os.system('cls' if os.name == 'nt' else 'clear')
    print("...")
    sleep(sec)
    print("\nYou feel like you've made more progress.")
    sleep(sec)
    print("\nThat's gotta be the stream! you can also hear the air traveling better. Only problem is to the right appears to\n"
          "be where the stream is coming from and to the left is where the wind blows.")
    sleep(sec)
    choice = input("\n    [1. Left    ]\n    [2. Straight]\n    [3. Right   ]\nSo which way forward?: ")
    while True:
        if choice == "2" or choice == "3":
            chance = chance_75()
            if chance == 4:
                caveFight()
                caveWrong()
                return
            else:
                caveWrong()
                return
        if choice == "1":
            PathChoices[2] = "Left"
            chance = chance_75()
            if chance == 4:
                caveFight()
            else:
                pass
            break
        else:
            print("\nThat's not a direction!")
            sleep(sec)
            continue
    cave4()
    return PathChoices

def cave4():
    global PathChoices
    os.system('cls' if os.name == 'nt' else 'clear')
    print("...")
    sleep(sec)
    print("\nYou feel like you've made progress.")
    sleep(sec)
    print("\nMuch to your dismay, the sounds suddenly stopped. You're not sure why, but let's make this choice count.")
    sleep(sec)
    
    choice = input("\n    [1. Left    ]\n    [2. Straight]\n    [3. Right   ]\nSo which way forward?: ")
    while True:
        if choice == "2" or choice == "3":
            chance = chance_75()
            if chance == 4:
                caveFight()
                caveWrong()
                return
            else:
                caveWrong()
                return
        if choice == "1":
            PathChoices[3] = "Left"
            chance = chance_75()
            if chance == 4:
                caveFight()
            else:
                pass
            break
        else:
            print("\nThat's not a direction!")
            sleep(sec)
            continue
    os.system('cls' if os.name == 'nt' else 'clear')
    print("...")
    sleep(sec)
    print("\nYou feel like these caves never end. This might have been a mistake. What are you doing here!? Why would Ivar's\n"
          "daughter even think about going through here!?")
    sleep(sec)
    print("\nJust as you begin to lose hope...")
    sleep(sec)
    print("\nThe floor crumbles below you!")
    sleep(sec)
    print("\nThis was, however, not a far fall.")
    sleep(sec)
    print("\nAs you got up, you first noticed the crisp smell of the air from the trees, then the light, and\n"
          "finally, the ruins looming in front of you!")
    sleep(sec)
    print("You did it!  You actually did it!")
    sleep(sec)
    input("Press enter to move on: ")
    ruins()
    return PathChoices

# ========== RUINS ========== #
# Ruins
def ruins():
    # variables we work with
    global sword, rations, Rogue, Chef, Ally, Player_Name, sec, Scary_axe

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    os.system('cls' if os.name == 'nt' else 'clear')
    print(utils.UnderLN("Ruins"))
    sleep(sec)
    print("When you walk out of the cave exit, you are hit with a pleasant breeze. As your eyes adjust to the light, you\n"
          "see before the great hill you stand on the ruins you've heard so much about just below.")
    sleep(sec)
    print("It's bigger than you thought, spanning eight miles out where you can see a decrepit fortress in the distance.\n"
          "You would hate to jump to conclusions, but that is likely where they took Ivar's daughter.")
    sleep(sec)
    if Rogue == 1:
        print(f"\n{Ally}: I doubt I need to tell you this coming to this point, but I would keep my guard up if I was you.\n"
              "There is too many places to hide and too many places to be ambushed. Keep your helm up though, looks like we're\n"
              "nearing the end of this journey.")
        sleep(sec)
    print("\nGiven that summary, you begin running down the steep slope to resume your march for the blacksmith's daughter.")
    sleep(sec)
    input("\nPress enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("After a brief five minutes, you approach the face of the ruins. It's an archway into a collection of dilapidated stone\n"
          "and bricks that's uncomfortably quiet. The surroundings although fallen apart, dwarf you in comparison.")
    sleep(sec)
    print("\nYou step under the grand archway, but before you can cross...")
    sleep(sec)
    print("Two giant halberds fall right before your face, stopping you in your tracks!")
    sleep(sec)
    print("Two huge figures, clad in plate of mythical proportions step from behind the opposite walls to block the path.")
    sleep(sec)
    print("\nKnight Sceád: NONE SHALL PASS WITHOUT ORDER OF OUR LORD. TO LINGER IS TO MEET YOUR DEMISE.")
    sleep(sec)
    print("\nKnight Fær: AS THE GUARDS SCEÁD AND FÆR, WE WILL NOT TOLERATE ANY POTENTIAL THREAT.")
    sleep(sec)
    print("\n...")
    sleep(sec)
    print("This is a pickle...")
    sleep(sec)
    print("With daunting oppression like this, it's very hard to negotiate charismatically, or even less practical, with battle.\n"
          "You know for a fact, however, that you want to see this quest through, especially with what you've gone through.")
    sleep(sec)
    input("\nPress anything to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    # Pull up a menu for how you'll handle the two knights and give user a choice
    while True:
        # Menus
        if Scary_axe == 1 or sword == 1:
            print("   1. Sneak through [CHANCE]\n"
                  "   2. Find another way in\n"
                  "   3. Fight\n"
                  "   4. Bribe [-WEAPON]\n")
        else:
            print("   1. Sneak through [CHANCE]\n"
                  "   2. Find another way in\n"
                  "   3. Fight\n")
        cho = input("How do you proceed?: ")
        # Sneak through main
        if cho == "1":
            print("\nYou figure the best way to get past the charisma or battle differences is to not be seen... hopefully.")
            sleep(sec)
            chance = chance_50()
            print("Forgetting about how you're standing right in front of the knights, you turn around slowly and walk away. You are far\n"
                  "from gone, however, as when you notice they lose sight, you hold your breath and make your move.")
            if chance == 1:
                # Success
                print("\nCareful precision in your foot placement and concious handle of your noisy metal armor allow you to slip past the\n"
                      "great vigilance of the great guards after a great climb of the side walls of the massive bricks.")
                sleep(sec)
                if Rogue == 1:
                    print(f"\n{Ally}: Way to go! You ought to drop the armor and join the rogues guild with me seeing slick moves\n" 
                          "like that!")
                    sleep(sec)
                input("\nPress enter to proceed: ")
                ruins_2()
                break
            else:
                # Failure
                print("\nYou manage to climb to the top of the side wall where they can't see you, all is well.")
                sleep(sec)
                print("\nSuddenly, out of the blue, you misplaced your foot and fell off the wall. The thunk that insued was loud, almost like a\n"
                      "bell in your armor.")
                sleep(sec)
                print("\nYou pick yourself up off the ground slowly and look around.")
                sleep(sec)
                print("\n... Oh no...")
                sleep(sec)
                print("\nYou are already surrounded by the guards.")
                sleep(sec)
                print("\nKnight Fær: YOU HAD YOUR WARNING; YOUR ONLY CHANCE.")
                sleep(sec)
                print("\nKnight Sceád: NOW TIME IS NIGH, TO REST WITH THE PLANTS.")
                sleep(sec)
                input("\nPress enter to proceed: ")
                ruins_fight()
                break
        # Find another way
        elif cho == "2":
            print("\nYou think that the best way forward is improvising another path, allowing you to avoid dealing with the knights\n"
                  "altogether. Even if you run into problems, they shouldn't be massive and armored in the very least.")
            sleep(sec)
            print("\nRather than taking the path straight to the castle, you follow the path along the wall of the ruins and hold out\n"
                  "hope for good fortune and favor.")
            sleep(sec)
            input("\nPress enter to proceed: ")
            ruins_alt()
            break
        # Fight (Very risky)
        elif cho == "3":
            if Rogue == 1:
                print(f"\n{Ally}: Are you mad or do you have a death wish!? Consider thinking again, those guys outnumber and outsize you!")
            cho2 = input("\nThis is what you want to do? [Y/N]: ").lower()
            if cho2 == "y":
                print("\nYou breathe in slowly, and then breathe out. You draw your weapon and brace yourself for the hurt.")
                sleep(sec)
                print("\nKnight Fær: PREPARE FOR TROUBLE.")
                sleep(1)
                print("Knight Sceád: AND MAKE IT DOUBLE.")
                sleep(sec)
                input("\nPress enter to proceed: ")
                ruins_fight()
                break
            else:
                print(f"\n{Ally} is right. There is a fine line between bravery and foolishness.")
                continue
        # Bribery
        elif cho == "4":
            if Scary_axe == 1 and sword == 1:
                print("\nYou have accumulated quite the collection of armaments, that being the lumberjack's axe and the big sword\n"
                      "you scored at Drabtown. At this point, you could probably afford to let one go.")
                trd_wpn = input("\n 1. Sword\n 2. Scary Axe\nWhich weapon will you part with? [1/2]: ")
                # Part with sword
                if trd_wpn == "1":
                    print("\nLet's keep our axe, looks more intimidating anyway.")
                    sleep(sec)
                    trd_wpn = 1
                # Part with axe
                elif trd_wpn == "2":
                    print("\nLet's keep our sword, you're more familiar with how to use it anyway.")
                    sleep(sec)
                    trd_wpn = 2
                sleep(sec)
            elif Scary_axe == 1 and sword == 0:
                print("\nSeeing those guys in with metal from head to toe, you wonder if you could bribe them with your axe you got\n"
                      "from the lumberjack.")
                trd_wpn = 2
                sleep(sec)
            elif sword == 1 and Scary_axe == 0:
                print("\nYou pull out the big sword you've been lugging on your back and wonder if you can't tempt them in exchange\n"
                      "for passage.")
                trd_wpn = 1
                sleep(sec)
            else:
                print("\nNo, you can't barter something you don't have. Try finding the axe!\n")
                continue
            wpn_cho = input("\nDo you wish to attempt bribery with your weapon? [Y/N]: ").lower()
            if wpn_cho == "y":
                print("\nLet's do this. Hopefully we won't need a weapon for the beast, unfortuantely thats likely wishful thinking.")
                sleep(sec)
                # Knight Dialogue portion + weapon variable decrease here
                print("\nYou walk back over to the knights and tap on their boot, holding your gift high above your head.")
                sleep(sec)
                print("\nKnight Sceád: UHH, WHAT IS THIS LITTLE MAN... A GIFT? NOT JUST ANY GIFT, A MINIATURE WEAPON! PERFECT FOR MY\n"
                      "LITTLE COLLECTION.")
                sleep(sec)
                print("\nKnight Sceád: NOW I'M NOT WITHOUT GRATITUDE, SO WHAT DO YOU WANT IN EXCHANGE?")
                sleep(sec)
                print("\nYou point towards the castle and gesture to your empty pockets.")
                sleep(sec)
                print("\nKnight Fær: SCEÁD, DON'T BE A BUCKET BRAIN, THIS IS OBVIOUSLY BRIBERY.")
                sleep(sec)
                print("\nKnight Sceád: ALAS, IT IS FINE. WITHOUT A WEAPON DO YOU EVEN THINK HE'D STAND A CHANCE AGAINST HIM?")
                sleep(sec)
                print("\nKnight Fær: HMMPH... YOU MAKE A GOOD POINT, BUT I DID NOT TAKE PART IN THIS DEAL... PROCEED LITTLE MAN.")
                sleep(sec)
                print("\nSweet Neptune, it worked! The tower is just up ahead now!")
                if trd_wpn == 1:
                    sword = 0
                elif trd_wpn == 2:
                    Scary_axe == 0
                sleep(sec)
                input("\nPress enter to proceed: ")
                ruins_2()
                break
            else:
                print("\nNah, nevermind. We'll need that for this upcoming beast that took Ivar's daughter!")
                sleep(sec)
                continue
        # Any other exception
        else:
            # Handle error
            print("\n! Please choose an number between the given range !\n")
            continue
    return sword, Scary_axe

# Ruins continued
def ruins_2():
    os.system('cls' if os.name == 'nt' else 'clear')
    global lives, lives_max, Rogue
    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    sleep(sec)
    print("After getting through the gate, before you is a bridge innumeral miles long, but still within decent walking distance.\n"
          "It's a straight shot to this castle with seemingly no challenge.")
    sleep(sec)
    print("\nLooks like you're nearing the end. Any vigor that might have been diminished is gathered once again. You begin jogging\n"
          "down it with no hesitation.")
    sleep(sec)
    # === Ally Dialogue Time === #
    # Chef
    if Chef == 1:
        print(f"\n{Ally}: Zoo-wee mama! We've come a long way since the start of our journey and finally, the castle is right before our eyes!\n")
        sleep(sec)
        print(f"\n{Ally}: I don't think I've got to know you as much as I could know you, Mr. Knight guy, let me ask you a-little something...")
        sleep(sec)
        print(f"\n{Ally}: What do you look like under all that shiny armor?")
        sleep(sec)
        # Answer loop
        while True:
            identity = input("\n [1.     A guy. ]\n [2.     A gal. ]\n [3. Not human. ]\n [4.        ... ]"
                         "\nHow do you answer?: ")
            # A guy
            if identity == "1":
                print(f"\n{Ally}: Ah yes, maybe this questions was too silly to ask. I can't imagine anyone else under that armor, but I wouldn't\n"
                      "object to anyone else going on adventures, I mean, I'm a cook and I'm out here risking my life for a yummy leaf. Good greif!")
                sleep(sec)
                print(f"{Ally}: \nI can't imagine anyone else under that armor, but I wouldn't object to anyone else going on adventures, I mean, I'm a cook and\n"
                      "I'm out here risking my life for a yummy leaf for my 'all-spice'. Good greif!")
                sleep(sec)
                break
            # A gal
            elif identity == "2": 
                print(f"\n{Ally}: Really!? A woman out here swinging swords and tackling giants!? How inspirational! Adventuring really is for everyone!")
                sleep(sec)
                print(f"\n{Ally}: I should probably start callin' ya 'Knight Gal', rather than Knight Guy... Er- maybe you just look like a girl.")
                sleep(sec)
                print(f"\n{Ally}: Regardless, it's been a pleasure workin' with ya!")
                sleep(sec)
                break
            # Not human
            elif identity == "3":
                print(f"\n{Ally}: Well, um... You're shaped human, but I guess I've never really seen ya. No pressure though, I'm just being curious.")
                sleep(sec)
                print(f"\n{Ally}: Do you have a good sense of smell, at least? I need a really good nose to find this forsaken herb; the final ingredient\n"
                      "of my all-spice...")
                sleep(sec)
                print(f"\n{Ally}: If you can find it, you'll definitely be the first to try, I promise that, just grab the seeds too, will ya?")
                sleep(sec)
                break
            # (No answer)
            elif identity == "4":
                print(f"\n{Ally}: Alright, uh- Fine then. Keep your secrets... Maybe I should just take your helmet off myself...")
                sleep(sec)
                break
            # EXCEPTION HANDLING
            else:
                print(f"\n{Ally}: Sorry, I saw a weird looking bird in the sky. What did you say?")
                sleep(sec)
                continue
        
        print(f"\nAfter that question ends, you think to youself about who {Ally} is... You think about it for a bit.")
        sleep(sec)
        print(f"You get an idea. You tap on {Ally}'s shoulder and ask...")
        sleep(sec)
        # Question loop
        while True:
            question = input("\n [1.       Anything you like besides cooking? ]\n [2. PLEASE tell me what this 'All-Spice' is! ]"
                         "\nWhat do you say?: ")
            # Likes besides cooking
            if question == "1":
                print(f"\n{Ally}: Hmmm... I love cooking, but if I were to never touch cookware again, I would be SUPER invested in\n"
                      "playing instruments, such as the cello. It's a shame no one keeps them around anywhere I could play them.")
                sleep(sec)
                print(f"\n{Ally}: Let me know if you see ANY STRINGED INSTRUMENT anywhere!")
                sleep(sec)
                break
            # What is the 'all-spice'
            if question == "2":
                if identity == "4":
                    print(f"\n{Ally}: You didn't reveal your secret, so I won't reveal mine. No hard feelings, Mr. Knight Guy!")
                    sleep(sec)
                    break
                elif identity == "3" or "2" or "1":
                    print(f"\n{Ally}: Ok, since you were honest with me about MY burning question, I'll be honest too, since we've\n"
                          "survived this far..")
                    sleep(sec)
                    print(f"\n{Ally}: This all-spice has a name. It's leaves are a vibrant yellow, serrated pattern of the edges, and\n"
                         "when ground up, has the sweetest aroma you've ever smelled... the Anima Mederi.")
                    sleep(sec)
                    print(f"\n{Ally}: You'll never need sugar or cocoa again- or so the legend goes... I know it's real though! You have to believe me!")
                    break
                
            # Misinput
            else:
                print(f"\n{Ally}: Whuh- Sorry, say that again. I'm paying attention now.")
                sleep(sec)
                continue
    # Rogue
    elif Rogue == 1:
        print(f"\n{Ally}: We've come so far and now we finally have moment to think. I suggest thinking about how you approach this lord\n"
              "we hear so much about.")
        sleep(sec)
        print(f"\n{Ally}: Since we're here again, let me ask you something...")
        sleep(sec)
        print(f"\n{Ally}: Is there anything you fear?")
        sleep(sec)
        # Answer loop
        while True:
            # If you're honest, maybe you'll learn a bit more about Kanra
            fear = input("\n [1.                   The dark. ]\n [2.                    Dragons. ]\n [3.                  Questions. ]\n"
                         " [4.                Being alone. ]\n [5.                 Being lost. ]\n [6.             I fear nothing. ]\n" 
                         " [7. Why are you asking me this? ]\n [8.             Something else. ]\nHow do you answer?: ")
            # The dark
            if fear == "1":
                print(f"\n{Ally}: Well, there are a lot of those spaces out in the world of adventuring, so I can't say if you're brave, foolish, or\n"
                      "haven't outgrown that childhood fear.")
                sleep(sec)
                print(f"\n{Ally}: I can tell you this much, to find a way out you don't always gotta see where your going and as long as you keep moving,\n"
                      "You'll always find the light. As long as you never give up, you'll find a way. Trust me, my lifestyle is testament to that.")
                sleep(sec)
                break
            
            # Dragons
            elif fear == "2":
                print(f"\n{Ally}: And you're an adventurer? Kind of silly to be dressed so galantly and fear the thing you're so associated to dealing with.\n"
                      "No judgement here, they are formidable creatures and ideally you don't want to be on the wrong side of them.")
                sleep(sec)
                print(f"\n{Ally}: If we do run into one, you're odds are better jumping off a cliff and hoping for no injury than to try and withstand that\n"
                      "hot breath. Don't even think about fighting it, even if you were to hurt it, they hold grudges hard. Do not get into draconic drama.")
                sleep(sec)
                break

            # Questions
            elif fear == "3":
                print(f"\n{Ally}: hmm... Sarcasm? If you don't want to tell I won't pry.")
                sleep(sec)
                break

            # Being alone (Kanra's fear)
            elif fear == "4":
                print(f"\n{Ally}: That's a hard fear for an adventurer to have... I hope it's not the sole reason we're allied up, cause for-hires are not\n"
                      "typically motivated by friendship, much of it is self-centered, from what I see.")
                sleep(sec)
                print(f"\n{Ally}: I would know, cause that's what I'm afraid of. It's why I was stuck inside the pub in the first place.")
                sleep(sec)
                print(f"\n{Ally}: Everyone is there, someone would know I went missing. People would also remember my stories and I wouldn't be forgotten.")
                sleep(sec)
                print(f"\n{Ally}: When you live away from the grid and you have no family line to etch your name in the pages of history, it's like true\n"
                      "death to never be remember; You will have never been.")
                sleep(sec)
                print(f"\nYou tell {Ally} that if no one remembers her, at least you will.")
                sleep(sec)
                print("You also tell her that if you don't remember her, the footprint she's already left on the world will.")
                sleep(sec)
                print(f"\n{Ally}: You're right... ugh, sorry for dumping that on you, but seeing we made it this far and you didn't turn tail and run or\n"
                      "give up on this quest, made me feel as if you could take what I had to say.")
                sleep(sec)
                print(f"\n{Ally}: Thanks for being such a great listener, {Player_Name}.")
                sleep(sec)
                break

            # Being lost
            elif fear == "5":
                print(f"\n{Ally}: Interesting... Seeing as you've found the way to this point, I'd argue you do well to know where you are. Not a bad\n"
                      "thing I suppose, but keep in mind, the world is finite. You'll always find a way, sometimes a shortcut!")
                sleep(sec)
                print(f"\n{Ally}: For that let me tell you mine, I trust you enough... I can't be alone; I dread it constantly.")
                sleep(sec)
                print(f"\n{Ally}: It's why I lurk in the pub and work for hire.")
                sleep(sec)
                print(f"\n{Ally}: Everyone is there, someone would know I went missing. People would also remember my stories and I wouldn't be forgotten.")
                sleep(sec)
                print(f"\n{Ally}: When you live away from the grid and you have no family line to etch your name in the pages of history, it's like true\n"
                      "death to never be remember; You will have never been.")
                sleep(sec)
                print(f"\nYou tell {Ally} that if no one remembers her, at least you will.")
                sleep(sec)
                print("You also tell her that if you don't remember her, the footprint she's already left on the world will.")
                sleep(sec)
                print(f"\n{Ally}: You're right... ugh, sorry for dumping that on you, but seeing we made it this far and you didn't turn tail and run or\n"
                      "give up on this quest, made me feel as if you could take what I had to say.")
                sleep(sec)
                print(f"\n{Ally}: Thanks for being such a great listener, {Player_Name}.")
                sleep(sec)
                break

            # "I fear nothing"
            elif fear == "6":
                print(f"\n{Ally}: I don't believe it, and if I'm going to believe it, maybe you haven't found what you're afraid of yet.")
                sleep(sec)
                print(f"\n{Ally}: I know I never used to be afraid, but when I was swept away from my family, something weeded it's way into my heart.")
                sleep(sec)
                print(f"\n{Ally}: I was alone. Truly out there on my own. Didn't know if I could even trust myself, but I figured out things in the pub.")
                sleep(sec)
                print(f"\n{Ally}: Everyone is there, someone would know I went missing. People would also remember my stories and I wouldn't be forgotten.")
                sleep(sec)
                print(f"\n{Ally}: When you live away from the grid and you have no family line to etch your name in the pages of history, it's like true\n"
                      "death to never be remember; You will have never been.")
                sleep(sec)
                print(f"\nYou tell {Ally} that if no one remembers her, at least you will.")
                sleep(sec)
                print("You also tell her that if you don't remember her, the footprint she's already left on the world will.")
                sleep(sec)
                print(f"\n{Ally}: You're right... ugh, sorry for dumping that on you, but seeing we made it this far and you didn't turn tail and run or\n"
                      "give up on this quest, made me feel as if you could take what I had to say.")
                sleep(sec)
                print(f"\n{Ally}: Thanks for being such a great listener, {Player_Name}.")
                sleep(sec)
                break

            # "Why are you asking me this?"
            elif fear == "7":
                print(f"\n{Ally}: Just talking honestly, but practically speaking, whatever horror we see inside the castle could be bad, so I want to\n"
                      "make sure you're prepared to face the situation ahead.")
                sleep(sec)
                continue

            # Something else...
            elif fear == "8":
                print(f"\n{Ally}: You're saying it's beyond simple fears? Hmm, maybe you don't want to tell me, but I don't need to know.\n"
                      "Just stay calm ahead, OK?")
                sleep(sec)
                break

            # EXCEPTION HANDLING
            else:
                print(f"\n{Ally}: Uhh... You were mumbling, or I couldn't hear over your helmet. Could you repeat that?")
                sleep(sec)
                continue
        print(f"\nAfter that question ends, you think to youself about who {Ally} is... You think about it for a bit.")
        sleep(sec)
        print(f"You get an idea. You tap on {Ally}'s shoulder and ask...")
        sleep(sec)
        # Question loop
        while True:
            question = input("\n [1.  After the quest, can we stick together? ]\n [2.     What are you doing after this quest? ]"
                             "\nWhat do you say?: ")
            # Sticking together
            if question == "1":
                print(f"\n{Ally}: I mean, if you're serious about it, and you don't die ahead, I wouldn't object... Let me think about it first...")
                sleep(sec)
                if fear == "4":
                    print(f"\n{Ally}: Acknowledging what I said earlier, huh? I appreciate the thought... I really do...")
                    sleep(sec)
                break
            # After the quest
            elif question == "2":
                print(f"\n{Ally}: To be frank, I don't know. Living life from things of the past isn't where I like to dwell, and I can't be sure\n"
                      "what the future holds, only in the present am I most capable of making choice and altering the future.")
                sleep(sec)
                print(f"\n{Ally}: If I had to guess, I'd take my earnings from our agreement and try to do good for the lesser out there.")
                break
            # Misinput
            else:
                print(f"\n{Ally}: Oh, uh, what did you say?")
                sleep(sec)
                continue
    
    # Pick up the main story again
    print("\nYou are about halfway there when suddenly, the ground rumbles violently...")
    sleep(sec)
    print("\nIs it an earthquake? shift of some kind?")
    sleep(sec)
    print("\nNo... It's worse...")
    sleep(sec)
    print("\nFrom behind you about 500 feet away, a booming cry of a monster, the dragon alerts you of your danger.")
    sleep(sec)
    print("\nDread grips you as you see it is tearing it's way towards you.")
    sleep(sec)
    print("\nThere is no doubt in your mind... It is time to run.")
    sleep(sec)
    input("\nPress enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    # Chase sequence goes here
    print(f"\n- = [ ESCAPE ] = -")
    sleep(sec)
    print("\nYou turn around a kick off the ground as fast as you can. You need to get away, no matter what.")
    sleep(sec)
    print("\nIn front of you, the bridge begins to collapse. You need to get over the gaps that form!")
    sleep(sec)
    print("\nAs you run up, a near pillar to the left begins to fall down.")
    sleep(sec)
    print("\nWith no time to think, you...")
    sleep(sec)
    # First escape choices
    while True:
        escape1 = input("\n [1.        Run to the left and jump over ]"
                        "\n [2.           Run faster down the center ]"
                        "\n [3. Run to the right and try to clear it ]"
                        "\nYour choice [1, 2 or 3]: ")
        # Go left to pillar base (100% Success)
        if escape1 == "1":
            print("\nYou direct yourself to the base where it is falling, away from danger and quickly vault"
                  "over the fallen pillar.")
            sleep(sec)
            break
        # Run faster down the center (75% success)
        elif escape1 == "2":
            print("\nNo time for silly ideas. you NEED to go faster!")
            sleep(sec)
            print("\nYou run with all your might, pillar coming ever nearer and...")
            # Roll for chance
            chance = chance_75()
            # Fail
            if chance == 1:
                print("\nYou hit your head on the top pillar and are immediately flipped on your back.")
                sleep(sec)
                lives -= 1
                print(f"Health: {lives}/{lives_max}")
                sleep(sec)
                if lives < 1:
                    print("\nUnfortunately, the pillar has fallen on top of you. You cannot fight your way out under the weight.")
                    sleep(sec)
                    print("\nThere is no way to save you. You can only wait for your demise with the ever approaching dragon.")
                    sleep(sec)
                    game_over()
                    break
                else:
                    print("\nAlas, you cleared the obsticle. You get up and hurry down the bridge!")
                    sleep(sec)
                    break
            # Success
            elif chance > 1:
                
                print("\nIn the nick of time, you manage to pass under the massive structure, maintaining quick pace.")
                sleep(sec)
                break
        # Go Right to give more room (15% success)
        elif escape1 == "3":
            print("\nYou got to get further away from the middle if you're gonna clear this!")
            sleep(sec)
            print("\nYou turn right and realize that you lose forward momentum. The pillar is inches away from your head!")
            sleep(sec)
            # Chance!
            chance = chance_75()
            # Success
            if chance == 1:
                
                print("\nBy some miracle, you manage to clear it.")
                sleep(sec)
                print("\nKeep running, it's not over!")
                break
            # Fail
            elif chance > 1:
                print("\nYou've been struck and laid flat on the floor!")
                lives -=1
                sleep(sec)
                print(f"Health: {lives}/{lives_max}")
                sleep(sec)
                if lives < 1:
                    print("\nUnfortunately, the pillar has fallen on top of you. You cannot fight your way out under the weight.")
                    sleep(sec)
                    print("\nThere is no way to save you. You can only wait for your demise with the ever approaching dragon.")
                    sleep(sec)
                    game_over()
                    break
                else:
                    print("\nYou're not down yet! You clambor your way back to your feet and continue your dash for life.")
                    sleep(sec)
                    break
            break
        # Exception Handling (continue statement)
        else:
            print("\n- You can only choose 1, 2, or 3!\n")
            continue
    
    print("\nYou're not done yet!")
    sleep(sec)
    print("\nFrom behind, a fiery wall of flames envelopes the bridge!")
    sleep(sec)
    print("\nYou notice the entrance is JUST up ahead!")
    sleep(sec)
    print("\nDespite little time, you eye some options.")
    # Second escape choices
    while True:
        if Rogue == 1:
            escape2 = input("\n [1. Dive for the boulder, wait for flames to pass! ]"
                            "\n [2.     Endure the flames, get to the castle gate! ]"
                            "\n [3.    Throw a dagger into the beasts eye! (KANRA) ]"
                            "\nYour choice [1, 2, or 3]: ")
        else:
            escape2 = input("\n [1. Dive for the boulder, wait for flames to pass! ]"
                            "\n [2.     Endure the flames, get to the castle gate! ]"
                            "\nYour choice [1 or 2]: ")
        # Safe Option
        if escape2 == "1":
            print("\nIt's a no brainer, take cover! There  is no way you'd want to face that flaming cloud of death!")
            sleep(sec)
            print("\nNot soon after your dive turns into a roll, the flames catch up and wash over above you.")
            sleep(sec)
            print("\nAfter a long 30 seconds, the flames finally stop, and so does the stomping.")
            sleep(sec)
            break
        # Skips the sanctum depths if you can survive the flames!
        elif escape2 == "2":
            print("\nYou breathe in, and then out...")
            sleep(sec)
            print("\nYou kick your legs forward as fast as you can and tighten your muscles as much as you can... You're gonna get to that gate...")
            sleep(sec)
            print("\nVery quickly, all you can see is the bright orange of the fire and are running blindly with not a clue your distance to the gate")
            sleep(sec)
            print("\nYour whole body seizes in pain, your skin crawling inside your armor.")
            lives -= 2
            print(f"\nHealth Remaining: {lives}/{lives_max}")
            if lives < 1:
                    print("\nIt's too much... You can't feel your legs anymore and you can't even tell if you're still running!")
                    sleep(sec)
                    print("\nYou can't breathe within the smoke and you can't keep moving as the pain is too great. It's over...")
                    sleep(sec)
                    game_over()
                    break
            else:
                print("\nThrough courage and sheer will to live, you fight your way through the pain and the flames to the other side and seal the door ahead\n"
                      "behind you!")
                sleep(sec)
                print("\nPromptly, you begin rolling on the floor to put out any of the remaining flames that still licked your armor.")
                sleep(sec)
                input("Press enter to continue: ")
                sanctum()
                return
        # KANRA (Rogue) option
        elif escape2 == "3" and Rogue == 1:
            print("You cry out to Kanra to try and hurt the beast and stop the flames!")
            sleep(sec)
            print(f"\n{Ally}: On it!")
            sleep(sec)
            print("\nWith absurdly superb precision, Kanra is able to stop the stream of fire headed your way with a keen shot to the dragons eye.")
            sleep(sec)
            print("\nThe monster belts out a cry that, you've no doubt reached all the way to Drab Town. Your helmet rings with its roar.")
            sleep(sec)
            print("\nVery quickly, your party gathers itself inside the threshold of the castle, shut down, and then bar the massive door.")
            sleep(sec)
            print(f"{Ally}: {Player_Name}, there is no way I'm forgetting this adventure or a guy like you after what just happened... We are so lucky to"
                  "\nstill be alive... That means you owe me a pint!")
            sleep(sec)
            input("Press enter to continue: ")
            sanctum()
            return
        # Handle exceptions (Continue statement)
        else:
            if Rogue == 1:
                print("\n- You can only choose 1, 2, or 3!\n")
            else:
                print("\n- You can only choose 1 or 2!\n")
            continue
    
    print("\nYou take your chance and run to the exit.")
    sleep(sec)
    print("\nSuddenly, from the skies...")
    sleep(sec)
    print("\n ! CRASH !")
    sleep(sec)
    print("\nThe dragon lands in front of the gate and between you two, the bridge breaks in two!")
    sleep(sec)
    print("\nThe beast prepares to lunge at you. It seems like you finally ran out of options...")
    sleep(sec)
    print("\nOr have you?..")
    # Final Escape option (I may change this later based on story direction, which should explain my if statement here)
    escape3 = input("\n [1. Jump into the void below ]"
                    "\nChoose: ")
    # Jump off the bridge.
    if escape3 == "1":
        print("\nYou take in what may be your final breath, and dash for the edge of the broken bridge.")
        sleep(sec)
        print("\nThen, you leapt.")
        sleep(sec)
        print("\nAs you plummet, you watch the world above wash away, and into darkness you go, swallowed by the void.")
        sleep(sec)
        input("\nPress enter to continue: ")
        sanctum_depths()
        return
    else: # Same thing for right now.
        print("\nYou take in what may be your final breath, and dash for the edge of the broken bridge.")
        sleep(sec)
        print("\nThen, you leapt.")
        sleep(sec)
        print("\nAs you plummet, you watch the world above wash away, and into darkness you go, swallowed by the void.")
        sleep(sec)
        input("\nPress enter to continue: ")
        sanctum_depths()
        return

# Fight the knights
def ruins_fight():
    global sword, Scary_axe, rations, Chef, Rogue, Ally, Player_Name, sec, Stick, lives, lives_max, Werewolf
    os.system('cls' if os.name == 'nt' else 'clear')

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    Scaed = 2
    Faer = 2
    defense = 0
    print("\n- = [ FIGHT ] = -")
    if Rogue == 1:
        sleep(sec)
        print(f"{Ally}: Hey, you'll only be able to take two hits from these guys in your prime state, stay alive!\n")

    # ========== FIGHT LOOP ============ #
    while True:
        # Reset status
        defense = 0
        # === YOUR TURN === #
        if Chef == 1:
            action = input(f"\nYOUR HEALTH: [{lives}]\n    [1. Attack   ]\n    [2. Defend   ]\n    [3. Heal (Tonio)]\nMake an action: ")
        else:
            action = input(f"\nYOUR HEALTH: [{lives}]\n    [1. Attack   ]\n    [2. Defend   ]\nMake an action: ")
        # ATTACK
        if action == "1":
            print("You took a swing at the hulking guard.")
            sleep(sec)
            chance = chance_75()
            chance_wpn = chance_50()
            if chance == 1:
                # Failure
                print("You struck his plated armor; your blade was repelled!")
                sleep(sec)
            elif chance == 4 or chance_wpn == 1:
                # Critical Success
                print("\nYou managed to sink your blade through a tight crevass between his chest armor and immediately felled this\n"
                      "champion of the gate!")
                sleep(sec)
                if Scaed == 0:
                    print("\nKnight Fær: AT LONG LAST... OUR LORD HAS MET HIS MATCH...")
                    sleep(sec)
                    print("\nThe final knight has fallen.")
                    Faer = 0
                    sleep(sec)
                else:
                    print("\nKnight Sceád: MAYBE I- URK... GRAVELY UNDERESTIMATED YOU, SMALL MAN...")
                    sleep(sec)
                    print("\nWith a mighty crash, the giant was down.")
                    Scaed = 0
                    sleep(sec)
            else:
                # Success
                print("You land a strike between the armor of the knight's leg!")
                sleep(sec)
                if Scaed == 0:
                    Faer -= 1
                    if Faer == 0:
                        print("\nKnight Fær: AT LONG LAST... OUR LORD HAS MET HIS MATCH...")
                        sleep(sec)
                        print("\nThe final knight has fallen.")
                        Faer = 0
                        sleep(sec)
                else:
                    Scaed -= 1
                    if Scaed == 0:
                        print("\nKnight Sceád: MAYBE I- URK... GRAVELY UNDERESTIMATED YOU, SMALL MAN...")
                        sleep(sec)
                        print("\nWith a mighty crash, the giant was down.")
                        Scaed = 0
                        sleep(sec)

        # DEFEND
        elif action == "2":
            # This will be pretty practical if you have the werewolf, as he will always attack.
            print("\nYou collect yourself and enter a defensive stance")
            sleep(sec)
            defense = 1
            print("! Your likely hood of avoiding an attack has increased !")
            sleep(sec)

        # HEAL (IF TONIO IS YOUR ALLY)
        elif action == "3" and Chef == 1 and lives < 3:
            print("\nTonio scrambles to your location!")
            sleep(sec)
            print(f"\n{Ally}: Knight Guy! Keep standing tall!")
            sleep(sec)
            if rations > 0:
                rations -= 1
                lives = 3
                print(f"RATIONS: {rations}")
            else:
                lives += 1
            print(f"A fast-acting herbal tonic restores you to your senses. [HEALTH {lives}/3]")
            sleep(sec)
        
        # Input Error
        else:
            print("\n! Invalid input !\n")
            continue

        # === WEREWOLF TURN === #
        if Werewolf == True:
            print("\nYour werewolf companion jumps into the fray and lunges toward the tall guard fearlessly!")
            sleep(sec)
            were_chance = chance_75()
            if were_chance == 1:
                # Failure
                print("\nUnfortuantely, the tall guard steps out of the way just in time and your friend misses!")
                sleep(sec)
            else:
                # Success
                print("\nHe latches on to the knights leg and rips off layers of armor!")
                sleep(sec)
                if Scaed == 0:
                    Faer -= 1
                    if Faer == 0:
                        print("\nKnight Fær: AT LONG LAST... OUR LORD HAS MET HIS MATCH...")
                        sleep(sec)
                        print("\nThe final knight has fallen.")
                        Faer = 0
                        sleep(sec)
                else:
                    Scaed -= 1
                    if Scaed == 0:
                        print("\nKnight Sceád: MAYBE I- URK... GRAVELY UNDERESTIMATED YOU, SMALL MAN...")
                        sleep(sec)
                        print("\nWith a mighty crash, the giant was down.")
                        Scaed = 0
                        sleep(sec)

        # === GUARDS' TURN === #
        # SCAED
        if Scaed > 0:
            print("\nSceád raises their halberd skyward, and then strikes down where your are standing!")
            sleep(sec)
            print("\n  CRASH!  ")
            sleep(sec)
            dodge = chance_50()
            if defense == 1:
                # IF YOU CHOSE DEFEND PRIOR TO THIS
                defend = chance_75()
                if defend == 1:
                    # Failure
                    print("\nDespite your defense stance, your guard was collapsed and you were struck to the earth!")
                    sleep(sec)
                    lives -= 1
                    if lives == 0:
                        print("\nThe world is spinning... You can't breathe...")
                        sleep(sec)
                        print("\nYou can't fight your way out, when the knight grabs you by the ankle and throws you far, far away\n" \
                        "from the castle. You were never seen in this land again...")
                        sleep(sec)
                        input("\nPress enter to proceed: ")
                        game_over()
                        break
                else:
                    # Success
                    print("\nYou slipped past the polearm crashing down, barely avoiding being planted into the ground!")
                    sleep(sec)
            else:
                if dodge == 1:
                    # Failure
                    print("\nYou were caught with your gaurd open and promptly forced to the ground!")
                    sleep(sec)
                    lives -= 1
                    if lives == 0:
                        print("\nThe world is spinning... You can't breathe...")
                        sleep(sec)
                        print("\nYou can't fight your way out, when the knight grabs you by the ankle and throws you far, far away\n" \
                        "from the castle. You were never seen in this land again...")
                        sleep(sec)
                        input("\nPress enter to proceed: ")
                        game_over()
                        break
                else:
                    # Success
                    print("\nYou slipped past the polearm crashing down, barely avoiding being planted into the ground!")
                    sleep(sec)
        
        # FAER
        if Faer > 0:
            print("\nFær drags their halberd across the ground and swipes horizontally towards you!")
            sleep(sec)
            print("\n  SWISH!  ")
            sleep(sec)
            dodge = chance_50()
            if defense == 1:
                # IF YOU CHOSE DEFEND PRIOR TO THIS
                defend = chance_75()
                if defend == 1:
                    # Failure
                    print("\nDespite your guard, you were struck by the sweeping attack and forced away!")
                    sleep(sec)
                    lives -= 1
                    if lives <= 0:
                        print("\nYou're lying on your back and your body won't let you up...")
                        sleep(sec)
                        print("When Fær approaches the place you lay, they lean over and ask you something...")
                        sleep(sec)
                        print("\nKnight Fær: WHAT IS YOUR NAME, LITTLE MAN?")
                        sleep(sec)
                        print("\nYou manage to get utter with your final breath.")
                        sleep(sec)
                        print(f"\nKnight Fær: REST WELL ON THIS HILL OF CHAMPIONS, {Player_Name}.")
                        sleep(sec)
                        print("\nYou promptly lost conciousness...")
                        sleep(sec)
                        input("\nPress enter to proceed: ")
                        game_over()
                        break
                    else:
                        # Success
                        print("\nYou slipped past the polearm crashing down, barely avoiding being planted into the ground!")
                        sleep(sec)
            else:
                if dodge == 1:
                    # Failure
                    print("\nYou were caught with your gaurd open and promptly forced to the ground!")
                    sleep(sec)
                    lives -= 2
                    if lives <= 0:
                        print("\nYou're lying on your back and your body won't let you up...")
                        sleep(sec)
                        print("When Fær approaches the place you lay, they lean over and ask you something...")
                        sleep(sec)
                        print("\nKnight Fær: WHAT IS YOUR NAME, LITTLE MAN?")
                        sleep(sec)
                        print("\nYou manage to get utter with your final breath.")
                        sleep(sec)
                        print(f"\nKnight Fær: REST WELL ON THIS HILL OF CHAMPIONS, {Player_Name}.")
                        sleep(sec)
                        print("\nYou promptly lost conciousness...")
                        sleep(sec)
                        input("\nPress enter to proceed: ")
                        game_over()
                        break
                else:
                    # Success
                    print("\nYou slipped past the polearm crashing down, barely avoiding being planted into the ground!")
                    sleep(sec)

        # === CHECK BATTLE STATUS === #
        # If both guards are defeated
        if Scaed <= 0 and Faer <= 0:
            print("\nBy the might of your weapon, or some stroke of luck, you managed to fell the two guards.")
            sleep(sec)
            if Chef == 1:
                print(f"{Ally}: Mr. {Player_Name} Knight Guy, I'm not sure how many of those fights I can take...")
                sleep(sec)
                print(f"{Ally}: If one thing is for sure, you keep my adrenaline a-pumpin'. We'll have stories to tell for generations!")
                sleep(sec)
            print("\n- = [ BATTLE WON ] = -")
            if Werewolf == True:
                print("\nAfter a breif moment, you hear something metal dragging across the ground. It's your werewolf friend\n"
                      "with the elbow guard of one of the knights you felled.")
                sleep(sec)
                print("\nhe drops it at your feet and urges you to inspect it.")
                sleep(sec)
                print("\nIn examining it, you deduce that it's perfect size for a shield! Given the towering foes, proper defense feels\n"
                      "like a miracle!")
                sleep(sec)
                print("\n You got the SHEILD!")
                shield = 1
                lives_max = 5
                lives += 2
                print("! Maximum Health Increased to 5 !")
                sleep(sec)
            print("\nWasting no time, you make your move through the archway, this time uninterrupted, and B-line straight to the castle.")
            sleep(sec)
            input("\nPress enter to proceed: ")
            break
    ruins_2()

# Find a new path
def ruins_alt():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Debug Info
    if DEBUG == True:
        print("\n================= DEBUGGING =================\n")
        print(f"DEBUG: sword={sword}, has_map={has_map}, rations={rations}, Rogue={Rogue}, Chef={Chef}, Lives={lives}")
        print("\n================= DEBUGGING =================\n")

    print(utils.UnderLN("Ruins Alt Path"))
    sleep(sec)
    print("\nYou're not sure where you are going. All you really can do is follow the walls and take the turns that bring\n" \
          "you closer to the looming castle.")
    sleep(sec)
    print("\nSo far, its been a long hike to find anything worthwhile, but as the sun sinks below the horizon, you pass by\n" \
          "a large door, which promptly stops you in your tracks.")
    sleep(sec)
    print("\nUpon approaching it, your breif examination of the door leads you to find a hand-shaped divot between the two\n" \
          "giant slabs of stone.")
    sleep(sec)
    print("\nThis must imply it is some kind of contraption. With nothing to lose but daylight, you place your hand inside\n" \
          "the hole.")
    sleep(sec)
    print("\nOn the other side, you can hear mechanisms work behind the doors and within the walls of this borderline labyrinth.")
    sleep(sec)
    print("\nSuddenly... A voice from an unidentifiable location envelopes the area.")
    sleep(sec)
    input("Press enter to proceed: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n???: To pass, one must answer the riddle of the wiser lords of this land...")
    sleep(sec)
    print("???: sayings from the harbingers of the future...")
    sleep(sec)
    print("???: Transient writings from the heralds of generation...")
    sleep(sec)
    print("\nThis sounds like it'll be quite advanced... You rack your head on the first ancient texts that come to your mind...\n"
          "only to be met with this question.")
    sleep(sec)
    print("\n???: Why did the chicken cross the road...")
    sleep(sec)
    # === Start the riddling === #
    # Sorry in advance... :(

    # Conditional accumulatory variable for an event related to answering.
    # This is the only place this is used.
    fail_counter = 0
    # Riddle 1
    while True:
        answer = input("\nWhat is your answer?: ").lower()
        if "to get to the other side" in answer:
            print("\n???: Correct... Next riddle...")
            sleep(sec)
            break
        else:
            print("\n???: Incorrect... Try again...")
            fail_counter += 1
            sleep(sec)
            if fail_counter >= 3:
                if Rogue == 1:
                    print(f"\n{Ally}: {Player_Name}... Do I really need to say this?")
                    sleep(sec)
                    print(f"{Ally}: Ugh... Fine... to get to the other side...")
                    sleep(sec)
                    print("\n???: Correct... Next riddle...")
                    sleep(sec)
                    break
                elif Chef == 1:
                    print(f"\n{Ally}: {Player_Name}, I know this one, let me have a crack at it!")
                    sleep(sec)
                    print(f"{Ally}: Mr. Voice, it is, to get to the other side!")
                    sleep(sec)
                    print("\n???: Correct... Next riddle...")
                    sleep(sec)
                    break
                else:
                    print("\nAs you begin to think about it more, you remember the common saying about getting to the other side.")
                    sleep(sec)
                continue
    # Riddle 2
    print("\n???: What do you call someone who takes care of hens?")
    sleep(sec)
    fail_counter = 0
    while True:
        answer = input("\nWhat is your answer?: ").lower()
        if "chicken tender" in answer:
            print("\n???: Correct again... Next riddle...")
            sleep(sec)
            break
        else:
            print("\n???: Incorrect... Try again...")
            fail_counter += 1
            sleep(sec)
            if fail_counter >= 3:
                if Rogue == 1:
                    print(f"\n{Ally}: ... Yeah okay...")
                    sleep(sec)
                    print(f"{Ally}: a chicken tender...")
                    sleep(sec)
                    print("\n???: Correct... Next riddle...")
                    sleep(sec)
                    break
                elif Chef == 1:
                    print(f"\n{Ally}: OH! I love this joke!")
                    sleep(sec)
                    print(f"{Ally}: A chicken tender!")
                    sleep(sec)
                    print("\n???: Correct again... Next riddle...")
                    sleep(sec)
                    break
                else:
                    print("\nAs you begin to think about it more, you find other words for a caregiver...\n"
                          "You're stuck on the word, 'tender'.")
                    sleep(sec)
                continue
    # Riddle 3
    print("\n???: What's a pirate's favorite letter?")
    sleep(sec)
    fail_counter = 0
    while True:
        answer = input("\nWhat is your answer?: ").lower()
        if "c" or "sea" in answer:
            print("\n???: Final riddle is... Correct.")
            sleep(sec)
            break
        else:
            print("\n???: Incorrect... Try again...")
            fail_counter += 1
            sleep(sec)
            if fail_counter >= 3:
                if Rogue == 1:
                    print(f"\n{Ally}: ... {Player_Name}, it's time to develop a sense of humor...")
                    sleep(sec)
                    print(f"{Ally}: You'd think it's 'R', but it's truly the 'C'...")
                    sleep(sec)
                    print("\n???: Final riddle is... Correct.")
                    sleep(sec)
                    break
                elif Chef == 1:
                    print(f"\n{Ally}: This is a classic from where I'm from!")
                    sleep(sec)
                    print(f"{Ally}: It's the 'C', not 'R'!")
                    sleep(sec)
                    print("\n???: Final riddle is... Correct.")
                    sleep(sec)
                    break
                else:
                    print("\nAs you begin to think about it more, Pirates typically say 'Arr', but what\n"
                          "other letter in the alphabet could sound pirate-related?")
                    sleep(sec)
                continue
    input("Press enter to proceed: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n???: You have proven yourself worthy of the humor of our lord... You may proceed to his highness...")
    sleep(sec)
    print("\nThe doors drop with a loud thud, and begin sliding slowly into the frame that held them together. The path opens before you.")
    sleep(sec)
    print("\nBefore you, by some miracle is a bridge leading directly to the castle. the entrance is plain for all to see!")
    sleep(sec)
    if Rogue == 1:
        print(f"\n{Ally}: ... Of all things to defend the fortress with... Father-styled jokes?...")
        sleep(sec)
        print(f"{Ally}: You've got to be kidding me...")
        sleep(sec)
    if Chef == 1:
        print(f"\n{Ally}: The chicken tender one gets me every time!")
        sleep(sec)
        print(f"{Ally}: If this is my sense o' humor, maybe I ought to start a family o' my own! Berate the kiddos with my own amazing jokes as\n"
              "I cook for 'em!")
        sleep(sec)
    print("\nWasting no time, you begin jogging down the great bridge straight into the castle.")
    sleep(sec)
    input("Press enter to continue: ")
    ruins_2()
            
# ========== SANCTUM ========== #
# Sanctum
def sanctum_depths():
    global Ally, Rogue, Chef, lives, lives_max, Player_Name
    os.system('cls' if os.name == 'nt' else 'clear')
    print(utils.UnderLN("Sanctum Depths"))
    sleep(sec)
    print("\n...")
    sleep(sec)
    print("\nYou begin to stir.")
    sleep(sec)
    print("\nAs you open your eyes, you begin to think you can't open them, only to realize it is incredibly dark wherever\n"
          "you ended up.")
    sleep(sec)
    print("\nYou stumble to your feet and turn back to see you've managed to break your fall through many lucky\n"
          "but rough impacts with trees shown by all the broken foliage in the crater you made.")
    sleep(sec)
    # If you have an ally, print some text to let you know they're missing
    if Rogue or Chef == 1:
        print(f"\nThe thought of {Ally} made your heart stutter. You search around frantically calling {Ally}'s name to no\n"
              "avail...")
        sleep(sec)
        print(f"\nYou can only hope they didn't have a worse fate than you.")
        sleep(sec)
    print("\nYou turn back around and search for anything that could help you.")
    sleep(sec)
    print("\nFortunately, there is a dim light ahead. It's sconces on the wall of a tunnel that seems to lead into the bowels\n"
          "of the castle.")
    sleep(sec)
    print("\nIt seems to be the only perceivable way forward, so get to it!")
    sleep(sec)
    input("\nPress enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(sec)
    print("\nAt the end of the tunnel is a series of extra tunnels and wider stretches that lead to who-knows-where. Along the\n"
          "walls of this place are shelves with an opening of 7 by 2 feet. Some have boxes in them that you'd rather not open\n"
          "and some valuable possessions alongside them.")
    sleep(sec)
    print("\nNearest to you is a shiny pouch of coins and a cluster of gemstones. Even in that small size its worth a fortune; a\n" \
          "little extra coin for your quest troubles or a deadly trap.\n")
    sleep(sec)

    # Choice loop!
    while True:
        take_coin = input("[1.       Take it. ]\n[2. Don't Take it. ]\nWhat will you do? [1 or 2]: ")
        # Remember, take_coin is a string input so when you want to reference it's value, do "1" or "2".
        if take_coin == "1":
            # Take the treasure
            print("\nNo one here is gonna need it anymore; it's better in your use than just sitting there idly!")
            sleep(sec)
            print("\nAs a matter of fact, just take whatever you can carry. What's an adventure without treasure?")
            sleep(sec)
            break
        elif take_coin == "2":
            # Do not take the treasure
            print("\nYou've been through too much to just assume things just work in your favour. Whether you prosper or not,\n"
                  "this is beneficial to raising the chances of your survival.")
            sleep(sec)
            break
        else:
            # Handle exception
            print("\n! Please choose 1 or 2. !\n")
            continue

    print("\nAs you move forward, there is a sensation that slowly, but surely grows but you can't pin it anywhere. Is it just\n"
          "anxiety? dread?")
    sleep(sec)
    print("\nNo. It feels like it's all in your head. Maybe it is in your head or maybe something is trying to communicate with\n"
          "you...")
    sleep(sec)
    print("\nJust keep moving forward. The sooner your out of here, the less this feeling is a problem.")
    sleep(sec)
    input("Press Enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(sec)
    print("\nSome time passes. Probably between 30 minutes or an hour of walking and wading through the dank and wet supposed\n"
              "catacomb/sewer-like interior.")
    sleep(sec)
    # Extra dialogue if you have a partner
    if Chef or Rogue == 1:
        print("\nSuddenly, you find something...")
        sleep(sec)
        print(f"\nUpon closer examination, it appears to be tattered peaces of {Ally}'s shirt.")
        sleep(sec)
        print("\nDid they get hurt? Is something wrong? Besides the questions, you know now that you are on the right track!")
        sleep(sec)
        print(f"\nSigns point to {Ally} traveling this path. Better follow it!")
        sleep(sec)

    print("\nYou finally come to something that looks very different. It's a cylindrical space with spiralling steps upward.")
    sleep(sec)
    print('\nAfter entering the center of the chamber, you can see light far up the top and what looks to be "not catacomb-\n' \
          '-sewer architecture!" Keep moving!')
    sleep(sec)
    print("\nSuddenly...")
    sleep(sec)
    print("\nYou stumble around failing to hold steady. A voice, thought of as earlier delusions becomes livid.")
    sleep(sec)
    print("\nIt's clear now, that the sensation from earlier is a voice... Someone else's voice...")
    sleep(sec)
    print("\nPeople's voice...")
    sleep(sec)
    # Create a spaced out version of player name.
    ghost_lingo_name = ""
    for i in range(len(Player_Name)):
        ghost_lingo_name += Player_Name[i] + " "

    print(f"\n???: . . . {ghost_lingo_name}. . .")
    sleep(sec)
    print("\nYour skin goes cold.")
    sleep(sec)
    # Judgement!!!
    if take_coin == "1":
        # You took the coins earlier
        print(f"\n???: . . . {ghost_lingo_name}. . . D o   y o u   r e a l i z e   w h a t   t a k i n g   f r o m   t h e\n"
              "   d e a d   m e a n s   f o r   y o u r   s o u l ? . .")
        sleep(sec)
        print("\n???: Y o u   w i l l   s e e . . .")
        sleep(sec)
        input("\nPress enter to continue: ")
        sanctum_depths_fight()
        return
    elif take_coin == "2":
        # You did not take the coins earlier
        print("\n???: . . .   T h o u g h   y o u   k n e w   n o t   i n   w h i c h   v a l u a b l e s   m e a n\n"
              "   t o   t h e   d e a d ,   y o u   d i d   n o t   t a k e   w h a t   w a s   n o t   y o u r s .")
        sleep(sec)
        print(f"\n???: {ghost_lingo_name} . . .   Y o u r   t r u e   w i l l   h a s   b e e n   r e a l i z e d . . .")
        sleep(sec)
        print("\nAnd just like that, the spectral weight you've been carrying dropped. On top of feeling invigorated,\n"
              "you feel that by acting for the good and conscious of others will always have merit. You feel realized.")
        sleep(sec)
        print("Keep moving forward; climb those stairs!")
        sleep(sec)
        input("Press enter to continue: ")
        sanctum()
        return

# You'll fight ghosts here; I'll figure out how later
def sanctum_depths_fight():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(utils.UnderLN("Sanctum Depths Fight"))
    print("\nCOMING SOON!")

# Crucial area before finale
def sanctum():
    # You can get here further into the sanctum, OR conversely if you 
    # have enough health to endure the dragon flames
    os.system('cls' if os.name == 'nt' else 'clear')
    print(utils.UnderLN("Sanctum"))
    print("\nCOMING SOON!")

# ========== Other methods ========== #
# Death
def game_over():
    utils.title("YOU HAVE FALLEN...")
    sleep(sec)
    os._exit(200)