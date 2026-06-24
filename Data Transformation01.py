# filtering and masking
import numpy as np

np.random.seed(5)
my_arr = np.random.randint(5,50,(8,))          #(5,50,(8,)) -->5 dekhi 50 vitra ko data dinxa tara 8 wata matra   
print(my_arr)
""" Output: [40 19 43 21 14 13 41 44] """


# filtering array greater than 20 from seeded random num. and resulting if the numbers meet the condition.
filter_mask = my_arr > 20           #compare garera corresponding indexes ma boolean array dinxa not exact values
print(filter_mask)
""" Output: [ True False  True  True False False  True  True] """


# filtering array greater than 20 from seeded random num.
filter_result = my_arr [filter_mask]        # alternet way--> my_arr [my_arr > 20]
print(filter_result)
""" Output:[40 43 21 41 44]"""


filter_even_result = my_arr [my_arr % 2== 0]
print(filter_even_result)
""" Output:[40 14 44] """

#filter odd num greater than 20
filter_mask =  (my_arr % 2 != 0) & (my_arr > 20)      #& use garne "and" use gare ma error
filter_odd_result = my_arr[filter_mask]
print(filter_odd_result)

