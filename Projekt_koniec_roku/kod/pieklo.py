from kod import swiat
import time
import random
from kod.statystyki import hero
from kod import funkcje

fotress_found = False
fortress = None
spawner_found = False
spawner = None
blaze_stick = random.randint(4, 6)
ender_pearl = random.randint(8, 12)
bastion_found = False
bastion = None

asortyment_w_handlu = ["perła", "złote jabłko", "magmowy krem", "płomienny patyk", "mikstura zdrowia", "żelazny miecz", "diamentowy miecz"]

class Wrogi_mob:
    def __init__(self, name, atak, mob_hp, loot):
        self.name = name
        self.atk = atak
        self.hp = mob_hp
        self.loot = loot
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

class Magma_cube(Wrogi_mob):
    def __init__(self, name, atak, mob_hp, loot):
        super().__init__(name, atak, mob_hp, loot)

class Wither_szkielet(Wrogi_mob):
    def __init__(self, name, atak, mob_hp, loot):
        super().__init__(name, atak, mob_hp, loot)

class Plomyk(Wrogi_mob):
    def __init__(self, name, atak, mob_hp, loot):
        super().__init__(name, atak, mob_hp, loot)

class Spawner_Blaze:
    def __init__(self, name, blaze:Plomyk):
        self.name = name
        self.blaze = blaze
    def spawn(self):
        print("Trzeba troche poczekać aż blaze'y się zespawnują...")
        time.sleep(random.randint(1, 4))
        funkcje.walka_z_mobem(Plomyk, "Blaze", 8, "płomienny patyk", random.randint(1, 4))

class Enderman(Wrogi_mob):
    def __init__(self, name, atak, mob_hp, loot):
        super().__init__(name, atak, mob_hp, loot)

class Gold:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def spawn(self, amount):
        inp = input(f"Udało ci się znalezć złoto w ilości {amount}! Czy chcesz go wykopać? ")
        if inp == "tak":
            print("Kopiesz złoto...")
            time.sleep(2)
            hero["złoto"] += amount
            print(f"Udało się! Teraz masz {hero['złoto']} złota")
        elif inp == "nie":
            print("Cóż, twój wybór!")
        else:
            print("Niepoprawna komenda!")

class Piglin:
    def __init__(self, name):
        self.name = name
    def spotkanie(self):
        print("==="*40)
        print(f"Spotykasz {self.name}! Jest to mieszkaniec bastionu u którego możesz dostać różne rzeczy za złoto")
    def handel(self):
        inp = input("Czy chcesz handlować z piglinem? ")
        if inp == "tak":
            price = random.randint(1, 8)
            bought_item = asortyment_w_handlu[random.randint(0, len(asortyment_w_handlu) - 1)]
            print(f'Za {price} złota piglin jest gotowy sprzedać {bought_item}')
            zgoda = input("Czy zgadzasz się na dokonanie tego zakupu? ")
            if hero['złoto'] >= price:
                if zgoda == "tak":
                    hero['złoto'] -= price
                    hero['inventory'].append(bought_item)
                elif zgoda == "nie":
                    print("Zakup niedokonany!")
                else:
                    print("Niepoprawna komenda")
            else:
                print("Nie masz wystarczająco złota!")
                pass
        elif inp == "nie":
            print("Idziesz dalej wgłąb bastionu")
        else:
            print("Niepoprawna komenda!")
        
class Bastion:
    def __init__(self, name, gold:Gold, piglin:Piglin):
        self.name = name
        self.gold = gold
        self.piglin = piglin
    def in_bastion(self) -> bool:
        inp = input("Gdzie chcesz pójść? Iść p - prosto, l - lewo, pr - prawo, e - wyjście z bastionu ")
        if inp == "e":
            return False
        elif inp == "p" or inp == "pr" or inp == "l":
            spawn_chance = random.randint(1, 6)
            if spawn_chance == 2:
                self.piglin.spotkanie()
                self.piglin.handel()
            elif spawn_chance == 3:
                funkcje.walka_z_mobem(Magma_cube, "Magma cube", 6, "magmowy krem", random.randint(1, 3))
            elif spawn_chance == 4:
                self.gold.spawn(random.randint(1, 8))
            else:
                print("Szukasz dalej")
        else:
            print("Niepoprawny kierunek!")
        return True

class Fortress:
    def __init__(self, name, czarny_szkielet:Wither_szkielet, blaze:Plomyk, spawner:Spawner_Blaze, kostka_magmy:Magma_cube, enderman:Enderman):
        self.name = name
        self.wither_skeleton = czarny_szkielet
        self.blaze = blaze
        self.spawner = spawner
        self.magma_cube = kostka_magmy
        self.enerman = enderman
    def in_fortress(self) -> bool:
        global spawner_found, spawner
        if spawner_found == True:
            inp = input("Gdzie chcesz pójść? Iść p - prosto, l - lewo, pr - prawo, s - spawner blaze'ów, e - wyjście z fortressu ")
        else:
            inp = input("Gdzie chcesz pójść? Iść p - prosto, l - lewo, pr - prawo, e - wyjście z fortressu ")
        if inp == "e":
            return False
        elif inp == "p" or inp == "pr" or inp == "l":
            event_choice = random.randint(1, 8)
            if event_choice == 1:
                funkcje.walka_z_mobem(Wither_szkielet, "Wither szkielet", 14, "kość", random.randint(2, 4))
            elif event_choice == 2:
                funkcje.walka_z_mobem(Magma_cube, "Magma cube", 6, "magmowy krem", random.randint(1, 3))
            elif event_choice == 4:
                print("==="*40)
                print(f"Udało ci się znalezć spawner blaze'ów! Potrzebujesz zdobyć {blaze_stick} płomiennych patyczków żeby móc przejść do innego świata!")
                print("==="*40)
                spawner_found = True
            elif event_choice == 5:
                funkcje.walka_z_mobem(Enderman, 'Enderman', 12, "perła", random.randint(3, 6))
        elif inp == "s":
            if spawner_found == True :
                self.spawner.spawn()
        else:
            print("Wpisano nieprawidłowy kierunek")
        return True

