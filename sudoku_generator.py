import pandas as pd
import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt


#best to return the exact values which are not proper so i dont have to do a permutation on all of them
#return index
#separate function for the altering of values


#minimum amount of squares to solve something is 17

_number_array = [1,2,3,4,5,6,7,8,9]

def check_row(row_number):
    numbers_to_check = set(S[row_number])
    print(f"row {row_number} ntc: ", numbers_to_check)
    if not (len(numbers_to_check) == 9):
        for i in range(9):
            for j in range(9):
                if S[row_number][i] == S[row_number][j] and i != j:
                    #return [i, S[row_number][i]]
                    return i
    return -1

def check_col(col_number):
    """check if all values of column are unique and return place of first wrong value if false"""
    numbers_to_check = set([S[x][col_number] for x in range(9)])

    #this checks the numbers. not the positions of the number
    # if len(numbers_to_check) != 9:
    #     return [y for y in range(1,10) if y not in numbers_to_check]

    print(f"col {col_number} ntc: ", numbers_to_check)
    if not len(numbers_to_check) == 9:
        for i in range(9):
            for j in range(9):
                if S[i][col_number] == S[j][col_number] and i != j:
                    #return [i, S[i][col_number]]
                    return i

    return -1


#these are not proper yet
def check_block(row_number, col_number):

    if row_number <= 2:
        if col_number <=2:
            numbers_to_check = set((S[0][:3], S[1][:3], S[2][:3]))
            if len(numbers_to_check) == 9:
                # for i in range(9):
                #     for j in range(9):

                return True

        elif (col_number >= 3 and col_number <= 5):
            numbers_to_check = set((S[0][3:6], S[1][3:6], S[2][3:6]))
            if len(numbers_to_check) == 9:
                return True

        elif col_number >= 6:
            numbers_to_check = set((S[0][6:], S[1][6:], S[2][6:]))
            if len(numbers_to_check) == 9:
                return True

    elif row_number >= 3 and row_number <= 5:
        if col_number <= 2:
            numbers_to_check = set((S[3][:3], S[4][:3], S[5][:3]))
            if (len(numbers_to_check)) == 9:
                return True

        elif col_number >= 3 and col_number <= 5:
            numbers_to_check = set((S[3][3:6], S[4][3:6], S[5][3:6]))
            if (len(numbers_to_check)) == 9:
                return True

        elif col_number >= 6:
            numbers_to_check = set((S[3][6:], S[4][6:], S[5][6:]))
            if len(numbers_to_check) == 9:
                return True

    elif row_number >= 6:
        if col_number <= 2:
            numbers_to_check = set((S[6][:3], S[7][:3], S[8][:3]))
            if (len(numbers_to_check)) == 9:
                return True

        elif col_number >= 3 and col_number <= 5:
            numbers_to_check = set((S[6][3:6], S[7][3:6], S[8][3:6]))
            if (len(numbers_to_check)) == 9:
                return True

        elif col_number >= 6:
            numbers_to_check = set((S[6][6:], S[7][6:], S[8][6:]))
            if len(numbers_to_check) == 9:
                return True

    return -1



#not working well. need to tweak my algorithm
#check the return values with as many prints as possible
#check if the sudoku array actually changes with the input values i try to add
#check if input values are the ones i actually want to input
def change_row(row_number):
    row_counter = 0
    row = check_row(row_number)
    if row != -1:
        numbers_to_check = set(S[row_number])
        input_value = [x for x in _number_array if x not in numbers_to_check]
        S[row_number, row] = input_value[0]
        row_counter += 1
        return False
    return True

def change_col(col_number):
    col = check_col(col_number)
    if col != -1:
        numbers_to_check = set([S[x][col_number] for x in range(9)])
        #print(numbers_to_check)
        input_value = [x for x in _number_array if x not in numbers_to_check]
        #print(input_value)
        #S[col_number, col[0]] = input_value[0]
        #S[col_number, col[0]] = input_value[0]
        print("input value ", input_value)
        S[col, col_number] = input_value[0]
        return False
    # if check_block(row_number, col_number) != -1:
    #     numbers_to_check = 
    #     #change valu
    return True
    
    

    
    



s = [np.random.permutation(range(1,10)).reshape(3,3) for x in range(9)]
S = np.reshape(np.array([s[a] for a in range(len(s))]), (9,9))

counter = 0

print(S)


i = 0
j = 0

row_results = []
col_results = []

verification = False
while verification == False:
    good_row = 0
    good_col = 0
    for i in range(9):
        res_row = change_row(i)
        if res_row == True:
            good_row += 1
    for j in range(9):
        res_col = change_col(j)
        if res_col == True:
            good_col += 1
    
    row_results.append(good_row)
    col_results.append(good_col)
    print(S)

    # for i in range(9):
    #     for j in range(9):
    #         res_row = change_row(i)
    #         #count all rows and cols to see if they are all correct. otherwise start while loop over
    #         if res_row == -1:
    #             good_row += 1
    #         res_col = change_col(j)
    #         if res_col == -1:
    #             good_col += 1
            
    counter += 1
    if counter == 20:
        break
    if good_row == 9 and good_col == 9:
        verification = True


#evens out at 15 consistently
plt.plot(row_results, label="row")
plt.plot(col_results, label="col")
plt.legend()
plt.show()


#print(S)

#can already do machine learning on the sudokus i guess?
#categorize how hard things are to solve

row_verify = True
col_verify = True
for i in range(9):
    if len(set(S[i])) != 9:
        row_verify = False
    if len(set([S[x][i] for x in range(9)])) != 9:
        col_verify=False

print(f"Row verify:{row_verify}\nCol verify:{col_verify}")
