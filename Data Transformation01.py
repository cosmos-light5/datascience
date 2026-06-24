# filtering and masking
import numpy as np

np.random.seed(5)
my_arr = np.random.randint(5,50,(8,))
print(my_arr)


filter_mask = my_arr > 20
print(filter_mask)