from abc import ABC, abstractmethod

class Chess_Piece(ABC):
    #Defines the ID, position, color, direction of a piece and also defines the board size
    
    def __init__(self, ID, position, color, direction, board_size):
        self.ID = ID
        self.position = position
        self.color = color
        self.direction = direction
        self.board_size = board_size
        

    def get_ID(self):
        #declares ID of each piece
        return self.ID

    def get_position(self):
        #able to place pieces but not move them
        return self.position

    def get_color(self):
        #Declares color of a pieces
        return self.color

    def get_direction(self):
        #declares direction the peice is facing
        return self.direction

    def get_board_size(self):
        #declares board size
        return self.board_size

    @abstractmethod
    def get_valid_moves(self):
        pass

    def is_piece_on_board(self):
        if self.position == (None,None):
            return False
        else:
            return True

    def place(self, target):
        if self.position == (None, None):
            if ((target[0]>0 and target[1]>0) and (target[0]<self.board_size[0] and target[1]<self.board_size[1])):
                self.position = target

    def move(self, target):
        a = self.get_valid_moves()
        i = 0
        while i< len(a):
            if target == a[i]:
                self.position = target
            i+=1
    
    def remove(self):
        self.position = (None, None)


    def take(self, chess_Piece):
        a = self.get_valid_moves()
        i = 0
        while i<len(a):
            if a[i] == chess_Piece.position:
                self.position = chess_Piece.position
                chess_Piece.remove()
            i+=1


