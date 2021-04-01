class Animal: 
    def __init__(self, animal_type, weight, height): 
        if weight <=0:
            raise ValueError("Sorry, weight should be number more than 0")
        self._weight=weight
        self._height=height
        self._animal_type=animal_type 
    def __str__(self):
        return self.animal_type
    def se_deplacer(self):
        print("none")
        return None
    
    def dosomething(self):
        print("something")