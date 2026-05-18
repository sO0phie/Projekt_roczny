from kod import statystyki
from kod import swiat
from kod.statystyki import hero
from kod.swiat import wioska_found
import time

print("Każda historia zaczyna się od pojawienia się bohatera....")
time.sleep(2)
imie = input("Nazwij swojego bohatera ")
statystyki.hero['imie'] = imie
print(f"Znakomicie! Zatem {statystyki.hero['imie']} idz w świat!")

while statystyki.hero['hp'] > 0:
    if wioska_found == True:
        czynnosc = input("Co chcesz zrobić? a - podróż, b - wgląd do inventory, c - wyświetl swoje statystyki, d - odwiedź wioskę ")
    else:
        czynnosc = input("Co chcesz zrobić? a - podróż, b - wgląd do inventory, c - wyświetl swoje statystyki ")
        if czynnosc == "a":
            if wioska_found == False:
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
else:
    print("Nie zostało tobie życia, koniec gry!")
    else:
        print("Wpisano niepoprawny kierunek")
else:
    print("Nie zostało tobie życia, koniec gry!")
