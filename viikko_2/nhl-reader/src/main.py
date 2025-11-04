from rich.table import Table
from rich.console import Console
import requests
from player import Player
from player import PlayerReader
from player import PlayerStats

def main():
    console = Console()
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    table = Table(title="Top Scorers by Nationality")

    table.add_column("Name", style="bold")
    table.add_column("Team")
    table.add_column("Goals")
    table.add_column("Assists")
    table.add_column("Total")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists)
        )

    console.print(table)


if __name__ == "__main__":
    main()
