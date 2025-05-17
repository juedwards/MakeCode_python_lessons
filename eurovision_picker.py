import random
import math

# Eurovision entries
eurovision_entries = [
    "🇳🇴 Norway | Kyle Alessandro – Lighter",
    "🇱🇺 Luxembourg | Laura Thorn – La Poupée Monte Le Son",
    "🇪🇪 Estonia | Tommy Cash – Espresso Macchiato",
    "🇮🇱 Israel | Yuval Raphael – New Day Will Rise",
    "🇱🇹 Lithuania | Katarsis – Tavo Akys",
    "🇪🇸 Spain | Melody – ESA DIVA",
    "🇺🇦 Ukraine | Ziferblat – Bird of Pray",
    "🇬🇧 United Kingdom | Remember Monday – What The Hell Just Happened?",
    "🇦🇹 Austria | JJ – Wasted Love",
    "🇮🇸 Iceland | VÆB – RÓA",
    "🇱🇻 Latvia | Tautumeitas – Bur Man Laimi",
    "🇳🇱 Netherlands | Claude – C’est La Vie",
    "🇫🇮 Finland | Erika Vikman – ICH KOMME",
    "🇮🇹 Italy | Lucio Corsi | Volevo Essere Un Duro",
    "🇵🇱 Poland | Justyna Steczkowska – GAJA",
    "🇩🇪 Germany | Abor & Tynna – Baller",
    "🇬🇷 Greece | Klavdia – Asteromáta",
    "🇦🇲 Armenia | PARG – SURVIVOR",
    "🇨🇭 Switzerland | Zoë Më – Voyage",
    "🇲🇹 Malta | Miriana Conte – SERVING",
    "🇵🇹 Portugal | NAPA – Deslocado",
    "🇩🇰 Denmark | Sissal – Hallucination",
    "🇸🇪 Sweden | KAJ – Bara Bada Bastu",
    "🇫🇷 France | Louane – maman",
    "🇸🇲 San Marino | Gabry Ponte – Tutta L’Italia",
    "🇦🇱 Albania | Shkodra Elektronike – Zjerm"
]

def main():
    print("Welcome to Eurovision Entry Picker!")
    names_input = input("Enter player names separated by commas: ")
    players = [name.strip() for name in names_input.split(",") if name.strip()]

    if not players:
        print("No players entered!")
        return

    # Shuffle entries and assign in round-robin fashion
    random.shuffle(eurovision_entries)
    assignments = {player: [] for player in players}

    for i, entry in enumerate(eurovision_entries):
        player = players[i % len(players)]
        assignments[player].append(entry)

    print("\nAssignments:")
    for player, entries in assignments.items():
        print(f"\n{player} gets:")
        for entry in entries:
            print(f"  - {entry}")

if __name__ == "__main__":
    main()