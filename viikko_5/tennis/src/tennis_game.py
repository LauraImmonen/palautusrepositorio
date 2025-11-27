class TennisGame:
    score_names = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player_1_score = 0
        self.player_2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player_1_score += 1
        else:
            self.player_2_score += 1

    def get_score(self):
        if self.is_it_a_tie():
            return self.tie_score()
        elif self.is_it_advantage_or_win():
            return self.advantage_or_win_score()
        else:
            return self.regular_score()

    def is_it_a_tie(self):
        return self.player_1_score == self.player_2_score

    def tie_score(self):
        if self.player_1_score < 3:
            return f"{self.score_names[self.player_1_score]}-All"
        else:
            return "Deuce"

    def is_it_advantage_or_win(self):
        return self.player_1_score >= 4 or self.player_2_score >= 4

    def advantage_or_win_score(self):
        minus_result = self.player_1_score - self.player_2_score
        if minus_result == 1:
            if minus_result == 1:
                return f"Advantage {self.player1_name}"
        elif minus_result == -1:
            return f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def regular_score(self):
        return f"{self.score_names[self.player_1_score]}-{self.score_names[self.player_2_score]}"