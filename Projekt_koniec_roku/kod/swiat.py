import random
from kod import funkcje

class Przyjazny_mob:
    def __init__(self):
        self.hp = random.randint(4, 8)
        self.xp = random.randint(1, 4)

class Kurczak(Przyjazny_mob):
    def __init__(self):
        super().__init__()
        self.name = "kurczak"
        self.loot = "kurczak"

class Krowa(Przyjazny_mob):
    def __init__(self):
        super().__init__()
        self.name = "krowa"
        self.loot = "wołowina"

def swiat():
    mob_choice = random.randint(1, 3)
    if mob_choice == 1:
        znalezione = funkcje.spawn_chance(Kurczak)
        if znalezione:
            funkcje.polowanie(znalezione, znalezione[0].xp, znalezione[0].loot, "kurczak")
    else:
        znalezione = funkcje.spawn_chance(Krowa)
        if znalezione:
            funkcje.polowanie(znalezione, znalezione[0].xp, znalezione[0].loot, "krowa")
