from math import inf as infinity
from random import choice
import platform
import time
from os import system


Player = -1
CPU = +1
GameBoard = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def EvaluateStatus(state):
    if CheckWin(state, CPU):
        score = +1
    elif CheckWin(state, Player):
        score = -1
    else:
        score = 0

    return score


def CheckWin(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def GameOverState(state):
    return CheckWin(state, Player) or CheckWin(state, CPU)


def EmptyCells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def CheckMoveValidity(x, y):
    if [x, y] in EmptyCells(GameBoard):
        return True
    else:
        return False


def SetMove(x, y, player):
    if CheckMoveValidity(x, y):
        GameBoard[x][y] = player
        return True
    else:
        return False


def Minimax(state, depth, player):
    if player == CPU:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or GameOverState(state):
        score = EvaluateStatus(state)
        return [-1, -1, score]

    for cell in EmptyCells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = Minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == CPU:
            if score[2] > best[2]:
                best = score  
        else:
            if score[2] < best[2]:
                best = score 

    return best


def ClearScreen():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def PrintDataOnScreen(state, c_choice, h_choice):
    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def CPU_Turn(c_choice, h_choice):
    depth = len(EmptyCells(GameBoard))
    if depth == 0 or GameOverState(GameBoard):
        return

    ClearScreen()
    print(f'Computer turn [{c_choice}]')
    PrintDataOnScreen(GameBoard, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = Minimax(GameBoard, depth, CPU)
        x, y = move[0], move[1]

    SetMove(x, y, CPU)
    time.sleep(1)


def Player_Turn(c_choice, h_choice):
    depth = len(EmptyCells(GameBoard))
    if depth == 0 or GameOverState(GameBoard):
        return

    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    ClearScreen()
    print(f'Player turn [{h_choice}]')
    PrintDataOnScreen(GameBoard, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = SetMove(coord[0], coord[1], Player)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    ClearScreen()
    h_choice = ''  
    c_choice = '' 
    first = ''  

    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    ClearScreen()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    while len(EmptyCells(GameBoard)) > 0 and not GameOverState(GameBoard):
        if first == 'N':
            CPU_Turn(c_choice, h_choice)
            first = ''

        Player_Turn(c_choice, h_choice)
        CPU_Turn(c_choice, h_choice)

    if CheckWin(GameBoard, Player):
        ClearScreen()
        print(f'Player turn [{h_choice}]')
        PrintDataOnScreen(GameBoard, c_choice, h_choice)
        print('YOU WIN!')
    elif CheckWin(GameBoard, CPU):
        ClearScreen()
        print(f'Computer turn [{c_choice}]')
        PrintDataOnScreen(GameBoard, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        ClearScreen()
        PrintDataOnScreen(GameBoard, c_choice, h_choice)
        print('DRAW!')

    exit()
    print("\n\n")


main()
