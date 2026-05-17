import random
from kod.statystyki import hero
import time

def spawn_chance(klasa) -> list:
    szansa = random.randint(1, 3)
    if szansa == 2:
        ilosc = random.randint(1, 2)
        mobs = []
        for _ in range(ilosc):
            mob = klasa()
            mobs.append(mob)
        print(f"Spotkałeś {ilosc} {mob.name}")
        return mobs
    print("Nikogo nie spotkałeś!")
    return []


def polowanie(mobs, xp, loot, nazwa):
    if not mobs:
        print("Brak mobów do upolowania.")
        return
    wybor = input(f"Czy chcesz upolować {nazwa}? ")
    if wybor != "tak":
        return
    while mobs:
        time.sleep(1)
        print(f"Hp moba : {mobs[0].hp}, twój atak {hero['atk']}")
        mobs[0].hp -= hero["atk"]
        if mobs[0].hp <= 0:
            a = random.randint(1, 2)
            print(f"Zabiłeś {nazwa}! Zdobywasz {xp} xp i {a} {loot}")
            hero["xp"] += xp
            hero["inventory"].append(a*loot)
            mobs.pop(0)
