import random, math, os, time, Cell as C
class Maze:
    def __init__(self,dimensions):
        self.dimensions = dimensions  # should be dimensions%3 == 0
        # self.maze = [['0']*dimensions for _ in range(dimensions)]   # create maze array of size n*n
        self.maze = [[C.Cell(n,m) for m in range(dimensions)] for n in range(dimensions)]
        roomIndices = [(x,y)for y in range(1,dimensions-1,2) for x in range(1,dimensions-1,2)]
        for (x,y) in roomIndices:
            self.maze[x][y].cellType = 'room'
        startingIndex = random.choice(roomIndices)
        self.mazeDig(self.maze[startingIndex[0]][startingIndex[1]])
    

    def printMaze(self):
        for row in self.maze:
           print ''.join(['##' if i.cellType=='wall' else ('\033[94m==\033[0m' if i.cellType == 'xcooridor' else ('\033[94m||\033[0m' if i.cellType == 'ycooridor' else '00')) for i in row ])

    def getAdjacents(self,cell):
        adjacents = []
        x = cell.x
        y = cell.y
        for n in range(-2,4,2):
            for m in range(-2,4,2):#checks up down left and right and filters out impossibles
                if ( 0<=x+n<self.dimensions and 0<=y+m<self.dimensions ) and ( not(n and m) and m!=n ):
                    adjacents.append(self.maze[x+n][y+m])
        return adjacents
    
    def filterOutVisited(self,cells):
        unvisited = []
        for c in cells:
            if not c.visited:
                unvisited.append(c)
        return unvisited

    def tilt(self,currentCell,adjCells):  #no tilting done here yet
        xdif = [cell for cell in adjCells if cell.x == currentCell.x]
        ydif = [cell for cell in adjCells if cell.y == currentCell.y]
        return ydif+xdif

    def mazeDig(self,currentCell,stack=[]):
        currentCell.visited = True#current cell visited
        # for row in self.maze:
        if any(not cell.visited for cell in [item for sublist in self.maze for item in sublist]):  #if unvisitied cells
            adjacents = self.getAdjacents(currentCell)
            unvisitedAdjacents = self.filterOutVisited(adjacents)
            if unvisitedAdjacents:#if unvisitbed neighboors
                stack.append(currentCell)
                unvisitedAdjacents = self.tilt(currentCell,unvisitedAdjacents)
                nextCell = random.choice(unvisitedAdjacents)
                if not(nextCell.x - currentCell.x):  #is diff on Y 
                    currentCell.cellType = 'xcooridor'
                    self.maze[nextCell.x][min(nextCell.y,currentCell.y)+1].cellType = 'xcooridor'
                else:
                    currentCell.cellType = 'ycooridor'
                    self.maze[min(nextCell.x,currentCell.x)+1][nextCell.y].cellType = 'ycooridor'
                time.sleep(.1)
                os.system('clear')
                self.printMaze()
                self.mazeDig(nextCell,stack)
            elif stack:  #backtrack down stack till we find an acceptable one
                nextCell = stack.pop()
                self.mazeDig(nextCell,stack)
lab =  Maze(27)

