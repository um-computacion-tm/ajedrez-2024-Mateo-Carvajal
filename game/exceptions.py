# Clase base para las excepciones del ajedrez
class ChessException(Exception):
    pass

# Excepción para piezas seleccionadas inválidas
class NoPiecesSelected(ChessException):
    def __init__(self, message = "There are no pieces selected"):
        self.__message__ = message
        super().__init__(message)
        

# Excepción una pieza se mueve fuera del tablero
class OutOfBounds(ChessException):
    def __init__(self, message = "The piece is moving out of bounds"):
        self.__message__ = message
        super().__init__(message)

# Excepción se intenta mover una pieza fuera de turno
class WrongTurn(ChessException):
    def __init__(self, message = "It's not your turn"):
        self.__message__ = message
        super().__init__(message)
        
# Excepción movimientos inválidos para una pieza específica
class InvalidPieceMovement(ChessException):
    def __init__(self, message = "Invalid movement for this piece"):
        self.__message__ = message
        super().__init__(self.__message__)

