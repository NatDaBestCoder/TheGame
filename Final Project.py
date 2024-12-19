import random

# Makes the time.sleep() function be called as wait()
from time import sleep as wait

# allows the playsound3.playsound() function to be called as playsound()
from playsound3 import playsound

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
    print("You have died, in the real world you where reported as missing and no one finds anything except THE GAME in its case, waiting for its next victim.")
    credits()
    wait(5)
    quit()
def credits():
    print(
    """
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
    """

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
    """

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
    """
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
    """

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
"""
  ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ 
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
     ░▒▓█▓▒░     ░▒▓████████▓▒░ ░▒▓██████▓▒░   
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
     ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░
""")
print(
"""

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
"""

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

asw = input("Do you Type in your name?/n y/n:")

while asw != "n" and asw != "y":
    asw = input("INVALID ANSWER \nDo you Type in your name?/n y/n:")
    
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
while w != 3 and l != 3:
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
if t == 0:
    lives = 4
print(result)
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
injury = False
rr = True
number = random.randrange(0,100)
while rr == True or guess == number:
    low = 0
    high = 100
    print("Guess ",r)
    if injury == True:
    # line not found
        print(10-r, " Guesses remaining") 
    else:
        print(15-r," Guesses remaining")
    wait(1)
    print("Range for number is ", low, " =< NUMBER >= ", high)
    wait(1)
    guess = input("What Number do you press?")
    while guess not in range(0,101) or guess < low or guess > high+1:
        print("You go to press the ",guess," key but its not there")
        guess = input("What Number do you press?")
    if r == 1:
        if guess < number:
            print("You go and press ", guess, " key, it goes down and falls into what seems to be a void.")
        elif guess > number:
            print("You go and press ", guess, " key, it and all the keys above it fall into what seems to be a void.")
        wait(2)
    
        print("Suddenly you have this intrusive thought, \"What would happen if I stuck a part of me in there?\"")
        wait(1)
        asw = input("Do you Stick in a part of your body?\nValid answers are no/finger/hand/shoulder/everything")
        if asw == "finger":
            print("As you put in the finger, you feel a tearing sensation as your finger is torn off your hand, You scream in agony and the walls move in 5 slots.")
    print("You go and press ", guess, " key, it goes down and disappears")
if guess == number:
    print("You go and press ", guess, " key, all the keys above and below it fall into the void. The only key that does not fall is the one you pressed")
    wait(2)
else:
    print("You go and press ", guess, " key, all the keys fall into the void.")
    ending()
##      describe teleporting to a room with 2 pianos and spikes behind you
##  start playing guess the number
##  rules: you must guess the number in under 15 tries pressing the piano key that corresponds to the number
##  to the left is 1 and the far right is 100
##  the piano keys fall out of the piano into a void dimension that opens in the piano
##  have the option to stick hand into the void, if they do they get to decide how far they 
##  put their hand in options are "Just pinky" "pointer" "hand" "up to elbow" "up to shoulder" and "what the worst that could happen(head)
##  you lose what you put into the void because the void is actually outerspace
##  if full body was put in void
##      describe the popping of their head as they are sucked into the void
##      quit game
##  if they put in shoulder or elbow they are bleeding heavily
##  they are reduced to 10 tries
##  if they fail to guess in 15 or 10 tries they are stabbed by the wall of spikes
##  if they win, they are healed one level up, (if up to shoulder they get their upper arm back) and bleeding slows a bit
##  congrats at guessing
## you are then teleported to a jeopardy style room but its all paper mache
## you do trivia with 3 lives 
## 
##  if you won rps with no losses then you get 4 lives
## if you fail trivia then the paper mache unfolds and starts giving paper cuts, killing you by a thousand cuts
##  if you win trivia you wake up in the video game store where you bought the game and you are holding the game about to buy it
## You Have all the injury from the game
## you freak out and snap the game in half causing a small explosion to go off and you are thrown to the back of the store and pass out,
## you wake at the hospital, handcuffed to the bed.
##  a officer comes in and say you are being charged with terrorism and its a miracle you were not injured because the explosion demolish the building
## you ask about your INJURY FROM GAME and a nurse comes in and says you always had that

# line not found