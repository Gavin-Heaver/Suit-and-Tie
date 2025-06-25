#Gavin Heaver, Trrique Mowatt, Quinton Williamceau
#November 13, 2022
#This program will have the user guess what type of card is randomly choosen,
#and give points to the user or users if correct


#import all files
from gavinFinalLibrary import welcomePage, highScore, cardShuffle, userChoice, tieGame, victoryScreen, scoreCompare
from quintonLibrary import userName, outro, exitGame
from tyriqueLibrary import MenuChoice, GetStart, UserContinuation

#define main function
def main():
    #define constants and variables
    userName1 = ""
    userName2 = ""
    userContinuation = ""
    playAgain = "yes"
    backToMenu = ""
    ranCards = []
    ranCardsTie = []
    points1 = 0
    points2 = 0
    turns = 0
    menuAnswer = 0
    
    #get welcomePage ()
    welcomePage()
    #get menuChoice ()
    while playAgain == "yes":
        while menuAnswer != 1 and menuAnswer != 3:
            menuAnswer = MenuChoice()
        #get highScore
            if menuAnswer == 2:
                backToMenu = highScore()
        #get start ()
        while playAgain == "yes":
            if menuAnswer == 1:
                GetStart()
            #get userName ()
                userName1, userName2 = userName()
            #get cardShuffle ()
                ranCards, ranCardsTie = cardShuffle()
            #get userChoice ()
                points1, points2, turns = userChoice(userName1, userName2, ranCards)
            #get tieGame ()
                if points1 == points2:
                    points1, points2, turns = tieGame(userName1, userName2, ranCardsTie, points1, points2, turns)
                    
            #get victoryScreen ()
                victoryScreen(userName1, userName2, points1, points2, turns)
            #get scoreCompare()
                scoreCompare(userName1, userName2, points1, points2, turns)
            #get userContinuation ()
                playAgain = UserContinuation()
            #get outro ()
                if playAgain == "no":
                    outro(userName1, userName2)
        #get exitGame()
            if menuAnswer == 3 or UserContinuation == "no":
                exitGame()
#call main
main()
