import numpy as np


mat_a=np.array([[1,-2],[0,5]])
mat_b=np.array([[3,0],[1,-1]])
print(mat_a)
print(mat_b)

corr_mult= mat_a * mat_b    #-->yesto gare individual corresponding elements matra multiply hunxa
print(corr_mult)


result= mat_a @ mat_b       #result= np.dot(mat_a,mat_b)
print(result)