def nether() -> bool:
    global fotress_found, fortress, bastion_found, bastion
    print("==="*50)
    print("Weszłeś do netheru! Bardzo niebezpiecznego miejsca, gdzie tylko nie pójdziesz spotkasz lawę lub ogień, twoim zadaniem jest znalezienie fortressu - piekielnego zamku")
    time.sleep(2)
    while hero['hp'] > 0:
        while swiat.nether_active == True and swiat.nether is not None:
            wybor = input("Co chcesz zrobić? a - wybór kierunku, b - heal, c - wgląd do inventory, e - wyjście z netheru ")
            if wybor == "a":
                if fotress_found == True and bastion_found == True:
                    action = input("Gdzie się tym razem wybierasz? Iść p - prosto, l - lewo, pr - prawo, f - fortress, b - bastion ")
                elif bastion_found == True:
                    action = input("Gdzie się tym razem wybierasz? Iść p - prosto, l - lewo, pr - prawo, b - bastion ")
                elif fotress_found == True:
                    action = input("Gdzie się tym razem wybierasz? Iść p - prosto, l - lewo, pr - prawo, f - fortress ")
                else:
                    action = input("Gdzie się tym razem wybierasz? Iść p - prosto, l - lewo, pr - prawo ")
                if action == "p" or action == "l" or action == "pr":
                    event_choice = random.randint(1, 10)
                    if event_choice == 1:
                        funkcje.walka_z_mobem(Hoglin, "Hoglin", 10, "wieprzowina", random.randint(1, 3))
                    elif event_choice == 2:
                        if funkcje.found_fortress(random.randint(1, 3)) == True:
                            fotress_found = True
                        else:
                            print("Fortress jest już gdzieś blisko...")
                    elif event_choice == 4:
                        funkcje.walka_z_mobem(Enderman, 'Enderman', 12, "perła", random.randint(3, 6))
                    elif event_choice == 5:
                        funkcje.walka_z_mobem(Magma_cube, "Magma cube", 6, "magmowy krem", random.randint(1, 3))
                    elif event_choice == 6:
                        if funkcje.found_bastion(random.randint(1, 2)) == True:
                            bastion_found = True
                        else:
                            print("Bastion jest już gdzieś blisko...")
                    else:
                        print("Idziesz dalej, nic nowego nie widać na drodze")
                elif action == "f":
                    print("==="*30)
                    print(f"Wchodzisz w piekielny zamek. Uważaj na siebie! ")
                    szkielet = Wither_szkielet("Wither szkielet", random.randint(2, 4), 14, "kość")
                    blaze = Plomyk("Blaze", random.randint(1, 4), 8, "płomienny patyk")
                    spawner = Spawner_Blaze("Spawner blaze'ów", blaze)
                    magma_cube = Magma_cube("Kostka magmy", random.randint(1, 3), 6, "magmowy krem")
                    enderman = Enderman('Enderman', random.randint(3, 6), 12, "perła")
                    piekielny_zamek = Fortress("Fortress", szkielet, blaze, spawner, magma_cube, enderman)
                    if fotress_found == True and piekielny_zamek.in_fortress() == True:
                        while piekielny_zamek.in_fortress() == True:
                            piekielny_zamek.in_fortress()
                    else:
                        print("Wychodzisz z zamku")
                        pass
                elif action == "b":
                    print("==="*30)
                    print(f"Wchodzisz w bastion - miejsce gdzie mieszkają pigliny które chętnie się z tobą wymienią na coś w zamian za złoto! ")
                    print(f"Musisz znalezć {ender_pearl} pereł aby przejść do kolejnego świata!")
                    p = Piglin("Piglin")
                    piglin_village = Bastion("Bastion", Gold("Złoto", random.randint(1, 8)), p)
                    if bastion_found == True and piglin_village.in_bastion() == True:
                        while piglin_village.in_bastion() == True:
                            piglin_village.in_bastion()
                    else:
                        print("Wychodzisz z bastionu")
                        pass
                else:
                    print("Wybrano nieprawidłowy kierunek!")
            elif wybor == "b":
                funkcje.add_health(hero["inventory"])
            elif wybor == "c":
                print("=="*60)
                print(hero["inventory"])
            elif wybor == "e":
                return False
    else:
        print("Nie zostało tobie życia, koniec gry!")
