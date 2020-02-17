import numpy as np


def nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

A = np.zeros(shape=(9,6))
#print(A)
for i in range(9):
    for j in range(6):
        if j == 2 or j == 3:
            A[i][j] =1
        elif (j == 1 and i == 7) or (j == 1 and i == 8):
            A[i][j] = 1
        elif (j == 4 and i == 7) or (j == 4 and i == 8):
            A[i][j] = 1

        ########
        elif (j == 1 and i == 0) or (j == 1 and i == 1):
            A[i][j] = 1
        elif (j == 4 and i == 0) or (j == 4 and i == 1):
            A[i][j] = 1


B = np.pad(A, ((1,1),(0,0)), 'constant')

#print(A)
#print(B)

y, x = np.mgrid[1:67:6, :6]
C = y + x
print(C)

D = np.multiply(B,C)

print(D)

E = new_arr_no_0 = D[np.where(D!=0)]
print(E)

max, min = E.max(), E.min()
F = (E - min) / (max - min)
print(F)
print(nearest(F, 0.25))


