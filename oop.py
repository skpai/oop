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
    def __add__(self, other):
        if isinstance(other, Zoo):
            return Zoo(self.liste+other.liste)
        else:
            return None


class Animal: 
    def __init__(self, animal_type): 
        if len(animal_type) < 2:
            raise ValueError("...")
        self.animal_type=animal_type 
    
    def __str__(self):
        return self.animal_type
    def se_deplacer(self):
        print("none")
        return None
    
    def dosomething(self):
        print("something")

class Serpent (Animal):  
    def __str__(self):
        return self.animal_type          
    def se_deplacer(self):
        print("je rampe")
        return None

class Oiseau(Animal):
    def __str__(self):
        return self.animal_type         
    def se_deplacer(self):
        print("je vole")
    def altitude_max(self):
        return 100
    def dosomething(self):
        super().dosomething() 

a = Animal('cat')
a.se_deplacer()
s=Serpent("Serpent")
s.se_deplacer()
o=Oiseau("Oiseau")
o.se_deplacer()
o.dosomething()
print(o.altitude_max())
z=Zoo([s,o])
z.dosomething()
print(z)
z.add_animal(a)
print(z)
print(z+z)

b= Animal('c')