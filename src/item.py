class Items:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location
        
    def __str__(self):
        return(F'{self.name} {self.description}')