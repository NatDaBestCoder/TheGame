import random
# Makes the time.sleep() function be called as wait()
from time import sleep as wait
# allows the playsound3.playsound() function to be called as playsound()
from playsound3 import playsound
# skips the rps portion for testing 1 = true 0 = false
dev = 0
namec = " "
# wins losses and ties in rps
w = 0
l = 0
t = 0
# rounds for rps
r = 1
# used to see if they have typed in their name yet at line 272
q = 0
# rps list of things computer can pick
pick = ["rock", "paper", "scissors"]

#happens after every death
def ending():
    print("You have died, in the real world you were reported as missing and no one finds anything except THE GAME in its case, waiting for its next victim.")
    wait(5)
    credits()
    wait(5)
    quit()
def credits():
    print(
    r"""
      _____              __  __   ______      _____   _____    ______              _______   ______   _____      ____   __     __
     / ____|     /\     |  \/  | |  ____|    / ____| |  __ \  |  ____|     /\     |__   __| |  ____| |  __ \    |  _ \  \ \   / /
    | |  __     /  \    | \  / | | |__      | |      | |__) | | |__       /  \       | |    | |__    | |  | |   | |_) |  \ \_/ / 
    | | |_ |   / /\ \   | |\/| | |  __|     | |      |  _  /  |  __|     / /\ \      | |    |  __|   | |  | |   |  _ <    \   /  
    | |__| |  / ____ \  | |  | | | |____    | |____  | | \ \  | |____   / ____ \     | |    | |____  | |__| |   | |_) |    | |   
     \_____| /_/    \_\ |_|  |_| |______|    \_____| |_|  \_\ |______| /_/    \_\    |_|    |______| |_____/    |____/     |_|   
                                                                                                                                
                                                                                                                                
                                         _   _              _______   _    _              _   _   _____   ______   _           
                                        | \ | |     /\     |__   __| | |  | |     /\     | \ | | |_   _| |  ____| | |          
                                        |  \| |    /  \       | |    | |__| |    /  \    |  \| |   | |   | |__    | |          
                                        | . ` |   / /\ \      | |    |  __  |   / /\ \   | . ` |   | |   |  __|   | |          
                                        | |\  |  / ____ \     | |    | |  | |  / ____ \  | |\  |  _| |_  | |____  | |____      
                                        |_| \_| /_/    \_\    |_|    |_|  |_| /_/    \_\ |_| \_| |_____| |______| |______|
    """)
    wait(3)
    print(
    r"""

     __  __   _    _    _____   _____    _____     ____   __     __                       
    |  \/  | | |  | |  / ____| |_   _|  / ____|   |  _ \  \ \   / /                       
    | \  / | | |  | | | (___     | |   | |        | |_) |  \ \_/ /                        
    | |\/| | | |  | |  \___ \    | |   | |        |  _ <    \   /                         
    | |  | | | |__| |  ____) |  _| |_  | |____    | |_) |    | |                          
    |_|  |_|  \____/  |_____/  |_____|  \_____|   |____/     |_|                          
                                                                                        
                                                                                        
                         _____    _____  __   __             ____              __     __
                        |  __ \  |_   _| \ \ / /     /\     |  _ \      /\     \ \   / /
                        | |__) |   | |    \ V /     /  \    | |_) |    /  \     \ \_/ / 
                        |  ___/    | |     > <     / /\ \   |  _ <    / /\ \     \   /  
                        | |       _| |_   / . \   / ____ \  | |_) |  / ____ \     | |   
                        |_|      |_____| /_/ \_\ /_/    \_\ |____/  /_/    \_\    |_|
    """)
    wait(3)
    print(
    r"""

      _____   _______    ____    _____   __     __   __          __  _____    _____   _______   _______   ______   _   _     ____   __     __
     / ____| |__   __|  / __ \  |  __ \  \ \   / /   \ \        / / |  __ \  |_   _| |__   __| |__   __| |  ____| | \ | |   |  _ \  \ \   / /
    | (___      | |    | |  | | | |__) |  \ \_/ /     \ \  /\  / /  | |__) |   | |      | |       | |    | |__    |  \| |   | |_) |  \ \_/ / 
     \___ \     | |    | |  | | |  _  /    \   /       \ \/  \/ /   |  _  /    | |      | |       | |    |  __|   | . ` |   |  _ <    \   /  
     ____) |    | |    | |__| | | | \ \     | |         \  /\  /    | | \ \   _| |_     | |       | |    | |____  | |\  |   | |_) |    | |   
    |_____/     |_|     \____/  |_|  \_\    |_|          \/  \/     |_|  \_\ |_____|    |_|       |_|    |______| |_| \_|   |____/     |_|   
                                                                                                                                            
                                                                                                                                            
                             _   _              _______   _    _              _   _   _____   ______   _                                   
                            | \ | |     /\     |__   __| | |  | |     /\     | \ | | |_   _| |  ____| | |                                  
                            |  \| |    /  \       | |    | |__| |    /  \    |  \| |   | |   | |__    | |                                  
                            | . ` |   / /\ \      | |    |  __  |   / /\ \   | . ` |   | |   |  __|   | |                                  
                            | |\  |  / ____ \     | |    | |  | |  / ____ \  | |\  |  _| |_  | |____  | |____                              
                            |_| \_| /_/    \_\    |_|    |_|  |_| /_/    \_\ |_| \_| |_____| |______| |______|
    """)
    wait(3)
    print(
    r"""
     _____    _                  __     __  _______   ______    _____   _______   ______   _____     _____                    
    |  __ \  | |          /\     \ \   / / |__   __| |  ____|  / ____| |__   __| |  ____| |  __ \   / ____|                   
    | |__) | | |         /  \     \ \_/ /     | |    | |__    | (___      | |    | |__    | |__) | | (___                     
    |  ___/  | |        / /\ \     \   /      | |    |  __|    \___ \     | |    |  __|   |  _  /   \___ \                    
    | |      | |____   / ____ \     | |       | |    | |____   ____) |    | |    | |____  | | \ \   ____) |                   
    |_|      |______| /_/    \_\    |_|       |_|    |______| |_____/     |_|    |______| |_|  \_\ |_____/                    
                                                                                                                            
                                                                                                                            
                                         _   _              _______   _    _              _   _   _____   ______   _        
                                        | \ | |     /\     |__   __| | |  | |     /\     | \ | | |_   _| |  ____| | |       
                                        |  \| |    /  \       | |    | |__| |    /  \    |  \| |   | |   | |__    | |       
                                        | . ` |   / /\ \      | |    |  __  |   / /\ \   | . ` |   | |   |  __|   | |       
                                        | |\  |  / ____ \     | |    | |  | |  / ____ \  | |\  |  _| |_  | |____  | |____   
                                        |_| \_| /_/    \_\    |_|    |_|  |_| /_/    \_\ |_| \_| |_____| |______| |______|  
                                                                                                                            
                                                                                                                            
                                         __  __   _____    _____              _    _                                        
                                        |  \/  | |_   _|  / ____|     /\     | |  | |                                       
                                        | \  / |   | |   | |         /  \    | |__| |                                       
                                        | |\/| |   | |   | |        / /\ \   |  __  |                                       
                                        | |  | |  _| |_  | |____   / ____ \  | |  | |                                       
                                        |_|  |_| |_____|  \_____| /_/    \_\ |_|  |_|                                       
                                                                                                                            
                                                                                                                            
                                                    _   _   _____       ____    _______   _    _   ______   _____     _____ 
                                            /\     | \ | | |  __ \     / __ \  |__   __| | |  | | |  ____| |  __ \   / ____|
                                           /  \    |  \| | | |  | |   | |  | |    | |    | |__| | | |__    | |__) | | (___  
                                          / /\ \   | . ` | | |  | |   | |  | |    | |    |  __  | |  __|   |  _  /   \___ \ 
                                         / ____ \  | |\  | | |__| |   | |__| |    | |    | |  | | | |____  | | \ \   ____) |
                                        /_/    \_\ |_| \_| |_____/     \____/     |_|    |_|  |_| |______| |_|  \_\ |_____/ 
                                                                                                                            
                                                                                                                            

    """)
    wait(3)
    print(
    r"""

      _____   _____    ______    _____   _____              _          _______   _    _              _   _   _  __   _____                  
     / ____| |  __ \  |  ____|  / ____| |_   _|     /\     | |        |__   __| | |  | |     /\     | \ | | | |/ /  / ____|                 
    | (___   | |__) | | |__    | |        | |      /  \    | |           | |    | |__| |    /  \    |  \| | | ' /  | (___                   
     \___ \  |  ___/  |  __|   | |        | |     / /\ \   | |           | |    |  __  |   / /\ \   | . ` | |  <    \___ \                  
     ____) | | |      | |____  | |____   _| |_   / ____ \  | |____       | |    | |  | |  / ____ \  | |\  | | . \   ____) |                 
    |_____/  |_|      |______|  \_____| |_____| /_/    \_\ |______|      |_|    |_|  |_| /_/    \_\ |_| \_| |_|\_\ |_____/                  
                                                                                                                                            
                                                                                                                                            
                         __  __   _____    _____   _    _              ______   _         __          __  _____   ______   _   _    _____ 
                        |  \/  | |_   _|  / ____| | |  | |     /\     |  ____| | |        \ \        / / |_   _| |  ____| | \ | |  / ____|
                        | \  / |   | |   | |      | |__| |    /  \    | |__    | |         \ \  /\  / /    | |   | |__    |  \| | | (___  
                        | |\/| |   | |   | |      |  __  |   / /\ \   |  __|   | |          \ \/  \/ /     | |   |  __|   | . ` |  \___ \ 
                        | |  | |  _| |_  | |____  | |  | |  / ____ \  | |____  | |____       \  /\  /     _| |_  | |____  | |\  |  ____) |
                        |_|  |_| |_____|  \_____| |_|  |_| /_/    \_\ |______| |______|       \/  \/     |_____| |______| |_| \_| |_____/
    """)
    wait(5)
