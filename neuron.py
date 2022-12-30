
import math
import random

class neuron:
    def __init__(self, layer: int, value=None) -> None:
        self.layer = layer
        self.value = random.random() if value is None else value
        self.weight = random.random()
        self.active = False

    def round(self) -> None:
        
        self.value = math.ceil(self.value * 1000) / 1000
        self.weight = math.ceil(self.weight * 1000) / 1000