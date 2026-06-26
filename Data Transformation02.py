# Linear Algebra Operations 
import numpy as np

np.random.seed(6)
# mean=25, std=2
mat_4x3=np.round(np.random.normal(25,2,(4,3)))      # (4,3)--> data ko shape
print(mat_4x3)
""" Output:
[[24. 26. 25.]
 [23. 20. 27.]
 [27. 22. 28.]
 [24. 30. 26.]] """
print()

transposed_mat = np.transpose(mat_4x3)    #mat_4x3.T 
print(transposed_mat)
""" Output: 
[[24. 23. 27. 24.]
 [26. 20. 22. 30.]
 [25. 27. 28. 26.]]"""

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
""" Output: 
[[ 1.2 23. ]
 [ 1.3 20. ]
 [ 0.1 12. ]
 [ 2.3 27. ]]
 
 [[ 1.6 26. ]
 [ 0.2 23. ]]"""


combined_data = np.concatenate([mahesh_readings,prakash_readings], axis=0)      #yaha concatinate garda both matrix lai row-row concatinate gareko le axis=0
print(combined_data)                                        #row thapda col no. same and col thapda row ko no. same hunuparxa
""" Output: 
[[ 1.2 23. ]
 [ 1.3 20. ]
 [ 0.1 12. ]
 [ 2.3 27. ]
 [ 1.6 26. ]
 [ 0.2 23. ]]"""
print()


# humidity, rainfall
rushter_reading = np.array([[1.2, 22],[0.3,20],[1.5,21]])
jairaj_reading = np.array([[1.2,0.1],[5.2,0.6],[2.7, 0.7]])

print(rushter_reading)
print()
print(jairaj_reading)
""" Output: 
[[ 1.2 22. ]
 [ 0.3 20. ]
 [ 1.5 21. ]]

[[1.2 0.1]
 [5.2 0.6]
 [2.7 0.7]]
"""
print()

# two matrix ma kunai col common huna sakxa so intersecting col eakpatak ra remaining lai add garna axis 1
combined_data = np.concatenate([rushter_reading,jairaj_reading], axis=1)
print(combined_data)
""" Output: 
[[ 1.2 22.   1.2  0.1]
 [ 0.3 20.   5.2  0.6]
 [ 1.5 21.   2.7  0.7]]"""
print()

#alternative way for axis=1
combined_data = np.hstack([rushter_reading,jairaj_reading])     #hstack(())--> row ko lagi 7.30; horizontal stack
print(combined_data)
""" Output: 
[[ 1.2 22.   1.2  0.1]
 [ 0.3 20.   5.2  0.6]
 [ 1.5 21.   2.7  0.7]]"""
print()

combined_data = np.vstack([rushter_reading,jairaj_reading])
print(combined_data)
""" Output: #alternative way for axis=1"""
print()

arr_1=np.array([2,3,8])
arr_2=arr_1.copy()              #arr_2=arr_1 matra vayeko vaye arr_1 ra 2 print garda same result hunthyo i.e. eutai manxeko duita nam jasto
arr_1[2]=4
print(arr_1)
print(arr_2)
""" Output: """
print()