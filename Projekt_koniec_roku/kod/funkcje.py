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
        
