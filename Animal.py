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