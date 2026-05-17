from kod import statystyki
from kod import swiat
from kod.statystyki import hero
import time

print("Każda historia zaczyna się od pojawienia się bohatera....")
time.sleep(2)
imie = input("Nazwij swojego bohatera ")
statystyki.hero['imie'] = imie
print(f"Znakomicie! Zatem {statystyki.hero['imie']} idz w świat!")

while statystyki.hero['hp'] > 0:
    if len(hero.get("inventory")) != 0:
        inp = input("Czy chcesz otworzyć swój inventory? ")
        if inp == "tak":
            print(hero.get("inventory"))
    kierunek = input("W jakim kierunku chcesz iść? Na p - północ, w - wschód, z - zachód czy po - południe? ")
    if kierunek == "p":
        statystyki.hero['Z'] += 1
        swiat.swiat()
    elif kierunek == "po":
        statystyki.hero['Z'] -= 1
        swiat.swiat()
    elif kierunek == "w":
        statystyki.hero['X'] -= 1
        swiat.swiat()
    elif kierunek == "z":
        statystyki.hero['X'] += 1
        swiat.swiat()
    else:
        print("Wpisano niepoprawny kierunek")
else:
    print("Nie zostało tobie życia, koniec gry!")
