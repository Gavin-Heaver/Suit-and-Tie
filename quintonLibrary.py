#Quinton williamceau
#Dec 1,2022
#define constants and variables 
userName1 = ""
userName2 = ""


#get the userName1 /ask if they have a second player
def userName():
  #Prompt for the first users name
  userName1 = input("\nPlease enter the first user's name: ").capitalize()
  #asking for the second users name
  userName2 = input(f"\nGreat to be introduced to {userName1}, now what is the second players name: ").capitalize()
  

  return(userName1, userName2)
  
#return: None
#parameters: 2 strings, the user names
#This will close out the program with nice text
def outro(userName1, userName2):
  print(f"\nThanks you {userName1} and {userName2} for playing the game! We hope you enjoyed it!! Play again whenever you'd like!\n\n ")


#return: None
#parameters: None
#This program shut down the program upon request
def exitGame():
  #exit the program
  print("\nBYE!")
  exit()
    
    


