import copy
import time
import numpy as np


class Game(object):
    """A tic-tac-toe game."""

    def __init__(self, grid):
        """Instances differ by their grid marks."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the game board."""
        for row in self.grid:
            print(row)

    def moves(self):
        """Return a list of possible moves given the current marks."""
        possible_moves = []
        index = 0
        for row in self.grid:
            for item in row:
                if(item == "-"):
                    possible_moves.append(index)
                ++index
        return possible_moves  # returns a list of indexes ex. [2,5,7]
        # Basically, check which space has - and return that this is a
        # a possible move. We will use it afterwards with minimax
        # returns the pair of possible locations

    def neighbor(self, move, mark):
        new_move = Game(self.grid)
        new_move.grid[move[0]][move[1]] = mark
        return new_move

    def utility(self):
        # turn 2d array into 1d array
        new_grid = np.resize(self.grid, (3, 3))
        if '-' not in new_grid:
            return 0
        win = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for i, j, k in win:
            if new_grid[i] == new_grid[j] == new_grid[k] and new_grid[i] != '-':
                self.
        #         if self.mark == "Y":
        #             return -1
        #         if self.mark == "X":
        #             return 1
            return None
        # YOU FILL THIS IN
        # for utility here, check the code from this link
        # http://www.sarathlakshman.com/2011/04/29/writing-a-tic-tac
        # to calculate the utility of this current board.


class Agent(object):
    """Knows how to play tic-tac-toe."""

    def __init__(self, mark):
        """Agents use either X or O."""
        self.mark = mark

    def minvalue(self, game, opponent):
        """Compute the lowest utility this game can have."""
        score = game.utility()
        if score != None:
            return (score, None)

        for move in game.moves():
            mark, _ = opponent.maxvalue(game.neighbor(move, self.mark), self)
        # bestvalue = float("inf")
        # for item in game.moves():
        #     score = game.utility
        #     if score != None:
        #         return (item, score)
        #     else:
        #         new_game = game.neighbor(item, self.mark)
        #         max_score = self.maxvalue(new_game, opponent)
        #         bestvalue = min(max_score, score)
        #         return (item, bestvalue)

    def maxvalue(self, game, opponent):
        """Compute the highest utility this game can have."""
        score = game.utility()
        if score != None:
            return (score, None)

        for move in game.moves():
            val, _ = opponent.minvalue(game.neighbor(move, self.mark), self)
        return (val, move)

        # bestvalue = float("-inf")
        # for item in game.moves():
        #     new_game = game.neighbor(item, self.mark)
        #     print(new_game)
        #     score = new_game.utility()
        #     print("Score ", score)
        #     # score = game.utility()
        #     if score != None:
        #         return (item, score)
        #     else:
        #         new_game = game.neighbor(item, self.mark)
        #         min_score = self.minvalue(new_game, opponent)
        #         print("MinScore: ", min_score, "Score: ", score)
        #         bestvalue = max(min_score, score)
        #         return (item, bestvalue)


def main():
    """Create a game and have two agents play it."""

    game = Game([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
    game.display()

    maxplayer = Agent('X')
    minplayer = Agent('O')
    (value, move) = maxplayer.maxvalue(game, minplayer)
    # print(value, move)
    game.display()
    
    # (value, move) = maxplayer.maxvalue(game, minplayer)
    # game = game.neighbor(move, maxplayer.mark)
    # game.display()


if __name__ == '__main__':
    main()
