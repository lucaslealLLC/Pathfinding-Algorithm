import random
from person17 import Person

# # # # # # # # # # # # # # # # # # 
#                                 #
#                                 #
#   Author: Lucas Leal da Costa   #
#                                 #
#                                 #
# # # # # # # # # # # # # # # # # #

class Matrix:

    empty = '.' # symbol of empty space

    def __init__(self, lines, columns, final_x=0, final_y=0):
        self.__lines = lines
        self.__columns = columns
        self.final_x, self.final_y = final_x, final_y # final positions
         # creating maze
        self.matriz = [[Matrix.empty for j in range(columns)] for i in range(lines)]
        self.matriz[final_x][final_y] = '#' # setting final position

    def print_sol(self, last, num):
        '''Method to print the solved maze'''
        
        pos_lin, pos_col = self.get_XY(num)

        for j in range(len(last)-1):
            i = int(last[j])
            if i == 1:
                # moved up
                pos_lin -= 1
                self.matriz[pos_lin][pos_col] = 'O'
            elif i == 2:
                # moved down
                pos_lin += 1
                self.matriz[pos_lin][pos_col] = 'O'
            elif i == 3:
                # moved left
                pos_col -= 1
                self.matriz[pos_lin][pos_col] = 'O'
            elif i == 4:
                # moved right
                pos_col += 1
                self.matriz[pos_lin][pos_col] = 'O'
        for lines in self.matriz:
            print('|', end=" ")
            for j in lines:
                print(str(j), end=" ")
            print('|')        

    def getLines(self):
        return self.__lines

    def getColumns(self):
        return self.__columns

    def isempty(self, x, y):
        '''checking if the position is empty or if it is final position'''
        if self.matriz[x][y] == Matrix.empty or self.matriz[x][y] == '#':
            return True
        else:
            return False

    def get_XY(self, num):
        '''getting x and y coordinates in the matrix'''
        for i, val in enumerate(self.matriz):
            for j, val_2 in enumerate(val):
                if val_2 == num:
                    return i, j

    def posicionar(self, person_posicionar, linha_pos=None, coluna_pos=None):
        '''Method to place objects in the matrix'''

        if linha_pos == None and coluna_pos == None:
            # loop to assure each position to different objects
            while True:
                linha_aleatoria = random.randint(0, self.__lines-1)
                coluna_aleatoria = random.randint(0, self.__columns-1)
                # check if that position if available
                if self.matriz[linha_aleatoria][coluna_aleatoria] == Matrix.empty:
                    self.matriz[linha_aleatoria][coluna_aleatoria] = person_posicionar.number
                    break
        else:
            if self.matriz[linha_pos][coluna_pos] == Matrix.empty:
                self.matriz[linha_pos][coluna_pos] = person_posicionar.number
            else:
                print(f"Esta posição ({linha_pos}, {coluna_pos}) já está preenchida")