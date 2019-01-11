from collections import deque


class Puzzle:
    """
    This puzzle simulates an 8 puzzle as well as provide helper methods to help solve it.
    b = the current board (or state) the puzzle is in
    dq = a doubley linked list (double ended queue)
    valid_moves = a list of moves each spot can make if it is empty
    """
    b = []
    dq = deque()
    valid_moves = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]

    def __init__(self, board, deq=deque()):
        self.b = board
        if not deq:
            self.dq.append(board)
        else:
            self.dq = deq

    def get_board(self):
        return self.b

    def get_dq(self):
        return self.dq

    def is_solved(self):
        if self.b == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return True
        return False

    def empty_square(self):
        """
        :return: the location of the 9
        """
        return self.b.index(9)

    def is_valid_move(self, move):
        if move in self.valid_moves[self.empty_square()]:
            return True
        return False

    def make_move(self, move):
        """
        :param move: location of square that wants to move
        if it is a valid move it will update the board and the queue
        """
        if self.is_valid_move(move):
            puz = self.b.copy()
            puz[self.empty_square()], puz[move] = puz[move], puz[self.empty_square()]
            self.dq.append(puz)
            self.b = puz

    def make_children(self):
        """
        :return: a list of puzzles after they had made a valid move from the current board
        """
        children = []
        for move in self.valid_moves[self.empty_square()]:
            board = self.b.copy()
            deq = self.dq.copy()
            puz = Puzzle(board, deq)
            puz.make_move(move)
            children.append(puz)
        return children

    def get_code(self):
        """
        :return: A string that has the numbers in the current order. Used for history
        """
        code = ""
        for i in self.b:
            code += str(i)
        return code

    def print_board(self, board):
        line = "-------"
        brd = ""
        for i in range(3):
            brd = brd + "|"
            for j in range(3):
                brd = brd + str(board[3 * i + j]) + "|"
            brd = brd + "\n" + line + "\n"
        brd = brd.replace("9", " ")
        print(brd)

    def print_puzzle(self):
        deq = self.dq.copy()
        while deq:
            self.print_board(deq.popleft())
            print()