# rps functions
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
#       Keep like this for a way to die stupidly
##    while user_choice not in pick:
##        user_choice = input("INVALID CHOICE \n Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(pick)

def winner(user_choice, computer_choice):
    global t
    global w
    global l
    if user_choice == computer_choice:
        t += 1
        return "It's a tie! J says \"Great Minds think alike\""
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        w += 1
        return "You win! J becomes a bit more mad"
    elif user_choice not in pick:
        print("You play ", user_choice," as J plays ", computer_choice,". J says, \"What the heck is that?\" You respond, \"",user_choice,"?\"")
        wait(2)
        print("\"Thats not a valid choice idiot\" J grabs you and crushes you")
        ending()
    else:
        l += 1
        return "You lose! J says nothing except a small smirk"

input("Please Fullscreen before continuing press enter when ready")
playsound('music/yes.wav', False)
print("It's March 3rd 2000, You just got home from gamestop with this new game called")
wait(2)
print(
r"""
  ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ 
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
     ░▒▓█▓▒░     ░▒▓████████▓▒░ ░▒▓██████▓▒░   
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░
""")
print(
r"""

 ░▒▓██████▓▒░   ░▒▓██████▓▒░   ░▒▓██████████████▓▒░  ░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒▒▓███▓▒░ ░▒▓████████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████▓▒░   
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
 ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ 
""")
wait(2)

