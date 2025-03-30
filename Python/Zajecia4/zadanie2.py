def zadanie2(nazwa_pliku):
    if ".bat" in nazwa_pliku or ".txt" in nazwa_pliku or ".csv" in nazwa_pliku or ".bin" in nazwa_pliku:
        with open(nazwa_pliku, 'r') as plik:
            linie = plik.readlines()
        return linie
    else:
        print('Nie poprawne rozszerzenie pliku')
    
if __name__ == "__main__":
    print(zadanie2("zadanie1.bin"))