# Program to Play the Rock, Paper, Scissors Game

from random import randint
    
# Write the inputs required
Games=["Rock","Paper","Scissors"]

# Initially set the Player to False
Player=False

#Computer Randomly Pick the one word from the list games 
Computer= Games[randint(0,2)]

while Player == False:
    Player = input("enter your choice Rock, Paper, Scissors?")
    if Player == Computer:
        print("Game Tied")
    elif Player == "Rock":
        if Computer == " Paper":
            print(" You Loose...!!", Computer, "covers",Player)
        else:
            print("You Win...!!", Computer, "Smashes", Player)
    elif Player == "Paper":
        if Computer == " Scissors":
            print("You Loose...!!",Computer, "Cuts",Player)
        else:
            print("You Win..!!",Player, "Covers",Computer)
    elif Player == "Scissors":
        if Computer == "Rock":
            print("You loose...!!", Computer, "Smashes", Player)
        else:
            print("You Win...!!", Player,"Cuts", Computer)
#    Here Player Can Enter "Stop" to stop the Game         
    elif Player == "Stop":
        print("Well Played Thank You... !! Bye...!!")
        break
    else:
        print("Pick Correct Word, Check Your Spelling")
    Player=False
    Computer=Games[randint(0,2)]
        
