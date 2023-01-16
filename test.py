
import numpy as np

from prints import prints
from save import save

np.random.seed(10)

input_size = 1 # n
output_size = 2 # k
data_size = 1
layer_size = 2 # n || k
layer_count = 2 # iterations

def generate() -> tuple:
    # generate random initial values
    weights = []
    biases = []

    weights.append(np.random.rand(layer_size, input_size))

    for i in range(layer_count - 1):
        weights.append(np.random.rand(layer_size, layer_size))
        biases.append(np.random.rand(layer_size, 1))
        
    weights.append(np.random.rand(output_size, layer_size))
    biases.append(np.random.rand(layer_size, 1))

def forward_prop(input):
    # forward propagation
    global weights, biases
    activations = [input]
    for wgh, bia in zip(weights[:-1], biases):
        val = activations[-1]
        activations.append(1 /(1 + np.exp(-(wgh.dot(val) + bia))))
    activations.append(weights[-1].dot(activations[-1]))
    return activations

def activation_grad(vals: list) -> list:
    return vals * (1 - vals)

def cost(error: list, delta=[], index=-2) -> list:
    # mean squared error - cost function
    global activations, weights, biases
    err = weights[index+1].transpose().dot(error) #.multiply(a_grad)
    delta.append((
        error.dot(activations[index].transpose()) / len(error),
        error.sum(axis=1, keepdims=True) / len(error)
    ))
    if (index > -len(weights)):
        delta, error = cost(err, delta, index-1)
    else:
        delta.append((
            error.dot(activations[0]),
            error.sum(axis=1, keepdims=True) / len(error)
        ))
    return delta, error
    
def backward_prop(cst: list) -> None:
    # updates weights and biases by cost function
    global weights, biases
    for i, c in enumerate(reversed(cst)):
        weights[i] -= c[0]
        if (i > 0):
            biases[i-1] -= c[1]

y = [[1], [0]]
inp = np.zeros((input_size, 1))
weights, biases = save.load("1673910147")

activations = forward_prop(inp)

prints.list_matrix(activations, "activations:")
"""
prints.list_matrix(weights, "weights:")
prints.list_matrix(biases, "biases:")
"""

error = activations[-1] - y
error = error * error
cst, error = cost(error)
backward_prop(cst)

prints.list_matrix(weights, "weights:")
prints.list_matrix(biases, "biases:")

save.save(weights, biases)




