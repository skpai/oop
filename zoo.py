class Zoo : 
    def __init__(self, liste): 
        self._liste=liste 
    def __str__(self):
        return ''.join([l._animal_type+" " for l in self._liste])

    def add_animal(self, a):
        return self._liste.append(a)

    def dosomething(self):
        for l in self._liste:
            print(l.dosomething(), end=",")
    def __add__(self, other):
        if isinstance(other, Zoo):
            return Zoo(self._liste+other._liste)
        else:
            return None
