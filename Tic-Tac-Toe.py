'''
Program currently does not keep track/score. Program will run 9 times then exit
'''

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# X goes first
turn = 'X'

#Iterate through each Tic Tac Toe space (of which there are 9)
for i in range(9):
    # print the Tic Tac Toe board
    printBoard(theBoard)
    # Ask Player 'X' or 'O' (logic to determine this is later) which space to play on
    print('Turn for ' + turn + '. Move on which space?')
    # Put Players response into move
    move = input()
    # Assign 'X' or 'O' to the key the player specied earlier (i.e. top-L, mid-R, etc.)
    theBoard[move] = turn
    # Change to player 'O' if player 'X' just completed their turn
    if turn == 'X':
        turn = 'O'
    # Switch to player 'X' if player 'O' just completed their turn
    else:
        turn = 'X'
