import random
class Dealer:
    def __init__(self):
        self.hand = []
        self.deck = self.create_deck()

    def add_card(self, card):
        self.hand.append(card)
    def create_deck(self):
        deck = [10, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 'q', 'q', 'q', 'q', 'k', 'k', 'k', 'k', 'j', 'j', 'j', 'j', 'a', 'a', 'a', 'a']
        random.shuffle(deck)
        return deck

    def hit(self):
        card = self.deck.pop()
        self.hand.append(card)

    def show_hand(self):
        return self.hand



    def calculate_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            if isinstance(card, int):
                score += card
            elif card in ['q', 'k', 'j']:
                score += 10
            elif card == 'a':
                aces += 1

        for _ in range(aces):
            if score + 11 > 21:
                score += 1
            else:
                score += 11

        return score

    def play(self):
        while self.calculate_score() < 17:
            self.hit()