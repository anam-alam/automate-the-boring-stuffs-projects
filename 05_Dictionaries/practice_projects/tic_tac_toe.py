import random

the_board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}





#printing the board
def printboard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6] )
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])



current_player = 'X' 
winner = None
game_running = True
wrong_move = False

#taking player input
def player_input(board):
    global wrong_move
    inp = int(input("Enter a a number 1-9: "))
    if inp>=1 and inp<=9 and board[inp] ==" ":
        board[inp] = current_player
        wrong_move = False
    else:
        print("Oops this spot is taken, try again !!")
        wrong_move = True

#check for win or tie
def check_horizontal_win(board):
    global winner
    if board[1] == board[2] == board[3] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        winner = board[4]
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ': 
        winner = board[7]
        return True

def check_vertical_win(board):
    global winner
    global winner
    if board[1] == board[4] == board[7] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        winner = board[2]
        return True
    elif board[3] == board[6] == board[9] and board[3] != ' ': 
        winner = board[3]
        return True

def check_diagonal(board):
    global winner
    if board[1] == board[5] == board[9] and board[1] != ' ':
        winner = board[1]
        return True
    elif board[3] == board[5] == board[7] and board[3] != ' ':
        winner = board[3]
        return True
    
def check_tie(board):
    global game_running
    if ' ' not in board.values():
        printboard(board)
        print("Its a tie !")
        game_running = False


def check_win():
    if check_diagonal(the_board) or check_horizontal_win(the_board) or check_vertical_win(the_board):
        printboard(the_board)
        print(f"The winner is {winner}")
        exit()

#switch player
def switch_player():
    global current_player
    if wrong_move == False:
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        current_player = current_player

#computer
def computer(board):
    while current_player == 'O':
        position = random.randint(1,9)
        if board[position] == ' ':
            board[position] = 'O'
            switch_player()

while game_running:
    printboard(the_board)
    player_input(the_board)
    check_win()
    check_tie(the_board)
    switch_player()
    computer(the_board)
    check_win()
    check_tie(the_board)
    
    