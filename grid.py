import queue
import random
import math

class Board:

    def __init__(self):
        #self.board = [list(range(1, 5)), list(range(5, 9)), list(range(9, 13)), list(range(13, 16)) + ['*']]
        N = input("Input a number for the size of the board")
        N = int(N)
        size_of_board = int(math.sqrt(N+1))
        self.board = []
        begin = 1
        tempValueHolder =0

        for i in range(1,size_of_board+1):
          row = [list(range(begin,size_of_board + 1))]
          self.board.append(row)
          #begin = size_of_board+1
        #self.board = [list()]
        #self.board = [list()]

        self.goal = []
        for i in self.board:
            self.goal.append(tuple(i))
        self.goal = tuple(self.goal)
        self.empty = [3, 3]

    def __repr__(self):
        string = ''
        for row in self.board:
            for num in row:
                if len(str(num)) == 1:
                    string += '   ' + str(num)
                elif len(str(num)) > 1:
                    string += '  ' + str(num)
            string += '\n'
        return string

    def convert_to_tuple(self, ar):
        result = []
        for i in ar:
            result.append(tuple(i))
        return tuple(result)

    def convert_to_list(self, tup):
        result = []
        for i in tup:
            result.append(list(i))
        return result

    def match(self, copy):
        a = Board()
        a.board = copy
        for row in range(0, 4):
            for col in range(0, 4):
                if a.board[row][col] == '*':
                    a.empty = [row, col]
        result = []
        for i in a.board:
            result.append(list(i))
        a.board = result
        return a

    def move_up(self): # move empty block up
        try:
            if self.empty[0] != 0:
                tmp = self.board[self.empty[0]-1][self.empty[1]]
                self.board[self.empty[0]-1][self.empty[1]] = '*'
                self.board[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0]-1, self.empty[1]]
        except IndexError:
            pass

    def move_down(self): # move empty block down
        try:
            tmp = self.board[self.empty[0]+1][self.empty[1]]
            self.board[self.empty[0]+1][self.empty[1]] = '*'
            self.board[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0]+1, self.empty[1]]
        except IndexError:
            pass

    def move_right(self): # move empty block right
        try:
            tmp = self.board[self.empty[0]][self.empty[1]+1]
            self.board[self.empty[0]][self.empty[1]+1] = '*'
            self.board[self.empty[0]][self.empty[1]] = tmp
            self.empty = [self.empty[0], self.empty[1]+1]
        except IndexError:
            pass

    def move_left(self): # move empty block left
        try:
            if self.empty[1] != 0:
                tmp = self.board[self.empty[0]][self.empty[1]-1]
                self.board[self.empty[0]][self.empty[1]-1] = '*'
                self.board[self.empty[0]][self.empty[1]] = tmp
                self.empty = [self.empty[0], self.empty[1]-1]
        except IndexError:
            pass

    def shuffle(self, steps):
        for i in range(0, steps):
            direction = random.randrange(1, 5)
            if direction == 1:
                self.move_up()
            elif direction == 2:
                self.move_right()
            elif direction == 3:
                self.move_left()
            elif direction == 4:
                self.move_down()

    def solve(self):
        start = self.convert_to_tuple(self.board)
        pred = {}
        visited = []
        frontier = queue.Queue()
        frontier.put(start)
        
        while frontier.qsize() > 0:
            tmp = frontier.get()
            
            if tmp == self.goal:
                path = []
                while tmp != start:
                    path.append(pred[tmp][1])
                    tmp = pred[tmp][0]
                return path[::-1]
            
            if tmp not in visited:
                visited.append(tmp)
                tmpboard = self.match(tmp)
                tmpboard.move_up()
                if self.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.convert_to_tuple(tmpboard.board))
                    if self.convert_to_tuple(tmpboard.board) not in pred:
                        pred[self.convert_to_tuple(tmpboard.board)]=[tmp, 'up']

                
                tmpboard = self.match(tmp)
                tmpboard.move_down()
                if self.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.convert_to_tuple(tmpboard.board))
                    if self.convert_to_tuple(tmpboard.board) not in pred:
                        pred[self.convert_to_tuple(tmpboard.board)]=[tmp, 'down']

                        
                tmpboard = self.match(tmp)
                tmpboard.move_right()
                if self.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.convert_to_tuple(tmpboard.board))
                    if self.convert_to_tuple(tmpboard.board) not in pred:
                        pred[self.convert_to_tuple(tmpboard.board)]=[tmp, 'right']

                
                tmpboard = self.match(tmp)
                tmpboard.move_left()
                if self.convert_to_tuple(tmpboard.board) != tmp:
                    frontier.put(self.convert_to_tuple(tmpboard.board))
                    if self.convert_to_tuple(tmpboard.board) not in pred:
                        pred[self.convert_to_tuple(tmpboard.board)]=[tmp, 'left']

        raise Exception('There is no solution.')


board = Board()
board.shuffle(20)
print (board)
path = board.solve()
print (path)

for dir in path:
    if dir == 'right':
        board.move_right()
    if dir == 'left': 
        board.move_left()
    if dir == 'up':
        board.move_up()
    if dir == 'down':
        board.move_down()

print (board)
