from ABS import Queue

class Position():
    """ Defines a positional grid for the knight to move on and holds the distance
        travelled by the knight"""

    def __init__(self, x, y, distance=0):
        self.x = x
        self.y = y
        self.distance = distance

    def __add__(self, p):
        return Position(self.x + p.x, self.y + p.y, self.distance + p.distance)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def get_distance(self):
        return self.distance

def find_coordinate(pos: str) -> Position:
    """ Converts chess notation to Position on grid"""
    move_key = {"a1": Position(0, 0), "b1": Position(0, 1), "c1": Position(0, 2), "d1": Position(0, 3), "e1": Position(0, 4), "f1": Position(0, 5), "g1": Position(0, 6), "h1": Position(0, 7), 
                "a2": Position(1, 0), "b2": Position(1, 1), "c2": Position(1, 2), "d2": Position(1, 3), "e2": Position(1, 4), "f2": Position(1, 5), "g2": Position(1, 6), "h2": Position(1, 7), 
                "a3": Position(2, 0), "b3": Position(2, 1), "c3": Position(2, 2), "d3": Position(2, 3), "e3": Position(2, 4), "f3": Position(2, 5), "g3": Position(2, 6), "h3": Position(2, 7), 
                "a4": Position(3, 0), "b4": Position(3, 1), "c4": Position(3, 2), "d4": Position(3, 3), "e4": Position(3, 4), "f4": Position(3, 5), "g4": Position(3, 6), "h4": Position(3, 7), 
                "a5": Position(4, 0), "b5": Position(4, 1), "c5": Position(4, 2), "d5": Position(4, 3), "e5": Position(4, 4), "f5": Position(4, 5), "g5": Position(4, 6), "h5": Position(4, 7), 
                "a6": Position(5, 0), "b6": Position(5, 1), "c6": Position(5, 2), "d6": Position(5, 3), "e6": Position(5, 4), "f6": Position(5, 5), "g6": Position(5, 6), "h6": Position(5, 7), 
                "a7": Position(6, 0), "b7": Position(6, 1), "c7": Position(6, 2), "d7": Position(6, 3), "e7": Position(6, 4), "f7": Position(6, 5), "g7": Position(6, 6), "h7": Position(6, 7), 
                "a8": Position(7, 0), "b8": Position(7, 1), "c8": Position(7, 2), "d8": Position(7, 3), "e8": Position(7, 4), "f8": Position(7, 5), "g8": Position(7, 6), "h8": Position(7, 7)}
    
    return move_key[pos]

def valid_move(cd: Position) -> bool:
    """ Checks if move made is within the valid bounds of the chessboard"""
    if (0 <= cd.x <= 7 and 0 <= cd.y <= 7):
        return True
    return False

def Q3():
    f = open("q3_in.txt", "r")
    start = find_coordinate(f.readline().strip("\n"))
    end = find_coordinate(f.readline().strip("\n"))
    f.close()
    # 2D Grid of squares that logs where the knight has visited
    visited_squares = [[False for row in range(8)] for col in range(8)]
    # List of moves that a knight can make, adds distance travelled
    k_move = [Position(2, 1, 1), Position(1, 2, 1), Position(-1, 2, 1), Position(-2, 1, 1),
             Position(-2, -1, 1), Position(-1, -2, 1), Position(1, -2, 1), Position(2, -1, 1)]
    
    moves = Queue()
    moves.enqueue(start)

    visited_squares[start.x][start.y] = True

    # Loops until a valid move sequence to target square has been found
    while True:
        s = moves.dequeue()
        
        # Move is dequeued, if it is equal to target square then a valid sequence has been found
        if s == end:
            ans = open("q3_out.txt", "w")
            ans.write(str(s.get_distance()))
            ans.close()
            return
              
        # Takes the current position of the knight and loops through all moves the knight can make
        # Then checks if the move is within the bounds of the chess board (0,0) -> (7,7).
        # And if the position on the board has not already been visited. Then sets board position
        # to visited and enqueues the new position of the knight.
        for i in range(len(k_move)):
            candidate = s + k_move[i]
            if (valid_move(candidate) and not visited_squares[candidate.x][candidate.y]):
                visited_squares[candidate.x][candidate.y] = True
                moves.enqueue(candidate)   
                                 
Q3()