print("The cover art is just abstract colors, and the disk is silver with no indication it is a game")
wait(1)

print("You speed on over to your computer to play it. As you wait for it to load you go get something to drink.")
wait(4)

print("As you walk back into your room there is a thudding noise.")
wait(5)

print("Its your drink hitting the ground.")
wait(6)

print("Although, you never hear the noise. You become Unconscious.")
wait(10)

credits()

print(
r"""

             _   _     _    _   _   _   _  __  _   _    ____   __          __  _   _          
     /\     | \ | |   | |  | | | \ | | | |/ / | \ | |  / __ \  \ \        / / | \ | |         
    /  \    |  \| |   | |  | | |  \| | | ' /  |  \| | | |  | |  \ \  /\  / /  |  \| |         
   / /\ \   | . ` |   | |  | | | . ` | |  <   | . ` | | |  | |   \ \/  \/ /   | . ` |         
  / ____ \  | |\  |   | |__| | | |\  | | . \  | |\  | | |__| |    \  /\  /    | |\  |         
 /_/    \_\ |_| \_|    \____/  |_| \_| |_|\_\ |_| \_|  \____/      \/  \/     |_| \_|         
                                                                                              
                                                                                              
             __  __    ____    _    _   _   _   _______      ____    ______                   
     /\     |  \/  |  / __ \  | |  | | | \ | | |__   __|    / __ \  |  ____|                  
    /  \    | \  / | | |  | | | |  | | |  \| |    | |      | |  | | | |__                     
   / /\ \   | |\/| | | |  | | | |  | | | . ` |    | |      | |  | | |  __|                    
  / ____ \  | |  | | | |__| | | |__| | | |\  |    | |      | |__| | | |                       
 /_/    \_\ |_|  |_|  \____/   \____/  |_| \_|    |_|       \____/  |_|                       
                                                                                              
                                                                                              
  _______   _____   __  __   ______     _____                _____    _____   ______    _____ 
 |__   __| |_   _| |  \/  | |  ____|   |  __ \      /\      / ____|  / ____| |  ____|  / ____|
    | |      | |   | \  / | | |__      | |__) |    /  \    | (___   | (___   | |__    | (___  
    | |      | |   | |\/| | |  __|     |  ___/    / /\ \    \___ \   \___ \  |  __|    \___ \ 
    | |     _| |_  | |  | | | |____    | |       / ____ \   ____) |  ____) | | |____   ____) |
    |_|    |_____| |_|  |_| |______|   |_|      /_/    \_\ |_____/  |_____/  |______| |_____/ 
                                                                                              
                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

""")
wait(5)
playsound('music/ambient.mp3',False)
print("As you come to your senses, you see you are in a pure white room.")
wait(2)

