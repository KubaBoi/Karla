
import numpy as np
import os
import time

class save:
    
    @staticmethod
    def save(weights, biases) -> None:
        s = ""
        for l in weights:
            s += str(l)
        s = save.replace(s)
        s += "\n"
        s2 = ""
        for l in biases:
            s2 += str(l)
        s2 = save.replace(s2)
        with open(os.path.join("saves", str(int(time.time()))), "w") as f:
            f.write(s + s2)
        
    @staticmethod
    def replace(s) -> str:
        s = s.replace("\n", "")
        s = s.replace("[[", "")
        s = s.replace("]]", "\n")
        s = s.replace("]", ",")
        s = s.replace("[", "")
        s = s.replace("  ", " ")
        return s
    
    @staticmethod
    def load(file) -> tuple:
        with open(os.path.join("saves", file), "r") as f:
            data_lines = f.readlines()
        
        weights = []
        for i, line in enumerate(data_lines):
            if (line == "\n"):
                index = i
                break
            weights.append([])
            for row in line.split(","):
                row = row.strip()
                weights[i].append([])
                for col in row.split(" "):
                    weights[i][len(weights[i]) - 1].append(float(col))
        
        biases = []
        for i, line in enumerate(data_lines[index+1:]):
            biases.append()
            for row in line.split(","):
                row = row.strip()
                biases[i].append([])
                for col in row.split(" "):
                    biases[i][len(biases[i]) - 1].append(float(col))
        return weights, biases 

        