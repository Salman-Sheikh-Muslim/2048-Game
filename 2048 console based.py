from random import randrange

def printGrid(): #actions
    for i in range(4):
        for j in range(4):
            endSpace="     "
            if(grid[i][j] > 9):
                endSpace = "    "
            if(grid[i][j] > 99):
                endSpace = "   "
            if(grid[i][j] > 999):
                endSpace = "  "
            print(grid[i][j] , end = endSpace)
        print("")



def generate():
    odds = randrange(5)         #60 % chance of 2 and 40 % chance of 4
    if(odds >= 0 and odds <= 2):
        randnumber=2
    else:
        randnumber=4
        
    randrow = randrange(4) #generates cordinates for filling tiles at random
    randcol = randrange(4) 
    
    while(grid[randrow][randcol] > 0 ): #greater than 0 tile filled
        randrow = randrange(4)         #will run untill empty till is selected
        randcol = randrange(4)
    
    grid[randrow][randcol] = randnumber
        


def compareGrid(grid1, grid2):
    for row in range(4):
        for col in range(4):
            if(grid1[row][col] != grid2[row][col]):
                return False
    return True

def endGame(grid1):
    for row in range(4):
        for col in range(4):
            if(grid1[row][col] == 2048):
                return True
    return False

def No_moves_possibe(grid1):
    for row in range(4):
        for col in range(4):
            if(grid1[row][col] == 0):
                return False
    return True

def merge(row, column, rowSecond, columnSecond):
    grid[rowSecond][columnSecond] =2*grid[rowSecond][columnSecond]

def shift_up(col): #for column 2_index
    for row in range(1 , 4): # Looping from top to bottom in the coloujmn so we can shift all of them up
        searchRow = row - 1  # will be used to search a cell above the current cell that is filled.
        while(grid[searchRow][col] == 0 and  searchRow > 0 ): #Will keep running to find a cell that is filled
            searchRow = searchRow - 1
        #Search row is now either at the top or found a filled cell.
        if(searchRow == 0 and grid[searchRow][col] == 0 ): #searchrow hit top and top number not filled , move current number to the top
            grid[0][col] = grid[row][col] # moves value to the top
            grid[row][col] = 0
        
        elif(grid[searchRow][col] == grid[row][col]): #if searchRow found cell that is filled and same a the current number
            merge(row, col, searchRow, col)
            grid[row][col] = 0
        
        elif(row > searchRow + 1): #cell filled value not same (searched cell is not directlty above the current cell)
            grid[searchRow+1][col] = grid[row][col]  # eg moves from row 3 to row 2
            grid[row][col] = 0

def shift_right(row):
    for col in range(2 , -1, -1): 
        searchCol = col + 1 
        while(grid[row][searchCol] == 0 and  searchCol < 3 ): 
            searchCol = searchCol + 1
       
        if(searchCol == 3 and grid[row][searchCol] == 0 ): 
            grid[row][3] = grid[row][col] 
            grid[row][col] = 0
        
        elif(grid[row][searchCol] == grid[row][col]): 
            merge(row, col, row, searchCol)
            grid[row][col] = 0
        
        elif(row < searchCol - 1): 
            grid[row][searchCol - 1] = grid[row][col] 
            grid[row][col] = 0

def shift_left(row): 
    for col in range(1 , 4): 
        searchCol = col - 1  
        while(grid[row][searchCol] == 0 and  searchCol > 0 ): 
            searchCol = searchCol - 1
            
        if(searchCol == 0 and grid[row][searchCol] == 0 ): 
            grid[row][0] = grid[row][col] 
            grid[row][col] = 0
        
        elif(grid[row][searchCol] == grid[row][col]):  
            merge(row, col, row, searchCol)
            grid[row][col] = 0
        
        elif(row > searchCol + 1): 
            grid[row][searchCol+1] = grid[row][col]  
            grid[row][col] = 0

def shift_down(col): 
    for row in range(2 , -1, -1): 
        searchRow = row + 1 
        while(grid[searchRow][col] == 0 and  searchRow < 3 ): 
            searchRow = searchRow + 1
       
        if(searchRow == 3 and grid[searchRow][col] == 0 ): 
            grid[3][col] = grid[row][col] 
            grid[row][col] = 0
        
        elif(grid[searchRow][col] == grid[row][col]): 
            merge(row, col , searchRow ,col)
            grid[row][col] = 0
        
        elif(row < searchRow - 1): 
            grid[searchRow - 1][col] = grid[row][col] 
            grid[row][col] = 0

grid = [[0 , 0 , 0 , 0], [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]











print("2048 Game is starting")

generate() # always two numbers at the start of the game
generate()

# a[1]=[0];
# b[1]=[1];
# c[1]=[2];
# d[1]=[3];

while(True):  #for now infinite due to TRUE
    printGrid()

    move = input("Move up , right , left or down. Enter 'W' ,  'D', 'A' , 'S' ")

    tempGrid = [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
    for row in range(4):
        for col in range(4):
            tempGrid[row][col] = grid[row][col]
    
    if(move == "W"):
        shift_up(0)
        shift_up(1)
        shift_up(2)
        shift_up(3)

            

    elif(move == "D"):
        shift_right(0)
        shift_right(1)
        shift_right(2)
        shift_right(3)

    elif(move == "A"):
        shift_left(0)
        shift_left(1)
        shift_left(2)
        shift_left(3)

    elif(move == "S"):
        shift_down(0)
        shift_down(1)
        shift_down(2)
        shift_down(3)
    
    if(compareGrid(grid, tempGrid) == False): #shift happens
        generate() #one random number is generated after each move
    
    if(No_moves_possibe(grid) == True):
        print("You Lost no more moves possible")
        break
    
    if(endGame(grid) == True):
        print("You Won")
        break
