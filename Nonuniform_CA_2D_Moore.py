# A implementation of nonuniform 2D CA
# using Moore neighborhood

import random
import numpy as np
import matplotlib.pyplot as plt

from Rule_Generator import rule_gen

# cell for CA
class cell:
    def __init__(self, state, rule_code):
        self.value = state
        self.rule = rule_gen(rule_code)
    
    def cell_update(self, neighborhood):
        # State of a cell is a 9-bit binary number, determined by value of its neighborhood (including itself)
        # Assuming the cell is (x,y)
        # 1st bit is the value of (x-1,y-1) cell
        # 2nd bit is the value of (x,y-1)   cell
        # 3rd bit is the value of (x+1,y-1) cell
        # 4th bit is the value of (x-1,y)   cell   
        # 5th bit is the value of (x,y)     cell
        # 6th bit is the value of (x+1,y)   cell
        # 7th bit is the value of (x-1,y+1) cell
        # 8th bit is the value of (x,y+1)   cell
        # 9th bit is the value of (x+1,y+1) cell
        # covert neighborhood to a 9-bit binary number
        self.state = 0b000000000
        for i in range(3):
            for j in range(3):
                self.state += neighborhood[i][j] * 2**(8-i*3-j) # 8-i*3-j is the index of bit
        self.value = self.rule(self.state)
        

class nonuniform_CA_2D:
    def __init__(self, width, height, rule_code_table):
        # generate width*height grid
        self.width  = width
        self.height = height
        self.grid   = [[cell(random.randint(0,1), rule_code_table[i][j]) for j in range(width)] for i in range(height)]
        
    def CA_update(self):
        # update the state of each cell
        for i in range(self.height):
            for j in range(self.width):
                # get the neighborhood of each cell, if an adjacent cell does not exist, its corresponding value in neighborhood is set to 0
                neighborhood = [ [0b0 for j in range(3)] for i in range(3)]
                
                neighborhood[1][1] = self.grid[i][j].value
                # check self.grid[i-1][j-1] exists or not
                if i-1 >= 0 and j-1 >= 0:
                    neighborhood[0][0] = self.grid[i-1][j-1].value
                else:
                    neighborhood[0][0] = 0b0
                
                # check self.grid[i][j-1] exists or not
                if j-1 >= 0:
                    neighborhood[0][1] = self.grid[i][j-1].value
                else:
                    neighborhood[0][1] = 0b0
                
                # check self.grid[i+1][j-1] exists or not
                if i+1 < self.height and j-1 >= 0:
                    neighborhood[0][2] = self.grid[i+1][j-1].value
                else:
                    neighborhood[0][2] = 0b0
                
                # check self.grid[i-1][j] exists or not
                if i-1 >= 0:
                    neighborhood[1][0] = self.grid[i-1][j].value
                else:
                    neighborhood[1][0] = 0b0
                
                # check self.grid[i-1][j+1] exists or not
                if i-1 >= 0 and j+1 < self.width:
                    neighborhood[2][0] = self.grid[i-1][j+1].value
                else:
                    neighborhood[2][0] = 0b0
                    
                # check self.grid[i][j+1] exists or not
                if j+1 < self.width:
                    neighborhood[2][1] = self.grid[i][j+1].value
                else:
                    neighborhood[2][1] = 0b0
                    
                # check self.grid[i+1][j+1] exists or not
                if i+1 < self.height and j+1 < self.width:
                    neighborhood[2][2] = self.grid[i+1][j+1].value
                else:
                    neighborhood[2][2] = 0b0
                    
                # update the value of each cell
                self.grid[i][j].cell_update(neighborhood)
    
    def CA_plot(self):
        # get the state of each cell
        self.state = [[self.grid[i][j].value for j in range(self.width)] for i in range(self.height)]
        
        # plot the CA according to the value of cell, 0 is black, 1 is white
        grid = np.array(self.state)
        plt.imshow(grid, cmap='gray', interpolation='nearest')
        plt.grid(True, which='both', color='black', linewidth=1)
        plt.xticks(np.arange(-0.5, self.width, 1))
        plt.yticks(np.arange(-0.5, self.height, 1))
        plt.show()
        
    def CA_state_output_as_sequence(self):
        # get the state of each cell
        self.state = [[self.grid[i][j].value for j in range(self.width)] for i in range(self.height)]
        
        return np.array(self.state).flatten()
        

############################################################### Test
# test rule_gen
def test_rule_gen():
        # ramdomly generate a rule code
    rule_code = ''
    for i in range(512):
        rule_code += str(random.randint(0,1))
    
    print("rule_code: ", rule_code)
    
    rule = rule_gen(rule_code)
    print("The next state of 0b00000000 is: ", rule(0b000000000))
    
def test_cell():
    # ramdomly generate a rule code
    rule_code = ''
    for i in range(512):
        rule_code += str(random.randint(0,1))
    
    print("rule_code: ", rule_code)
    
    rule = rule_gen(rule_code)
    
    # ramdomly generate a neighborhood
    neighborhood = [[random.randint(0,1) for j in range(3)] for i in range(3)]
    print("neighborhood: ", neighborhood)
    
    # test cell_update
    cell_test = cell(0, rule_code)
    cell_test.cell_update(neighborhood)
    print("The next value of cell is: ", cell_test.value)
    
def test_CA_init():
    width  = 12
    height = 12
    
    rule_code_table = []
    for i in range(height):
        rule_code_table.append([])
        for j in range(width):
            rule_code_table[i].append('')
            for k in range(512):
                rule_code_table[i][j] += str(random.randint(0,1))
                
    CA = nonuniform_CA_2D(width, height, rule_code_table)
    CA.CA_plot()

    print("The initial state of CA is: ", CA.CA_state_output_as_sequence())
    
    CA.CA_update()
    print("The next state of CA is: ", CA.CA_state_output_as_sequence())
    CA.CA_plot()
    
if __name__ == '__main__':
#    test_rule_gen()
#    test_cell()
    test_CA_init()