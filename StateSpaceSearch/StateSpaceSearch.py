from Puzzle import Puzzle
from queue import Queue

def sss(puzzle):
    """
    :param puzzle: Put an eight Puzzle in and if it can be solved it will be solved
    :return: solved puzzle
    Uses State Space Search Algorithm (with history) to iterate through all possible moves
    in Breadth First Search order to find the solved state.
    """
    q = Queue()
    history = {}
    q.put(puzzle)
    history[puzzle.get_code()] = True
    while not q.empty():
        p = q.get()
        if p.is_solved():
            return p
        else:
            for child in p.make_children():
                if child.get_code() not in history:
                    history[child.get_code()] = True
                    q.put(child)
    print("Not Solvable")

if __name__ == "__main__":
    puz = Puzzle([2,4,1,7,6,8,3,9,5])
    solved = sss(puz)
    solved.print_puzzle()
