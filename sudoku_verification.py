import numpy as np

class Verification():
    def verify_row(self, S, row_number):
        row_numbers_set = set(S[row_number])

        if len(row_numbers_set) < 9:
            return False
        else:
            return True

    def verify_col(self, S, col_number):
        col_numbers_set = set([S[x][col_number] for x in range(9)])

        if len(col_numbers_set) < 9:
            return False
        else:
            return True
        

    #returns 81 lines. not working correctly
    def verify_block(self, S, row_number, col_number):
        if row_number <= 2:
            if col_number <=2:
                square_numbers_set = (set((S[0][:3])), set((S[1][:3])), set((S[2][:3])))
                if len(square_numbers_set) < 9:
                    return False
            
            elif (col_number >= 3 and col_number <= 5):
                square_numbers_set = (set((S[0][3:6])), set((S[1][3:6])), set((S[2][3:6])))
                if len(square_numbers_set) < 9:
                    return False
            
            elif col_number >= 6:
                square_numbers_set = (set((S[0][6:])), set((S[1][6:])), set((S[2][6:])))
                if len(square_numbers_set) < 9:
                    return False
        
        elif row_number >= 3 and row_number <= 5:
            if col_number <= 2:
                square_numbers_set = (set((S[3][:3])), set((S[4][:3])), set((S[5][:3])))
                if len(square_numbers_set) != 9:
                    return False
            
            elif col_number >= 3 and col_number <= 5:
                square_numbers_set = (set((S[3][3:6])), set((S[4][3:6])), set((S[5][3:6])))
                if len(square_numbers_set) != 9:
                    return False
            
            elif col_number >= 6:
                square_numbers_set = (set((S[3][6:])), set((S[4][6:])), set((S[5][6:])))
                if len(square_numbers_set) != 9:
                    return False
        
        elif row_number >= 6:
            if col_number <= 2:
                square_numbers_set = (set((S[6][:3])), set((S[7][:3])), set((S[8][:3])))
                if len(square_numbers_set) != 9:
                    return False
            
            elif col_number >= 3 and col_number <= 5:
                square_numbers_set = (set((S[6][3:6])), set((S[7][3:6])), set((S[8][3:6])))
                if len(square_numbers_set) != 9:
                    return False
            
            elif col_number >= 6:
                square_numbers_set = (set((S[6][6:])), set((S[7][6:])), set((S[8][6:])))
                if len(square_numbers_set) != 9:
                    return False
        
        return True