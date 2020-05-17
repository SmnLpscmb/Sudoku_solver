#Sudoku Solver

class Sudoku(object):

    def __init__(self, grid):
        """
        grid is a list of lists, representing each row of the grid;
        grid is made of rows, columns and squares, each composed of cases
        """
        self.rows = grid
        self.update(self.rows)

    def update(self, grid):
        self.rows = grid
        self.columns = [[x[y] for x in grid] for y in range(9)]
        squares = []
        row, column = 0, 0
        for i in range(9):
            square = []
            for j in range(row, row+3):
                for k in range(column, column+3):
                    square.append(grid[j][k])
            squares.append(square)
            column += 3
            if column == 9:
                column = 0
                row += 3
        self.squares = squares
        cases = {}
        row = 0
        for elt in grid:
            row += 1
            column = 1
            for case in elt:
                cases[(row, column)] = case
                column += 1
        self.cases = cases

    def is_solved(self):
        return '0' not in self.cases.values()

    def getRow(self, case):
        return self.rows[case[0]-1]

    def getColumn(self, case):
        return self.columns[case[1]-1]

    def getSquare(self, case):
        row_pos = (case[0] - 1) // 3
        column_pos = (case[1] -1) // 3
        square_rows = [
                    [self.squares[0], self.squares[1], self.squares[2]],
                    [self.squares[3], self.squares[4], self.squares[5]],
                    [self.squares[6], self.squares[7], self.squares[8]]
                    ]
        return square_rows[row_pos][column_pos]

    def is_possible(self, number, case):
        """number the number we're trying, case the coordinates of the case"""
        return self.cases[case] == '0' and number not in self.getRow(case) and number not in self.getColumn(case) and number not in self.getSquare(case)

    def getPossibility(self, case):
        """returns a list of possible numbers that could go in the case"""
        numbers = ['1','2','3','4','5','6','7','8','9']
        for number in numbers[:]:
            if number in self.getRow(case) or number in self.getColumn(case) or number in self.getSquare(case):
                numbers.remove(number)
        return numbers

    def is_only_possible_here(self, number, case):
        possible_in_row = []
        possible_in_column = []
        for i in range(1,10):
            possible_in_row.append(self.is_possible(number, (case[0], i)))
            possible_in_column.append(self.is_possible(number, (i, case[1])))
        possible_in_square = []
        row_pos = ((case[0]-1) // 3) * 3
        col_pos = ((case[1]-1) // 3) * 3
        for i in range(1,10):
            possible_in_square.append(self.is_possible(number, (row_pos+1, col_pos+1)))
            col_pos += 1
            if i % 3 == 0:
                col_pos -= 3
                row_pos += 1
        return sum(possible_in_row) == 1 or sum(possible_in_column) == 1 or sum(possible_in_square) == 1

    def count_zero(self):
        count = 0
        for elt in self.cases.values():
            if elt == '0':
                count += 1
        return count

    def __str__(self):
        sudoku = '-------------------------------\n'
        b = 0
        for row in self.rows:
            c = 0
            sudoku += '|'
            for elt in row:
                sudoku += ' ' + elt + ' '
                c += 1
                if c % 3 == 0:
                    sudoku += '|'
                if c % 9 == 0:
                    sudoku += '\n'
            b += 1
            if b == 3:
                sudoku += '-------------------------------\n'
                b = 0
        return sudoku

    def solve(self):
        sanity_check = 0
        while not self.is_solved():
            sanity_check += 1
            if sanity_check > 100:
                print("Err, something went wrong...")
                break
            before = 0
            after = -1
            while before != after:
                before = self.count_zero()
                for i in range(1,10):
                    for j in range(1,10):
                        if self.cases[(i,j)] == '0':
                            options = self.getPossibility((i,j))
                            if len(options) == 1:
                                self.rows[i-1][j-1] = options[0]
                                self.update(self.rows)
                after = self.count_zero()
            for i in range(1,10):
                for j in range(1,10):
                    if self.cases[(i,j)] == '0':
                        options = self.getPossibility((i,j))
                        for number in options:
                            if self.is_only_possible_here(number, (i,j)):
                                self.rows[i-1][j-1] = number
                                self.update(self.rows)
                                break
        return self

 


sudoku_ex = Sudoku([
            ['0','9','6','0','0','0','0','0','0'],
            ['0','3','0','9','0','7','6','0','0'],
            ['1','0','8','0','6','0','9','0','0'],
            ['8','0','0','0','0','6','0','0','0'],
            ['6','0','9','1','0','5','7','0','2'],
            ['0','0','0','4','0','0','0','0','3'],
            ['0','0','5','0','1','0','3','0','8'],
            ['0','0','4','7','0','9','0','0','0'],
            ['0','0','0','0','0','0','5','4','0']
            ])

# sudoku_ex2 = Sudoku([
#             ['0', '0', '3', '4', '7', '5', '0', '0', '0'],
#             ['0', '0', '0', '0', '0', '8', '0', '0', '0'],
#             ['0', '6', '5', '0', '0', '0', '0', '9', '0'],
#             ['6', '9', '0', '2', '0', '0', '0', '0', '3'],
#             ['0', '0', '0', '0', '4', '0', '0', '0', '0'],
#             ['1', '0', '0', '0', '0', '9', '0', '7', '2'],
#             ['0', '2', '0', '0', '0', '0', '9', '5', '0'],
#             ['0', '0', '0', '3', '0', '0', '0', '0', '0'],
#             ['0', '0', '0', '7', '5', '4', '2', '0', '0']
#             ])

print(sudoku_ex.solve())