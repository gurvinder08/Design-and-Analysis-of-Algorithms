grid=[[5,1,7,6,0,0,0,3,4],
      [2,8,9,0,0,4,0,0,0],
      [3,4,6,2,0,5,0,9,0],
      [6,0,2,0,0,0,0,1,0],
      [0,3,8,0,0,6,0,4,7],
      [0,0,0,0,0,0,0,0,0],
      [0,9,0,0,0,0,0,7,8],
      [7,0,3,4,0,0,5,6,0],
      [0,0,0,0,0,0,0,0,0]]


backtracks=0
def findEmpty(gd):
    for i in range(len(gd)):
        for j in range(len(gd[0])):
            if gd[i][j]==0:
                return (i,j)
    return None

def displayGrid(gd):
    for i in range(len(gd)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - - ")
        for j in range(len(gd[0])):
            if j%3==0 and j!=0:
                print("|", end="")
            if j==8:
                print(gd[i][j])
            else:
                print(str(gd[i][j]), " ", end="")


def validateGrid(gd, num , pos):
    for i in range(len(gd[0])):
        if gd[pos[0]][i]==num and pos[1]!=i:
            return False
    for i in range(len(gd)):
        if gd[i][pos[1]]==num and pos[0]!=i:
            return False

    xgrid=pos[1] // 3
    ygrid= pos[0] //3

    for i in range(ygrid*3,ygrid*3+3):
        for j in range(xgrid*3,xgrid*3+1):
            if gd[i][j]==num and (i,j) != pos:
                return False
    return True


def solvesudoku(gd):
    global backtracks
    find= findEmpty(gd)
    if not find:
        return True
    else:
        row,col=find
    for i in range(1,10):
        if validateGrid(gd,i,(row,col)):
            gd[row][col]=i
            if solvesudoku(gd):
                return True
            backtracks+=1
            gd[row][col]=0
    return False


displayGrid(grid)
solvesudoku(grid)
print("_____________________________")
print(" ")
displayGrid(grid)
print(("Number of backtracks:",backtracks))


