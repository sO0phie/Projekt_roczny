from kod import statystyki
import time

print("Każda historia zaczyna się od pojawienia się bohatera....")
time.sleep(2)
imie = input("Nazwij swojego bohatera ")
statystyki.hero['imie'] = imie
print(f"Znakomicie! Zatem {statystyki.hero['imie']} idz w świat!")

while statystyki.hero['hp'] > 0:
    kierunek = input("W jakim kierunku chcesz iść? Na p - północ, w - wschód, z - zachód czy po - południe? ")
    if kierunek == "p":
        statystyki.hero['Z'] += 1
    elif kierunek == "po":
        statystyki.hero['Z'] -= 1
    elif kierunek == "w":
        statystyki.hero['X'] -= 1
    elif kierunek == "z":
        statystyki.hero['X'] += 1
    else:
        print("Wpisano niepoprawny kierunek")