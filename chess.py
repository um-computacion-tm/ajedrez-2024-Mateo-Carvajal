class Chess:
    def __init__(self, board, turn):
        self.__board__ = board()
        self.__turn__ = "White" # White or Black
    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col
    ):
        #validate cords
        piece = self.board.get_piece(from_row, from_col)
        self.change_turn()
       
    def change_turn(self):
        if self.__turn__ == "White":
            self.__turn__ = "Black"
        else:
            self.__turn__ = "White"