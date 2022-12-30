
import random

from prints import prints
from neuron import neuron

def generate_random_data(length, wrong=False) -> tuple:
    data = []
    for i in range(length):
        if (wrong): data.append(0)
        else: data.append(random.randint(0, 1))
    if (not wrong): data[0] = 1
    return data

def create_layer(index: int, count: int) -> None:
    layer = []
    for i in range(count):
        new_neuron = neuron(index)
        new_neuron.round()
        
        layer.append(new_neuron)
    return layer

def create_first_layer(data: list, neurons: list) -> None:
    first_layer = []
    for i in data:
        new_neuron = neuron(0, i)
        new_neuron.round()
        first_layer.append(new_neuron)
    neurons[0] = first_layer

def edit_first_layer(data: list, neurons: list) -> None:
    for i, d in enumerate(data):
        neurons[0][i].value = d

def create_new_network(output_size, 
                        hidden_layers_count,
                        hidden_layers_nodes_count):
    neurons = [[]]
    
    for l in range(hidden_layers_count):
        layer = create_layer(l, hidden_layers_nodes_count)
        neurons.append(layer)

    last_layer = create_layer(len(neurons), output_size)
    neurons.append(last_layer)
    
    return neurons


def calc_neurons(neurons: list) -> None:
    for i, layer in enumerate(neurons[1:]):
        p_layer = neurons[i]
        layer_constant = 0
        layer_count = 0
        for p in p_layer:
            val = p.value * p.weight
            if (val < 1): 
                continue
            p.active = True
            layer_count += 1
            layer_constant += val
        if (layer_count == 0): layer_constant = 0
        else: layer_constant -= layer_count           

        for neur in layer:
            neur.value = int(1*(layer_constant + neur.weight) >= 1)
            #neur.value /= layer_count + 1
            neur.round()

def calc_errors(neurons: list, right_index: int) -> list:
    """
    Method calculates errors of last neurons
    """
    errors = []
    for i, neur in enumerate(neurons[-1]):
        if (i == right_index):
            errors.append(1 - neur.value)
        else:
            errors.append(0 - neur.value)
    return errors

def rework_network(neurons: list, errors: list, right_answer: int) -> None:
    """
    Reworks weights by errors list.
    Changes node's weight by error deviation,
    those nodes are the once which are set as active

    errors: list of deviations of last layer's value 
            from expected value
    """
    error_sum = sum(errors)
    for layer in neurons:
        for neur in layer:
            if (not neur.active): continue
            neur.active = False
            neur.weight += error_sum#errors[right_answer]
            neur.round()
                

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
neurons = create_new_network(output_length, 7, 7)

prints.print_network(neurons)
data_sets = [True, False]

for it, d in enumerate(data_sets):
    data = generate_random_data(data_length, d)
    right_answer = int(not d)
    create_first_layer(data, neurons)
    for i in range(iterations):
        print("\n", 5*"==", f"Learning iteration {it}.{i} - {d}", 5*"==")
        calc_neurons(neurons)
        errors = calc_errors(neurons, right_answer)
        prints.print_network(neurons, errors, right_answer)
        rework_network(neurons, errors, right_answer)

print("\n", 10*"==", "Learning end", 10*"==")


data = generate_random_data(data_length)
right_answer = 1
edit_first_layer(data, neurons)
calc_neurons(neurons)
errors = calc_errors(neurons, right_answer)
prints.print_network(neurons, errors, right_answer)

print("")
prints.print_layer(neurons, -1)
print("")

data = generate_random_data(data_length, True)
right_answer = 0
edit_first_layer(data, neurons)
calc_neurons(neurons)
errors = calc_errors(neurons, right_answer)
#prints.print_network(neurons, errors, right_answer)

print("")
prints.print_layer(neurons, -1)
