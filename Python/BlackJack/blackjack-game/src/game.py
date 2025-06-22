import random
import json
import os
from datetime import datetime
from player import Player
from dealer import Dealer

class Game:
    def __init__(self, player_name="Player", history_path="history.json"):
        self.deck = [10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 'q', 'q', 'q', 'q', 'k', 'k', 'k', 'k', 'j', 'j', 'j', 'j', 'a', 'a', 'a', 'a']
        self.player = Player()
        self.dealer = Dealer()
        self.player_name = player_name
        self.history_path = history_path
        self.balance = 100  # startowa waluta
        # Utwórz plik historii jeśli nie istnieje
        if not os.path.exists(self.history_path):
            with open(self.history_path, "w") as f:
                json.dump([], f)

    def deal_card(self):
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

    def calculate_score(self, hand):
        score = 0
        aces = hand.count('a')
        for card in hand:
            if card in ['k', 'q', 'j']:
                score += 10
            elif card == 'a':
                score += 11
            else:
                score += card
        while score > 21 and aces:
            score -= 10
            aces -= 1
        return score

    def save_history(self, player_score, dealer_score, winner, bet):
        with open(self.history_path, "r") as f:
            data = json.load(f)
        data.append({
            "player": self.player_name,
            "player_hand": self.player.hand,
            "player_score": player_score,
            "dealer_hand": self.dealer.hand,
            "dealer_score": dealer_score,
            "winner": winner,
            "bet": bet,
            "balance": self.balance,
            "datetime": datetime.now().isoformat()
        })
        with open(self.history_path, "w") as f:
            json.dump(data, f, indent=2)

    def show_history(self):
        try:
            with open(self.history_path, "r") as f:
                data = json.load(f)
            games = [g for g in data if g["player"] == self.player_name]
            if not games:
                print("Brak historii dla tego gracza.")
                return
            for i, g in enumerate(games, 1):
                print(f"\n--- Gra {i} ---")
                print(f"Data: {g['datetime']}")
                print(f"Ręka gracza: {g['player_hand']} (wynik: {g['player_score']})")
                print(f"Ręka krupiera: {g['dealer_hand']} (wynik: {g['dealer_score']})")
                print(f"Zakład: {g['bet']}")
                print(f"Saldo po grze: {g['balance']}")
                print(f"Zwycięzca: {g['winner']}")
        except Exception as e:
            print(f"Błąd odczytu historii: {e}")

    def show_stats(self):
        try:
            with open(self.history_path, "r") as f:
                data = json.load(f)
            games = [g for g in data if g["player"] == self.player_name]
            total = len(games)
            wins = sum(1 for g in games if g["winner"] == "player")
            losses = sum(1 for g in games if g["winner"] == "dealer")
            draws = sum(1 for g in games if g["winner"] == "draw")
            avg_player = sum(g["player_score"] for g in games) / total if total else 0
            avg_dealer = sum(g["dealer_score"] for g in games) / total if total else 0
            from collections import Counter
            win_scores = [g["player_score"] for g in games if g["winner"] == "player"]
            if win_scores:
                most_common = Counter(win_scores).most_common(1)[0][0]
                recommendation = f"Najczęściej wygrywasz przy {most_common} pkt."
            else:
                recommendation = "Brak wygranych do analizy."
            print(f"\nStatystyki gracza: {self.player_name}")
            print(f"Liczba rozgrywek: {total}")
            print(f"Wygrane: {wins}")
            print(f"Przegrane: {losses}")
            print(f"Remisy: {draws}")
            print(f"Średni wynik gracza: {round(avg_player,2)}")
            print(f"Średni wynik krupiera: {round(avg_dealer,2)}")
            print(f"Rekomendacja: {recommendation}")
        except Exception as e:
            print(f"Błąd analizy statystyk: {e}")

    def start_game(self):
        # Reset deck and hands
        self.deck = [10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 'q', 'q', 'q', 'q', 'k', 'k', 'k', 'k', 'j', 'j', 'j', 'j', 'a', 'a', 'a', 'a']
        self.player.hand = []
        self.dealer.hand = []

        print(f"\nYour balance: {self.balance}")
        while True:
            try:
                bet = int(input("Place your bet (min 1, max 100): "))
                if 1 <= bet <= min(self.balance, 100):
                    break
                else:
                    print("Invalid bet amount.")
            except ValueError:
                print("Please enter a valid number.")

        # Initial dealing
        for _ in range(2):
            self.player.add_card(self.deal_card())
            self.dealer.add_card(self.deal_card())

        print(f"Your hand: {self.player.hand}, current score: {self.calculate_score(self.player.hand)}")
        print(f"Dealer's first card: {self.dealer.hand[0]}")

        game_over = False
        player_bust = False

        while not game_over:
            action = input("Type 'hit' to get another card, 'stand' to pass: ").lower()
            if action == 'hit':
                self.player.add_card(self.deal_card())
                print(f"Your hand: {self.player.hand}, current score: {self.calculate_score(self.player.hand)}")
                if self.calculate_score(self.player.hand) > 21:
                    print("You went over. You lose!")
                    player_bust = True
                    game_over = True
            elif action == 'stand':
                game_over = True

        while self.calculate_score(self.dealer.hand) < 17:
            self.dealer.add_card(self.deal_card())

        print(f"Dealer's hand: {self.dealer.hand}, dealer's score: {self.calculate_score(self.dealer.hand)}")

        player_score = self.calculate_score(self.player.hand)
        dealer_score = self.calculate_score(self.dealer.hand)

        if player_bust:
            winner = "dealer"
            self.balance -= bet
            print(f"You lost {bet}. New balance: {self.balance}")
        elif dealer_score > 21 or player_score > dealer_score:
            winner = "player"
            self.balance += bet
            print(f"You win {bet}! New balance: {self.balance}")
        elif player_score < dealer_score:
            winner = "dealer"
            self.balance -= bet
            print(f"You lost {bet}. New balance: {self.balance}")
        else:
            winner = "draw"
            print("It's a draw!")

        self.save_history(player_score, dealer_score, winner, bet)

    def ask_player_name(self):
        if self.player_name == "Player":
            name = input("Podaj swoje imię: ").strip()
            if name:
                self.player_name = name
                print(f"Witaj, {self.player_name}!")
            else:
                print("Używam domyślnej nazwy: Player")

    def menu(self):
        self.ask_player_name()
        while True:
            print("\n--- MENU ---")
            print("1. Nowa gra")
            print("2. Pokaż historię gier")
            print("3. Pokaż statystyki gracza")
            print("4. Wyjście")
            choice = input("Wybierz opcję: ")
            if choice == "1":
                self.start_game()
            elif choice == "2":
                self.show_history()
            elif choice == "3":
                self.show_stats()
            elif choice == "4":
                print("Do zobaczenia!")
                break
            else:
                print("Nieprawidłowy wybór!")