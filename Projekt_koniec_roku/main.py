from kod import statystyki
from kod import swiat
from kod.statystyki import hero
from kod import funkcje
import time

print("Każda historia zaczyna się od pojawienia się bohatera....")
time.sleep(2)
imie = input("Nazwij swojego bohatera ")
statystyki.hero['imie'] = imie
print(f"Znakomicie! Zatem {statystyki.hero['imie']} idz w świat!")

while statystyki.hero['hp'] > 0:
    if swiat.wioska_found and swiat.working_portal:
        czynnosc = input("Co chcesz zrobić? a - podróż, b - wgląd do inventory, c - wyświetl swoje statystyki, e - heal, d - odwiedź wioskę, p - portal ")
    elif swiat.wioska_found:
        czynnosc = input("Co chcesz zrobić? a - podróż, b - wgląd do inventory, c - wyświetl swoje statystyki, e - heal, d - odwiedź wioskę ")
    elif swiat.working_portal:
        czynnosc = input("Co chcesz zrobić? a - podróż, b - wgląd do inventory, c - wyświetl swoje statystyki, e - heal, p - portal ")
    else:
        czynnosc = input("Co chcesz zrobić? a - podróż, b - wgląd do inventory, c - wyświetl swoje statystyki ")
    if czynnosc == "a":
        kierunek = input("W jakim kierunku chcesz iść? Na p - północ, w - wschód, z - zachód czy po - południe? ")
        if kierunek == "p" or kierunek == "po" or kierunek == "w" or kierunek == "z":
            swiat.swiat()
        else:
            print("Wpisano niepoprawny kierunek")
                
    elif czynnosc == "b":
        if len(hero.get("inventory")) != 0:
            print(hero.get("inventory"))
        else:
            print("Wygląda na to że nic jeszcze nie masz!")
    elif czynnosc == "c":
        print("="*30)
        for k, v in hero.items():
            time.sleep(1)
            print(f"{k} ----- {v}")
    elif czynnosc == "e":
        funkcje.add_health(hero["inventory"])
    elif czynnosc == "d":
        if swiat.wioska_found == True and swiat.wioska is not None:
            swiat.wioska.use()
        else:
            print("Nie ma wioski do odwiedzenia.")
    elif czynnosc == "p":
        if swiat.working_portal == True and swiat.portal is not None:
            swiat.portal.functionable()
        else:
            print("Portal nie jest dostępny.")
    else:
        print("Wpisano niepoprawną komendę")
else:
    print("Nie zostało tobie życia, koniec gry!")
