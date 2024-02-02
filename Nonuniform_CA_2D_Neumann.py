# Implementation of a 2D nonuniform cellular automaton in paper "On the generation of high-quality random numbers by two-dimensional cellular automata"
# Using Neumann neighborhood

import random
import numpy as np
import matplotlib.pyplot as plt
import math
import struct

from Rule_Generator import additive_rule_gen

def calculate_entropy(probabilities):
    entropy = 0
    for prob in probabilities:
        if prob != 0:  # to avoid log(0)
            entropy -= prob * math.log2(prob)
    return entropy

def entropy(input_sequence):
    k = 2  # number of possible values per sequence position (binary in this case)
    h = 4  # subsequence length
    
    # Convert the binary input to a string
    #input_sequence = format(input_sequence_binary, '010b')
    
    subsequences = [input_sequence[i:i+h] for i in range(len(input_sequence) - h + 1)]
    
    # Generate all possible subsequences of length h
    possible_subsequences = [ "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111",
                              "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]

    # Calculate probabilities for each subsequence
    probabilities = [subsequences.count(subseq) / len(subsequences) for subseq in set(possible_subsequences)]

    # Calculate entropy
    entropy = calculate_entropy(probabilities)

#    print(f"Input Sequence: {input_sequence}")
#    print(f"Subsequences: {subsequences}")
#    print(f"Probabilities: {probabilities}")
#    print(f"Entropy (E_h): {entropy}")
    
    return entropy

class cell:
    def __init__(self, state, rule_code):
        self.value = state
        self.rule = additive_rule_gen(rule_code)
    
    def cell_update(self, neighborhood):
        # State of a cell is a 5-bit binary number, determined by value of its neighborhood (including itself)
        # Assuming the cell is (x,y)
        # 1st bit is the value of (x,y-1)   cell
        # 2nd bit is the value of (x-1,y)   cell   
        # 3rd bit is the value of (x,y)     cell
        # 4th bit is the value of (x+1,y)   cell
        # 5th bit is the value of (x,y+1)   cell
        # covert neighborhood to a 5-bit binary number
        self.state = 0b00000
        for i in range(5):
            self.state += neighborhood[i] * 2**(4-i)
        
        return self.rule(self.state)
        
class nonuniform_CA_2D:
    def __init__(self, width, height, rule_code_table, run):
        # generate width*height grid
        self.width  = width
        self.height = height
        self.grid   = [[cell(random.randint(0,1), rule_code_table[i][j]) for j in range(width)] for i in range(height)]
        self.run    = run
        
    def CA_update(self):
        # update the state of each cell
        
        next_state = [[0b0 for j in range(self.width)] for i in range(self.height)]
        
        for i in range(self.height):
            for j in range(self.width):
                # get the neighborhood of each cell, if an adjacent cell does not exist, its corresponding value in neighborhood is set to 0

                neighborhood = [ 0b0 for i in range(5)] # corresponding to (x-1,y), (x,y-1), (x,y), (x,y+1), (x+1,y)
                
                neighborhood[2] = self.grid[i][j].value
                
                # check self.grid[i][j-1] exists or not
                if j-1 >= 0:
                    neighborhood[1] = self.grid[i][j-1].value
                else:
                    neighborhood[1] = 0b0
                    
                # check self.grid[i-1][j] exists or not
                if i-1 >= 0:
                    neighborhood[0] = self.grid[i-1][j].value
                else:
                    neighborhood[0] = 0b0
                    
                # check self.grid[i][j+1] exists or not
                if j+1 < self.width:
                    neighborhood[3] = self.grid[i][j+1].value
                else:
                    neighborhood[3] = 0b0
                    
                # check self.grid[i+1][j] exists or not
                if i+1 < self.height:
                    neighborhood[4] = self.grid[i+1][j].value
                else:
                    neighborhood[4] = 0b0
                
                #self.grid[i][j].cell_update(neighborhood)
                next_state[i][j] = self.grid[i][j].cell_update(neighborhood)
                
        # update the state of each cell
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j].value = next_state[i][j]

    def CA_plot(self):
        self.state = [[self.grid[i][j].value for j in range(self.width)] for i in range(self.height)]
        
        grid = np.array(self.state)
        plt.imshow(grid, cmap='gray', interpolation='nearest')
        plt.grid(True, which='both', color='black', linewidth=1)
        plt.xticks(np.arange(-0.5, self.width, 1))
        plt.yticks(np.arange(-0.5, self.height, 1))
        plt.show()
        
    def CA_state_output_as_sequence(self):
        self.state = [[self.grid[i][j].value for j in range(self.width)] for i in range(self.height)]
        
        # convert above 2D list to string
        sequence = ""
        for i in range(self.height):
            for j in range(self.width):
                sequence += str(self.state[i][j])
        
        return sequence
    
    def CA_envolution(self):
