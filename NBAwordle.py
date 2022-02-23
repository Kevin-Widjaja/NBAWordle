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
        #print(name) #remove comment to view solution
        #print(possibleNames) #remove to view all possible names
        
        print(str(turnsRemaining) + " turns remaining.") #state number of turns remaining
        guess = list(input("Guess the NBA player: ").lower()) #take guess into a list
        print("****************************************************************************************")
        hint = ["X", "X", "X", "X", "X"]

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
            for i in range(5):
                if guess[i] == name[i]:
                    hint[i] = "1"

                elif guess[i] in name:
                    hint[i] = "0"

            print("Guess: " + listToString(guess))
            print("Hint:  " + listToString(hint))
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
        print("****************************************************************************************")
        print("Guess the NBA player last name within your first 5 tries. The name has 5 letters in it.")
        print("After guessing, you will be given a hint which shows whether your guess had in the \
right position or wrong position.")
        print("Your hints will either be an 'X', '0' or '1':")
        print("'1' means the letter is in the word and in the correct spot.")
        print("'0' means the letter is in the word but in the incorrect spot.")
        print("'X' means that the letter is not in the word in any spot.")
        print("")
        print("For example, say the solution is Stephen 'Curry' and your guess is Birch, \
your hint would look as follows:")
        print("Solution: curry")
        print("Guess:    birch") 
        print("Hint:     XX10X")
        print("Another Hint: The player must be an active player in the NBA right now. \
Search nba.com/players for all possible players.")
    elif answer == 'y':
        play()
    elif answer == 'n':
        break
    else:
        print("Please choose a valid option.")

exit()
