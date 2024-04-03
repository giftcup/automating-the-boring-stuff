theBoard = {'0': '0', '1': '1', '2': '2',
 '3': '3', '4': '4', '5': '5',
 '6': '6', '7': '7', '8': '8'}

def printBoard(board):
    for i in range(0, 9, 3):
        print(board[str(i)] + '|' + board[str(i+1)] + '|' + board[str(i+2)])
        if (i > 3):
            continue
        print('-+-+-')


 
#  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#  print('-+-+-')
#  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(f"Turn for {turn}. Move on which space? ")
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)