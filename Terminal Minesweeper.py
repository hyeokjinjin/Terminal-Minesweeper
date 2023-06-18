import random

def createGameMasterField(bombInput):
    global GameMasterList
    
    GameMasterList = []
    i = 0
    while i < 10:
        j = 0
        rowList = []
        while j < 10:
            rowList.append(0)
            j += 1
        GameMasterList.append(rowList)
        i += 1
    
    bombPick = 0
    while bombPick < bombInput:
        rowBomb = random.randint(0, 9)
        colBomb = random.randint(0,9)
        if GameMasterList[rowBomb][colBomb] == 0:
            GameMasterList[rowBomb][colBomb] = 1
            bombPick += 1
    
    return GameMasterList

def createUserField():
    global UserList
    
    UserList = []
    i = 0
    while i < 10:
        j = 0
        rowList = []
        while j < 10:
            rowList.append("_")
            j += 1
        UserList.append(rowList)
        i += 1
    return UserList
    
def printUserField():
    colLabel = 1
    print("     1   2   3   4   5   6   7   8   9   10")
    print("--------------------------------------------")
    for row in UserList:
        if colLabel == 10:
            print(str(colLabel) + " ", end="")
        else:
            print(str(colLabel) + "  ", end="")
        for col in row:
            print("| " + col + " ", end="")
        print("|")
        colLabel += 1
    print("--------------------------------------------")

def changeUserField(rowIn, colIn):
    if GameMasterList[rowIn][colIn] == 1:
        return "Over"
    else:
        return "OK"
    
def surroundingBombNumber(rowIn, colIn):
    bombNumber = 0
    row = rowIn - 1
    while row <= (rowIn + 1):
        if row >= 0 and row < 10:
            col = colIn - 1
            while col <= (colIn + 1):
                if col >= 0 and col < 10:
                    bombNumber += GameMasterList[row][col]
                col += 1
        row += 1
    return bombNumber


numBombs = int(input("How many bombs should there be? (1 - 99): "))
createGameMasterField(numBombs)

for row in GameMasterList:
    print(row)

guess = 0
createUserField()
while guess < (100 - numBombs):
    printUserField()
    pickRow = (int(input("Choose a row (1 - 10): ")) - 1) 
    pickColumn = (int(input("Choose a column (1-10): ")) - 1)
    nextStep = changeUserField(pickRow, pickColumn)
    if nextStep == "Over":
        print("GAME OVER!! YOU HIT A BOMB!")
        for i in range(0, 10):
            for j in range(0, 10):
                if GameMasterList[i][j] == 1:
                    UserList[i][j] = "X"
        printUserField()
        break
    elif nextStep == "OK":
        numberOfBombs = surroundingBombNumber(pickRow, pickColumn)
        UserList[pickRow][pickColumn] = str(numberOfBombs)
    guess += 1
        