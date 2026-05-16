import random

class Przyjazny_mob:
    def __init__(self):
        self.hp = random.randint(4, 8)
        self.xp = random.randint(1, 4)

class Kurczak(Przyjazny_mob):
    def __init__(self):
        super().__init__()
        self.loot = "kurczak"
    def dzwiek(self):
        print("Kukuryku")

# class Kurczak(Przyjazny_mob):
#     def __init__(self):
#         super().__init__()
#         self.loot = "kurczak"
#     def dzwiek(self):
#         print("")

class Swiat:
    def __init__(self):
        pass