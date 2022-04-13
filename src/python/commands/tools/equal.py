
class Equal:

    @staticmethod
    def starts(text, listOfPosibilities):
        for l in listOfPosibilities:
            if (text.startswith(l)):
                return l
        return False
    
    @staticmethod
    def ends(text, listOfPosibilities):
        for l in listOfPosibilities:
            if (text.endswith(l)):
                return l
        return False

    @staticmethod
    def inside(text, listOfPosibilities):
        for l in listOfPosibilities:
            if (text.find(l) >= 0):
                return l
        return False