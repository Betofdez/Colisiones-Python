import random

class Territory:
    def __init__(self, name):
        self.name = name
        self.owner = None
        self.armies = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.territories = []

class Game:
    def __init__(self, players, territories):
        self.players = [Player(name) for name in players]
        self.territories = [Territory(name) for name in territories]

    def assign_territories(self):
        random.shuffle(self.territories)
        for i, territory in enumerate(self.territories):
            player = self.players[i % len(self.players)]
            player.territories.append(territory)
            territory.owner = player

    def display_board(self):
        for player in self.players:
            print(f"{player.name}'s territories:")
            for territory in player.territories:
                print(f"{territory.name} (Armies: {territory.armies})")
            print()

if __name__ == "__main__":
    players = ["Player 1", "Player 2"]
    territories = ["Territory 1", "Territory 2", "Territory 3", "Territory 4"]

    risk_game = Game(players, territories)
    risk_game.assign_territories()
    risk_game.display_board()
