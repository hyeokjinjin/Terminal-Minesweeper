import random


class Minesweeper:
    
    #init function that initializes the needed variables and sets up the GameMasterList and UserList
    def __init__(self, bombInput):
        self.GameMasterList = []
        self.UserList = []
        self.bombInput = bombInput
        self.gameStatus = False
        self.userRow = 0
        self.userColumn = 0
        
        #Creates GameMasterList with known bomb locations and the UserList
        for i in range(0, 10):
            gmRowList = []
            ufRowList = []
            for j in range(0, 10):
                gmRowList.append(0)
                ufRowList.append("_")
            self.GameMasterList.append(gmRowList)
            self.UserList.append(ufRowList)
        
        #Randomly designates spots on the board to have bombs
        pickedBomb = 0
        while pickedBomb < self.bombInput:
            rowBomb = random.randint(0, 9)
            colBomb = random.randint(0, 9)
            if self.GameMasterList[rowBomb][colBomb] == 0:
                self.GameMasterList[rowBomb][colBomb] = 1
                pickedBomb += 1
        
        
    #Prints out the User's bomb field utilizing the UserList    
    def printUserField(self):
        print("     1   2   3   4   5   6   7   8   9   10")
        print("--------------------------------------------")
        for i in range(1, 11):
            if i == 10: print(str(i) + " ", end="")
            else: print(str(i) + "  ", end="")
            for spot in self.UserList[i - 1]:
                print("| " + spot + " ", end="")
            print("|")
        print("--------------------------------------------")


    #Returns a value based on if the user selected a bomb or not
    def updateUserField(self):
        if self.GameMasterList[self.userRow][self.userColumn] == 1:
            return -1
        else:
            return 1


    #Both functions used to debug
    def getGameMasterList(self) -> list[list[int]]:
        for array in self.GameMasterList:
            print(array)
        return self.GameMasterList
    def getUserList(self) -> list[list[str]]:
        for array in self.UserList:
            print(array)
        return self.UserList


    #Returns the number of bombs surrounding the inputted location
    def surrBombNum(self, userRow, userColumn):
        bombNum = 0
        row = userRow - 1
        while row <= (userRow + 1):
            if row >= 0 and row < 10:
                col = userColumn - 1
                while col <= (userColumn + 1):
                    if col >= 0 and col < 10:
                        bombNum += self.GameMasterList[row][col]
                    col += 1
            row += 1
        return bombNum


    #Returns a list containing the surrounding locations of the inputted location
    def getSurroundings(self, userRow, userColumn):
        surroundList =[]
        row = userRow - 1
        while row <= (userRow + 1):
            if row >= 0 and row < 10:
                col = userColumn - 1
                while col <= (userColumn + 1):
                    if col >= 0 and col < 10:
                        surroundList.append([row, col])
                    col += 1
            row += 1
        surroundList.remove([userRow, userColumn])
        return surroundList


    #Recursion function that automatically reveals the surrounding locations with 0 or reveals the bomb number
    def surrAutoReveal(self, userRow, userColumn):
        self.UserList[userRow][userColumn] = str(self.surrBombNum(userRow, userColumn))
        for location in self.getSurroundings(userRow, userColumn):
            if self.surrBombNum(location[0], location[1]) == 0 and self.UserList[location[0]][location[1]] == "_":
                self.UserList[location[0]][location[1]] = str(self.surrBombNum(location[0], location[1]))
                self.surrAutoReveal(location[0], location[1])
            elif self.surrBombNum(location[0], location[1]) != 0 and self.GameMasterList[location[0]][location[1]] != 1:
                self.UserList[location[0]][location[1]] = str(self.surrBombNum(location[0], location[1]))


    #Calculates how many untouched spots on the UserField is left
    def getLeftSpots(self):
        leftSpot = 0
        for array in self.UserList:
            for spot in array:
                if spot == "_":
                    leftSpot += 1
        return leftSpot


    #Main game function. Continuously loops until user either hits a bomb or has only untouched bomb spots left.
    def gameEnder(self): 
        try:
            self.printUserField()   
            while self.gameStatus == False:
                self.userRow = (int(input("Choose a row (1 - 10): ")) - 1)
                self.userColumn = (int(input("Choose a column (1 - 10): ")) - 1)
                if self.updateUserField() == -1:
                    print()
                    print()
                    print()
                    print("GAME OVER!! YOU HIT A BOMB!")
                    for i in range(0, 10):
                        for j in range(0, 10):
                            if self.GameMasterList[i][j] == 1:
                                self.UserList[i][j] = "X"
                    self.printUserField()
                    self.gameStatus = True
                elif self.updateUserField() == 1:
                    print()
                    print()
                    print()
                    self.surrAutoReveal(self.userRow, self.userColumn)
                    self.printUserField()
                    if self.bombInput == self.getLeftSpots():
                        self.gameStatus = True
                        print("Congratulations! You cleared the board without blowing up!")
        except (IndexError, ValueError):
            print("Invalid Input! Try again.")
            self.gameEnder()


#Creates an instance of the Minesweeper class and then loops in the gameEnder() function
game = Minesweeper(int(input(
    "Choose the number of bombs on the field (1 - 99): ")))
game.gameEnder()