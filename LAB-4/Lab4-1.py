global n
n=int(input("Enter a number between 2 and 9:"))
backtracks=0

def CheckConflicts(board, r, c):
    for i in range(r):
        if board[i][c] == 'Q':
            return False

    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1


    (i, j) = (r, c)
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
    return True

def nQueen(board, r):
    global backtracks
    if r == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=' ')
            print()
        print("********************")
        return

    for i in range(n):
        if CheckConflicts(board, r, i):
            board[r][i] = 'Q'
            nQueen(board, r + 1)
            backtracks+=1
            board[r][i] = '-'


board = [['-' for x in range(n)] for y in range(n)]

nQueen(board, 0)
print("Number of backtracks:",backtracks)