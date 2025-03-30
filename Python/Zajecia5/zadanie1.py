def dodajDoListy(lista):
    liczba = int(input("Podaj wynik: "))
    if len(lista) == 5:
        print("Lista jest pełna")
        min_val = minListy(lista)
        if liczba > min_val:
            lista.remove(min_val)
            lista.append(liczba)
    else:
        lista.append(liczba)
    return lista

def usunZListy(lista):
    while True:
        liczba = int(input("Podaj wynik: "))
        if liczba in lista:
            break
    lista.remove(liczba)
    return lista

def sortujListe(lista):
    lista.sort()
    return lista

def zwrocListe(lista):
    return lista

def minListy(lista):
    return min(lista)

def program():
    while True:
        polecenie = int(input("Podaj polecenie: 1-dodaj do listy, 2-usun z listy, 3-sortuj liste, 4-zwroc liste, 5-wyjdz: "))
        match polecenie:
            case 1:
                dodajDoListy(List)
            case 2:
                usunZListy(List)
            case 3:
                sortujListe(List)
                print("Lista posortowana:", List)
            case 4:
                print("Aktualna lista:", zwrocListe(List))
            case 5:
                print("Koniec programu.")
                break
            case _:
                print("Nieznane polecenie, spróbuj ponownie.")

List = []
if __name__ == '__main__':
    program()