import random

def set_ships():
    """Losuje współrzędne 5 jednomasztowych statków i zwraca zbiór tych współrzędnych."""
    ships = set()
    while len(ships) < 5:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        ships.add((row, col))
    return ships
 
def print_board(board):
    """Wyświetla aktualny stan planszy."""
    print("\n  ", end="")
    for i in range(10):
        print(f" {i}", end="")
    print("\n")
    
    for i in range(10):
        print(f"{i} ", end="")
        for j in range(10):
            print(f" {board[i][j]}", end="")
        print()

def game():
    """Realizuje całą rozgrywkę aż do momentu zatopienia wszystkich statków."""
    # Inicjalizacja planszy
    board = [['.' for _ in range(10)] for _ in range(10)]
    ships = set_ships()
    moves = 0
    
    print("Witaj w grze w statki!")
    print("Zasady:")
    print(". - nieodkryte pole")
    print("X - trafiony statek")
    print("O - nietrafione pole")
    print("\nLokalizacje statków:")
    for ship in sorted(ships):
        print(f"Statek na pozycji: wiersz {ship[0]}, kolumna {ship[1]}")
    print("\nRozpoczynamy grę!")
    
    while ships:
        print_board(board)
        
        # Pobieranie współrzędnych od gracza
        while True:
            try:
                row = int(input("\nPodaj numer wiersza (0-9): "))
                col = int(input("Podaj numer kolumny (0-9): "))
                if 0 <= row <= 9 and 0 <= col <= 9:
                    if board[row][col] != '.':
                        print("To pole zostało już odkryte! Spróbuj ponownie.")
                        continue
                    break
                else:
                    print("Współrzędne muszą być z zakresu 0-9! Spróbuj ponownie.")
            except ValueError:
                print("Wprowadź poprawne liczby!")
        
        moves += 1
        
        # Sprawdzenie trafienia
        if (row, col) in ships:
            print("Trafiony!")
            board[row][col] = 'X'
            ships.remove((row, col))
            if not ships:
                print_board(board)
                print(f"\nGratulacje! Zatopiłeś wszystkie statki w {moves} ruchach!")
        else:
            print("Pudło!")
            board[row][col] = 'O'

if __name__ == "__main__":
    game()
