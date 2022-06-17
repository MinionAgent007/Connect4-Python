# creates a board with 7 columns and 6 rows filled with E for empty
board = [["E" for i in range(7)] for k in range(6)]
#number of tokens in a column
columnStat = [0 for i in range(7)]

p1Turn = True

def printBoard():   
    for i in range(7):
        print(i+1, end = " ")
    print()
    for j in board:
        for i in j:
            print(i, end = " ")
        print()
    print()

def dropToken(num):
    
    global p1Turn
    
    if num > 7 or num < 0:
        print("Not Possible")
        return
    if columnStat[num-1] >= 6:
        print("This is already full")
        return
    if p1Turn:
        board[5-columnStat[num-1]][num-1] = "O"
    if not p1Turn:
        board[5-columnStat[num-1]][num-1] = "X"

    p1Turn = not p1Turn
    
    columnStat[num-1] += 1
    #checkBoard(num)
    printBoard()

def checkHorTok(row,col,leftToken):
    for i in range(4):
        if board[row][col + i] != leftToken:
            return False
    
    return True

def checkVertTok(row,col,topToken):
    for i in range(4):
        if board[row+1][col] != topToken:
            return False
    return True

def checkHorBoard(tok):
    won = False
    for r in range(6):
        for c in range(4):
            if checkHorTok(r,c,tok):
                print(tok + " WINS!")
                won = True
                break
        if won:
            break
    return won

def checkVertBoard(tok):
    won = False
    for r in range(3):
        for c in range(7):
            if checkVertTok(r,c,tok):
                print(tok + " WINS!")
                won = True
                break
        if won:
            break
    return won

#neg for negative because the tokens are in a negative line
def checkNegTok(row,col,topRightToken):
    for i in range(4):
        if board[row+i][col+i] != topRightToken:
            return False
    return True

def checkNegBoard(tok):
    won = False
    for r in range(3):
        for c in range(4):
            if checkNegTok(r,c,tok):
                print(tok + " WINS!")
                won = True
                break
        if won:
            break
    return won

# pos for positive because tokens are in a positive line
def checkPosTok(row,col,bottomRightToken):
    for i in range(4):
        if board[row-i][col+i] != bottomRightToken:
            return False
    return True

def checkPosBoard(tok):
    won = False
    for r in range(3):
        for c in range(4):
            if checkPosTok(r+3, c, tok):
                print(tok + " WINS!")
                won = True
                break
        if won:
            break
    return won

board[5][3] = "O"
board[4][4] = "O"
board[3][5] = "O"
board[2][6] = "O"

printBoard()

checkPosBoard('O')