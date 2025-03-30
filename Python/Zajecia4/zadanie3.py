def zadanie3 (nazwa_pliku,text):
    with open(nazwa_pliku, 'a') as plik:
        plik.write(text)


zadanie3('d:\\Studia\\Studies\\Python\\Zajecia4\\plik2.txt','\nHello World!')