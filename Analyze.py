import numpy as np
import matplotlib.pyplot as plt

width = 19
height = 19
filename = "rule_table_v19"

rule_code_table = []

with open(filename + '.txt', "r") as f:
    for i in range(height):
        rule_code_table.append([])
        rule_code = f.readline().split()
        for j in range(width):
            rule_code_table[i].append(int(rule_code[j]))
            
# count

Count = [0 for i in range(64)]

for i in range(height):
    for j in range(width):
        Count[rule_code_table[i][j]] += 1

# if count[i] != 0, add i to x_bar and add count[i] to y_bar
x_bar = []
y_bar = []

for i in range(64):
    if Count[i] != 0:
        x_bar.append(i)
        y_bar.append(Count[i])

# plot
plt.figure(figsize=(20, 10))
plt.bar(x_bar, y_bar)
plt.xlabel('Rule Code')
plt.ylabel('Count')
plt.title('Rule: ' + str(x_bar) + '\n' + 'Count: ' + str(y_bar))
plt.savefig(filename + '.png')
plt.show()