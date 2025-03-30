def zadanie5():
    czyPrawda = True
    while czyPrawda:
        number = int(input('Podaj liczbe: '))
        if number == 0:
            print('Koniec')
            czyPrawda = False
        else:
            if number % 2 == 0:
                print('Liczba jest parzysta')
                with open('even.txt', 'a') as plik:
                    plik.write(str(number) + '\n')
            else:
                print('Liczba jest nieparzysta')
                with open('odd.txt', 'a') as plik:
                    plik.write(str(number) + '\n')

if __name__ == '__main__':
    zadanie5()