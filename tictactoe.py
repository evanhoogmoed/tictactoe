import copy
import time
        
class Game(object):
    """A tic-tac-toe game."""

    def __init__(self, grid):
        """Instances differ by their grid marks."""
        self.grid = copy.deepcopy(grid) # No aliasing!

    def display(self):
        """Print the game board."""
        for row in self.grid:
            print(row)

    def moves(self):
        """Return a list of possible moves given the current marks."""

        onedarr = []
        for row in self.grid:
          for col in row:
            onedarr.append(col)
        
        get_indexes = lambda onedarr, xs: [i for (y, i) in zip(xs, range(len(xs))) if onedarr == y]
        moves = get_indexes('-',onedarr)
        print(moves)
        return(moves)
        


    def neighbor(self, move, mark):
        """Return a Game instance like this one but with one move made."""
        #Make game identical to this with independent copy of grid
        game = self.grid
        new_game = copy.deepcopy(game)
        other_game = []
        for row in new_game:
          for col in row:
            other_game.append(col)
        other_game[move] = mark
        return other_game
        
    def utility(self):
        """Return the minimax utility value of this game:
        1 = X win, -1 = O win, 0 = tie, None = not over yet."""
        win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8), (2,4,6)]

        for i,j,k in win_positions:
          if self.grid[i] == self.grid[j] == self.grid[k] and self.grid[i]!= '-':
            if self.grid[i] == 'X':
              return 1
            else:
              return -1
        
        if '-' not in self.grid:
          return 0
        return None
        # for utility here, check the code from this link
        #http://www.sarathlakshman.com/2011/04/29/writing-a-tic-tac
        #to calculate the utility of this current board.

class Agent(object):
    """Knows how to play tic-tac-toe."""

    def __init__(self, mark):
        """Agents use either X or O."""
        self.mark = mark

    def maxvalue(self, game, opponent):
        """Compute the highest utility this game can have.
           Return the utility and a corresponding move."""
        utility = game.utility()
        #the utility function returns none if the game is not done yet
        if utility is not None:
            return (utility, None)
        bestval = None
        bestmove = None
        for move in game.moves():
            val, _ = opponent.minvalue(game.neighbor(move, self.mark), self)
            if bestval is None or val > bestval:
                bestval, bestmove = val, move
        return (bestval, bestmove)

    def minvalue(self, game, opponent):
        """Compute the low utility this game can have.
           Return the utility and a corresponding move."""
        utility = game.utility()
        #the utility function returns none if the game is not done yet
        if utility is not None:
            return (utility, None)
        bestval = None
        bestmove = None
        for move in game.moves():
            val, _ = opponent.maxvalue(game.neighbor(move, self.mark), self)
            if bestval is None or val < bestval:
                bestval, bestmove = val, move
        return (bestval, bestmove)

def main():
    """Create a game and have two agents play it."""

    game = Game([['-','-','-'], ['-','-','-'], ['-','-','-']])
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
