def hit(deck, hand):
    card = deck.pop()
    hand.append(card)
    return card

def calculate_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        if card in ['k', 'q', 'j']:
            score += 10
        elif card == 'a':
            ace_count += 1
            score += 11  # Initially count Ace as 11
        else:
            score += card  # For numbered cards
    # Adjust for Aces if score exceeds 21
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score

def save_results(results):
    with open('results.txt', 'a') as file:
        file.write(results + '\n')