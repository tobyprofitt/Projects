# Imports
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from tqdm import tqdm
from datetime import datetime

# Get the data from the AFL website
def get_data_by_matchIDs(match_ids):
    dfs = []
    bad_match_ids = []
    for match_id in match_ids:
        try:
            print(match_id)
            url = f"https://www.footywire.com/afl/footy/ft_match_statistics?mid={match_id}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the table element with the match statistics
            match_stats_table = soup.find("table", {"id": "match-statistics-div"})
            if match_stats_table is None:
                print(f"No match statistics div found for match ID {match_id}")
                continue

            # Find the round number and year
            if match_id < 1840:
                year_round = soup.find('td', {"class": "lnorm", "height":"22"})
                round = year_round.text[0:year_round.text.find(',')]
                year = year_round.text[-4:]
            else:
                year_round = soup.find('td', {"class": "lnorm", "height":"22"})
                round = year_round.text[0:year_round.text.find(',')]
                year_round = soup.find('td', {"class": "lnorm", "height":"22"}).find_next('td', {"class": "lnorm", "height":"22"})
                year = year_round.text[-4:]

            if 'final' in round.lower():
                print(f"There is 'final' in this round: {round}")
                continue

            # Find the rows with player statistics
            player_stats_rows = match_stats_table.find_all("tr", {"class": ["darkcolor", "lightcolor"], "onmouseover": "this.className='highlightcolor';", "onmouseout": ["this.className='darkcolor';", "this.className='lightcolor';"]})
            first_team = soup.find("td", {"class": "innertbtitle", "align": "left"}).find("b").text
            first_team = first_team[:first_team.find("Match Statistics")].strip()
            second_team = soup.find("td", {"class": "innertbtitle", "align": "left"}).find_next("td", {"class": "innertbtitle", "align": "left"}).find("b").text
            second_team = second_team[:second_team.find("Match Statistics")].strip()

            if 'defeats' in soup.title.text.lower():
                winner = first_team
            else:
                winner = second_team

            # Extract the data from each row and create a pandas dataframe
            data = []
            for i, row in enumerate(player_stats_rows):
                team = first_team if i < len(player_stats_rows)/2 else second_team
                cols = row.find_all("td")
                cols = [col.text.strip() for col in cols]
                if len(cols) == 11:
                    result = 1 if team == winner else 0
                    new_row = [year, round, team, result] + cols
                    data.append(new_row)
                    columns=["Year", "Round", "Team Name", "Win", "Player", "K", "HB", "D", "M", "G", "B", "T", "HO", "FF", "FA"]
                elif len(cols) == 15:
                    result = 1 if team == winner else 0
                    new_row = [year, round, team, result] + cols
                    data.append(new_row)
                    columns=["Year", "Round", "Team Name", "Win", "Player", "K", "HB", "D", "M", "G", "B", "T", "HO", "GA", "I50", "FF", "FA", "AF", "SC"]
                elif len(cols) == 18:
                    result = 1 if team == winner else 0
                    new_row = [year, round, team, result] + cols
                    data.append(new_row)
                    columns=["Year", "Round", "Team Name", "Win", "Player", "K", "HB", "D", "M", "G", "B", "T", "HO", "GA", "I50", "CL", "CG", "R50", "FF", "FA", "AF", "SC"]

            if data:
                df = pd.DataFrame(data, columns=columns)
                df["Match ID"] = match_id   

                # Get Brownlow votes
                brownlow_votes = soup.find(string=re.compile("Brownlow Votes:"))
                if brownlow_votes:
                    votes = {}
                    for i in range(3):
                        player = brownlow_votes.find_next("a").text.strip()
                        player_parts = player.split(" ")
                        last_name = player_parts[-1]
                        first_initial = player_parts[0][0]
                        player_reversed = " ".join(player_parts[::-1])
                        votes[player_reversed] = 3-i
                        brownlow_votes = brownlow_votes.find_next("a")
                    df["Votes"] = df["Player"].apply(lambda x: votes.get(x.split()[-1] + ' ' + x.split()[0][0], 0))
                else:
                    df["Votes"] = 0

                dfs.append(df)
                print(f"Processed match ID {match_id}")
        except Exception as e:
            print(f"Error processing match ID {match_id}: {e}")
            bad_match_ids.append(match_id)

    # Concatenate all dataframes into a single one
    df_final = pd.concat(dfs)

    return df_final


if __name__ == "__main__":
    # if invalid_match_ids exists, read it in
    try:
        with open("invalid_match_ids.txt", "r") as f:
            invalid_match_ids = f.read().splitlines()
        df_final = get_data_by_matchIDs(invalid_match_ids)
        
    except: # do all matches
        first_game = 1
        last_game = 10741
        match_ids = range(first_game, last_game+1)
        df_final = get_data_by_matchIDs(match_ids)

    # save with timestamp
    df_final.to_csv("player_stats_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv", index=False)


