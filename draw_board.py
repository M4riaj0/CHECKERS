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
    def __init__(self, screen):
        self.screen = screen
        self.createChessBoard()
        self.game = Game()
        self.drawPieces(self.game.board.pieces)

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
        for piece in pieces:
            x, y = self.convertPositionToCoords(piece.position)
            if piece.captured:
                continue  # No dibujar fichas capturadas
            color = "blue" if piece.player == 1 else "red"  # Asignar color según el jugador
            self.drawPawn(x, y, color, piece.king)

    # Método para convertir la posición de la ficha a coordenadas (x, y) en el tablero
    def convertPositionToCoords(self, position):
        #positions can be 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 .... 32
        row = (position - 1) // 4
        col = ((position - 1) % 4) * 2 + 1 - (row % 2)
        return col, row
        

    # Método para dibujar una ficha en una posición específica del tablero
    def drawPawn(self, x, y, color, isKing):
        pixelX = x * Grid.gridSize
        pixelY = y * Grid.gridSize
        square = Grid(self.screen)
        square.moveGrid(x, y)
        square.colored = False  # Dibujar la ficha sobre el espacio vacío
        square.draw()
        pawn = turtle.Turtle()
        pawn.hideturtle()
        pawn.speed(0)
        pawn.width(3)
        pawn.up()
        pawn.goto(pixelX, pixelY - Grid.gridSize // 2)
        if isKing:
            pawn.color("red")
            pawn.begin_fill()
            pawn.circle(Grid.gridSize // 4)
            pawn.end_fill()
        pawn.color(color)
        pawn.goto(pixelX, pixelY - Grid.gridSize // 3)
        pawn.begin_fill()
        pawn.circle(Grid.gridSize // 4)
        pawn.end_fill()
        pawn.up()

# Función principal
def main():
    # Configurar la pantalla
    wn = turtle.Screen()
    wn.tracer(0, 0)
    wn.title("Tablero de ajedrez")

    # Crear el tablero de ajedrez y las fichas
    chess_board = ChessBoard(wn)

    # Mantener la ventana abierta
    wn.mainloop()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
