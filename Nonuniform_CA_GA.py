import math
import random
import numpy as np
import matplotlib.pyplot as plt

from Rule_Generator import additive_rule_gen
from Nonuniform_CA_2D_Neumann import calculate_entropy, entropy, cell, nonuniform_CA_2D

# Rule code format: XCNWSE

# single-point crossover
def crossover(parent_code_1, parent_code_2):
    
    parent_1 = np.array(list(format(parent_code_1, '06b')), dtype=int)
    parent_2 = np.array(list(format(parent_code_2, '06b')), dtype=int)
    
    crossover_point = np.random.randint(1, len(parent_1))
    
    child = np.concatenate((parent_1[:crossover_point], parent_2[crossover_point:]))
    child = int(''.join(str(i) for i in child), 2)
    
    return child

#def mutation(rule_code, mutation_rate):
def mutation(rule_code):
    rule_code_str = np.array(list(format(rule_code, '06b')), dtype=int)
    
    mutation_rate = 0.001
    for i in range(len(rule_code_str)):
        if random.random() < mutation_rate:
            rule_code_str[i] = 1 - rule_code_str[i]
            
    rule_code = int(''.join(str(i) for i in rule_code_str), 2)

def CA_GA():
    
    class entory_and_rule:
        def __init__(self, entory, rule):
            self.entory = entory
            self.rule = rule
    
    class fitter_info:
        def __init__(self, fitter, num_fitter):
            self.fitter = fitter
            self.num_fitter = num_fitter
    
    width = 8
    height = 8
    CA_sim_steps = 32*100
    
    num_generations = 100
    
    # generate random rule table
    rule_code_table = []
    for i in range(height):
        rule_code_table.append([])
        for j in range(width):
            rule_code_table[i].append(random.randint(0, 0b111111))
    
    for num in range(num_generations):    
        # generate CA with rule code
        CA = nonuniform_CA_2D(width, height, rule_code_table, CA_sim_steps)
        CA.CA_envolution()
        
        # calculate entropy of CA
        cell_entropys = []
        for i in range(width):
            for j in range(height):
                cell_entropy = entropy(CA.sequence_in_cells[i][j])
                cell_entropys.append(cell_entropy)
        
        if(num % 20 == 0):
            # statistics of cell entropys and plot it in histogram
            plt.hist(cell_entropys, bins=20)
            plt.title("Histogram of cell entropys")
            plt.xlabel("Entropy")
            plt.ylabel("Frequency")
            plt.show()
        
        # covert cell_entorpys to 2D list
        cell_entropys = np.array(cell_entropys).reshape(width, height)
        
        # fitter information generate
        fitter = [[ fitter_info([], 0) for i in range(height)] for j in range(width)]
        for i in range(width):
            for j in range(height):
                neighbor_entropy = [entory_and_rule(0,0),
                                    entory_and_rule(0,0),
                                    entory_and_rule(cell_entropys[i][j],rule_code_table[i][j]),
                                    entory_and_rule(0,0),
                                    entory_and_rule(0,0)
                                    ] # (i-1,j), (i,j-1),(i,j), (i,j+1), (i+1,j)
                if i-1 >= 0:
                    neighbor_entropy[0] = entory_and_rule(cell_entropys[i-1][j],rule_code_table[i-1][j])
                if j-1 >= 0:
                    neighbor_entropy[1] = entory_and_rule(cell_entropys[i][j-1],rule_code_table[i][j-1])
                if i+1 < width:
                    neighbor_entropy[4] = entory_and_rule(cell_entropys[i+1][j],rule_code_table[i+1][j])
                if j+1 < height:
                    neighbor_entropy[3] = entory_and_rule(cell_entropys[i][j+1],rule_code_table[i][j+1])
                    
                for k in range(5):
                    if neighbor_entropy[k].entory > cell_entropys[i][j]:
                        fitter[i][j].fitter.append(neighbor_entropy[k].rule)
                        fitter[i][j].num_fitter += 1
                        
        # crossover and mutation accoding fitter information
        for i in range(width):
            for j in range(height):
                if fitter[i][j].num_fitter == 1:
                    rule_code_table[i][j] = fitter[i][j].fitter[0]
                if fitter[i][j].num_fitter == 2:
                    rule_code_table[i][j] = crossover(fitter[i][j].fitter[0], fitter[i][j].fitter[1])
                if fitter[i][j].num_fitter > 2:
                    # random select two fitter as parents
                    parent_1 = random.randint(0, fitter[i][j].num_fitter-1)
                    parent_2 = random.randint(0, fitter[i][j].num_fitter-1)
                    while parent_1 == parent_2:
                        parent_2 = random.randint(0, fitter[i][j].num_fitter-1)
                    rule_code_table[i][j] = crossover(fitter[i][j].fitter[parent_1], fitter[i][j].fitter[parent_2])
                    mutation(rule_code_table[i][j])
    
    # save the rule_table in .txt
    with open("rule_table.txt", "w") as f:
        for i in range(width):
            for j in range(height):
                f.write(str(rule_code_table[i][j]) + " ")
            f.write("\n")
     
########################################################################################

def test_crossover():
    rule_code_1 = 0b001011
    rule_code_2 = 0b011101
    
    print("Parent 1: ", format(rule_code_1, '06b'))
    print("Parent 2: ", format(rule_code_2, '06b'))
    
    child = crossover(rule_code_1, rule_code_2)
    
    print("Child: ", format(child, '06b'))
    
    return child

def test_mutation():
    rule_code = 0b001011
    
    print("Before mutation: ", format(rule_code, '06b'))
    
    mutation(rule_code)
    
    print("After mutation: ", format(rule_code, '06b'))

def test_CA_entropy():
    width  = 8
    height = 8
    run    = 32*100
    
    """
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
    """
    
    """
    # generate random rule code table
    rule_code_table = []
    for i in range(height):
        rule_code_table.append([])
        for j in range(width):
            rule_code_table[i].append(random.randint(0, 0b111111))
    """
    
    # read from rule_table_v*.txt to get rule_code_table
    rule_code_table = []
    with open("rule_table_v2.txt", "r") as f:
        for i in range(height):
            rule_code_table.append([])
            rule_code = f.readline().split()
            for j in range(width):
                rule_code_table[i].append(int(rule_code[j]))
    
    CA = nonuniform_CA_2D(width, height, rule_code_table, run)
    CA.CA_envolution()
    
    cell_entropys = []
    for i in range(height):
        for j in range(width):
            cell_entropy = entropy(CA.sequence_in_cells[i][j])
            cell_entropys.append(cell_entropy)
            #cell_entropys.append(math.log(cell_entropy))
    
    # statistics of cell entropys and plot it in histogram
    plt.hist(cell_entropys, bins=20)
    plt.title("Histogram of cell entropys")
    plt.xlabel("Entropy")
    plt.ylabel("Frequency")
    plt.show()
if __name__ == '__main__':
    test_CA_entropy()
    #test_crossover()
    #test_mutation()
    #CA_GA()