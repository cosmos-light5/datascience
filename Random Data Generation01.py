import numpy as np

# Set the random seed to 42 for reproducibility.

np.random.seed(42)

random_data=np.random.randint(45)
print(random_data)


# Generate a 3x3 array of random integers between 1 and 100.
random_mat=np.random.randint(1,100,(3,3))
print(random_mat)


# Create a 4x4 array of random samples from a standard normal distribution.
random_4x4_samples = np.random.randint(1,20,(4,4))
print(random_4x4_samples)


# rng = np.random.default_rng()     -->Initialize the recommended random number generator

# array_4x4 = rng.standard_normal(size=(4, 4))      -->Generate a 4x4 array of standard normal samples
# array_4x4 = random_4x4_samples.standard_normal(size=(4, 4))
# print(array_4x4)


# Generate a 5x5 identity matrix.
id_mat=np.identity(5)
print(id_mat)


# Create 5x4 array with values from normal distribution of mean 50, std 10.

