
import numpy as np

from prints import prints

np.random.seed(10)

input_size = 1 # n
output_size = 2 # k
data_size = 1
layer_size = 2 # n || k
layer_count = 2 # iterations

values = [np.zeros((input_size, 1))]
weights = []
weights.append(np.random.rand(layer_size, input_size))

biases = []

for i in range(layer_count - 1):
    weights.append(np.random.rand(layer_size, layer_size))
    biases.append(np.random.rand(layer_size, 1))
    
weights.append(np.random.rand(output_size, layer_size))
biases.append(np.random.rand(layer_size, 1))
biases.append(np.random.rand(output_size, 1))

for wgh, bia in zip(weights, biases):
    val = values[-1]
    values.append(wgh.dot(val) + bia)

prints.list_matrix(values, "values:")
prints.list_matrix(weights, "weights:")
prints.list_matrix(biases, "biases:")


