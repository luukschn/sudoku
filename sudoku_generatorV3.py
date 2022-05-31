import numpy as np
import matplotlib.pyplot as plt
from sudoku_verification import Verification
from sudoku_change_values import Alteration


"""Minimum amount of visible squares to solve is 17"""

#setup sudoku
s = [np.random.permutation(range(1,10)).reshape(3,3) for x in range(9)]
S = np.reshape(np.array([s[a] for a in range(len(s))]), (9,9))

verification = Verification()
alteration = Alteration()

#TODO: focus on rows and columns first
# for i in range(9):
#     #print(verification.verify_row(S, i))
#     print(verification.verify_col(S, i))

# for i in range(9):
#     for j in range(9):
#         print(verification.verify_block(S, i, j))
print(S)


#I DONT UNDERSTANAD
#keeps stabalizing at 5. there is something with 10 which is fucking this up
def check_sudoku_values():
    proper_row_count = 0
    for row_num in range(9):
        if verification.verify_row(S, row_num) == False:
            alteration.alter_row(S, row_num)
            #can i start the recursion here?
        else:
            proper_row_count += 1
    
    row_count.append(proper_row_count)
    
    proper_col_count = 0
    for col_num in range(9):
        if verification.verify_col(S, col_num) == False:
            alteration.alter_col(S, col_num)
        else:
            proper_col_count += 1

    col_count.append(proper_col_count)

    global counter
    counter += 1

    if counter > 15:
        print(S)


    if (proper_row_count + proper_col_count) < 18 and counter <= 20:
        check_sudoku_values()
    elif (proper_row_count + proper_col_count) == 18:
        return
    
    
    
    
    
        #check rows
        #check columsn
        #if improper:
            #change row values
            #change col values
            #Call function again -> terminating conditions is both
            #rows and columns returning True

counter = 0

row_count = []
col_count = []

check_sudoku_values()

print(S)

plt.plot(row_count, label="row")
plt.plot(col_count, label="col")
plt.legend()
plt.show()

