class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            if isinstance(card, int):
                score += card
            elif card in ['j', 'q', 'k']:
                score += 10
            elif card == 'a':
                aces += 1

        for _ in range(aces):
            if score + 11 > 21:
                score += 1
            else:
                score += 11

        return score

    def reset_hand(self):
        self.hand = []