print("The room feels like it is spinning, your head pounding. You suddenly hear something...")
wait(2.5)

print("As the room slowly stops spinning, you are able to understand what the noise is.")
wait(1.5)

print("Its a voice, but something about it does not sound right.")
wait(2.5)

print("It sounds mechanical... but it also sounds human-like.")
wait(2.5)

print("You realize that you probably should not be focusing on what it sounds like, instead you focus on what it is saying.")
wait(2.5)

print("As you focus on the words it is saying you hear, \"Welcome to THE GAME! Here you will play 3 different games to Escape with your life\"")
wait(2.5)

print("It continues to speak, never stopping to breathe; \"The first game is ROCK PAPER SCISSORS, the second game is GUESS THE NUMBER, the third game is TRIVIA ON GENERAL SUBJECTS.\"")
wait(2.5)

print("It stops talking for a second and then says in a more harsh tone, \"Please Enter Name to agree to Terms and Conditions\"")
wait(1)

while namec != "y":
    name = input("Come to think of it, you can't remember anything other than this room. What is your name? (TYPE IN NAME NOW)").title()
    namec = input(name + " Is this correct? y/n:")
    while namec != "n" and namec != "y":
        namec = input("INVALID ANSWER \n"+ name+ " Is this correct? y/n:")
wait(1)

print("after thinking for a moment you pick a name you do remember,", name,", although you know its not yours")
wait(2.5)

print("\"Please Enter Name To Agree To Terms And Conditions\" it says louder and more harsh, thats when you notice the keyboard that is floating right in front of you")
wait(1.5)

asw = input("Do you Type in your name?\ny/n:")

