# import numpy

# A=numpy.array([[5,7,9],[-1,6,7],[22,-9,8]])
# B=numpy.array([[90,8,-3],[4,4,-2],[0,8,5]])
# AB=A*B
# print(AB)
# print(numpy.linalg.det(AB))


A = [[1, 2], [3, 4]] 
B = [[1, 2], [3, 4]]

C = [[0]*len (A[0]) for i in range(len(B))]

for i in range (len (A[0])):

    for j in range (len (B)): 
        for k in range (len (A[0])):

            C[j][k] += A[k][i]*B[i][j]

print(C)