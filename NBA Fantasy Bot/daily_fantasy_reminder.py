# TO-DO
# 1. Hide passwords (look up useful packages) SEMI-DONE
# 2. Set as daily task DONE
# 3. Beautify email message
# 4. Handle no internet connection

##### START IMPORTS #####
# generic packages
import numpy as np
import pandas as pd
import datetime
import copy

# basketball package
from espn_api.basketball import League

# email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# settings
from settings import SWID, ESPN_S2, bot_email, bot_pass

##### END IMPORTS #####


#### START FUNCTIONS #####
def send_mail(to_mail, message, s):
    from_mail = bot_email
    #to_mail = 'tobyprofitt1@gmail.com'

    msg = MIMEMultipart()

    # setup the parameters of the message
    msg['From'] = from_mail
    msg['To'] = to_mail
    msg['Subject'] = message

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg

def send_outs(league, EMAILS, s):

    first_day = datetime.date(2021, 10, 19)
    today = datetime.date.today()
    diff = today - first_day
    gameday_id = diff.days
    todays_games = league._get_pro_schedule(gameday_id)

    for team in league.teams:
        message = 'Injury report for: ' + str(team)[5:-1] + '\n\n'
        TO_EMAIL = EMAILS[team.team_id]
        if TO_EMAIL != 0:
            for player in team.roster:
                team_name = player.proTeam
                team_id = PRO_TEAM_MAPPING[team_name]
                if team_id in todays_games.keys():
                    if player.injuryStatus != "ACTIVE":
                        extraMessage = ''
                        if player.lineupSlot not in ['BE', 'IR']:
                            extraMessage = '... Put them in your IR or bench if you can, they are playing today!'
                        message += str(player)[7:-1] + ' (' + str(player.lineupSlot) + ') is ' + str(player.injuryStatus) + extraMessage + '\n'
            message += '\nChange your team here https://fantasy.espn.com/basketball/team?leagueId=55416621&teamId=' + str(team.team_id)
            send_mail(TO_EMAIL, message, s)
#### END FUNCTIONS #####

def main():
    # CONSTANTS
    LEAGUE = 55416621
    YEAR = 2022

    league = League(league_id=LEAGUE, year=YEAR, espn_s2 = ESPN_S2, swid = SWID)
    Jack, Toby, Nick, Mish, Cam, Markey = league.teams

    # http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams
    global PRO_TEAM_MAPPING
    PRO_TEAM_MAPPING =  {'ATL':1, 'BOS':2, 'NOP':3, 'CHI':4, 'CLE':5, 'DAL':6, 'DEN':7, 'DET':8, 'GSW':9, 'HOU':10, 'IND':11, 'LAC':12, 'LAL':13, 'MIA':14, 'MIL':15, 
    'MIN':16, 'BKN':17, 'NYK':18, 'ORL':19, 'PHL':20, 'PHO':21, 'POR':22, 'SAC':23, 'SAS':24, 'OKC':25, 'UTA':26, 'WAS':27, 'TOR':28, 'MEM':29, 'CHA':30}
    PRO_TEAM_MAPPING_COPY = copy.copy(PRO_TEAM_MAPPING)
    for k, v in PRO_TEAM_MAPPING_COPY.items():
        PRO_TEAM_MAPPING[v] = k
    
    email_jack   = 0
    email_toby   = 'tobyprofitt1@gmail.com'
    email_cam    = 0
    email_nick   = 0
    email_markey = 0
    email_mish   = 0
    EMAILS = {Jack.team_id:email_jack, Toby.team_id:email_toby, Cam.team_id:email_cam, 
        Nick.team_id:email_nick, Markey.team_id:email_markey, Mish.team_id:email_mish}

    # Set up email connection
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(bot_email, bot_pass)

    send_outs(league, EMAILS, s)
    print('done')

if __name__ == "__main__":
    main()
