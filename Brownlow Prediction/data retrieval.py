from bs4 import BeautifulSoup
import pandas as pd
import requests

dfs = []
for match_id in range(1245, 10751):
    print(match_id)
    url = f"https://www.footywire.com/afl/footy/ft_match_statistics?mid={match_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table element with the match statistics
    match_stats_table = soup.find("table", {"id": "match-statistics-div"})
    if match_stats_table is None:
        print(f"No match statistics div found for match ID {match_id}")
        continue

    # Find the rows with player statistics
    player_stats_rows = match_stats_table.find_all("tr", {"class": ["lightcolour", "darkcolour"]})
    print(player_stats_rows)

    # Extract the data from each row and create a pandas dataframe
    data = []
    for row in player_stats_rows:
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        if len(cols) == 11:
            data.append(cols)

    if data:
        df = pd.DataFrame(data, columns=["Player", "K", "HB", "D", "M", "G", "B", "T", "HO", "FF", "FA"])
        df["Match ID"] = match_id
        print(df.head(2))
        dfs.append(df)
        print(f"Processed match ID {match_id}")

# Concatenate all dataframes into a single one
df_final = pd.concat(dfs)

# Save the data to a CSV file
df_final.to_csv("player_stats.csv", index=False)
