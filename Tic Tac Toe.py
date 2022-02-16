#TIC TAC TOE


#from IPython.display import clear_output

def display_board(board):
    #clear_output()
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + " | " + board[8] + " | " + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + " | " + board[5] + " | " + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + " | " + board[2] + " | " + board[3])
    print('   |   |')





def player_input():
    '''
    OUTPUT: (Player 1 marker, Player 2 marker)
    
    '''
    
    marker = ''
    
    #...Ask player1 for choosing "X" or "O"
    
    while marker != 'X' and marker != 'O':
        marker = input("Hello, Player1! Please choose 'X' or 'O': ").upper()
        
    #...Return (player 1 marker, player 2 marker)
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')






def place_marker(board, marker, position):
    board[position] = marker




def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or 
    (board[4] == board[5] == board[6] == mark) or 
    (board[1] == board[2] == board[3] == mark) or 
    (board[7] == board[4] == board[1] == mark) or 
    (board[8] == board[5] == board[2] == mark) or 
    (board[9] == board[6] == board[3] == mark) or 
    (board[7] == board[5] == board[3] == mark) or 
    (board[1] == board[5] == board[9] == mark))





import random

def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'






def space_check(board, position):
    return board[position] == ' '






def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    #If board full, return True
    return True





def player_choice(board):
    
    position = 0
    
    while position not in range(1,11) and not space_check(board, position):
        position = int(input("Choose a position: (1-9) "))
        
    return position





def replay():
    choice = input('Do you want to play again? Enter "Yes" or "No"').lower()
    
    return choice == 'yes'










print("Let's play Tic Tac Toe!")

#Begin game

while True:
    
    #Set the board, marker, choose first
    board = [' ']*10
    (player1_marker, player2_marker) = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Are you ready to play? y or n?')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    #Gameplay
    while game_on:
        if turn == 'Player 1':
        #Player 1 turn
        
            #Show the board
            display_board(board)
        
            #Choose a position
            position = player_choice(board)
        
            #Place marker to the position
            place_marker(board, player1_marker, position)
        
            #Check Win
            if win_check(board, player1_marker):
                display_board(board)
                print('CONGRATS! Player 1 has won!')
                game_on = False
            
            else:
                #Check Tie
                if full_board_check(board):
                    display_board(board)
                    print("It's a Tie!!")
                    game_on = False
            
                else:
                    #If not win or tie, Player's 2 turn
                    turn = 'Player 2'
                
                
        
        else:
            #Player 2 turn
            
            
            #Show the board
            display_board(board)
        
            #Choose a position
            position = player_choice(board)
        
            #Place marker to the position
            place_marker(board, player2_marker, position)
        
            #Check Win
            if win_check(board, player2_marker):
                display_board(board)
                print('CONGRATS! Player 2 has won!')
                game_on = False
            
            else:
                #Check Tie
                if full_board_check(board):
                    display_board(board)
                    print("It's a Tie!!")
                    game_on = False
            
                else:
                    turn = 'Player 1'            
        
    
    if not replay():
        break



