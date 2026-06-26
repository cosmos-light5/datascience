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
""" Output:[43 21 41] """

#using  "or" 
filter_mask =  (my_arr % 2 == 0) | (my_arr > 40)
filtered_result = my_arr[filter_mask]
print(filtered_result)
""" Output:[40 43 14 41 44] """


filter_mask =  (my_arr % 2 == 0) | (my_arr > 40)
filtered_condition = my_arr[~filter_mask]         #~tilday/ negation i.e. not ;  condition satis fy nagarna ko lagi
print(filtered_condition)
""" Output:[19 21 13] """




np.random.seed(20)

arr_2 = np.random.randint(-5, 20,(10,))            # -5 bata 20 samma 10 wata generate garne vaneko
print(arr_2)


#replace -ve value with 0

filter_mask =arr_2 <0
arr_2[filter_mask] = 0      #my_list[condition] = value
print(arr_2)



