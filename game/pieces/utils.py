#Usado para calcular movimientos posibles en todas las direcciones en king.py
def gather_positions(row, col, *position_functions):
    possibles = []
    for func in position_functions:
        possibles += func(row, col)
    return possibles