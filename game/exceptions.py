# Clase base para las excepciones del ajedrez
class ChessException(Exception):
    pass

# Excepción para movimientos inválidos
class InvalidMoveException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción una pieza se mueve fuera del tablero
class OutOfBoundsException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción se intenta mover una pieza fuera de turno
class TurnException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción posiciones inválidas en el tablero
class InvalidPositionException(ChessException):
    def __init__(self, message="La posición es inválida. Debe estar dentro del tablero."):
        self.message = message
        super().__init__(self.message)

# Excepción movimientos inválidos para una pieza específica
class InvalidPieceMovementException(ChessException):
    def __init__(self, message="Movimiento no válido para esta pieza."):
        self.message = message
        super().__init__(self.message)

# Excepción se intenta hacer un movimiento en el turno de otro jugador
class WrongTurnException(ChessException):
    def __init__(self, message="Es el turno del otro jugador."):
        self.message = message
        super().__init__(self.message)
