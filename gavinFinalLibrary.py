#Gavin Heaver
#November 13, 2022
#Make a series of algorithms for the final project,
#which deals with randomly selecting cards.

import random
import time

#return: none
#parameters: None
#purpose: Create an inviting and explanitory intro
#Define welcome page
def welcomePage(): 
#Declare constants and variables
  #none
#Display title
  print("Suit and Tie".center(60,"-"))
#Display inviting intro 
  print("Welcome to Suit and Tie! This is an easy to play card game, that you can play with against a friend."
        " We hope you have fun playing it!\n")
#Display rules of the game
  print("Rules of the game: \n1. This is a 2 player game, so 2 players are necessary to play the game, no more or less\n2. Pick a card face for 1 point \n3. Decide if you want to choose the value of the card for 3 points"
        "\n4. Guess card value IF player requested \n5. If either guess is incorrect, card will be placed randomly in pile and no points will be assigned"
        "\n6. If the user gets 1 or 3 points by being correct, the card is taken out from the pile \n7. A new card will be generated after each guess"
        "\n8. After each guess, it becomes the other players turn to guess on a card \n9. There are 20 random cards per pile to be guess on\n10. "
        "Turns are counted after both users have done an attempt \n\nHAVE FUN!!!!")
#Display a dividing line of "-"
  print("--"*30)

  
#return: 1 string, and empty line to show they are done seeing the highscores
#parameters: 2 ints and 1 string, 1 int for high score, 1 for turns, and 1 string for user name
#This program will display the user who had the highest score and how many turns it took to get it
#define highScore
def highScore():
#Declare constants and variables
  finished = "a"
  with open("highScores.txt", "r") as infile:
    best = infile.readline().strip()
    score = infile.readline().strip()
    turns = infile.readline().strip()
#Display dividing line
  print("--"*30)
#Display username with highest score
  print(f"\nThe player with the highest score is {best}.\n")
#Display highest score
  print(f"\nThey had a score of {score}.\n")
#Display turns taken
  print(f"\nThe game lasted {turns} turns.\n")
#Display dividing line
  print('--'*30)
  #Prompt user if they are finished in this section and put error if they type incorrectly
  while finished != "":
    finished = input("When you are done looking at the high score, please press just enter.")
    if finished != "":
      print("\nYou didn't just press enter. Please try again if you are finished.\n")
  #return finished
  return(finished)

#return: 2 strings, 1 for card face and 1 for card value
#parameters: None
#purpose: this will randomly choose 20 cards
#Define card shuffle
def cardShuffle():
#Declare constants and variables
  cardList = ["D A","D 2","D 3","D 4","D 5","D 6","D 7","D 8","D 9","D 10","D J","D Q","D K",
              "H A","H 2","H 3","H 4","H 5","H 6","H 7","H 8","H 9","H 10","H J","H Q","H K",
              "C A","C 2","C 3","C 4","C 5","C 6","C 7","C 8","C 9","C 10","C J","C Q","C K",
              "S A","S 2","S 3","S 4","S 5","S 6","S 7","S 7","S 8","S 9","S 10","S J","S Q","S K"]
  ranCards=[]
  ranCardsTie=[]
  #randomly choose 20 cards from card list 
  ranCards = random.sample(cardList,20)
  #Make them the same "deck," but reshuffle
  ranCardsTie = random.sample(ranCards,20)

#return random face and value
  return(ranCards, ranCardsTie)


#return: 3 integers, 1 set of points for each player and turns
#parameters: 3 strings, player 1 name, player 2 name, and card set
#purpose: this will make a random card, split it into the components, and take the user's guesses and assign points based on being correct
#define users choice
def userChoice(user1, user2, ranCards):
#declare constants and variables
  points1 = 0
  points2 = 0
  turns = 1
  cardsLeft = 20
  faceGuess1 = ""
  valueGuess1 = ""
  valueRequest1 = ""
  faceGuess2 = ""
  valueGuess2 = ""
  valueRequest2 = ""
  ranFace = ""
  ranFace = ""
  ranCard = ""

#make loop until card pile is gone
  while cardsLeft != 0 and faceGuess1 == "":
  #Randomly choose a card from ranCards
    ranCard = random.choice(ranCards)
  #split card into its components of face and value
    ranFace, ranValue = ranCard.split()

