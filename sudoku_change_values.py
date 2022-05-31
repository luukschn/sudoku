import numpy as np

class Alteration():
    def alter_row(self, S, row_number):
        number_array = [1,2,3,4,5,6,7,8,9]

        row_values_set = set(S[row_number])
        input_values = [x for x in number_array if x not in row_values_set]

        break_out_flag = False
        for i in range(9):
            for j in range(9):
                if (S[row_number][i] == S[row_number][j]) and (i != j):
                    S[row_number][i] = input_values[0]
                    break_out_flag = True
                    return S
            if break_out_flag:        
                break
            
        
    def alter_col(self, S, col_number):
        number_array = [1,2,3,4,5,6,7,8,9]

        col_values_set = set([S[x][col_number] for x in range(9)])
        input_values = [x for x in number_array if x not in col_values_set]

        break_out_flag = False
        for i in range(9):
            for j in range(9):
                if (S[i][col_number] == S[j][col_number]) and (i != j):
                    S[i, col_number] = input_values[0]
                    break_out_flag = True
                    return S
            if break_out_flag:
                break
            