class Oiseau(Animal):
    _animal_type="Oiseau"
    def __str__(self):
        return self.animal_type         
    def se_deplacer(self):
        print("je vole")
    def altitude_max(self):
        return 100
    def dosomething(self):
        super().dosomething() 