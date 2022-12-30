
import math
import random

class neuron:
    def __init__(self, layer, next_layer_size, value=None) -> None:
        self.layer = layer
        self.value = 0 if value is None else value
        self.bias = random.random() 
        self.active = False

        self.weights = []
        for i in range(next_layer_size):
            self.weights.append(random.random())

    def round(self, dec=1000) -> None:     
        self.value = math.ceil(self.value * dec) / dec
        for i, w in enumerate(self.weights):
            self.weights[i] = math.ceil(w * dec) / dec

    def decide_activity(self) -> None:
        """
        Decides if node is activated or not
        """
        self.active = self.value - self.bias >= 0

    def set_next_layer(self, neurons) -> None:
        """
        Adds itselfes influence at next neurons into their add_value
        """
        self.decide_activity()
        if (not self.active):
            return
        for i, next_neur in enumerate(neurons[self.layer + 1]):
            if (next_neur.add_value is None):
                next_neur.add_value = 0
            next_neur.add_value += self.weights[i] * self.value