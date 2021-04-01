from Animal import Animal
class Oiseau(Animal):
    def __init__(self, animal_type, weight, height,_altitude_max ):
        super().__init__(animal_type, weight, height) 
        self._altitude_max =_altitude_max
        self._animal_type="Oiseau"
    @property
    def altmax(self):
        return self._altitude_max
    @altmax.setter #For no use now
    def altmax(self, value):
        print("setter of altitude_max called")
        self._altitude_max = value


    def __str__(self):
        return self.animal_type         
    def se_deplacer(self):
        print("je vole")
    def dosomething(self):
        super().dosomething() 