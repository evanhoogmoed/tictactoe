import copy
import time
import numpy as np


class Game(object):
    """A tic-tac-toe game."""

    def __init__(self, grid):
        """Instances differ by their grid marks."""
        self.grid = copy.deepcopy(grid)  # No aliasing!
        self.lastmoves = []
        self.winner = None

    def display(self):
        """Print the game board."""
        for row in self.grid:
            print(row)

    def possible_moves(self):   #def get_free_positions AKA def moves(self)
        """Return a list of possible moves given the current marks."""
        possible_moves = []
        for row in self.grid:
            for spot in row:
                if(spot == "-"):
                    possible_moves.append(row)
        return possible_moves  
        # returns a list of indexes ex. [2,5,7]
        # Basically, check which space has - and return that this is a
        # a possible move. We will use it afterwards with minimax
        # returns the pair of possible locations

    def neighbor(self, move, mark):
        """Return a Game instance like this one but with one move made."""
        one_move = self.grid[move] = mark
        self.lastmvoes.append(move)
        return one_move

    def mark(self, mark, pos):
        '''Mark a position with marker X or O'''
        self.board[pos] = mark
        self.lastmoves.append(pos)

    def revert_last_move(self): 
        """Undo the last move - Not an original function"""
        self.grid[self.lastmoves.pop()] = '-'
        self.winner = None

    def utility(self): #def is_gameover()
        '''Test whether game has ended'''
        win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for i, j, k in win_positions:
            if self.board[i] == self.board[j] == self.board[k] and self.board[i] != '-':
                self.winner = self.board[i]
                return True
        
        if '-' not in self.board:
            self.winner = '-'
            return True

        return False
        # YOU FILL THIS IN
        # for utility here, check the code from this link
        # http://www.sarathlakshman.com/2011/04/29/writing-a-tic-tac
        # to calculate the utility of this current board.


class Agent(object):
    """Knows how to play tic-tac-toe."""

    def __init__(self, mark):
        """Agents assigned to either X or O"""
        self.mark = mark

    def maxvalue(self, game, opponent):
        """Compute the highest utility this game can have."""
        bestscore = None
        bestmove = None

        for move in game.possible_moves():
            game.mark(self.mark, move)

            if game.utility():
                score = self.utility(game)
            else:
                move_pos, score = self.minvalue(game)

            game.revert_last_move()

            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = move
        return bestmove, bestscore


    def minvalue(self, game, opponent):
        """Compute the lowest utility this game can have."""
        bestscore = None
        bestmove = None

        for m in game.possible_moves():
            game.mark(opponent.mark, m)
        
            if game.utility():
                score = self.utility(game)
            else:
                move_position, score = self.maxvalue(game)

            game.revert_last_move

            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

def main():
    """Create a game and have two agents play it."""

    game = Game([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
    game.display()

    maxplayer = Agent('X')
    minplayer = Agent('O')

    while True:

        (value, move) = maxplayer.maxvalue(game, minplayer)
        game = game.neighbor(move, maxplayer.mark)
        time.sleep(1)
        game.display()
        
        if game.utility() is not None:
            break
        
        (value, move) = minplayer.minvalue(game, maxplayer)
        game = game.neighbor(move, minplayer.mark)
        time.sleep(1)
        game.display()
        
        if game.utility() is not None:
            break


if __name__ == '__main__':
    main()
