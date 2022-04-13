
# # # # # # # # # # # # # # # # # # 
#                                 #
#				                  #
#   Author: Lucas Leal da Costa   #
#                                 #
#                                 #
# # # # # # # # # # # # # # # # # #

class Person:
    
    num_init = 0 # counter to assure first person is number 1

    def __init__(self, matrix):

        if Person.num_init == 0:
            self.number = 1
        else:
            self.number = '+'
        Person.num_init += 1
        
        self.matrix = matrix

    def cache(self, matrix):
        '''to create a cache of memoization'''
        lines = matrix.getLines()
        columns = matrix.getColumns()
        cache_matrix = [[0 for j in range(columns)] for i in range(lines)]
        return cache_matrix

    def cache_check(self, matrix_cache, line, column):
        '''check in the cache'''
        if matrix_cache[column][line] == 0:
                return True
        else:
            return False

    def validar_move(self, matrix, last_moves, move):
        '''method to validate each movement in the matrix'''
        
        x, y = matrix.get_XY(self.number) # initial position


        for i in list(str(last_moves)):
            if i == str(1):
                # up line
                x -= 1
            
            elif i == str(2):
                # down line
                x += 1
            
            elif i == str(3):
                # left column
                y -= 1

            elif i == str(4):
                # right column
                y += 1

        if move == 1: # if moved upwards
            x -= 1
            if x in range(0, matrix.getLines()) and matrix.isempty(x,y) and self.cache_check(self.cache_mat, line=x, column=y):
                self.cache_mat[y][x] = 1
                return True
            else:   return False
        elif move == 2: # if moved downwards
            x += 1
            if x in range(0, matrix.getLines()) and matrix.isempty(x,y) and self.cache_check(self.cache_mat, line=x, column=y):
                self.cache_mat[y][x] = 1
                return True
            else:   return False
        elif move == 3: # if moved leftwards
            y -= 1
            if y in range(0, matrix.getColumns()) and matrix.isempty(x,y) and self.cache_check(self.cache_mat, line=x, column=y):
                self.cache_mat[y][x] = 1
                return True
            else:   return False
        elif move == 4: # if moved rightwards
            y += 1
            if y in range(0, matrix.getColumns()) and matrix.isempty(x,y) and self.cache_check(self.cache_mat, line=x, column=y):
                self.cache_mat[y][x] = 1
                return True
            else:   return False

    def solution(self, last_moves, matrix):
        
        x, y = matrix.get_XY(self.number) # initial position

        for i in list(str(last_moves)):
            if i == str(1):
                # up line
                x -= 1
            
            elif i == str(2):
                # down line
                x += 1
            
            elif i == str(3):
                # left column
                y -= 1

            elif i == str(4):
                # right column
                y += 1

        # if final position if reached
        if x == self.matrix.final_x and y == self.matrix.final_y:
            return True
        else: False

    def print_solucao(self, last):
        '''Method to print the full path of maze solving'''

        last = list(str(last))
        print('===================================================================================\n')
        print('', end=' - ')
        for i in last:
            if i == str(1):
                print('Up', end=' - ')
            elif i == str(2):
                print('Down', end=' - ')
            elif i == str(3):
                print('Left', end=' - ')
            elif i == str(4):
                print('Right', end=' - ')
        print('\n')
        print('===================================================================================\n')
        
        self.matrix.print_sol(last, self.number) # printing the maze solved

    def soluciona(self, matrix):
        '''Main method to solve the maze'''

        self.cache_mat = self.cache(matrix) # cache matrix

        # initiating queue
        queue = [0]
        # possible movements
        moves = [1, 2, 3, 4] # 1 = up, 2 = down, 3 = left, 4 = right

        while True:
            try: 
                last = queue.pop()
            except:
                # in the case of impossible maze
                print('\n\nImpossible maze was created, try it again.\n')
                self.print_solucao(last) # printing impossible maze
                print('\nShutting down...')
                break

            if self.solution(last, matrix): # check if last position was reached
                self.print_solucao(last) # printing solution
                break
            
            for step in moves:

                if self.validar_move(matrix, last, step): # validating movements
                    new_last = str(last) + str(step) # adding path to queue
                    queue.insert(0, new_last)
        
        return last
