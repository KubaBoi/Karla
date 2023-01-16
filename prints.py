
class prints:
    
    @staticmethod
    def list_matrix(lst: list, text="") -> None:
        print(text)
        for m in lst:
            print(m.view())
            print("---")
            
    @staticmethod
    def count(*lst: list) -> None:
        txt = ""
        for ls in lst:
            l = 0
            for m in ls:
                l += len(m)
            txt += str(l) + " "
        print(txt)
        