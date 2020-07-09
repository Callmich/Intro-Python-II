# Implement a class to hold room information. This should have name and
# description attributes.
from item import Items


class Room:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor
        self.N_to = None
        self.S_to = None
        self.E_to = None
        self.W_to = None
        self.items = {}
    
    # def addItems(self, items):
    #     for x in items:
    #         Items(x)
    #         (self.items).append(x)
    #         pass

    
    
    def __str__(self):
        return(F'You find yourself in the {self.name}.\n{self.flavor}\nOn the ground there are {self.items}\nWhich direction shall you travel?')
    






