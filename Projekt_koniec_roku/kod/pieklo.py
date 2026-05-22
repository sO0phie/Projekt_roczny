from kod import swiat
import time
import random
from kod.statystyki import hero
from kod import funkcje

class Wrogi_mob:
    def __init__(self, name, atak, mob_hp, loot):
        self.name = name
        self.atk = atak
        self.hp = mob_hp
        self.loot = loot
    def ucieczka(self):
        chance = random.randint(1, 3)
        if chance == 3:
            print(f"{self.name} uciekł! Możesz iść dalej!")
        else:
            pass
    def bitwa(self):
        print(f"{self.name} cię atakuje!")
        hero['hp'] -= self.atk
        if hero['hp'] < 0:
            hero['hp'] = 0
        print(f"Twoje hp: {hero['hp']}")
        time.sleep(1)
        print(f"Atakujesz {self.name}!")
        self.hp -= hero['atk']
        if self.hp < 0:
            self.hp = 0
        print(f"Hp {self.name}: {self.hp}")
        time.sleep(1)

class Hoglin(Wrogi_mob):
    def __init__(self, name, atak, mob_hp, loot):
        super().__init__(name, atak, mob_hp, loot)

def nether() -> None:
    print("==="*40)
    print("Weszłeś do netheru! Bardzo niebezpiecznego miejsca, gdzie tylko nie pójdziesz spotkasz lawę lub ogień, twoim zadaniem jest znalezienie fortressu - piekielnego zamku")
    time.sleep(2)
    while swiat.nether_active == True and swiat.nether is not None:
        wybor = input("Co chcesz zrobić? a - wybór kierunku, b - heal, c - wgląd do inventory ")
        if wybor == "a":
            action = input("Gdzie się tym razem wybierasz? Iść p - prosto, l - lewo, pr - prawo ")
            if action == "p" or action == "l" or action == "pr":
                event_choice = random.randint(1, 5)
                if event_choice == 1:
                    funkcje.walka_z_hoglinem(Hoglin)
            else:
                print("Wybrano nieprawidłowy kierunek!")
        elif wybor == "b":
            funkcje.add_health(hero["inventory"], hero["hp"])
        elif wybor == "c":
            print("="*30)
            print(hero["inventory"])