while asw != "n" and asw != "y":
    asw = input("INVALID ANSWER \nDo you Type in your name?\ny/n:")
    
if asw == "n":

    print("You decide not to type in your name and instead sit there with your arms crossed; this was a bad decision, the voice asks once more to enter your name")
    wait(2.5)

    print("Although this time it said something extra at the end, \"If you do not sign in the next 30 seconds you will quit the game\"")
    wait(1.5)

    asw = input("Do you Type in your name now? \n y/n:")
    while asw != "n" and asw != "y":
        asw = input("INVALID ANSWER \nDo you Type in your name now?/n y/n:")
    
    if asw == "n":
        print("As you continue to sit there in spite, the walls close in slowly, the keyboard is gone, and the voice says, \"QUITTING GAME\". You panic as the walls slowly begin to close in faster and faster")
        wait(1.5)

        print("You try as much as you can to keep the walls from closing in more, all in vain. the walls become so close you can only stay there in a ball, but the walls don't care, They crush you")
        wait(2)
        
        ending()
    else:
        print("You rush to Type in your name. You finish typing in time. the voice then says \"Welcome ",name.upper()," To THE GAME\"")
        wait(2)
        q = 1
elif q == 0:
    print("You type in your name. The voice then says \"Welcome ",name.upper()," To THE GAME\"")
    wait(1)

print("You feel funny then your vision goes fuzzy and then a bright flash of colors rendering your eyes useless, making the headache worse.")
wait(1.5)

print("You try to hold your head in your hands, but you can't move. You feel as though you are weightless. This lasts for what feels like 15 seconds.")
wait(2)

print("When it stops you feel a sharp pain in your knees as if you jumped off a 3 foot ledge only to land on your knees. Thats when you feel a floor hit your head because you forgot about gravity")
wait(2)

print("As you recover your vision you see a yellow room with what you HOPE is dirty water in the corners of the room. It has a linoleum floor that seems to be rotted as you try to stand up.")
wait(2)

print("As you stand up you throw up presumably because your senses were overloaded during what happened. You try to figure out what that was and your only conclusion was teleportation")
wait(2)

print("You wipe the spit off your mouth as you hear the voice again.")
wait(1.5)

print("\"Game 1, ROCK,PAPER,SCISSORS. RULES are as follows, ROCK beats SCISSORS, PAPER beats ROCK, SCISSORS beats PAPER, and you MUST win 3 times before J does to continue\"")
wait(2)

print("\"Who the heck is J?\" You say aloud. You get your answer as a Giant fist emerges from the ugly yellow wall, it makes a mouth with its hands as two evil looking googly eyes appear on top")
wait(2)

print("In a booming voice the hand says, \"I am J, Ready to play?\"")
wait(0.5)

asw = input("You hesitate for a moment and then answer..? Pick y/n:")
while asw != "n" and asw != "y":
    asw = input("INVALID ANSWER \nWhat do you answer?/n y/n:")
if asw == "n":
    print("\"No\" You say firmly. \"Wrong choice buddy\" says J in his booming voice. J grabs you and crushes you in his hand")
    wait(2)

    ending()
print("\"Great! Lets Begin\" he somehow makes a face that looks like >:}")
wait(2)
# this is rock paper scissors
while w != 3 and l != 3 and dev == 0:
    print("Round", r)
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose: " + user_choice.title())
    wait(1)
    print("J chose: " + computer_choice.title())
    result = winner(user_choice, computer_choice)
    print(result)
    print(w,"-",l,"-",t)
    wait(1)
    r = r + 1
if l == 3:
    print("\"HAHAHA loser!\" J grabs you and slowly squeezes you till you pop")
    wait(2)
    print("After you die J covers himself in your fluids and learns all of your knowledge and becomes stronger")
    wait(4)
    ending()
if t == 0 and l == 0:
    lives = 4
wait(2)

print("You somehow win Rock Paper Scissors. J does not seem to be happy about this.")
wait(2)

