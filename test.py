
import random

from prints import prints
from neuron import neuron
from network import network

def generate_random_data(length, wrong=False) -> tuple:
    data = []
    for i in range(length):
        if (wrong): data.append(0)
        else: data.append(random.randint(0, 1))
    if (not wrong): data[0] = 1
    return data

number = [
    0, 0, 1, 0, 0,
    0, 1, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 1, 0, 0
]

random.seed(10)

output_length = 2
iterations = 2
data_length = 1
layer_size = 7
layer_count = 7

netw = network(output_length, layer_count, layer_size)

prints.print_network(netw.neurons)
data_sets = [True, False]

for it, d in enumerate(data_sets):
    data = generate_random_data(data_length, d)
    right_answer = int(not d)
    netw.create_first_layer(data, layer_size)
    for i in range(iterations):
        print("\n", 5*"==", f"Learning iteration {it}.{i} - {not d}", 5*"==")
        netw.calc_neurons()
        errors = netw.calc_errors(right_answer)
        prints.print_network(netw.neurons, errors, right_answer)
        netw.rework_network(errors, right_answer)

print("\n", 10*"==", "Learning end", 10*"==")

print("")
prints.print_layer(netw.neurons, -1)
