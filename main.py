from matrix import Matrix
from person17 import Person
import random

# # # # # # # # # # # # # # # # # # 
#                                 #
#				                  #
#   Author: Lucas Leal da Costa   #
#                                 #
#                                 #
# # # # # # # # # # # # # # # # # #

def create_maze():

	num_lines = int(input('Set matrix order:\n> ')) # matrix of nxn order

	print(f'\nInitial and final x and y must be between {0} and {num_lines-1}')

	x_init = int(input('\nSet initial x:\n> ')) # setting initial position
	y_init = int(input('Set initial y:\n> '))  # setting initial position

	final_x = int(input('\nSet final x:\n> ')) # setting final position
	final_y = int(input('Set final y:\n> ')) # setting final position

	m1 = Matrix(num_lines, num_lines, final_y, final_x) # creating matrix and final position
	p1 = Person(m1) # creating person 1 to move in the matrix
	
	num_obstacles = int(input('\nSet number of obstacles:\n> '))

	# set random obstacles or position each obstacle
	flag1 = int(input('Do you wish to set random positions? (1/0)\n> '))

	if flag1 == 1: # random positioning

		for i in range(num_obstacles):
			p2 = Person(m1)
			m1.posicionar(p2)

	else: # positioning each obstacle in the matrix
		for i in range(num_obstacles):
			
			p2 = Person(m1) # creating obstacle

			x_pos = int(input('Set position x: ')) # setting x position
			y_pos = int(input('Set position y: ')) # setting y position
			print('\n')

			m1.posicionar(p2, y_pos, x_pos)	# placing the obstacles

	m1.posicionar(p1, y_init, x_init) # placing person 1 to move on maze
	
	p1.soluciona(m1) # maze solving

create_maze()