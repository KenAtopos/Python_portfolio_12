import requests
import pandas as pd

# Define the API endpoint URL
url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2021-22&SeasonType=Regular+Season&StatCategory=PTS"

# Define the headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://stats.nba.com/",
    "Accept": "application/json, text/plain, */*",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true",
}

# Send a GET request to the API endpoint
response = requests.get(url, headers=headers)

# Parse the JSON response
data = response.json()

# Extract the player stats
headers = data["resultSet"]["headers"]
rows = data["resultSet"]["rowSet"]
df = pd.DataFrame(rows, columns=headers)

# Save the player stats to a CSV file
df.to_csv("nba_player_stats.csv", index=False)
