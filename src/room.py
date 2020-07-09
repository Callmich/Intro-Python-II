# Implement a class to hold room information. This should have name and
# description attributes.



class Room:
    def __init__(self, name, flavor, *items):
        self.name = name
        self.flavor = flavor
        self.N_to = None
        self.S_to = None
        self.E_to = None
        self.W_to = None
        self.items = Items(items)
    
    def __str__(self):
        return(F'You find yourself in the {self.name}.\n{self.flavor}\nOn the ground there are {self.items}\nWhich direction shall you travel?')



class Items:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return(F'{self.name} ')





