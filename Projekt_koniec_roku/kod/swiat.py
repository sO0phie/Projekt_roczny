import random
from kod import funkcje
from kod.statystyki import hero
import time

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

class Miecz:
    def __init__(self, name, atk):
        self.name = name
        self.atak = atk

class Budynek:
    def __init__(self, name):
        self.name = name

class Blacksmith(Budynek):
    def __init__(self):
        super().__init__("kuźnia")
    def zakup(self):
        print("Weszłeś do kuzni, tutaj możesz kupić miecz który zwiększy twój atak ")
        inp = input("Czy chcesz coś kupić? ")
        if inp == "tak":
            inp = input("Drewniany miecz - zwiększa atak o 1 , Kamienny miecz - zwiększa atak o 4 , Żelazny miecz - zwiększa atak o 8 , Diamentowy miecz - zwiększa atak o 12 ")
            if inp == "drewniany miecz":
                check = funkcje.if_miecz(5, "drewniany miecz") 
                if check == True:
                    wooden_sword = Miecz("drewniany miecz", 1)
                    hero["atk"] += wooden_sword.atak
                    hero["inventory"].append(wooden_sword.name)
            elif inp == "kamienny miecz":
                check = funkcje.if_miecz(15, "kamienny miecz")
                if check == True:
                    stone_sword = Miecz("kamienny miecz", 4)
                    hero["atk"] += stone_sword.atak
                    hero["inventory"].append(stone_sword.name)
            elif inp == "żelazny miecz":
                check = funkcje.if_miecz(30, "żelazny miecz") 
                if check == True:
                    iron_sword = Miecz("żelazny miecz", 8)
                    hero["atk"] += iron_sword.atak
                    hero["inventory"].append(iron_sword.name)
            elif inp == "diamentowy miecz":
                check = funkcje.if_miecz(60, "diamentowy miecz") 
                if check == True:
                    diamond_sword = Miecz("diamentowy miecz", 12)
                    hero["atk"] += diamond_sword.atak
                    hero["inventory"].append(diamond_sword.name)
        else:
            print("Wychodzisz z kuzni")

class Village():
    def __init__(self, name, kuznia:Blacksmith):
        self.name = name
        self.kuznia = kuznia
    def use(self):
        global wioska_found
        wioska_found = True
        print("=="*20)
        print("Znalazłeś wioskę, tutaj możesz handlować z lokalnymi mieszkańcami oraz zdobyć pottrzebne materiały ")
        time.sleep(1)
        inp = input("Gdzie chcesz pójść? k - kuznia ")
        if inp == "k":
            self.kuznia.zakup()
def swiat():
    event_choice = random.randint(1, 5)
    if event_choice == 1:
        znalezione = funkcje.spawn_chance(Kurczak)
        if znalezione:
            funkcje.polowanie(znalezione, znalezione[0].xp, znalezione[0].loot, "kurczak")
    elif event_choice == 3:
        znalezione = funkcje.spawn_chance(Krowa)
        if znalezione:
            funkcje.polowanie(znalezione, znalezione[0].xp, znalezione[0].loot, "krowa")
    elif event_choice == 5 and wioska_found == False:
        k = Blacksmith()
        wioska = Village("wioska", k)
        wioska.use()
    else:
        print("Nic nie widać na drodze")