print("thats when you hear what seems to be jello tearing; J falls off the wall wiggling in agony, the wall is bleeding and so is J.")
wait(2)

print("J stops moving and disappears as the \"Teleportation\" occurs again")    
wait(2)

print("This time you aren't as nauseous. When the \"Teleporting\" is done you aren't on the floor instead you are standing behind 2 pianos.")
wait(2)

print("You hear the voice again, \"Welcome to GUESS THE NUMBER, Here you must guess the number in under 20 guesses. In front of you are 2 pianos, each key corresponds to a number\"")
wait(2)

print("You notice that some of the piano keys are missing and have been replaced by plywood.")
wait(1)
print("The voice says, \"Begin\"")
injury = False
rr = True
guess = ()
r = 0
low = 0
# line not found
high = 100
numberg = []
number = int(random.randrange(0,100))
while rr == True and guess != number:
    r = r+1
    if injury == True:
        print(11-r, " Guesses remaining") 
        if r == 10:
            rr = False
    elif r >= 2:
        print(16-r," Guesses remaining")
        if r == 15:
            rr = False
    wait(1)
    print( low, " is greater than or equal to NUMBER is less than or equal to ", high)
    wait(1)
    guess = int(input("What Number do you press?"))
    if guess < low or guess > high:
        print("(INVALID ANSWER)   You go to press ", guess," but its not there")
        guess = int(input("What Number do you press?"))  
    if r == 1:
        if guess < number:
            print("You go and press ", guess, " key, it goes down and falls into what seems to be a void.")
            low = guess+1
        elif guess > number:
            print("You go and press ", guess, " key, it and all the keys above it fall into what seems to be a void.")
            high = guess-1
        wait(2)
        print("As you stare at the void, you hear a large rumbling as the wall behind you generates spikes and moves closer. You start examining the room for a way out when the wall stops.")
        wait(2)
        print("You notice slots on the side walls that the spike wall seems to stop at. You count the slots in the walls and you see 14.")
        wait(2)
        print("You turn back to the pianos. Suddenly you have this intrusive thought, \"What would happen if I stuck a part of me in there?\"")
        wait(1)
        asw = input("Do you Stick in a part of your body?\nValid answers are no/finger/hand/shoulder/everything:  ")
        if asw == "finger":
            injury = True
            itype = "finger"
            print("As you put in the finger, you feel a tearing sensation as your finger is torn off your hand, You scream in agony and the walls move in 5 slots.")
            wait(2)
            print("You are bleeding from your missing finger, but since the wound is so small you can help stop the bleeding with a piece of your shirt")
        elif asw == "hand":
            injury = True
            itype = "hand"
            print("As you put in your hand, you feel a tearing sensation as your hand is torn off your arm, You scream in agony and the walls move in 5 slots.")
            wait(2)
            print("Your injury is bleeding a lot but you where in the boy scouts when you where 5 and make a tourniquet from your shirt and a pen you find in the piano")
        elif asw == "shoulder":
            injury = True
            itype = "shoulder"
            print("As you put in your whole arm, you feel a tearing sensation as your arm is torn from the socket, you scream in agony and the wall moves 5 slots closer")
            wait(2)
            print("You are bleeding heavily from your shoulder, you make a makeshift bandage with your shirt tied around your torso. The bandage only makes the blood not go everywhere")

        elif asw == "everything":
            print("You think, \"Whats the worst that could happen?\" You Go over and get on top of the piano and you jump in. You are sucked into the void")
            wait(2)
            print("After jumping in, all the air is sucked out of your lungs. You feel like you are boiling and your last thought is, \"This was a bad ide-\"")
            wait(2) 
            print("Your head explodes and you die")
            wait(2)
            ending()
        else:
            itype = "none"
        wait(2)
        if injury == True:
            print("You remember hearing the walls move again, you turn around and count the slots, you just lost 5 guesses. \"Curiosity kills the cat\" You say under your breath")
    
    else:
        if guess < number:
            print("You go and press ", guess, " key, it and all the keys below it fall into the void.")
            low = guess + 1
        elif guess > number:
            print("You go and press ", guess, " key, it and all the keys above it fall into the void.")
            high = guess - 1
