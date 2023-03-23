'''
This project is the game "Tic-Tac-Toe". 
It contains input validation and modular functions to prevent errors.

Author: Nand Patel
Date: March 22, 2023
Current Version: v1.12

HISTORY:
v1.00 - Game operates without user input validation and does not support replay
v1.10 - Game supports user input validation and replay
v1.11 - Game is optimized to run with less code
v1.12 - Minor tweaks with game board design
'''
#Used for the choose_first() function.
import random

#Displays the current board in the terminal.
def display_board(board):

    for i in range(1,10,3):
        
        print(f"{board[i]} |", f"{board[i + 1]} |", f"{board[i + 2]}")
        
        if i == 7: 
            break
        
        print("---------")

#Checks all possible board combinations to see if a player has won.
def win_check(board, mark):

     return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

#Randomly selects first player.
def choose_first():
    
    if random.randint(0,1) == 0:
        return "X goes first."
    else:
        return "O goes first."

#Returns a boolean indicating if the selected position is available.
def space_check(board, position):
    
    return board[position] == ' '

#Checks if all spaces on the board have been filled.
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
          
    return True

#Queries the user for their choice.
def player_choice(board):
    
    next_position = ' '
    
    #Runs while the user has not entered a valid option.
    while next_position.isdigit() == False:

        next_position = input("Please enter your next position between 1-9.")
        
        #Verifies if the input is an integer.
        if next_position.isdigit() == True: 
            
            next_position = int(next_position)
            
            #Verifies if the position is within the range of the board.
            if (next_position > 0) & (next_position < 10):

                #Verifies if the position is empty.
                if space_check(board, next_position) == True:
                    return next_position
                else:
                    print("That spot is not available.")
                    next_position = ' '
            else:
                print("That number is not in the given range.")
                next_position = ' '
        else:
            print('Please enter an integer.')

#Asks user if they want to contine playing or exit the game after the match.
def replay():
    
    continue_playing = ' '

    #Runs while the user has not entered a valid option.
    while continue_playing.isdigit() == False:
    
        continue_playing = input("Do you want to play again? Enter 1 for yes and 0 for no.")
        
        #Verifies if the input is an integer.
        if continue_playing.isdigit() == True:
            
            continue_playing = int(continue_playing)
            
            if continue_playing == 1:
                return True
            
            elif continue_playing == 0:
                return False
            
            else: 
                print("That is not valid option.")
                continue_playing = ' '

################# MAIN ###################

print('Welcome to Tic Tac Toe!')
       
#while True:
while True:
    
    #Creates an empty board, declares and initializes game variables.
    match_running = True
    game_board = [' '] * 10
    turn = choose_first()
    symbol = 'A'
    
    #Prints which player goes first to the terminal.
    print(turn)

    #Updates the game logic with the current player's symbol.
    if turn == "X goes first.":
        symbol = 'X'
    else:
        symbol = 'O'
    
    while True:
    
        display_board(game_board) 
        
        #Finding which position the user has chosen and updates the board after passing validation.
        position = player_choice(game_board)
        game_board[position] = symbol
        
        #Checks if a player has won. If not, the symbol is reassigned to the other player.
        if win_check(game_board, symbol) == True:
            display_board(game_board)
            print(f"{symbol} has won the game!")

            break
        else:
            if symbol == 'X':
                symbol = 'O'   
            else:
                symbol = 'X'
                
        #Check if the game has ended with no winner.        
        if full_board_check(game_board) == True:
            display_board(game_board)
            print("Tie game!")
            
            break  
    
    #If the user has opted to stop playing, the program ends.
    if replay() == False:
        break