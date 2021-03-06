
class Stringer:

    @staticmethod
    def starts(text, listOfPosibilities):
        for l in listOfPosibilities:
            if (text.startswith(l)):
                return True
        return False
    
    @staticmethod
    def ends(text, listOfPosibilities):
        for l in listOfPosibilities:
            if (text.endswith(l)):
                return True
        return False

    @staticmethod
    def inside(text, listOfPosibilities):
        for l in listOfPosibilities:
            if (text.find(l) >= 0):
                return True
        return False

    @staticmethod
    def accept(text, type=False):
        if (text == "yes" or
            text == "yeah"):
            return True
        return False