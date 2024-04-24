import turtle
from checkers.game import Game
import time

# Clase para definir un espacio de la cuadrícula y sus propiedades
class Grid(turtle.RawTurtle):
    # variables que establecen el tamaño de la cuadrícula
    gridSize = 60

    # crea un espacio de la cuadrícula y le da atributos predeterminados
    def __init__(self, screen):
        self.screen = screen
        self.defaultAttributes()
        self.createPen()

    # crea la tortuga que dibujará el espacio de la cuadrícula
    def createPen(self):
        super(Grid, self).__init__(self.screen)
        self.hideturtle()
        self.speed(0)
        self.width(3)
        self.up()

    # establece los atributos de la cuadrícula
    def defaultAttributes(self):
        self.gridX = 0
        self.gridY = 0
        self.colored = False  # True si el cuadrado está sombreado, False si es blanco
        self.selected = 0  # 0 si el espacio es normal, 1 o 2 si el espacio está resaltado

    # coloca la cuadrícula en un nuevo conjunto de coordenadas
    def moveGrid(self, gX, gY):
        self.gridX = gX
        self.gridY = gY

    # dibuja el espacio de la cuadrícula
    def draw(self):
        pixelX = int(self.gridX * Grid.gridSize - 4 * Grid.gridSize)
        pixelY = int(self.gridY * Grid.gridSize - 4 * Grid.gridSize)
        self.clear()

        self.goto(pixelX, pixelY)
        self.seth(0)
        self.down()
        if self.colored:
            if self.selected in [1, 2]:
                self.color((0, 0, 0), (0.5, 1, 0.5))  # resaltado en verde claro
            else:
                self.color((0, 0, 0), (0.75, 0.75, 0.75))  # gris claro
            self.begin_fill()
        for _ in range(4):
            self.fd(Grid.gridSize)
            self.left(90)
        self.end_fill()
        self.up()

# Clase para manejar el tablero de ajedrez y las fichas
class ChessBoard:
    def __init__(self, screen, pieces):
        self.screen = screen
        self.pieces = pieces
        self.createChessBoard()
        self.drawPieces(self.pieces)

    # Función para crear el tablero de ajedrez
    def createChessBoard(self):
        for i in range(8):
            for j in range(8):
                square = Grid(self.screen)
                square.moveGrid(j, i)
                # Alternar entre blanco y gris
                if (i + j) % 2 == 0:
                    square.colored = False
                else:
                    square.colored = True
                square.draw()

    # Método para dibujar las fichas en el tablero
    def drawPieces(self, pieces):
        self.createChessBoard()
        for piece in pieces:
            if not piece.captured:
                x, y = self.convertPositionToCoords(piece.position)
                color = "blue" if piece.player == 1 else "red"  # Asignar color según el jugador
                self.drawPawn(x, y, piece.player, piece.king)

    # Método para convertir la posición de la ficha a coordenadas (x, y) en el tablero
    def convertPositionToCoords(self, position):
        row = (position - 1) // 4
        col = ((position - 1) % 4) * 2 + 1 - (row % 2)
        return col+ 0.5, row + 0.67

    # Método para dibujar una ficha en una posición específica del tablero
    def drawPawn(self, x, y, player, isKing):
        pixelX = x * Grid.gridSize - (4 * Grid.gridSize)  # Ajuste de posición para centrar la ficha en el cuadrado
        pixelY = y * Grid.gridSize - (4 * Grid.gridSize)  # Ajuste de posición para centrar la ficha en el cuadrado
        pawn = turtle.Turtle()  # Usar la misma tortuga para dibujar la ficha en el cuadrado existente
        pawn.hideturtle()
        pawn.speed(0)
        pawn.width(3)
        pawn.up()
        pawn.goto(pixelX, pixelY - Grid.gridSize // 2)
        if(player == 1):
            pawn.color((0,0,0),(1,0.5,0.5))
        elif(player == 2):
            pawn.color((0,0,0),(0.5,0.5,1))
        else:
            pawn.color((0,0,0),(1,0.5,1))
        pawn.down()
        pawn.begin_fill()
        pawn.circle(20,360,16)
        pawn.end_fill()
        pawn.up()

        if isKing:
            pawn.goto(pixelX, pixelY - Grid.gridSize*0.65 // 2)
            pawn.color((0,0,0),(1,0.85,0))
            pawn.down()
            pawn.begin_fill()
            pawn.circle( 10,360,16)
            pawn.end_fill()
            pawn.up()

# Función principal
def main():
    # Configurar la pantalla
    wn = turtle.Screen()
    wn.tracer(0, 0)
    wn.title("Checkers Game")

    # Crear el tablero de ajedrez y las fichas
    chess_board = ChessBoard(wn)

    # Mantener la ventana abierta
    wn.mainloop()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