if guess == number:
    print("You go and press ", guess, " key, all the keys above and below it fall into the void. The only key that does not fall is the one you pressed")
    wait(2)
else:
    print("You go and press ", guess, " key, all the keys fall into the void.")
    wait(2)
    print("The spikes are now touching you and slowly impales you.")
    wait(2)
    ending()
print("The voice comes back, \"Congrats at Guessing, time for some TRIVIA ON GENERAL SUBJECTS\"")
wait(2)
this = (True,False,False,False,False,False,False)
asw = random.choice(this)
if injury == True and asw == True:
    print("You teleport, this time you are not effected but your injury is no longer bleeding and seems to be scabbed over.")
elif injury == True and asw == False:
    print("You teleport, this time you are not effected but your bleeding is slowed and is just oozing blood now.")
else:
    print("You teleport, this time it does not effect you at all")
wait(2)
print("you notice that you are in a room that is made with Papier-mâché. It also looks like the show called jeopardy")
wait(2)
print("The voice says, \"This is TRIVIA, here you must answer questions correctly, you have 3 lives, you lose a life anytime you get a question wrong")
wait(2)
if lives == 4:
    print("the voice says quickly, \"You Beat J with no losses so you get 4 lives to start\"")
    wait(2)
else: lives = 3
print("You expect the voice say begin, The voice continues, Question 1\nWhat is the Year?(IN GAME YEAR)")
that = ("a","b","c","d")
asw = input("A: 2024\nB: 1999\nC: 2000\nD: 2176\n Pick A/B/C/D:  ").lower()
while asw not in that:
    print("INVALID ANSWER")
    asw = input("A: 2024\nB: 1999\nC: 2000\nD: 2176\n Pick A/B/C/D:  ").lower()
if asw == "c":
    print("You Hear a ding and the voice says, \"CORRECT\"")
    wait(2)
else:
    print("You hear a Buzzer and the voice says, \"WRONG\"\none of the papers fly over to you and gives you a paper cut")
    wait(2)
    lives = lives - 1
    print(lives, "LIVES REMAINING")
wait(3)
print("QUESTION 2")
wait(1)
print("What was the name of the Hand that played Rock, Paper, Scissors against you?")
wait(1.5)
asw = input("A: Jay\nB: J\nC: Jayson\nD: Kye\n Pick A/B/C/D:  ").lower()
while asw not in that:
    print("INVALID ANSWER")
    asw = input("A: Jay\nB: J\nC: Jayson\nD: Kye\n Pick A/B/C/D:  ").lower()
if asw == "b":
    print("You Hear a ding and the voice says, \"CORRECT\"")
    wait(2)
else:
    print("You hear a Buzzer and the voice says, \"WRONG\"\nOne of the papers fly over to you and gives you a paper cut")
    wait(2)
    lives = lives - 1
    print(lives, " LIVES REMAINING")
wait(3)
print("QUESTION 3")
wait(1)
print("How do you enter a number in GUESS THE NUMBER?")
wait(1.5)
asw = input("A: Fingers\nB: Voice\nC: Keyboard\nD: Piano\n Pick A/B/C/D:  ").lower()
while asw not in that:
    print("INVALID ANSWER")
    asw = input("A: Fingers\nB: Voice\nC: Keyboard\nD: Piano\n Pick A/B/C/D:  ").lower()
if asw == "d":
    print("You Hear a ding and the voice says, \"CORRECT\"")
    wait(2)
else:
    print("You hear a Buzzer and the voice says, \"WRONG\"\nOne of the papers fly over to you and gives you a paper cut")
    wait(2)
    lives = lives - 1
    print(lives, " LIVES REMAINING")
if lives == 0:
    print("The room falls apart and all the paper give you paper cuts. killing you by a thousand cuts")
    wait(3)
    ending()


