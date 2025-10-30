import unittest
from statistics_service import StatisticsService
from statistics_service import SortBy
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

    def test_top_by_points(self):
        top_players = self.stats.top(3, sort_by=SortBy.POINTS)
        self.assertEqual("Gretzky", top_players[0].name)
        self.assertEqual("Lemieux", top_players[1].name)
        self.assertEqual("Yzerman", top_players[2].name)

    def test_top_by_goals(self):
        top_players = self.stats.top(3, sort_by=SortBy.GOALS)
        self.assertEqual("Lemieux", top_players[0].name)
        self.assertEqual("Yzerman", top_players[1].name)
        self.assertEqual("Kurri", top_players[2].name)

    def test_by_assists(self):
        top_players = self.stats.top(3, sort_by=SortBy.ASSISTS)
        self.assertEqual("Gretzky", top_players[0].name)
        self.assertEqual("Yzerman", top_players[1].name)
        self.assertEqual("Lemieux", top_players[2].name)

    def test_by_default_points(self):
        top_players = self.stats.top(3)
        self.assertEqual("Gretzky", top_players[0].name)
        self.assertEqual("Lemieux", top_players[1].name)
        self.assertEqual("Yzerman", top_players[2].name)