#        self.sequence_in_cells = [[ str(self.grid[i][j].value) for j in range(self.width)] for i in range(self.height)]
        self.sequence_in_cells = [[ "" for j in range(self.width)] for i in range(self.height)]
        
        cout = 0
        
        for i in range(self.run):
            print("The iteration is: ", i+1)
            # add new value to sequence_in_cells
            for j in range(self.height):
                for k in range(self.width):
                    self.sequence_in_cells[j][k] += str(self.grid[j][k].value)
                    
            self.CA_update()
            #self.CA_plot()
                    
            if (i+1) % 32 == 0:
                cout += 1
                
                # convert sequence_in_cells to bit_sequence
                # every 32 bits in sequences will be converted to a hexadecimal digit
                self.sequence_in_cells = [[ int(self.sequence_in_cells[i][j], 2) for j in range(self.width)] for i in range(self.height)]
                
                # output bit sequence to file .bin
                with open("random_numbers.bin", 'wb') as file:
                    for j in range(self.height):
                        for k in range(self.width):
                            file.write(struct.pack('>I', self.sequence_in_cells[j][k]))
                            
                # reset
                self.sequence_in_cells = [[ "" for j in range(self.width)] for i in range(self.height)]   
                
        print("The number of 32 bits is: ", cout*self.width*self.height)         
        
#####################################################

def test_entropy():
    input_sequence = "1101010010"
    entropy(input_sequence)

def test_rule_gen():
    #rule_code = random.randint(0,6)
    
    # set rule code is 00110
    rule_code = 0b001110
    
    rule = additive_rule_gen(rule_code)
    
    # print rule_code in binary format
    print("rule_code: ", bin(rule_code)[2:].zfill(6))
    
    state = random.randint(0,31)
    # print state in binary format
    print("state: ", bin(state)[2:].zfill(5))
    
    next_state = rule(state)
    # print next state in binary format
    print("next state: ", bin(next_state)[2:].zfill(5))


def test_CA():
    width  = 8
    height = 8
    run    = 1000000*32 # 32000000
#    run    = 10*32
    
    #rule_code_table = [[random.randint(0,63) for j in range(width)] for i in range(height)]
    rule_15 = 0b001011
    rule_31 = 0b011011
    rule_47 = 0b101111
    rule_63 = 0b111111
    rule_code_table = [
        [rule_31, rule_31, rule_31, rule_31, rule_31, rule_63, rule_63, rule_15],
        [rule_63, rule_63, rule_63, rule_31, rule_31, rule_63, rule_63, rule_63],
        [rule_63, rule_63, rule_31, rule_31, rule_31, rule_63, rule_63, rule_63],
        [rule_47, rule_47, rule_63, rule_63, rule_63, rule_63, rule_63, rule_63],
        [rule_15, rule_63, rule_31, rule_63, rule_63, rule_63, rule_63, rule_31],
        [rule_63, rule_63, rule_31, rule_63, rule_63, rule_63, rule_15, rule_31],
        [rule_31, rule_63, rule_31, rule_31, rule_31, rule_31, rule_63, rule_31],
        [rule_63, rule_63, rule_31, rule_31, rule_31, rule_31, rule_15, rule_31]   
    ]
    
    CA = nonuniform_CA_2D(width, height, rule_code_table, run)
#    CA.CA_plot()
    
#    print("The initial state of CA is: ", CA.CA_state_output_as_sequence())
    
#    CA.CA_update()
#    print("The next state of CA is: ", CA.CA_state_output_as_sequence())
#    CA.CA_plot()
    
    CA.CA_envolution()
#    print("The bit sequence of CA is: ", bit_sequence)

    """
    cell_entropys = []
    for i in range(height):
        for j in range(width):
            cell_entropy = entropy(CA.sequence_in_cells[i][j])
            cell_entropys.append(cell_entropy)
            #print("The entropy of cell ({}, {}) is: {}".format(i, j, cell_entropy))
    
    # statistics of cell entropys and plot it in histogram
    plt.hist(cell_entropys, bins=20)
    plt.title("Histogram of cell entropys")
    plt.xlabel("Entropy")
    plt.ylabel("Frequency")
    plt.show()
    """
if __name__ == '__main__':
#    test_rule_gen()
    test_CA()
#    test_entropy()