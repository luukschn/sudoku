import numpy as np
import matplotlib.pyplot as plt
from sudoku_verification import Verification

#setup sudoku
s = [np.random.permutation(range(1,10)).reshape(3,3) for x in range(9)]
S = np.reshape(np.array([s[a] for a in range(len(s))]), (9,9))

verification = Verification()