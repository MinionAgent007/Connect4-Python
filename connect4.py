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

def checkHorTok(row,col,tok):
    count = 0
    for i in range(4):
        if board[row][col + i] != tok:
            
            return False
    return True

def checkHorBoard(tok):
    won = False
    for r in range(6):
        for c in range(4):
            if checkHorTok(r,c,tok):
                print(tok + " WINS!")
                print(str(r) + ' ' + str(c))
                won = True
                break
        if won:
            break
    print("Code Ends")


# def checkBoard(col):
#     if p1Turn:
#         checkPiece = "X"
#     if not p1Turn:
#         checkPiece = "O"
    
#     cInd = col-1
#     rInd = 6 - columnStat[cInd]

#     print(cInd)
#     print(rInd)
    
#     print(board[rInd][cInd])
    
#     seq = 0
#     if board[rInd][cInd] == checkPiece:
#         print(checkPiece + " wins!")
        
printBoard()
dropToken(7)
dropToken(1)
dropToken(1)
dropToken(3)
dropToken(1)
dropToken(4)
dropToken(1)
dropToken(2)
dropToken(1)

checkHorBoard('E')