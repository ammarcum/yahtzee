import random, sys, os, math, pprint

#Variables
userName = ' '#This is initializing the player name
userBoard = [{'aces': ' '},
               {'twos': ' '},
               {'threes': ' '},
               {'fours': ' '},
               {'fives': ' '},
               {'sixes': ' '},
               {'totalScore': ' '},
               {'bonus': ' '},
               {'totalUpperSection': ' '},
               {'threeOfaKind': ' '},
               {'fourOfaKind': ' '},
               {'fullHouse': ' '},
               {'smStraight': ' '},
               {'lgStraight': ' '},
               {'yahtzee': ' '},
               {'chance': ' '},
               {'totalScoreLowerSection': ' '},
               {'finalScore': '0'}]#This list is where a players' board in tracked. As default finalScore is set to 0.
               
diceset = [-1,-1, -1, -1, -1]#This is initializing a set of dice           
KRInstruction = ['R','R','R','R','R'] #This is initializing the first roll of the dice
playAgain = True #This is initializing the playAgain bool as True so you do not have to check the first time whether you want to play again

#####Functions#####
# Need to define what a board of fields looks like
# Need a function to update a specific field
# Need a function to display the board
# Need a function to check whether the spot was already taken
# Need a function to calculate total score
# Need a function to calculate the score per field definition


def getName(): #This method requests the user's name.  The name will be used to address the player and in multiplayer mode differentiate each player.
    global userName
    print ('What is your name?')
    userName = input()

def playSinglePlayer(): #This method plays a Single Player version of the game
    global userBoard
    finalScore = 0
    print('You started a single-player game.')
    
    numTurn = 1
    
    while numTurn <= 13: ##Each player has 13 turns per game
        yahtzeeTurn(numTurn)
        showBoard(userBoard)
        numTurn +=1
    
    print('You finished your single-player game. You final score was ' + str(finalScore)+'. Huzzah!')

def showBoard(Board):
    print('Insert Current Board.')

def rollDice():
    global diceset
    global KRInstruction

    for i in range (5):
        if KRInstruction[i] == 'R' or KRInstruction[i] == 'r':
            diceset[i] = random.randint(1,6)
    
def showDice():
    print('Your dice reads: ')
    for i in range (5):
        print(diceset[i], end = ' ')
    print('\n')
        

def yahtzeeTurn(numTurn):
    print('This is Turn # ' + str(numTurn) + '.')
    global userBoard
    global KRInstruction
    
    numRoll = 0

    rollAgain = True
    
    print('Press enter to roll.')
    playerSelection = input()
    KRInstruction = ['R','R','R','R','R']
        
    rollDice()
    showDice()
    
    print('Would you like to reroll the dice?')
    print('Example: KKKKR represents keep the first four dice but reroll the fifth dice.')
    print('You can reroll two more times.')

    KRInstruction = list(input())
    
    if 'R' not in KRInstruction and 'r' not in KRInstruction:
        print('You chose to keep all of your dice.')
        showDice()
    else:
        print('You chose to reroll your dice.')
        rollDice()
        showDice()

        print('Would you like to reroll the dice?')
        print('Example: KKKKR represents keep the first four dice but reroll the fifth dice.')
        print('You can reroll one more time.')

        KRInstruction = list(input())
    
        if 'R' not in KRInstruction and 'r' not in KRInstruction:
            print('You chose to keep all of your dice.')
            showDice()
        else:
            print('You chose to reroll your dice.  This is your final roll.')
            rollDice()
            showDice()
            
    print('Press enter to see your current score sheet.')
    showBoard(userBoard)

    print('Where would you like to mark this roll?')
    playerSelection = input()
    print('You selected ' + playerSelection + '.')    

def yesNoEvaluator(yesNo):
    yesVariants = ['yes','y']
    if yesNo.lower() in yesVariants:
        return True 

#####This is where the main process starts#####
    
print ('''Hello! Welcome to Audrey's Python Yahtzee!''')
    
getName()

print ('Nice to meet you ' + userName + '!')

playSinglePlayer()

while playAgain == True:
    print ('We played Yahtzee. Cool!')
    print ('Would you like to play again?')

    yesNo = input()

    if yesNoEvaluator (yesNo):
        playAgain = True
        playSinglePlayer()
    else:
        playAgain = False

print ('''Thank you for playing Audrey's Python Yahtzee Game.  Have a good day!''')
