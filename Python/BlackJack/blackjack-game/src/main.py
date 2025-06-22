import random
from game import Game

def main():
    print("Welcome to Blackjack!")
    game = Game()  # możesz dodać player_name, history_path jeśli chcesz
    game.menu()    # <-- wywołaj menu zamiast start_game()

if __name__ == "__main__":
    main()