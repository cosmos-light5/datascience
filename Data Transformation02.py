# Linear Algebra Operations 
import numpy as np

np.random.seed(6)
# mean=25, std=2
mat_4x3=np.round(np.random.normal(25,2,(4,3)))      # (4,3)--> data ko shape
print(mat_4x3)
print()

transposed_mat = np.transpose(mat_4x3)    #mat_4x3.T 
print(transposed_mat)


""" -->Use the .T attribute to transpose
mat_3x4 = mat_4x3.T

print(mat_3x4) """
print()

#co2, temp
mahesh_readings = np.array([[1.2, 23],[1.3,20],[0.1,12],[2.3,27]])
prakash_readings = np.array([[1.6,26],[0.2,23]])

print(mahesh_readings)
print()
print(prakash_readings)
print()

combined_data = np.concatenate([mahesh_readings,prakash_readings], axis=0)      #row thapda col no. same and col thapda row ko no. same hunuparxa
print(combined_data)