import random
import pandas as pd 

#find table which lists all active NBA players
table = pd.read_html("https://basketball.realgm.com/nba/players")
df = table[0]
names = list(df['Player']) #save the names of all players on the list

#consider only the last names of players (and remove all commas)
for i in range(len(names)):
    full_name = names[i].split()
    last_name = full_name[1]
    last_name = last_name if last_name[-1] != "," else last_name[:-1]
    names[i] = last_name

#set all possible names the game can choose to be all last names with 5 letters and remove duplicates    
possibleNames = [i.lower() for i in names if len(i) == 5]
possibleNames = list(set(possibleNames))

#function to play the game
def play():    

    #set name and number of turns
    name = list(random.choice(possibleNames))
    turnsRemaining = 5

    while turnsRemaining > 0:
        print(str(turnsRemaining) + " turns remaining.") #state number of turns remaining
        print(name)
        guess = list(input("Guess the NBA player: ").lower()) #take guess into a list
        print("")
        if len(guess) != 5: #check that guess has 5 letters
            print("List a 5-letter last name!")
            continue
        
        if guess == name: #win condition
            print("You win!")
            break

        elif listToString(guess) not in possibleNames: #check that name is in database
            print("Player not in database")
            continue
        
        #if guess is incorrect, give hints on correct name, and decrease turns remaining
        else:
            noLettersGuessed = True
            for i in range(5):
                if guess[i] == name[i]:
                    print(guess[i] + " is in the correct position (letter #" + str(i+1) + ")")
                    noLettersGuessed = False
                elif guess[i] in name:
                    print(guess[i] + " is in the name but in the wrong position (letter #" + str(i+1) + ")")
                    noLettersGuessed = False
            if noLettersGuessed == True:
                print("No letters found in any spot")

            turnsRemaining -= 1
    
    #if user runs out of guesses, give them the solution
    if turnsRemaining == 0:
        print("")
        print("Sorry, you weren't able to get the correct answer.")
        print("The correct answer is: " + listToString(name))

#function to turn a list into a string
def listToString(myList):
    return ("".join(myList))

#loop to continue playing or show rules
while True:
    print("")
    answer = input("Do you want to play NBA Wordle? Type 'Y' for yes, or 'N' for no, or 'R' for rules: ").lower()
    if answer == 'r':
        print("")
        print("Guess the NBA player last name within your first 5 tries. The name has 5 letters in it")
        print("You will be told if the letters you guess are in the right position or if they are in the wrong position")
        print("Hint: The player must be an active player in the NBA right now. \
Search nba.com/players for all possible players.")
    elif answer == 'y':
        play()
    elif answer == 'n':
        break
    else:
        print("Don't understand")