#Display turn and point countercounter
    print("-"*60)
    print(f"\n{user1} has {points1} points\n")
    print(f"\n{user2} has {points2} points\n")
    print(f"\nThis is turn {turns}\n")
    print(f"\nThere are {cardsLeft} cards in the pile to be picked from\n")
    print("-"*60)
    
#prompt user for card face. make error message if not correct input
    while faceGuess1 != "H" and faceGuess1 != "S" and faceGuess1 != "C" and faceGuess1 != "D":
      faceGuess1 = input(f"{user1}, please choose whichever face you think the card is,"
                         " typing the first letter of the face's name."
                         "\n\n'C'=Club\n'D'=Diamond\n'H'=Hearts\n'S'=Spades\n\nSo now, what is your guess: ").upper()
      if faceGuess1 != "H" and faceGuess1 != "S" and faceGuess1 != "C" and faceGuess1 != "D":
        print("\nYou didn't type a correct guess, please try again.\n")
        
  #prompt user if they want to guess card value make error message if not correct input
    while valueRequest1 != "y" and valueRequest1 != "n": 
      valueRequest1 = input("\nNow then, would you like to risk the card and try to guess the value? Please type 'y' for yes and 'n' for no: ").lower()
      if valueRequest1 != "y" and valueRequest1 != "n":
        print("\nYou didn't type either a 'y' or 'n'. Please try again.")
      
  #prompt user for card value if requested. make error message if not correct input
    while valueRequest1 == "y" and valueGuess1 != 'A' and valueGuess1 != '2' and valueGuess1 != '3' and valueGuess1 != '4' and valueGuess1 != '5' and valueGuess1 != '6' and valueGuess1 != '7' and valueGuess1 != '8' and valueGuess1 != '9'and valueGuess1 != '10' and valueGuess1 != 'J' and valueGuess1 != 'Q' and valueGuess1 != 'K':
      valueGuess1 = str(input(f"\nYour a risky person {user1}... so lets see what happens."
                              " What value do you think the card is? \nType the number or first letter of ('j' for jack,'q' for queen, 'k' for king, and 'a' for Ace):")).upper()
      if valueGuess1 != 'A' and valueGuess1 != '2' and valueGuess1 != '3' and valueGuess1 != '4' and valueGuess1 != '5' and valueGuess1 != '6' and valueGuess1 != '7' and valueGuess1 != '8' and valueGuess1 != '9' and valueGuess1 != '10' and valueGuess1 != 'J' and valueGuess1 != 'Q' and valueGuess1 != 'K':
        print("\nYou didn't type a valid response. Please try again")
  
  #make delay of 1 second for suspense
    print("\nAre you right...?")
    time.sleep(1)
    
  #make selection structure based on being correct or not with face and/or card value. Assign points to player 1 if correct. Make time delay to let person read
    if faceGuess1 == ranFace and ranValue == valueGuess1:
      print(f"\nYOU DID IT, YOU GOT THEM BOTH! IT WAS THE {ranValue} OF {ranFace}!"
            f" HERE'S YOUR WELL EARNED 3 POINTS!\n")
      print(f"The {ranValue} of {ranFace} has been removed from the pile")
      points1 += 3
      cardsLeft = cardsLeft - 1
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCards.remove(ranCard)
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()

  
    elif faceGuess1 == ranFace and valueRequest1 == "n":
      print(f"\nGood job, you got the face right!"
      f" The card was the {ranValue} of {ranFace}. You get a point!\n")
      print(f"The {ranValue} of {ranFace} had been removed from the pile")
      points1 += 1
      cardsLeft = cardsLeft - 1
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCards.remove(ranCard)
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()

    
    elif faceGuess1 != ranFace and valueRequest1 == "n":
      print(f"\nAh, you didn't get the face right."
            f" The card was the {ranValue} of {ranFace}. No points")
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()

      
    elif faceGuess1 == ranFace and valueGuess1 != ranValue:
      print(f"\nShouldn't have gambled, you got the face but not the value."
            f" It was the {ranValue} of {ranFace}. No points")
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()

  
    elif faceGuess1 != ranFace and valueGuess1 == ranValue:
      print(f"\nWell... this one sucks. You got the value, but not the face."
            f" It was the {ranValue} of {ranFace}. Sorry, but no points for you")
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()

    
    elif faceGuess1 != ranFace and valueGuess1 != ranValue:
      print(f"\nWell your additional guess didn't matter in the end, as you were wrong on both guesses."
            f" The card was the {ranValue} of {ranFace}. No points")
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()

      
  #repeat prompt steps for player 2, adding points to player 2 if correct. Also add 1 to the turn counter at the end to show what turn it is    
    #exit program if cards left = 0 midway through program
    if cardsLeft == 0:
      if points1 > points2 or points1 < points2:
         turns -=1      
      return(points1,points2,turns)
      exit()

      
    #Display turn and point countercounter
    print("-"*60)
    print(f"\n{user1} has {points1} points\n")
    print(f"\n{user2} has {points2} points\n")
    print(f"\nThis is turn {turns}\n")
    print(f"\nThere are {cardsLeft} cards in the pile to be picked from\n")
    print("-"*60)


    #prompt user for face guess. Display error if incorrectly input
    while faceGuess2 != "H" and faceGuess2 != "S" and faceGuess2 != "C" and faceGuess2 != "D":
      faceGuess2 = input(f"{user2}, please choose whichever face you think the card is, typing the first letter of the face's name."
                         "\n\n'C'=Club\n'D'=Diamond\n'H'=Hearts\n'S'=Spades\n\nSo now, what is your guess: ").upper()
      if faceGuess2 != "H" and faceGuess2 != "S" and faceGuess2 != "C" and faceGuess2 != "D":
        print("\nYou didn't type a correct guess, please try again.\n")
        
  #prompt user if they want to guess card value make error message if not correct input
    while valueRequest2 != "y" and valueRequest2 != "n": 
      valueRequest2 = input("\nNow then, would you like to risk the card and try to guess the value? Please type 'y' for yes and 'n' for no: ").lower()
      if valueRequest2 != "y" and valueRequest2 != "n":
        print("\nYou didn't type either a 'y' or 'n'. Please try again.")
        
  #prompt user for card value if requested. make error message if not correct input
      while valueRequest2 == "y" and valueGuess2 != 'A' and valueGuess2 != '2' and valueGuess2 != '3' and valueGuess2 != '4' and valueGuess2 != '5' and valueGuess2 != '6' and valueGuess2 != '7' and valueGuess2 != '8' and valueGuess2 != '9' and valueGuess2 != '10' and valueGuess2 != 'J' and valueGuess2 != 'Q' and valueGuess2 != 'K':
        valueGuess2 = str(input(f"\nYour a risky person {user2}... so lets see what happens. What value do you think the card is?"
                                "\nType the number or first letter of royals ('j' for jack,'q' for queen,'k' for king, and 'a' for Ace):")).upper()
        if valueGuess2 != 'A' and valueGuess2 != '2' and valueGuess2 != '3' and valueGuess2 != '4' and valueGuess2 != '5' and valueGuess2 != '6' and valueGuess2 != '7' and valueGuess2 != '8' and valueGuess2 != '9' and valueGuess2 != '10' and valueGuess2 != 'J' and valueGuess2 != 'Q' and valueGuess2 != 'K': 
          print("\nYou didn't type a valid response. Please try again")
  
  #make delay of 1 second for suspense
    print("\nAre you right...?")
    time.sleep(1)
    
  #make selection structure based on being correct or not with face and/or card value. Assign points to player 2 if correct. Make a delay for user to read
    if faceGuess2 == ranFace and ranValue == valueGuess2:
      print(f"\nYOU DID IT, YOU GOT THEM BOTH! IT WAS THE {ranValue} OF {ranFace}!"
            " HERE'S YOUR WELL EARNED 3 POINTS!\n")
      print(f"The {ranValue} of {ranFace} had been removed from the pile")
      points2 += 3
      cardsLeft = cardsLeft - 1
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCards.remove(ranCard)
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()
       
      
      
    elif faceGuess2 == ranFace and valueRequest2 == "n":
      print(f"\nGood job, you got the face right! The card was the {ranValue} of {ranFace}."
            " You get a point!\n")
      print(f"The {ranValue} of {ranFace} had been removed from the pile")
      points2 += 1
      cardsLeft = cardsLeft - 1
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCards.remove(ranCard)
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()
      
    elif faceGuess2 != ranFace and valueRequest2 == "n":
      print(f"\nAh, you didn't get the face right."
            f" The card was the {ranValue} of {ranFace}. No points")
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()
  
    elif faceGuess2 == ranFace and valueGuess2 != ranValue:
      print(f"\nShouldn't have gambled, you got the face but not the value."
            f" It was the {ranValue} of {ranFace}. No points")
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()
  
    elif faceGuess2 != ranFace and valueGuess2 == ranValue:
      print(f"\nWell... this one sucks. You got the value, but not the face."
            f" It was the {ranValue} of {ranFace}. Sorry, but no points for you")
      turns +=1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()

    elif faceGuess2 != ranFace and valueGuess2 != ranValue:
      print(f"\nWell your additional guess didn't matter in the end, as you were wrong on both guesses."
            f" The card was the {ranValue} of {ranFace}. No points")
      turns += 1
      time.sleep(2.5)
      if cardsLeft != 0:
        ranCard = random.choice(ranCards)
        ranFace, ranValue = ranCard.split()
      
    #reset variables
    faceGuess1 = ""
    valueGuess1 = "" 
    valueRequest1 = ""
    valueRequest2 = ""
    faceGuess2 = ""
    valueGuess2 = ""

  #Incase of tie, make if statement for turn counter
  if points1 > points2 or points1 < points2:
    turns -=1

  return(points1, points2, turns)


  
