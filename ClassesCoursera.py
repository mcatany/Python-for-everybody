# Classes
# Uses python3

# Base class PartyAnimal
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name)
        
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

# Child class FootballFan
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)

		
# Example of usage
if __name__ == "__main__":	
	an = PartyAnimal("Sally")
	an.party()
	wentz = FootballFan("Carson")
	wentz.touchdown()
