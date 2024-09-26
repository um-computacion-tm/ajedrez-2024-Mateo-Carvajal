def gather_positions(row, col, *position_functions):
    possibles = []
    for func in position_functions:
        possibles += func(row, col)
    return possibles