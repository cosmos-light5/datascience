# filtering and masking
import numpy as np

np.random.seed(5)
my_arr = np.random.randint(5,50,(8,))
print(my_arr)


# filtering array greater than 20 from seeded random num. and resulting if the numbers meet the condition.
filter_mask = my_arr > 20
print(filter_mask)


# filtering array greater than 20 from seeded random num.
filter_result = my_arr [filter_mask]        # alternet way--> my_arr [my_arr > 20]
print(filter_result)