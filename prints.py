
class prints:
    
    @staticmethod
    def list_matrix(lst: list, text="") -> None:
        print(text)
        for m in lst:
            print(m.view())
            print("---")