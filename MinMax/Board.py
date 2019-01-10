# This class is used to represent the game board
class Board:
    # 1D array because I wanted it to keep track of the player
    board = []

    def __init__(self, start=[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]):
        # 0-8 represent board spaces 9 represents player
        # start is the starting layout of the board
        self.board = start

    # Return the player taking their turn
    def get_turn(self):
        return self.board[9]

    def get_board(self):
        return self.board

    # Print the board neatly
    def print_board(self):
        line = "-------"
        brd = ""
        for i in range(3):
            brd = brd + "|"
            for j in range(3):
                brd = brd + str(self.board[3 * i + j]) + "|"
            brd = brd + "\n" + line + "\n"
        print(brd)

    # If no piece has moved at place then it will place a piece there and change turns
    def move(self, place):
        if self.board[place] == 0:
            self.board[place] = self.get_turn()
            if self.get_turn() == 1:
                self.board[9] = 2
            else:
                self.board[9] = 1

    # Returns a copy of the board with a movement
    def make_child(self, place):
        lis = self.board.copy()
        child = Board(lis)
        child.move(place)
        return child

    # Checks all gameover conditions to see if anyone of them is true
    def game_over(self):
        if ((self.board[0] != 0 and self.board[0] == self.board[1] and self.board[0] == self.board[2]) or
                (self.board[3] != 0 and self.board[3] == self.board[4] and self.board[3] == self.board[5]) or
                (self.board[6] != 0 and self.board[6] == self.board[7] and self.board[6] == self.board[8]) or
                (self.board[0] != 0 and self.board[0] == self.board[3] and self.board[0] == self.board[6]) or
                (self.board[1] != 0 and self.board[1] == self.board[4] and self.board[1] == self.board[7]) or
                (self.board[2] != 0 and self.board[2] == self.board[5] and self.board[2] == self.board[8]) or
                (self.board[0] != 0 and self.board[0] == self.board[4] and self.board[0] == self.board[8]) or
                (self.board[6] != 0 and self.board[6] == self.board[4] and self.board[6] == self.board[2])):
            return True
        else:
            if 0 in self.board:
                return False
            return True

    # Returns True if the spot is 0
    def isfree(self, place):
        return self.board[place] == 0