print("QUESTION 4")
wait(1)
print("What Color was the disk this game resides on?")
wait(1.5)
asw = input("A: Blue\nB: Silver\nC: Clear\nD: Black\n Pick A/B/C/D:  ").lower()
while asw not in that:
    print("INVALID ANSWER")
    asw = input("A: Blue\nB: Silver\nC: Clear\nD: Black\n Pick A/B/C/D:  ").lower()
if asw == "b":
    print("You Hear a ding and the voice says, \"CORRECT\"")
    wait(2)
else:
    print("You hear a Buzzer and the voice says, \"WRONG\"\nOne of the papers fly over to you and gives you a paper cut")
    wait(2)
    lives = lives - 1
    print(lives, " LIVES REMAINING")
if lives == 0:
    print("The room falls apart and all the paper give you paper cuts. killing you by a thousand cuts")
    ending()


print("QUESTION 5")
wait(1)
print("BONUS QUESTION: Was this game fun?")
wait(1.5)
asw = input("A: Yes\nB: No\nC: NO\nD: N O\n Pick A/B/C/D:  ").lower()
while asw not in that:
    print("INVALID ANSWER")
    asw = input("A: Yes\nB: No\nC: NO\nD: N O\n Pick A/B/C/D:  ").lower()
if asw == "a":
    print("You Hear a ding and the voice says, \"CORRECT\"")
    wait(2)
else:
    print("You realize that that may have been a bad answer because you hear a large rumbling and then you die in every possible way over and over again")
    ending()
    
print("\"Congratulations On winning all games\", Says the voice in a slowing tone, you blink and suddenly you are back at gamestop about to buy the game.")
wait(2)
print("In fear, you snap the disk in half causing an explosion. You are flung to the back of the store and you black out")
wait(3)
if itype == "shoulder":
    print("You wake up in a hospital, your nose is itchy and you try to itch it but your hand is stopped, you try the other hand, but you don't feel anything")
    wait(4)
    print("you look down to see your arm missing and your other arm handcuffed to the bed, a police officer is in the room with you and says,\"Bold of you to bomb a game stop, you lost an arm doing that\"")

elif itype == "hand":
    print("You wake up in a hospital, your nose is itchy and you try to itch it but your hand is stopped by something, too weak to fight the force, you try the other hand, and all that comes to itch your nose is a stump at your wrist")
    wait(4)
    print("You look down to see your other arm handcuffed to the bed, a police officer is in the room with you and says,\"Bold of you to bomb a game stop, you're lucky to just lose a hand\"")

elif itype == "finger":
    print("You wake up in a hospital, your nose is itchy and you try to itch it but your hand is stopped by something, too weak to fight the force, you try the other hand, it is also stopped")
    wait(4)
    print("You look down to see both your arms handcuffed to the bed, you are missing one finger, a police officer is in the room with you and says,\"Bold of you to bomb a game stop, you're lucky to just lose a finger\"")

else:
    print("You wake up in a hospital, your nose is itchy and you try to itch it but your hand is stopped by something, too weak to fight the force, you try the other hand, it is also stopped")
    wait(4)
    print("You look down to see your other arm handcuffed to the bed, a police officer is in the room with you and says,\"Bold of you to bomb a game stop, you're lucky you don't have any major injuries\"")
wait(3)
print("ONE MONTH LATER\nYou Are in a mental asylum due to your outlandish story of a game that does not exist, that can teleport you and you had no part in the bombing")
wait(5)
print("The Doctors say you have PTSD from something and you can't be tried for the bombing because of insanity")
wait(4)
if injury == False:
    print("This is the Good ending")
else:
    print("This is the Bad Ending")
wait(4)
credits()
print("THE END\nThank you for playing my game, this took about 1 week to make. I hope this was fun!")
wait(1)
print("Quitting Game in 3")
wait(1)
print("Quitting Game in 2")
wait(1)
print("Quitting Game in 1")
wait(1)
print("Quitting Game in 0")
quit()