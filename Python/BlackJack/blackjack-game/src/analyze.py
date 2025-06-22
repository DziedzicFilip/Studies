import json
import argparse
from collections import Counter, defaultdict

def load_history(path):
    with open(path, "r") as f:
        return json.load(f)

def analyze(history, player=None, ignore=None):
    games = [g for g in history if (not player or g["player"] == player)]
    if ignore:
        games = [g for g in games if g["winner"] not in ignore]

    total = len(games)
    wins = sum(1 for g in games if g["winner"] == "player")
    losses = sum(1 for g in games if g["winner"] == "dealer")
    draws = sum(1 for g in games if g["winner"] == "draw")
    avg_player = sum(g["player_score"] for g in games) / total if total else 0
    avg_dealer = sum(g["dealer_score"] for g in games) / total if total else 0

    # Najczęstsze wygrywające wyniki
    win_scores = [g["player_score"] for g in games if g["winner"] == "player"]
    if win_scores:
        most_common = Counter(win_scores).most_common(1)[0][0]
        recommendation = f"Najczęściej wygrywasz przy {most_common} pkt."
    else:
        recommendation = "Brak wygranych do analizy."

    stats = {
        "gracz": player or "wszyscy",
        "liczba_rozgrywek": total,
        "wygrane": wins,
        "przegrane": losses,
        "remisy": draws,
        "średni_wynik_gracza": round(avg_player, 2),
        "średni_wynik_krupiera": round(avg_dealer, 2),
        "rekomendacja": recommendation
    }
    return stats

def compare_players(history):
    players = set(g["player"] for g in history)
    results = {}
    for p in players:
        results[p] = analyze(history, player=p)
    return results

def list_players(history):
    return sorted(set(g["player"] for g in history))

def show_history(history, player=None):
    games = [g for g in history if (not player or g["player"] == player)]
    for i, g in enumerate(games, 1):
        print(f"\n--- Gra {i} ---")
        print(f"Data: {g['datetime']}")
        print(f"Gracz: {g['player']}")
        print(f"Ręka gracza: {g['player_hand']} (wynik: {g['player_score']})")
        print(f"Ręka krupiera: {g['dealer_hand']} (wynik: {g['dealer_score']})")
        print(f"Zakład: {g['bet']}")
        print(f"Saldo po grze: {g['balance']}")
        print(f"Zwycięzca: {g['winner']}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="history.json", help="Ścieżka do pliku historii")
    parser.add_argument("--player", help="Imię gracza do analizy")
    parser.add_argument("--ignore", nargs="*", help="Wyklucz wyniki (np. draw)")
    parser.add_argument("--compare", action="store_true", help="Porównaj wszystkich graczy")
    parser.add_argument("--output", default="statystyki.json", help="Zapisz statystyki do pliku")
    parser.add_argument("--show-history", action="store_true", help="Pokaż historię rozgrywek gracza")
    parser.add_argument("--list-players", action="store_true", help="Wyświetl listę wszystkich graczy")
    args = parser.parse_args()

    history = load_history(args.input)
    if args.list_players:
        players = list_players(history)
        print("Dostępni gracze:")
        for p in players:
            print(f"- {p}")
        return
    if args.show_history:
        show_history(history, player=args.player)
        return
    if args.compare:
        stats = compare_players(history)
    else:
        stats = analyze(history, player=args.player, ignore=args.ignore)

    print(json.dumps(stats, indent=2, ensure_ascii=False))
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()