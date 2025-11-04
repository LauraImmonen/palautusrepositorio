import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']

    def __str__(self):
          return f"{self.name:20} team {self.team} {self.goals} + {self.assists} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):

        players = self.reader.get_players()
        nationality = nationality

        filtered = [player for player in players if player.nationality == nationality]

        return filtered