#return: 3 integers, the total points for each player and new turn amount
#parameters: 3 strings and 2 int, player 1 name, player 2 name, all the cards, and the points for both players from the first game
#purpose: this will make the game last longer if there is a tie from the previous program, going up to 3 points
def tieGame(user1, user2, ranCardsTie, points1, points2, turns):
  #declare and initialize constants and variables
  tiePoints1 = 0
  tiePoints2 = 0
  totalPoints1 = 0
  totalPoints2 = 0
  faceGuess1 = ""
  valueGuess1 = "" 
  valueRequest1 = ""
  valueRequest2 = ""
  faceGuess2 = ""
  valueGuess2 = ""
  ranCardTie = ""
  ranFaceTie = ""
  ranValueTie = ""
  cardsLeft = 20


  #State that it is a tie
  print("\nWell, after all of this, its come to a tie. Here's how this will work, the game continues until a user gains 3 more points than they are at right now."
        "\nThat means a player can end the game right now by guessing both face and value, or win by guessing face 3 times."
        "\nThere is no second chance for the other player, so when 3 extra points are scored, that is the end of the game."
        "\nTurns will continue to be counted starting from the latest turn. It'll continue with the same cards choosen, so you know what cards are in this pile. Good luck")
  
  #loop until 3 extra points by one player is scored are scored
      #Randomly choose a card from ranCards
  ranCardTie = random.choice(ranCardsTie)
  #split card into its components of face and value
  ranFaceTie, ranValueTie = ranCardTie.split()
  
  while tiePoints1 < 3 and tiePoints2 < 3:
    
    print("-"*60)
    print(f"\n{user1} has {points1 + tiePoints1} points\n")
    print(f"\n{user2} has {points2 + tiePoints2} points\n")
    print(f"\nThis is turn {turns}\n")
    print(f"There are {cardsLeft} cards in the pile to be picked from")
    print("-"*60)  
    
  #prompt user for card face. make error message if not correct input
    while faceGuess1 != "H" and faceGuess1 != "S" and faceGuess1 != "C" and faceGuess1 != "D":
      faceGuess1 = input(f"{user1}, please choose whichever face you think the card is, typing the first letter of the face's name."
                         "\n\n'C'=Club\n'D'=Diamond\n'H'=Hearts\n'S'=Spades\n\nSo now, what is your guess: ").upper()
      if faceGuess1 != "H" and faceGuess1 != "S" and faceGuess1 != "C" and faceGuess1 != "D":
        print("\nYou didn't type a correct guess, please try again.\n")
        
  #prompt user if they want to guess card value make error message if not correct input
    while valueRequest1 != "y" and valueRequest1 != "n": 
      valueRequest1 = input("\nNow then, would you like to risk the card and try to guess the value? Please type 'y' for yes and 'n' for no: ").lower()
      if valueRequest1 != "y" and valueRequest1 != "n":
        print("\nYou didn't type either a 'y' or 'n'. Please try again.\n")
        
  #prompt user for card value if requested. make error message if not correct input
      while valueRequest1 == "y" and valueGuess1 != 'A' and valueGuess1 != '2' and valueGuess1 != '3' and valueGuess1 != '4' and valueGuess1 != '5' and valueGuess1 != '6' and valueGuess1 != '7' and valueGuess1 != '8' and valueGuess1 != '9' and valueGuess1 != '10' and valueGuess1 != 'J' and valueGuess1 != 'Q' and valueGuess1 != 'K':
        valueGuess1 = str(input(f"\nYour a risky person {user2}... so lets see what happens. What value do you think the card is?"
                                "\nType the number or first letter of royals ('j' for jack,'q' for queen,'k' for king, and 'a' for Ace):")).upper()
        #Show error message
        if valueGuess1 != 'A' and valueGuess1 != '2' and valueGuess1 != '3' and valueGuess1 != '4' and valueGuess1 != '5' and valueGuess1 != '6' and valueGuess1 != '7' and valueGuess1 != '8' and valueGuess1 != '9' and valueGuess1 != '10' and valueGuess1 != 'J' and valueGuess1 != 'Q' and valueGuess1 != 'K':
          print("\nYou didn't type a valid response. Please try again")
  
  #make delay of 1 second for suspense
    print("\nAre you right...?")
    time.sleep(1)
    
  #make selection structure based on being correct or not with face and/or card value. Assign points to player 1 if correct. Make a delay for user to read
    if faceGuess1 == ranFaceTie and ranValueTie == valueGuess1:
      print(f"\nYOU DID IT, YOU GOT THEM BOTH! IT WAS THE {ranValueTie} OF {ranFaceTie}!"
            " HERE'S YOUR WELL EARNED 3 POINTS!\n")
      print(f"The {ranValueTie} of {ranFaceTie} had been removed from the pile")
      tiePoints1 += 3
      cardsLeft = cardsLeft - 1
      turns += 1
      time.sleep(2.5)
      ranCardsTie.remove(ranCardTie)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()
                              
      
    elif faceGuess1 == ranFaceTie and valueRequest1 == "n":
      print(f"\nGood job, you got the face right! The card was the {ranValueTie} of {ranFaceTie}."
            " You get a point!\n")
      print(f"The {ranValueTie} of {ranFaceTie} had been removed from the pile")
      tiePoints1 += 1
      cardsLeft = cardsLeft - 1
      turns += 1
      time.sleep(2.5)
      ranCardsTie.remove(ranCardTie)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()
      
      
    elif faceGuess1 != ranFaceTie and valueRequest1 == "n":
      print(f"\nAh, you didn't get the face right."
            f" The card was the {ranValueTie} of {ranFaceTie}. No points")
      turns += 1
      time.sleep(2.5)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()
      
  
    elif faceGuess1 == ranFaceTie and valueGuess1 != ranValueTie:
      print(f"\nShouldn't have gambled, you got the face but not the value."
            f" It was the {ranValueTie} of {ranFaceTie}. No points")
      turns += 1
      time.sleep(2.5)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()
      
  
    elif faceGuess1 != ranFaceTie and valueGuess1 == ranValueTie:
      print(f"\nWell... this one sucks. You got the value, but not the face."
            f" It was the {ranValueTie} of {ranFaceTie}. Sorry, but no points for you")
      turns += 1
      time.sleep(2.5)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()

      
    elif faceGuess1 != ranFaceTie and valueGuess1 != ranValueTie:
      print(f"\nWell your additional guess didn't matter in the end, as you were wrong on both guesses."
            f" The card was the {ranValueTie} of {ranFaceTie}. No points")
      turns += 1
      time.sleep(2.5)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()
      
      
    #exit program midway if conditions are met
    if tiePoints1 >= 3:
      totalPoints1 = tiePoints1 + points1
      totalPoints2 = tiePoints2 + points2
      turns -= 1  
      return(totalPoints1, totalPoints2, turns)
      exit()

      
  #repeat prompt steps for player 2, adding points to player 2 if correct. Also add 1 to the turn counter at the end to show what turn it is
    #Display turn and point countercounter
    print("-"*60)
    print(f"\n{user1} has {points1 + tiePoints1} points\n")
    print(f"\n{user2} has {points2 + tiePoints2} points\n")
    print(f"\nThis is turn {turns}\n")
    print(f"\nThere are {cardsLeft} cards in the pile to be picked from\n")
    print("-"*60)
    
    #Make selection structure for user input, with error message
    while faceGuess2 != "H" and faceGuess2 != "S" and faceGuess2 != "C" and faceGuess2 != "D":
      faceGuess2 = input(f"{user2}, please choose whichever face you think the card is, typing the first letter of the face's name."
                         "\n\n'C'=Club\n'D'=Diamond\n'H'=Hearts\n'S'=Spades\n\nSo now, what is your guess: ").upper()
      if faceGuess2 != "H" and faceGuess2 != "S" and faceGuess2 != "C" and faceGuess2 != "D":
        print("\nYou didn't type a correct guess, please try again.\n")
        
  #prompt user if they want to guess card value make error message if not correct input
    while valueRequest2 != "y" and valueRequest2 != "n": 
      valueRequest2 = input("\nNow then, would you like to risk the card and try to guess the value? Please type 'y' for yes and 'n' for no: ").lower()
      if valueRequest2 != "y" and valueRequest2 != "n":
        print("\nYou didn't type either a 'y' or 'n'. Please try again.\n")
        
  #prompt user for card value if requested. make error message if not correct input
      while valueRequest2 == "y" and valueGuess2 != 'A' and valueGuess2 != '2' and valueGuess2 != '3' and valueGuess2 != '4' and valueGuess2 != '5' and valueGuess2 != '6' and valueGuess2 != '7' and valueGuess2 != '8' and valueGuess2 != '9' and valueGuess2 != '10' and valueGuess2 != 'J' and valueGuess2 != 'Q' and valueGuess2 != 'K':
        valueGuess2 = str(input(f"\nYour a risky person {user1}... so lets see what happens. What value do you think the card is?"
                                "\nType the number or first letter of royals ('j' for jack,'q' for queen,'k' for king, and 'a' for Ace):")).upper()
        if valueGuess2 != 'A' and valueGuess2 != '2' and valueGuess2 != '3' and valueGuess2 != '4' and valueGuess2 != '5' and valueGuess2 != '6' and valueGuess2 != '7' and valueGuess2 != '8' and valueGuess2 != '9' and valueGuess2 != '10' and valueGuess2 != 'J' and valueGuess2 != 'Q' and valueGuess2 != 'K': 
          print("\nYou didn't type a valid response. Please try again")

          
  #make delay of 1 second for suspense
    print("\nAre you right...?")
    time.sleep(1)
  #make selection structure based on being correct or not with face and/or card value. Assign points to player 2 if correct. Make a delay for user to read
    if faceGuess2 == ranFaceTie and ranValueTie == valueGuess2:
      print(f"\nYOU DID IT, YOU GOT THEM BOTH! IT WAS THE {ranValueTie} OF {ranFaceTie}!" 
            " HERE'S YOUR WELL EARNED 3 POINTS!\n")
      print(f"The {ranValueTie} of {ranFaceTie} had been removed from the pile")
      tiePoints2 += 3
      cardsLeft = cardsLeft - 1
      turns += 1
      time.sleep(2.5)
      ranCardsTie.remove(ranCardTie)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()
      
      
    elif faceGuess2 == ranFaceTie and valueRequest2 == "n":
      print(f"\nGood job, you got the face right! The card was the {ranValueTie} of {ranFaceTie}." 
            " You get a point!\n")
      print(f"The {ranValueTie} of {ranFaceTie} had been removed from the pile")
      tiePoints2 += 1
      cardsLeft = cardsLeft - 1
      turns += 1
      time.sleep(2.5)
      ranCardsTie.remove(ranCardTie)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()
      
      
    elif faceGuess2 != ranFaceTie and valueRequest2 == "n": 
      print(f"\nAh, you didn't get the face right."
            f" The card was the {ranValueTie} of {ranFaceTie}. No points")
      turns += 1
      time.sleep(2.5)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()

    
    elif faceGuess2 == ranFaceTie and valueGuess2 != ranValueTie:
      print(f"\nShouldn't have gambled, you got the face but not the value."
            f" It was the {ranValueTie} of {ranFaceTie}. No points")
      turns += 1
      time.sleep(2.5)
      ranCardTie = random.choice(ranCardsTie)    
      ranFaceTie, ranValueTie = ranCardTie.split()

    
    elif faceGuess2 != ranFaceTie and valueGuess2 == ranValueTie:
      print(f"\nWell... this one sucks. You got the value, but not the face."
            f" It was the {ranValueTie} of {ranFaceTie}. Sorry, but no points for you")
      turns += 1
      time.sleep(2.5)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()

    
    elif faceGuess2 != ranFaceTie and valueGuess2 != ranValueTie:
      print(f"\nWell your additional guess didn't matter in the end, as you were wrong on both guesses."
            f" The card was the {ranValueTie} of {ranFaceTie}. No points")
      turns += 1
      time.sleep(2.5)
      ranCardTie = random.choice(ranCardsTie)
      ranFaceTie, ranValueTie = ranCardTie.split()

      
    #reset variables
    faceGuess1 = ""
    valueGuess1 = "" 
    valueRequest1 = ""
    valueRequest2 = ""
    faceGuess2 = ""
    valueGuess2 = ""
      

  totalPoints1 = tiePoints1 + points1
  totalPoints2 = tiePoints2 + points2
  turns -= 1
  return(totalPoints1, totalPoints2, turns)


