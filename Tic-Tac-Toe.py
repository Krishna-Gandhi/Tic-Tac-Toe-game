'''
1. Board
2. Display boar
Play game
handle a turn
3. check win
  i. rows
  ii. columns
  iii. diagonals
4. check tie
5. flip player
'''

#GLOBAL VARIABLES

#board
board=["-","-","-",
       "-","-","-",
       "-","-","-" ]

#if game is still going
game_still_going = True
# Winner or Tie
winner=None

#current player
current_player="X"


#display the board
def display_board():
    print(board[0]+ " | " + board[1] + " | "+ board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#play the game
def play_game():
    #display empty board 1st
    display_board()

    #when game is still going on
    while game_still_going:

        #handle a turn
        handle_turn(current_player)

        #game over?
        check_if_game_over()

        #other player
        flip_player()

    #the game is over
    if winner == "X" or winner=="O":
        print(winner+ " won.")
    elif winner == None:
        print("Tie.")


#handle a turn
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1" , "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position)-1

        if board[position]=="-":
            valid = True
        else:
            print("You can't got there.Enter again.")

    board[position]=player
    display_board()

#game over?
def check_if_game_over():
    check_for_winner()
    check_if_tie()

#if the move is a win move
def check_for_winner():

    #set of global variables
    global winner

    #ROWS
    row_winner = check_rows()
    #COLUMNS
    column_winner =check_columns()
    #DIAGONALS
    diagonal_winner =check_diagonals()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner= None

    return

def check_rows():
    #global variales
    global game_still_going
    #checking if they have same values
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any have a match, imples win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #returing winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # global variales
    global game_still_going
    # checking if they have same values
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any have a match, imples win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # returing winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # global variales
    global game_still_going
    # checking if they have same values
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # if any have a match, imples win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # returing winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
    return


def flip_player():
    #glaobal variables
    global current_player
    #changing X to O
    if current_player == "X":
        current_player="O"
    #changing O to X
    elif current_player =="O":
        current_player="X"
    return




play_game()
