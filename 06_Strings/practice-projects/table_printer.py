

def print_table(table):
    length = len(table)

    colwidth = [0] * length
    for i in range(length):
        colwidth[i] = len(max(table[i], key = len)) #storing the len of largest string in each row
    

    for rows in range(len(table[0])): # iterating over the number of elements in EACH sublists 
        for columns in range(length): # iterating over the number of sublists
            print (table[columns][rows].rjust(colwidth[columns]), end=' ')
        print()
    

if __name__ == "__main__":
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]
    print_table(table_data)




















