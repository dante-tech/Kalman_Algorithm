import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Define the number of samples, input features, and output features
n_samples = 100
n_input = 2
n_output = 1

# Generate random input features from a uniform distribution
X = np.random.uniform(-1, 1, size=(n_samples, n_input))

# Define a nonlinear function of the input features
f = lambda x: np.sin(2 * np.pi * x[:, 0]) * np.cos(2 * np.pi * x[:, 1])

# Generate the output feature by adding some Gaussian noise to the function
y = f(X) + np.random.normal(0, 0.1, size=(n_samples, n_output))


