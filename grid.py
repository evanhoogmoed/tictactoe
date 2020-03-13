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
        for row in self.grid:
          if self.grid == '-':
            possible_moves = [self.grid]
        return possible_moves
        #Basically, check which space has - and return that this is a
        #a possible move. We will use it afterwards with minimax
        #returns the pair of possible locations

    def neighbor(self, move, mark):
        """Return a Game instance like this one but with one move made."""
        
        # YOU FILL THIS IN

    def utility(self):
        """Return the minimax utility value of this game:
        1 = X win, -1 = O win, 0 = tie, None = not over yet."""
        # YOU FILL THIS IN
        # for utility here, check the code from this link
        #http://www.sarathlakshman.com/2011/04/29/writing-a-tic-tac
        #to calculate the utility of this current board.
       

class Agent(object):
    """Knows how to play tic-tac-toe."""

    def __init__(self, mark):
        """Agents use either X or O."""
        self.mark = mark

    def maxvalue(self, game, opponent):
        """Compute the highest utility this game can have."""
        # YOU FILL THIS IN

    def minvalue(self, game, opponent):
        """Compute the lowest utility this game can have."""
        # YOU FILL THIS IN

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
