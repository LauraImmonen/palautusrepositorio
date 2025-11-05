from rich.table import Table
from rich.console import Console
from player import PlayerReader
from player import PlayerStats


def fetch_players():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    return stats.top_scorers_by_nationality("FIN")

def create_table(players):
    table = Table(title="Top Scorers by Nationality")

    table.add_column("Name", style="bold")
    table.add_column("Team")
    table.add_column("Goals")
    table.add_column("Assists")
    table.add_column("Total")

    for player in players:
        total = player.goals + player.assists
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(total),
        )

    return table

def main():
    console = Console()
    players = fetch_players()
    table = create_table(players)
    console.print(table)


if __name__ == "__main__":
    main()
