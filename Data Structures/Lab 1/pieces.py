from chess_piece import Chess_Piece

class Pawn(Chess_Piece):
    def __init__(self, ID, position, color, direction, board_size = (8,8), piece_on_board = 0,
                 valid_moves = 0, move = 0, remove = 0, take = 0, replace = 0, place = (None, None)):
        super().__init__(ID, position, color, direction, board_size)

    def get_valid_moves(self):
        validMoves = []
        x = self.position[0]
        y = self.position[1]
        bX = self.board_size[0]-1
        bY = self.board_size[1]-1
        if (self.direction == "UP"):
            move1 = y + 1
            move2 = y + 2
            if (move1<=bY):
                validMoves.append((x, move1))
            if (move2<=bY):
                validMoves.append((x, move2))
        else:
            move1 = y - 1
            move2 = y - 2
            if (move1>0):
                validMoves.append((x, move1))
            if (move2>0):
                validMoves.append((x, move2))
        return validMoves

    def take(self, chess_Piece):
        x = self.position[0]
        y = self.position[1]
        enemyX = chess_Piece.position[0]
        enemyY = chess_Piece.position[1]
        if self.direction == "UP":
            if ((x-1 == enemyX) and (y+1 == enemyY)) or ((x+1 == enemyX) and (y+1 == enemyY)):
                self.position = chess_Piece.position
                chess_Piece.position = (None, None)
        else:
            if ((x-1 == enemyX and y-1 == enemyY)) or ((x+1 == enemyX and y-1 == enemyY)):
                self.position = chess_Piece.position
                chess_Piece.position = (None, None)

    def replace(self, chess_Piece):
        if chess_Piece.position == (None, None):
            chess_Piece.position = self.position
            self.remove()

class King(Chess_Piece):
    def __init__(self, ID, position, color, direction, board_size = (8,8), piece_on_board = 0,
                 valid_moves = 0, move = 0, remove = 0, take = 0, place = (None, None)):
        super().__init__(ID, position, color, direction, board_size)

    def get_valid_moves(self):
        validMoves = []
        x = self.position[0]
        y = self.position[1]
        bX = self.board_size[0]-1
        bY = self.board_size[1]-1
        posMoveX = x + 1
        posMoveY = y + 1
        negMoveX = x - 1
        negMoveY = y - 1
        #checks y positions that are on the same x as piece
        if (x <= bX):
            if (posMoveY<= bY):
                validMoves.append((x,posMoveY))
            if (negMoveY>=0):
                validMoves.append((x,negMoveY))

        #checks y positions for spots in front of the piece
        if (posMoveX <= bX):
            if (posMoveY<= bY):
                validMoves.append((posMoveX,posMoveY))
            if (negMoveY>=0):
                validMoves.append((posMoveX,negMoveY))
            if (y <= bX):
                validMoves.append((posMoveX,y))

        #checks y positions for spots below the piece
        if (negMoveX>0):
            if (posMoveY<= bY):
                validMoves.append((negMoveX,posMoveY))
            if (negMoveY>=0):
                validMoves.append((negMoveX,negMoveY))
            if (y <= bX):
                validMoves.append((negMoveX,y))
        return validMoves

class Knight(Chess_Piece):
    def __init__(self, ID, position, color, direction, board_size = (8,8), piece_on_board = 0,
                 valid_moves = 0, move = 0, remove = 0, take = 0, place = (None, None)):
        super().__init__(ID, position, color, direction, board_size)

    def get_valid_moves(self):
        validMoves = []
        x = self.position[0]
        y = self.position[1]
        bX = self.board_size[0]-1
        bY = self.board_size[1]-1
        #2 up, 1 left or right
        if (y+2<=bY):
            if (x-1>=0):
                validMoves.append((x-1,y+2))
            if (x+1<= bX):
                validMoves.append((x+1, y+2))   

        #2 down, 1 left or right
        if (y-2>=0):
            if (x-1>=0):
                validMoves.append((x-1,y-2))
            if (x+1<= bX):
                validMoves.append((x+1, y-2))

        #2 right, 1 up or down
        if (x+2<= bX):
            if (y-1>=0):
                validMoves.append((x+2,y-1))
            if (y+1<= bY):
                validMoves.append((x+2, y+1))

        #2 right, 1 up or down
        if (x-2>=0):
            if (y-1>=0):
                validMoves.append((x-2,y-1))
            if (y+1<= bY):
                validMoves.append((x-2, y+1))
        return validMoves


class Bishop(Chess_Piece):
    def __init__(self, ID, position, color, direction, board_size = (8,8), piece_on_board = 0,
                 valid_moves = 0, move = 0, remove = 0, take = 0, place = (None, None)):
        super().__init__(ID, position, color, direction, board_size)

    def get_valid_moves(self):
        validMoves = []
        x = self.position[0]
        y = self.position[1]
        bX = self.board_size[0]-1
        bY = self.board_size[1]-1
        i = 1
        #Moves up and right
        while ((y+i<=bY) and (x+i<=bX)):
            validMoves.append((x+i, y+i))
            i+=1
        i = 1

        #Moves down and right
        while ((y-i>=0) and (x+i<=bX)):
            validMoves.append((x+i, y-i))
            i+=1
        i = 1

        #Moves up and left 
        while ((y+i<=bY) and (x-i>=0)):
            validMoves.append((x-i, y+i))
            i+=1
        i = 1

        #Moves down and left
        while ((y-i>=0) and (x-i>=0)):
            validMoves.append((x-i, y-i))
            i+=1   
        return validMoves

class Rook(Chess_Piece):
    def __init__(self, ID, position, color, direction, board_size = (8,8), piece_on_board = 0,
                 valid_moves = 0, move = 0, remove = 0, take = 0, place = (None, None)):
        super().__init__(ID, position, color, direction, board_size)

    def get_valid_moves(self):
        validMoves=[]
        x = self.position[0]
        y = self.position[1]
        bX = self.board_size[0]-1
        bY = self.board_size[1]-1
        i = 0
        p = 0
        #move left and right
        while (i<=bX):
            if (i!=x):
                validMoves.append((i,y))
            i+=1
                
        #move up and down
        while (p<=bY):
            if (p!=y):
                validMoves.append((x,p))
            p+=1
        return validMoves

class Queen(Rook, Bishop):
    def __init__(self, ID, position, color, direction, board_size = (8,8), piece_on_board = 0,
                 valid_moves = 0, move = 0, remove = 0, take = 0, place = (None, None)):
        super().__init__(ID, position, color, direction, board_size)
        
    def get_valid_moves(self):
        #calls on both rook and bishops get_valid_moves and combines output
        a = Rook.get_valid_moves(self)
        b = Bishop.get_valid_moves(self)
        return a+b
    
