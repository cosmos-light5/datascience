# Linear Algebra Operations 
import numpy as np

np.random.seed(6)

mat_4x3=np.round(np.random.normal(25,2,(4,3)))
print(mat_4x3)


transposed_mat = np.transpose(mat_4x3)    #mat_4x3.T 

print(transposed_mat)


""" -->Use the .T attribute to transpose
mat_3x4 = mat_4x3.T

print(mat_3x4) """