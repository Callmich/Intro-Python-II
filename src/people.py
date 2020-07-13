people = ["Abe", "Bill", "Charles", "Dolly", "David", "Evelyn", "Frank", "Gunther"]
# comp for names that start with D
a = [person for person in people if person[-1]== "y"]
print(a)
# comp for names that end in Y

# comp for names that start with B through D

# comp for names but in uppercase

c = [person.upper() for person in people]
print(c)
