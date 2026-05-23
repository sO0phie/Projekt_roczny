import random
from kod.statystyki import hero
import time

def spawn_chance(klasa) -> list:
    szansa = random.randint(1, 3)
    if szansa == 2:
        mobs = []
        mob = klasa()
        mobs.append(mob)
        print("==="* 40)
        print(f"Spotkałeś {mob.name}")
        return mobs
    return []


def polowanie(mobs, xp, loot, nazwa):
    wybor = input(f"Czy chcesz upolować {nazwa}? ")
    if wybor != "tak":
        print(f"Pozwalasz {nazwa} uciec, podróżujesz dalej")
        return
    while mobs:
        time.sleep(1)
        print(f"Hp moba : {mobs[0].hp}, twój atak {hero['atk']}")
        mobs[0].hp -= hero["atk"]
        if mobs[0].hp <= 0:
            print(f"Zabiłeś {nazwa}! Zdobywasz {xp} xp i {loot}")
            hero["xp"] += xp
            hero["inventory"].append(loot)
            mobs.pop(0)

def if_miecz(required_xp, in_inventory) -> bool:
    if hero["xp"] < required_xp:
        print("Masz za mało xp!")
        return False
    elif in_inventory in hero["inventory"]:
        print("Masz już ten miecz!")
        return False
    else:
        return True
    
def trade(inventory, item):
    if len(inventory) >= 1:
        a = input(f'Co chcesz wymienić? {inventory} ')
        if a in inventory:
            inp = input(f'Za {a} możesz otrzymać {item}, czy zgadzasz sie na tą wymianę? ')
            if inp == "tak":
                inventory.remove(a)
                inventory.append(item)
                print(f"Transakcja zakończona pomyślnie!")
            else:
                print("Transakcja anulowana")
        else:
            print("Takiej rzeczy nie ma w twoim inventory")
    else:
        print("Masz pusty inventory! Do zobaczenia następnym razem")
    
def sell(inventory):
    amount = random.randint(2, 10)
    if len(inventory) >= 1:
        a = input(f'Co chcesz sprzedać? {inventory} ')
        if a in inventory:
            inp = input(f'Za {a} możesz otrzymać {amount} monet , czy zgadzasz sie na tą wymianę? ')
            if inp == "tak":
                inventory.remove(a)
                hero["monety"] += amount
                print(f"Transakcja zakończona pomyślnie!")
            else:
                print("Transakcja anulowana")
        else:
            print("Takiej rzeczy nie ma w twoim inventory")
    else:
        print("Masz pusty inventory! Do zobaczenia następnym razem")

def shopping(money, inventory ,items):
    price = random.randint(10, 50)
    print(f"Witaj w sklepie, tutaj możesz kupić różne rzeczy za monety. Obecnie masz {money} monet")
    time.sleep(1)
    inp = input(f'Asortyment sklepu: {items} . Co chcesz kupić? ')
    if inp in items:
        decision = input(f'{inp} kosztuje {price} monet, czy chcesz go kupić ')
        if money >= price:
            if decision == "tak":
                money -= price
                inventory.append(inp)
                items.remove(inp)
                print(f"Transakcja zakończona pomyślnie!")
            else:
                print("Transakcja anulowana")
        else:
            print("Nie masz wystarczającej ilości monet")
    else:
        print("Taka rzecz nie jest jeszcze sprzedawana w sklepie!")

def odbudowa(inventory, xp) -> bool:
    print("=="*70)
    print(f"Znalazłeś zniszczony portal! Żeby móc teleportować się do innego świata potrzebujesz obsydianu oraz krzesiwo!")
    if "obsydian" in inventory and "krzesiwo" in inventory:
        if xp >= 20 and "kamienny miecz" in inventory:
            inp = input("Czy chcesz odbudować portal? ")
            if inp == "tak":
                for el in inventory:
                    if el == "obsydian":
                        inventory.remove("obsydian")
                print("Portal odbudowany! Teraz możesz odkrywać inny świat po drugiej stronie portalu!")
                print("==="*50)
                return True
            print("Jak chcesz, jest to bardzo przydatna struktura w świecie!")
            return False
        print("Masz za mało doświadczenia!")
        return False
    print("Coś poszło nie tak i odchodzisz od portalu")
    return False

def walka_z_mobem(klasa, name, hp, loot, atk):
    print("=="*80)
    inp = input(f"Uważaj, biegnie do ciebie {name}, w - walka, u - ucieczka (szansa ucieczki 50%) ")
    mob = klasa(name, atk, hp, loot)
    if inp == "u":
        szansa = random.randint(1, 2)
        if szansa == 1:
            print("Nie udało się tobie uciec!")
            while hero["hp"] > 0 and mob.hp > 0:
                mob.bitwa()
            if mob.hp <= 0:
                a = random.randint(1, 6)
                hero["inventory"].append(mob.loot)
                hero["xp"] += a
                print(f"Udało ci się go pokonać! Zdobywasz {mob.loot} oraz {a} xp!")
        elif szansa == 2:
            print("Dzisiaj szczęście jest na twojej stronie! Udało ci się uciec!")
    elif inp == "w":
        while hero["hp"] > 0 and mob.hp > 0:
            mob.bitwa()
        if mob.hp <= 0:
            a = random.randint(1, 6)
            hero["inventory"].append(mob.loot)
            hero["xp"] += a
            print(f"Udało ci się go pokonać! Zdobywasz {mob.loot} oraz {a} xp!")
    else:
        print(f"Niepoprawna komenda, {mob.name} atakuje cię!")
        while hero["hp"] > 0 and mob.hp > 0:
            mob.bitwa()
        if mob.hp <= 0:
            a = random.randint(1, 6)
            hero["inventory"].append(mob.loot)
            hero["xp"] += a
            print(f"Udało ci się go pokonać! Zdobywasz {mob.loot} oraz {a} xp!")

def add_health(inventory):
    if "kurczak" in inventory or "wieprzowina" in inventory or "wołowina" in inventory or "wieprzowina" in inventory or "jabłko" in inventory or "tort" in inventory or "chleb" in inventory or "barszcz" in inventory or "jagoda" in inventory or "złote jabłko" in inventory or "mikstura zdrowia" in inventory:
        inp = input(f"Jakie jedzenie chcesz zjeść żeby się uleczyć? {inventory} ")
        if inp in inventory:
            if inp == "kurczak" or inp == "wieprzowina" or inp == "wołowina" or inp == "wieprzowina" or inp == "jabłko" or inp == "tort" or inp == "chleb" or inp == "barszcz" or inp == "jagoda" or inp == "złote jabłko" or inp == "mikstura zdrowia":
                inventory.remove(inp)
                hero["hp"] += random.randint(2, 6)
                print(f"Uleczyłeś się! Teraz twoje hp wynosi {hero['hp']}")
            else:
                print("Wprowadzona rzecz nie jest jedzeniem!")
        else:
            print("Takiego jedzenia nie ma w twoim inventory!")
    else:
        print("W twoim inventory nie ma żadnego jedzenia!")

def found_fortress(chance) -> bool:
    if chance == 1:
        print("=="*50)
        print("Udało ci się znalezć fortress!")
        print("=="*50)
        return True
    return False

def found_bastion(chance) -> bool:
    if chance == 1:
        print("=="*50)
        print("Udało ci się znalezć bastion!")
        print("=="*50)
        return True
    return False
