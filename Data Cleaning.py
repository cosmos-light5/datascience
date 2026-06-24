# Write a function clean_outlier that takes 1D array, replaces outliers with median & return clean data. (Outliers: data below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR).


# Write a function clean_outlier_std that implements similar task but different outlier definition. (data below mean - 2 * std or above mean + 2 * std).


# You have sensor recording data over time. It records invalid value as -1. Write a function clean_invalid that takes 1D array, replace -1 with surrounding mean & return clean data.


# Write function fix_invalid_data that takes 2D NumPy array. Array contains invalid value represented as -999. Function has to substitute invalid value with mean of data. Optionally function should have axis argument. If axis=0, replacement has to be done by column mean. If axis=1, replace by row mean else overall mean. [Hint: np.apply_along_axis(fn, axis, data)].

