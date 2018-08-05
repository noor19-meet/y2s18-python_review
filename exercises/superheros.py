# Write your solutions for 1.5 here!
class Superheros:
    def __init__(self, name, superpower, strength):
        self.name = name
        self.superpower = superpower
        self.strength = strength
    def name_strength(self):
        print("My name is", self.name)
        print("My strength is", self.strength)

    def save_civilian(self, work):
    
        if work > self.strength:   
            print ("Superhero is not strong enough! :(")
            return
        self.strength = self.strength - work
Noor = Superheros ("Noor", "fly", 100)
Noor.name_strength()
Noor.save_civilian(99)