import random
from kod.statystyki import hero
import time

def spawn_chance(klasa) -> list:
    szansa = random.randint(1, 3)
    if szansa == 2:
        mobs = []
        mob = klasa()
        mobs.append(mob)
        print(f"Spotkałeś {mob.name}")
        return mobs
    return []


def polowanie(mobs, xp, loot, nazwa):
    wybor = input(f"Czy chcesz upolować {nazwa}? ")
    if wybor != "tak":
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

def odbudowa(inventory) -> bool:
    print(f"Znalazłeś zniszczony portal! Żeby móc teleportować się do innego świata potrzebujesz obsydianu oraz krzesiwo!")
    if "obsydian" in inventory and "krzesiwo" in inventory:
        inp = input("Czy chcesz odbudować portal? ")
        if inp == "tak":
            for el in inventory:
                if el == "obsydian":
                    inventory.remove("obsydian")
            print("Portal odbudowany! Teraz możesz odkrywać inny świat po drugiej stronie portalu!")
            return True
    print("Coś poszło nie tak i odchodzisz od portalu")
    return False

def if_miecz(required_xp, in_inventory) -> bool:
    if hero["xp"] < required_xp:
        print("Masz za mało xp!")
        return False
    elif in_inventory in hero["inventory"]:
        print("Masz już ten miecz!")
        return False
    else:
        return True
        
