import os
import secrets


#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []
for key in theBoard:
    board_keys.append(key)
    
scores = {'X': 0,
          'O': 0}
    

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    # Randomly start with X or O
    turn_list = ['X', 'O']
    turn = secrets.choice(turn_list)
    
    count = 1

    while count < 10:
        print('\n##########   Round:', count, '   ##########')
        print('It is', turn, 'turn. Make a move.')
        printBoard(theBoard)

        move = input()        
        
        if move not in [str(x) for x in list(range(1,10))]:
            if move == 'n':
                break
            else:
                print('That is a wrong input. Please try again.')
                continue
        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print('That place is already filled.')
            continue

        # Now we will check if player X or O has won, for every move after 5 moves. 
        if count >= 5:
            
            if ((theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ') or # across the top
                (theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ') or # across the middle
                (theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ') or # across the bottom
                (theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ') or # down the left side
                (theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ') or # down the middle
                (theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ') or # down the right side
                (theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ') or # diagonal
                (theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ')): # diagonal
                
                scores[turn] += 1
                
                print('\n##########   GAME OVER   ##########')                
                print('##########     ' + turn + ' WON!    ##########')
                printBoard(theBoard)
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print('\n##########   GAME OVER   ##########\n')                  
            print('It is a Tie!!')

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    print('\nCurrent Score:')
    print('X:', scores['X'])
    print('O:', scores['O'])
    restart = input('Do want to play again? (Y/N)\n')
    if restart not in ['n', 'N']:  
        for key in board_keys:
            theBoard[key] = ' '

        game()

if __name__ == '__main__':
    game()