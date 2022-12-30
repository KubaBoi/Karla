class prints:

    @staticmethod
    def fit_in_spaces(long, short, char=" ") -> str:
        """
        Fills space pre and post short string to be same length as long

        Example:
        longlonglong    # 12
            short       # 5 -> 4 + 5 + 3 = 12 
        """
        spaces_count = len(long) - len(short)
        half_spaces = spaces_count // 2
        pre = half_spaces * char
        post = pre
        if (spaces_count % 2 == 1):
            pre += char
        return f"{pre}{short}{post}"

    @staticmethod
    def print_network(neurons: list, errors=[], right_answer=0) -> None:
        """
        Prints whole network

        neurons: list of list of neurons
        """
        #minimal_str="-200.250773993808049" 
        minimal_str="000.000"
        for i in range(len(neurons)):
            prints.print_layer(neurons, i, minimal_str)

        s = ""
        for e in errors:
            e_str = prints.fit_in_spaces(minimal_str, str(e))
            s += f" | {e_str}"
        delimiter = prints.fit_in_spaces(s, "-", "-")
        print(delimiter + "\n" + s)
        spaces = right_answer*(len(minimal_str) + 3)*" "
        spaces += ((len(minimal_str) + 3) // 2)*" "
        print(spaces, "^")
        print(spaces, right_answer)


    @staticmethod
    def print_layer(neurons: list, index: int, minimal_str="000.000") -> int:
        """
        Prints one layer of network

        returns length of last line
        """
        s = f"{index}: \n"
        layer = neurons[index]

        edges_str = ""
        neurs_str = ""
        for neuron in layer:
            e_str = prints.fit_in_spaces(minimal_str, f"{neuron.bias}")
            edges_str += f" | {e_str}"

            b_str = str(neuron.value)
            neurs_str += f" | {prints.fit_in_spaces(minimal_str, b_str)}"

        layer_spaces = "" #index * ((len(minimal_str) + 3) * " ")
        s += layer_spaces + neurs_str + "\n" + layer_spaces + edges_str
        print(s)
        return len(edges_str)
