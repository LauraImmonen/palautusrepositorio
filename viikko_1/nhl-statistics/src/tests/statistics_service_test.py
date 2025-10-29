import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing_player(self):
        player = self.stats.search("Semenko")
        self.assertEqual("Semenko", player.name)

    def test_search_nonexisting_player(self):
        player = self.stats.search("Nobody")
        self.assertIsNone(player)

    def test_team(self):
        team_name = "EDM"
        players = self.stats.team(team_name)
        self.assertEqual(3, len(players))

    def test_top(self):
        top_players = self.stats.top(3)
        self.assertEqual(3, len(top_players))


