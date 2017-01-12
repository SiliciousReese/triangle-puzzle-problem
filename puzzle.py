class Triangle_Puzzle:
    ''' TODO A triangle of integers. In each row, there should be one more integer
    than in the previous row. Only positive integers are allowed. '''

    def __init__(self, puzzle_array):
        '''
        TODO Create valid puzzle from array or throw exception if not valid.
        '''
        pass

    def getRandomPuzzle():
        ''' TODO Returns a random, valid, Triangle_Puzzle. '''

        puzzle_array = [0]
        return Triangle_Puzzle(puzzle_array)

    def draw_Puzzle_new(self):
        ''' TODO Draw the puzzle. '''
        pass

    def draw_Puzzle(puzzle):
        '''
        Print an array to standard out. This method will be deprecated by
        draw_Puzzle_New().
        '''

        newline_vals = [0]

        prev_val = 0
        counter = 2

        for i in range(len(puzzle)):
            prev_val = prev_val + counter
            newline_vals.append(prev_val)
            counter += 1

        out_string = ''

        for i in range(len(puzzle)):
            out_string += str(puzzle[i]) + ' '

            if i in newline_vals:
                print(out_string)
                out_string = ''


class Triangle_Puzzle_Path:
    ''' TODO A path through a Triangle_Puzzle '''

    def __init__(self):
        ''' TODO Create valid path. '''
        pass

    def draw_Puzzle_Path(self, puzzle):
        ''' TODO Draw the triangle puzzle with the path shown. '''
        pass


if __name__ == '__main__':

    # print('''\
    #       1
    #       2 3
    #       4 5 6
    #       7 8 9 9''')

    simple_puzzle = [1, 2, 3, 4, 5, 6]
    Triangle_Puzzle.draw_Puzzle(simple_puzzle)

    # print(simple_puzzle[0])
    # print(simple_puzzle[1], simple_puzzle[2])
    # print(simple_puzzle[3], simple_puzzle[4], simple_puzzle[5])

    pass
