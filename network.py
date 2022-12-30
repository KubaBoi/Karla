
from neuron import neuron

class network:
    def __init__(self, 
                output_size, 
                hidden_layers_count,
                hidden_layers_nodes_count):
        self.output_size = output_size
        self.hidden_layers_count = hidden_layers_count
        self.hidden_layers_nodes_count = hidden_layers_nodes_count
        self.neurons = [[]]
        self.create_new_network()        
    
    def create_layer(self, index: int, count: int, next_count: int) -> list:
        layer = []
        for i in range(count):
            new_neuron = neuron(index, next_count)
            new_neuron.round()
            
            layer.append(new_neuron)
        return layer

    def create_first_layer(self, data: list, next_layer_size: int) -> None:
        first_layer = []
        for i in data:
            new_neuron = neuron(0, next_layer_size, i)
            new_neuron.round()
            first_layer.append(new_neuron)
        self.neurons[0] = first_layer

    def edit_first_layer(self, data: list) -> None:
        for i, d in enumerate(data):
            self.neurons[0][i].value = d

    def create_new_network(self) -> None:
        neurons = [[]]
        
        for l in range(self.hidden_layers_count - 1):
            layer = self.create_layer(l, self.hidden_layers_nodes_count, self.hidden_layers_nodes_count)
            neurons.append(layer)

        last_hidden_layer = self.create_layer(l, self.hidden_layers_nodes_count, self.output_size)
        neurons.append(last_hidden_layer)

        last_layer = self.create_layer(len(neurons), self.output_size, 1)
        neurons.append(last_layer)
        
        return neurons


    def calc_neurons(self) -> None:
        for layer in self.neurons:
            for neur in layer:
                neur.set_next_layer(self.neurons)
                neur.round()

    def calc_errors(self, right_index: int) -> list:
        """
        Method calculates errors of last neurons
        """
        errors = []
        for i, neur in enumerate(self.neurons[-1]):
            if (i == right_index):
                errors.append(1 - neur.value)
            else:
                errors.append(0 - neur.value)
        return errors

    def rework_network(self, errors: list, right_answer: int) -> None:
        """
        Reworks weights by errors list.
        Changes node's weight by error deviation,
        those nodes are the once which are set as active

        errors: list of deviations of last layer's value 
                from expected value
        """
        error_sum = sum(errors)
        for layer in self.neurons:
            for neur in layer:
                if (not neur.active): continue
                neur.active = False
                neur.round()
                    