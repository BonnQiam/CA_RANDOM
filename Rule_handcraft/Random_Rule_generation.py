import random

if __name__ == '__main__':

    Reference_rule_list = [14,15,27,31,47,51,55,59,63]

    filenames = [
            'rule_table_v1.txt', 'rule_table_v2.txt', 'rule_table_v3.txt', 'rule_table_v4.txt', 'rule_table_v5.txt',
            'rule_table_v6.txt', 'rule_table_v7.txt', 'rule_table_v8.txt', 'rule_table_v9.txt', 'rule_table_v10.txt',
            'rule_table_v11.txt', 'rule_table_v12.txt', 'rule_table_v13.txt', 'rule_table_v14.txt', 'rule_table_v15.txt',
            'rule_table_v16.txt', 'rule_table_v17.txt', 'rule_table_v18.txt', 'rule_table_v19.txt', 'rule_table_v20.txt',
            'rule_table_v21.txt', 'rule_table_v22.txt', 'rule_table_v23.txt', 'rule_table_v24.txt', 'rule_table_v25.txt',
            'rule_table_v26.txt', 'rule_table_v27.txt', 'rule_table_v28.txt', 'rule_table_v29.txt', 'rule_table_v30.txt'
        ]
    
    #filenames = ['rule_table_v1.txt']
    
    width = 8
    space = 8
    
    for filename in filenames:
        # random rule code table (size is width*space), the random result is taken from the Reference_rule_list
        rule_code_table = []
        for i in range(width):
            rule_code_table.append([])
            for j in range(space):
                rule_code_table[i].append(random.choice(Reference_rule_list))
                
        # write rule_code_table to filename
        with open(filename, 'w') as f:
            for i in range(width):
                for j in range(space):
                    f.write(str(rule_code_table[i][j]) + ' ')
                f.write('\n')

