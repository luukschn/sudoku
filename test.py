import numpy as np


s = [np.random.permutation(range(1,10)).reshape(3,3) for x in range(9)]
S = np.reshape(np.array([s[a] for a in range(len(s))]), (9,9))

print(S)
c = set([S[x][0] for x in range(9)])

print(len(c))