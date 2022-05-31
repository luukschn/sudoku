import numpy as np
import matplotlib.pyplot as plt

"""Minimum amount of squares to solve a sudoku is 17"""




def verify_row(row_number):
    row_numbers_set = set(S[row_number])

    #check if all numbers are present in row
    if len(row_numbers_set) != 9:

        #compare all values within the row to the other numbers
        for i in range(9):
            for j in range(9):
                if (S[row_number][i] == S[row_number][j]) and i != j:
                    #return index of row value which is duplicate
                    #possible that there are more values but this should be solved in a
                    #following iteration
                    return [row_number, i]
        
    #else return -1 to indicate that row is proper
    return -1

def verify_col(col_number):
    """returns [index of duplicate value, column number]"""
    col_numbers_set = set([S[x][col_number] for x in range(9)])

    if len(col_numbers_set) != 9:
        for i in range(9):
            for j in range(9):
                if (S[i][col_number] == S[j][col_number]) and i != j:
                    #maybe helpful to return col number as well so i have the exact coords
                    return [i, col_number]

    return -1

#TypeError: unhashable type: 'numpy.ndarray'
#set((S[0][:3], S[1][:3], S[2][:3]))
def verify_block(row_number, col_number):
    #returns [row number, duplicate value within row]
    if row_number <= 2:
        if col_number <=2:
            square_numbers_set = (set((S[0][:3])), set((S[1][:3])), set((S[2][:3])))
            if len(square_numbers_set) != 9:
                for i in range(3):
                    for I in range(3):
                        for j in range(3):
                            for J in range(3):
                                if (S[i][I] == S[j][J]) and (i != j and I != J):
                                    #returns exact index of the position. as i will be
                                    #altering the i and J values for each block
                                    return [i, I]

        elif (col_number >= 3 and col_number <= 5):
            square_numbers_set = (set((S[0][3:6])), set((S[1][3:6])), set((S[2][3:6])))
            if len(square_numbers_set) != 9:
                for i in range(3):
                    for I in range(3,6):
                        for j in range(3):
                            for J in range(3,6):
                                if (S[i][I] == S[j][J]) and (i != j and I != J):
                                    return [i, I]

        elif col_number >= 6:
            square_numbers_set = (set((S[0][6:])), set((S[1][6:])), set((S[2][6:])))
            if len(square_numbers_set) != 9:
                for i in range(3):
                    for I in range(6, 9):
                        for j in range(3):
                            for J in range(6, 9):
                                if (S[i][I] == S[j][J]) and (i != j and I != J):
                                    return [i, I]

    elif row_number >= 3 and row_number <= 5:
        if col_number <= 2:
            square_numbers_set = (set((S[3][:3])), set((S[4][:3])), set((S[5][:3])))
            if len(square_numbers_set) != 9:
                for i in range(3,6):
                    for I in range(3):
                        for j in range(3,6):
                            for J in range(3):
                                if (S[i][I] == S[j][J]) and (i != j and I != J):
                                    return [i, I]

        elif col_number >= 3 and col_number <= 5:
            square_numbers_set = (set((S[3][3:6])), set((S[4][3:6])), set((S[5][3:6])))
            if len(square_numbers_set) != 9:
                for i in range(3,6):
                    for I in range(3,6):
                        for j in range(3,6):
                            for J in range(3,6):
                                if (S[i][I] == S[j][J]) and (i != j and I != J):
                                    return [i, I]

        elif col_number >= 6:
            square_numbers_set = (set((S[3][6:])), set((S[4][6:])), set((S[5][6:])))
            if len(square_numbers_set) != 9:
                for i in range(3,6):
                    for I in range(6,9):
                        for j in range(3,6):
                            for J in range(6,9):
                                if (S[i][I] == S[j][J]) and (i != j and I != J):
                                    return [i, I]

    elif row_number >= 6:
        if col_number <= 2:
            square_numbers_set = (set((S[6][:3])), set((S[7][:3])), set((S[8][:3])))
            if len(square_numbers_set) != 9:
                for i in range(6,9):
                    for I in range(3):
                        for j in range(6,9):
                            for J in range(3):
                                if (S[i][I] == S[j][J]) and (i != j and I != J):
                                    return [i, I]

        elif col_number >= 3 and col_number <= 5:
            square_numbers_set = (set((S[6][3:6])), set((S[7][3:6])), set((S[8][3:6])))
            if len(square_numbers_set) != 9:
                for i in range(6,9):
                    for I in range(3,6):
                        for j in range(6,9):
                            for J in range(3,6):
                                if (S[i][I] == S[j][J]) and (i != j and I != J):
                                    return [i, I]

        elif col_number >= 6:
            square_numbers_set = (set((S[6][6:])), set((S[7][6:])), set((S[8][6:])))
            if len(square_numbers_set) != 9:
                for i in range(6,9):
                    for I in range(6,9):
                        for j in range(6,9):
                            for J in range(6,9):
                                if (S[i][I] == S[j][J]) and (i != j and I != J):
                                    return [i, I]

    return -1


s = [np.random.permutation(range(1,10)).reshape(3,3) for x in range(9)]
S = np.reshape(np.array([s[a] for a in range(len(s))]), (9,9))

print(S)

# for i in range(9):
#     #print(verify_row(i))
#     print(verify_col(i))

# for i in range(9):
#     for j in range(9):
#         print(verify_block(i,j))


