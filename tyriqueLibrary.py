# Tyrique Mowatt
#Nov 10, 2022
# Function for menuChoice, Start, Continuation

# Retrun: None
# Parameters: none
# Purpose: Deisplay the different choices to the player before starting the game
# MENUCHOICES
# If statment for the the player if they would to play with another player
# Or a computer Instead
# Ask the player to select the diffculty
def MenuChoice():
    userAnswer = 0
    
    while userAnswer != 1 and userAnswer !=2 and userAnswer != 3:
        try:
            print("\nMenu: ")
            print("1) Start game \n2) Highscore \n3) Exit Game")
            userAnswer = int(input("\nPlease Type here: "))
            if userAnswer != 1 and userAnswer != 2 and userAnswer != 3:
                print("/nPlease type 1, 2,or 3/n")
        except:
            print("/nPlease type 1, 2,or 3/n")

    return(userAnswer)    


# Return: None
# Parameters: None
# Purpose: Asking the plyer if they would like to start game now
# GETSTART
def GetStart():
    start = ""
    while start != "yes":
        start = input("\nThis is a final check to make sure your ready. Make sure both players"
          " are here and ready. Type yes when ready to play: ").lower()
        if start != "yes" and start != "no":
            print("\nYou did not type a valid response. Please try again.")
        elif start == "no":
            print("\nAlrighty then, take your time to get ready. We will ask"
                  " the same question again, and respond 'yes' when ready")
            
    



# Return: None
# Parameters: None
# Purpose: Ask the the if they would like to continue the game
# USERCONTINUATION
# If statement for the player want to play the game again
def UserContinuation():
    playAgain = ""
    while playAgain != "yes" and playAgain != "no":
        playAgain = input("Play again(yes or no)? ").lower()
        if playAgain != "yes" and playAgain != "no":
            print("You didn't type a valid response. Please try again")

    return(playAgain)

