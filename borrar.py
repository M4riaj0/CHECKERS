#import needed functions
import turtle
from datetime import datetime
from random import randint

gameTitle = "pyCheckers v4.17"

#setup output window
wn = turtle.Screen()
wn.tracer(0,0)
wn.title(gameTitle)

#checks to see if coordinates (x, y) are on the board
def onGrid(x,y):
    if((x in range(8)) and (y in range(8))):
        return True
    else:
        return False

#prints a log string to the console
def logToConsole(*strings):
    dt = datetime.today()
    print("<%02i/%02i/%04i" % (dt.month,dt.day,dt.year),end=" ")
    print("%02i:%02i:%02i>" % (dt.hour,dt.minute,dt.second),end=" ")
    for string in strings:
        print(string,end="")
    print()

#main game class
class checkers:

    #create game instance
    def __init__(self,screen):
        self.screen = screen
        self.resetGame()
        self.createTitles()

    #resets the matrix that stores game data
    def resetGame(self):
        self.turn = randint(1,2)
        logToConsole("\tStarting Player: %s" % (self.turn))
        self.createGrid()

    #create the matrix that stores the game data
    def createGrid(self):
        #create empty matrix
        self.matrix = [[None]*8,[None]*8,[None]*8,[None]*8,[None]*8,[None]*8,[None]*8,[None]*8]

        #populate matrix with grid objects and assign them attributes
        for x in range(8):
            for y in range(8):
                self.matrix[x][y] = grid(self.screen)
                self.matrix[x][y].moveGrid(x,y)
                if(((x + y) % 2) == 1):
                    self.matrix[x][y].colored = True
                    if(y in [0,1,2]):
                        self.matrix[x][y].pawn = True
                        self.matrix[x][y].player = 1
                    if(y in [5,6,7]):
                        self.matrix[x][y].pawn = True
                        self.matrix[x][y].player = 2
                self.matrix[x][y].draw()

        #create list to hold values of highlighted spaces
        self.highlightedSpaces = []
        self.spaceSelected = False

    #creates text to display game information such as the current turn
    def createTitles(self):
        self.text0 = titles(self.screen)
        self.text1 = titles(self.screen)
        self.text0.writeTitle()
        self.text1.writeTurn(self.turn)

    #this funcion is called whenever the window is clicked
    def mouseEvent(self,pixelX,pixelY):
        x = int((pixelX + 4*grid.gridSize) // grid.gridSize)
        y = int((pixelY + 4*grid.gridSize) // grid.gridSize)
        if(onGrid(x,y) == True):
            logToConsole("Mouse Event at coords (%s,%s)" % (x,y))

            #if grid clicked contains a pawn and the current player it, highlight it's possible moves
            if((self.matrix[x][y].pawn == True) and (self.matrix[x][y].player == self.turn)):
                if(self.spaceSelected != 0):
                    self.deselectAll()
                moves = self.findMoves(x,y)
                jumps = self.findJumps(x,y)
                for move in moves:
                    self.matrix[move[0]][move[1]].selected = 1
                    self.highlightedSpaces.append((move[0],move[1]))
                    self.matrix[move[0]][move[1]].draw()
                for move in jumps:
                    self.matrix[move[0]][move[1]].selected = 2
                    self.highlightedSpaces.append((move[0],move[1]))
                    self.matrix[move[0]][move[1]].draw()
                self.spaceSelected = (x,y)
                logToConsole("\tMoves Highlighted for pawn at (%s,%s)" % (x,y))

            #if grid clicked can be moved too, move the selected pawn
            elif(self.matrix[x][y].selected == 1):
                self.movePawn(self.spaceSelected,(x,y))
                self.deselectAll()
                self.endTurn()

            #if grid clicked can be jumped too, jump the selected pawn
            elif(self.matrix[x][y].selected == 2):
                self.jumpPawn(self.spaceSelected,(x,y))
                jumps = self.findJumps(x,y)
                if(jumps != []):
                    self.deselectAll()
                    self.spaceSelected = (x,y)
                    for move in jumps:
                        self.matrix[move[0]][move[1]].selected = 2
                        self.highlightedSpaces.append((move[0],move[1]))
                        self.matrix[move[0]][move[1]].draw()
                else:
                    self.deselectAll()
                    self.endTurn()
            else:
                self.deselectAll()
            logToConsole("\tMouse Event completed\n")

    #deselects all of the selected grid spaces
    def deselectAll(self):
        for space in self.highlightedSpaces:
            self.matrix[space[0]][space[1]].selected = 0
            self.matrix[space[0]][space[1]].draw()
        self.spaceSelected = False
        logToConsole("\tAll Spaces Un-highlited")

    #returns moves available to a pawn at (x, y)
    def findMoves(self,x,y):
        if(self.matrix[x][y].player == 1):
            moves = [(-1,1),(1,1)]
            if(self.matrix[x][y].king == 1):
                moves += [(-1,-1),(1,-1)]

        elif(self.matrix[x][y].player == 2):
            moves = [(-1,-1),(1,-1)]
            if(self.matrix[x][y].king == 1):
                moves += [(-1,1),(1,1)]

        coords = []
        for move in moves:
            x1 = x + move[0]
            y1 = y + move[1]
            if((onGrid(x1,y1) == True) and (self.matrix[x1][y1].pawn == False)):
                coords.append((x1,y1))
        return coords

    #returns coords of jumps available to a pawn at coords (x, y)
    def findJumps(self,x,y):
        if(self.matrix[x][y].player == 1):
            moves = [(-1,1),(1,1)]
            if(self.matrix[x][y].king == 1):
                moves += [(-1,-1),(1,-1)]

        elif(self.matrix[x][y].player == 2):
            moves = [(-1,-1),(1,-1)]
            if(self.matrix[x][y].king == 1):
                moves += [(-1,1),(1,1)]

        coords = []
        for move in moves:
            x1 = x + move[0]
            y1 = y + move[1]
            x2 = x + 2*move[0]
            y2 = y + 2*move[1]
            if((onGrid(x2,y2) == True) and (self.matrix[x2][y2].pawn == False)):
                if((self.matrix[x1][y1].pawn == True)):
                    if((self.matrix[x][y].player == 1) and (self.matrix[x1][y1].player == 2)):
                        coords.append((x2,y2))
                    elif((self.matrix[x][y].player == 2) and (self.matrix[x1][y1].player == 1)):
                        coords.append((x2,y2))
        return coords

    #moves a pawn from gridA to gridB
    def movePawn(self,gridA,gridB):
        self.matrix[gridB[0]][gridB[1]].importPawn(self.matrix[gridA[0]][gridA[1]])
        self.matrix[gridA[0]][gridA[1]].clearPawn()
        self.kingPawn(gridB[0],gridB[1])
        logToConsole("\tMoved pawn at %s to %s" % (gridA,gridB))

    #moves a pawn from gridA to gridC by jumping over the pawn in gridB
    def jumpPawn(self,gridA,gridC):
        gridB = (int((gridC[0]+gridA[0])/2),int((gridC[1]+gridA[1])/2))
        self.matrix[gridC[0]][gridC[1]].importPawn(self.matrix[gridA[0]][gridA[1]])
        self.matrix[gridB[0]][gridB[1]].clearPawn()
        self.matrix[gridA[0]][gridA[1]].clearPawn()
        self.kingPawn(gridC[0],gridC[1])
        logToConsole("\tPawn at %s jumped over pawn at %s to coords %s" % (gridA,gridB,gridC))

    #kings the pawn at coords (x, y) if it has reached it's kings row
    def kingPawn(self,x,y):
        if((self.matrix[x][y].player == 1) and (y == 7)):
            self.matrix[x][y].king = True
            self.matrix[x][y].draw()
            logToConsole("\tPawn at (%s,%s) was Kinged" % (x,y))
        elif((self.matrix[x][y].player == 2) and (y == 0)):
            self.matrix[x][y].king = True
            self.matrix[x][y].draw()
            logToConsole("\tPawn at (%s,%s) was Kinged" % (x,y))

    #ends the current turn
    def endTurn(self):
        if(self.turn == 1):
            logToConsole("\tRed Player's turn has ended")
            self.turn = 2
        elif(self.turn == 2):
            logToConsole("\tBlue Player's turn has ended")
            self.turn = 1
        self.text1.writeTurn(self.turn)

#class that writes text on the screen
class titles(turtle.RawTurtle):

    def __init__(self,screen):
        self.screen = screen
        self.createPen()

    #creates the turtle that will write the text
    def createPen(self):
        super(titles,self).__init__(self.screen)
        self.hideturtle()
        self.speed(0)
        self.width(3)
        self.up()

    #writes the game title and how to play
    def writeTitle(self):
        line0 = gameTitle
        line1 = "Click a pawn to see its possible moves"
        line2 = "Capture enemy pawns by jumping over them"
        line3 = "The player with the last pawn Wins"

        self.clear()
        self.color("black")
        self.goto(-4*grid.gridSize,4.8*grid.gridSize)
        self.write(line0,align="left",font=("Arial",20,"normal"))
        self.goto(4*grid.gridSize,5*grid.gridSize)
        self.write(line1,align="right",font=("Arial",14,"normal"))
        self.goto(4*grid.gridSize,4.75*grid.gridSize)
        self.write(line2,align="right",font=("Arial",14,"normal"))
        self.goto(4*grid.gridSize,4.5*grid.gridSize)
        self.write(line3,align="right",font=("Arial",14,"normal"))

    #writes the current turn on the screen
    def writeTurn(self,turn):
        if(turn == 1):
            string = "It's Red Player's Turn"
            self.color("red")
        elif(turn == 2):
            string = "It's Blue Player's Turn"
            self.color("blue")
        elif(turn == 0):
            string = "Turns are disabled"

        self.clear()
        self.goto(0,-5*grid.gridSize)
        self.write(string,align="center",font=("Arial",20,"normal"))

#class that defines a grid space and its properties
class grid(turtle.RawTurtle):

    #variables that set the grids size
    gridSize = 60
    pawnRadius = 20
    crownRadius = 10

    #create grid space and give it default attributes
    def __init__(self,screen):
        self.screen = screen
        self.defaultAttributes()
        self.createPen()

    #creates the turtle that will draw the grid space
    def createPen(self):
        super(grid,self).__init__(self.screen)
        self.hideturtle()
        self.speed(0)
        self.width(3)
        self.up()

    #sets the grid's attributes
    def defaultAttributes(self):
        self.gridX = 0
        self.gridY = 0
        self.colored = False #True if the square is shaded, False if white
        self.selected = 0 #0 if space is normal, 1 or 2 if space is highlighted
        self.pawn = False #True if there is a pawn on the grid space
        self.player = 0 #1 if pawn is player1 (red), 2 if pawn is player2 (blue)
        self.king = False #True if pawn has been kinged

    #removes the pawn from the grid
    def clearPawn(self):
        self.selected = False
        self.pawn = False
        self.player = 0
        self.king = False
        self.draw()

    #imports all attributes from another grid object
    def importPawn(self,gridObj):
        self.colored = gridObj.colored
        self.pawn = gridObj.pawn
        self.player = gridObj.player
        self.king = gridObj.king
        self.draw()

    #places the grid at a new set of coords
    def moveGrid(self,gX,gY):
        self.gridX = gX
        self.gridY = gY

    #draws the grid
    def draw(self):
        pixleX = int(self.gridX*grid.gridSize - 4*grid.gridSize)
        pixleY = int(self.gridY*grid.gridSize - 4*grid.gridSize)
        self.clear()

        self.goto(pixleX,pixleY)
        self.seth(0)
        self.down()
        if(self.colored == True):
            if(self.selected in [1,2]):
                self.color((0,0,0),(0.5,1,0.5))
            else:    
                self.color((0,0,0),(0.75,0.75,0.75))
            self.begin_fill()
        for f in range(4):
            self.fd(grid.gridSize)
            self.left(90)
        self.end_fill()
        self.up()

        if(self.pawn == True):
            self.goto(pixleX + 0.5*grid.gridSize,pixleY + 0.5*grid.gridSize - grid.pawnRadius)
            if(self.player == 1):
                self.color((0,0,0),(1,0.5,0.5))
            elif(self.player == 2):
                self.color((0,0,0),(0.5,0.5,1))
            else:
                self.color((0,0,0),(1,0.5,1))
            self.down()
            self.begin_fill()
            self.circle(grid.pawnRadius,360,16)
            self.end_fill()
            self.up()

            if(self.king == True):
                self.goto(pixleX + 0.5*grid.gridSize,pixleY + 0.5*grid.gridSize - grid.crownRadius)
                self.color((0,0,0),(1,0.85,0))
                self.down()
                self.begin_fill()
                self.circle(grid.crownRadius,360,16)
                self.end_fill()
                self.up()

#creates game instance
logToConsole("Program Starting...")
logToConsole("Running Game: ",gameTitle)
game = checkers(wn)

#attach mouseEvent to click
wn.onclick(game.mouseEvent)

#begin main program loop
logToConsole("Mouse Event attatched to window")
logToConsole("Beginning Main Program Loop...\n")
wn.mainloop()

#announce end of main program loop
logToConsole("Main Program Loop Ended")