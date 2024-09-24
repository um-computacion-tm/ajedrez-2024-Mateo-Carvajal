# Clase base para las excepciones del ajedrez
class ChessException(Exception):
    pass

# Excepción para piezas seleccionadas inválidas
class NoPiecesSelected(ChessException):
    def __init__(self, message = "No hay ninguna pieza en esta posición"):
        self.message = message
        super().__init__(message)
        

# Excepción una pieza se mueve fuera del tablero
class OutOfBounds(ChessException):
    def __init__(self, message = "Coordenadas fuera de los límites del tablero"):
        self.message = message
        super().__init__(message)

# Excepción se intenta mover una pieza fuera de turno
class WrongTurn(ChessException):
    def __init__(self, message = "No es tu turno"):
        self.message = message
        super().__init__(message)
        
# Excepción movimientos inválidos para una pieza específica
class InvalidPieceMovement(ChessException):
    def __init__(self, message = "Movimiento inválido para esta pieza"):
        self.message = message
        super().__init__(self.message)

