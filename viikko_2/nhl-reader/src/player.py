import requests

class Player:
    def __init__(self, data):
        self.name = data['name']
        self.team = data['team']
        self.goals = data['goals']
        self.assists = data['assists']
        self.nationality = data['nationality']

    def __str__(self):
        return f"{self.name:20} team {self.team} {self.goals} + {self.assists} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout = 10).json()

        players = []

        for player_data in response:
            player = Player(player_data)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):

        players = self.reader.get_players()
        nationality = nationality.upper()
        return [p for p in players if p.nationality.upper() == nationality]