#return: None
#parameters: 2 strings and 3 integers, strings for the user names, 2 integers for points and one for turns
#This program will display the user that won, and on what turn
#define victory screen
def victoryScreen(user1, user2, user1points, user2points, turns):
#declare constants and variables
#display the user that won and with however many points 
  #use selection structure based on whichever user won
  #display a seperation screen
  print('-'*60)

  #Make selection structure based on points
  if user1points > user2points:
    print(f"\n{user1} has won against {user2}, by a score of {user1points} to {user2points}!\n")
    
  elif user2points > user1points:
    print(f"\n{user2} has won against {user1}, by a score of {user2points} to {user1points}!")
    
#display how many turns it took to complete the game
  print(f"The game lasted {turns} turns.\n")
  
  #Display a seperation screen
  print('-'*60)

  
#return: none
#parameters: 2 strings for both usernames and 3 ints, one for each player and a turns counter
#This will compare the points scored in the most recent game with the highscore and then either assign 
def scoreCompare(user1, user2, points1, points2, turns):
  #declare and initialize variables
  highName = ""
  highScore = ""
  highTurns = ""
  
  with open("highScores.txt", "r") as infile:
    highName = infile.readline().strip()
    highScore = infile.readline().strip()
    highTurns = infile.readline()

    #make highScore and highTurns int
    highScore = int(highScore)
    highTurns = int(highTurns)
  #make selection structure based on if the points just scored are higher than the current highest scores
  #write over if they meet standards
  if points1 > highScore and points2 > highScore:
    if points1 > points2:
      points1 = str(points1)
      turns = str(turns)
      with open("highScores.txt","w") as outfile:
        print(user1, file = outfile)
        print(points1, file = outfile)
        print(turns, file = outfile)
        
    elif points2 > points1:
      points2 = str(points2)
      turns = str(turns)
      with open("highScores.txt","w") as outfile:
        print(user2, file = outfile)
        print(points2, file = outfile)
        print(turns, file = outfile)
      
      
  elif points1 > highScore:
    points1 = str(points1)
    turns = str(turns)
    with open("highScores.txt","w") as outfile:
        print(user1, file = outfile)
        print(points1, file = outfile)
        print(turns, file = outfile)
      
  elif points2 > highScore:
    points2 = str(points2)
    turns = str(turns)
    with open("highScores.txt","w") as outfile:
        print(user2, file = outfile)
        print(points2, file = outfile)
        print(turns, file = outfile)
      


