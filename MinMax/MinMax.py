from Board import Board


# This file will allow the user to play Tic Tac Toe with an AI
# The AI will be using the minmax algorithm with alpha beta pruning

def eval_pieces(pieces, max_player):
    # Helper function for evaluate
    score = 0
    if pieces[0] + pieces[1] == 3 and pieces[1] > 0:
        temp = 1 * (10 ** (pieces[1] - 1))
        if max_player != 1:
            temp = temp * -1
        score += temp
    elif pieces[0] + pieces[2] == 3 and pieces[2] > 0:
        temp = 1 * (10 ** (pieces[2] - 1))
        if max_player != 2:
            temp = temp * -1
        score += temp
    elif pieces[1] + pieces[2] == 3:
        if not pieces[max_player] == 2:
            score += 50
    return score


def evaluate(board, max_player):
    """
    :return: the score of the board
    How to score:
    +1 for one in a line and two empty cells
    +10 for two in a line and one empty cells
    +50 for blocking min player
    +100 for three in a line
    - same criteria for opponents pieces
    a line is the 3 horizontals, 3 verticals, and 2 diagonals
    """
    score = 0

    # Horizontals
    for i in range(3):
        pieces = [0, 0, 0]
        for j in range(3):
            pieces[board.get_board()[3 * i + j]] += 1
        score += eval_pieces(pieces, max_player)

    # Verticals
    for i in range(3):
        pieces = [0, 0, 0]
        for j in range(3):
            pieces[board.get_board()[3 * j + i]] += 1
        score += eval_pieces(pieces, max_player)

    # Diagonals
    pieces = [0, 0, 0]
    pieces[board.get_board()[0]] += 1
    pieces[board.get_board()[4]] += 1
    pieces[board.get_board()[8]] += 1
    score += eval_pieces(pieces, max_player)

    pieces = [0, 0, 0]
    pieces[board.get_board()[2]] += 1
    pieces[board.get_board()[4]] += 1
    pieces[board.get_board()[6]] += 1
    score += eval_pieces(pieces, max_player)

    return score


def minmax(board, depth, max_player, alpha, beta):
    """
    :param board: the Board object being evaluated
    :param depth: the depth that it searched
    :param max_player: which player is max
    :param alpha: the value of alpha
    :param beta: the value of beta
    :return: which move it thinks is best
    Uses the minmax algorithm with alpha beta pruning.
    Minmax searches through possible moves and finds the best move for the max player.
    Alpha beta pruning decreases the amount we have to search through the board.
    """

    MAX_DEPTH = 1  # The max depth it goes through

    if board.game_over() or depth >= MAX_DEPTH:
        return {"best": evaluate(board, max_player), "child": board}

    if max_player == board.get_turn():
        best = -1000
        best_child = []
        for i in range(9):
            if board.isfree(i):
                child = board.make_child(i)
                value = minmax(child, depth + 1, max_player, alpha, beta)["best"]
                best = max(best, value)
                if best == value:
                    best_child = i
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return {"best": best, "child": best_child}
    else:
        best = 1000
        best_child = []
        for i in range(9):
            if board.isfree(i):
                child = board.make_child(i)
                value = minmax(child, depth + 1, max_player, alpha, beta)["best"]
                best = min(best, value)
                if best == value:
                    best_child = i
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return {"best": best, "child": best_child}


def play():
    game = Board()
    game.print_board()
    while not game.game_over():
        if game.get_turn() == 1:
            move = input("Enter space 0-8: ")
            game.move(int(move))
        else:
            game.move(minmax(game, 0, 2, -1000, 1000)["child"])
        game.print_board()


if __name__ == "__main__":
    play()
