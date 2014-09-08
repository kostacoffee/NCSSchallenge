lines = int(input())
board = ["" for i in range(lines)]
if (lines > 0):
    board[0] = input()
    print(board[0])
    for row in range(1, lines):
        line = ""
        for col in range(len(board[row-1])):
            left = 0
            right = 0
            c = '.'
            if (board[row-1][col-1] == "*"):
                left = 1
            if col == len(board[row-1])-1: col = -1
            if (col < len(board[row-1])-1 and board[row-1][col+1] == "*"):
                right = 1
            if (left ^ right):
                c = '*'
            line += c
        print(line)
        board[row] = line
