class Animal():
    def __init__(self, name:str):
        self.name = name


a = ["Cat", "Dog", "Poule"]

b = [Animal(animal) for animal in a]

c = b[0]

b[0].name += "s"

print(b[0].name)
print(c.name)