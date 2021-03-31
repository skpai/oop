class Zoo : 
    def __init__(self, liste): 
        self.liste=liste 
    def __str__(self):
        return ''.join([l.animal_type+" " for l in self.liste])

    def add_animal(self, a):
        return self.liste.append(a)

    def dosomething(self):
        for l in self.liste:
            print(l.dosomething(), end=",")