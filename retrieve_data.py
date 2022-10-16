# import libraries
from nba_api.stats.endpoints import shotchartdetail as scd, leaguegamelog as lgl, boxscoreadvancedv2 as bsa, playercareerstats as pcs
from nba_api.stats.static import teams, players
import time

# define global filter parameters
nba_league_id = "00"
season_id = "2015-16"
season_type = "Regular Season"
context_measure = "FGA"

"""
# get team data
full_team_list = teams.get_teams()

# extract id and team name only
team_list = []
for team in full_team_list:
    team_list.append({"id": team["id"], "full_name": team["full_name"]})

# get player data
full_player_list = players.get_players()

# extract id and player name only
player_list = []
for player in full_player_list:
    player_list.append({"id": player["id"], "full_name": player["full_name"]})

# define player and team to be searched for
search_player_list = ["James Harden", "Anthony Davis", "LeBron James", "Kevin Durant", "Stephen Curry", "Russell Westbrook", "Blake Griffin", "Kawhi Leonard", "Rudy Gobert", "Danny Green"]
search_player_ids = []
search_team_list = ["Houston Rockets", "New Orleans Pelicans", "Cleveland Cavaliers", "Oklahoma City Thunder", "Golden State Warriors", "Oklahoma City Thunder", "Los Angeles Clippers", "San Antonio Spurs", "Utah Jazz", "San Antonio Spurs"]
search_team_ids = []

# extract ids of players
for player_name in search_player_list:
    search_player = list(filter(lambda player: player["full_name"] == player_name, player_list))
    search_player_ids.append(search_player[0]["id"])

# extract ids of teams
for team_name in search_team_list:
    search_team = list(filter(lambda team: team["full_name"] == team_name, team_list))
    search_team_ids.append(search_team[0]["id"])

for idx, (search_player_id, search_team_id) in enumerate(zip(search_player_ids, search_team_ids)):
    if idx == 0:
        shot_chart = scd.ShotChartDetail(team_id = search_team_id, player_id = search_player_id, context_measure_simple = context_measure, season_nullable = season_id, season_type_all_star = season_type)
        sc_content = shot_chart.shot_chart_detail.get_data_frame()
        sc_content.to_csv('shotchartdetail.csv', index = False)
    else:
        shot_chart = scd.ShotChartDetail(team_id = search_team_id, player_id = search_player_id, context_measure_simple = context_measure, season_nullable = season_id, season_type_all_star = season_type)
        sc_content = shot_chart.shot_chart_detail.get_data_frame()
        sc_content.to_csv('shotchartdetail.csv', mode = 'a', index = False, header = False)

# get game data
league_games = lgl.LeagueGameLog(season = season_id, season_type_all_star = season_type)
lg_content = league_games.league_game_log.get_data_frame()
lg_content.to_csv('leaguegames.csv')


# get box score data
league_games = lgl.LeagueGameLog(season = season_id, season_type_all_star = season_type)
lg_content = league_games.league_game_log.get_data_frame()
lg_content = lg_content.loc[:,"GAME_ID"]
lg_content = lg_content.values.tolist()

for idx, search_game_id in enumerate(lg_content):
    if idx == 0:
        box_score = bsa.BoxScoreAdvancedV2(game_id = search_game_id)
        bs_content = box_score.team_stats.get_data_frame()
        bs_content.to_csv('boxscore.csv', index = False)
        time.sleep(1)
    elif (idx % 2) == 0:
        box_score = bsa.BoxScoreAdvancedV2(game_id = search_game_id)
        bs_content = box_score.team_stats.get_data_frame()
        bs_content.to_csv('boxscore.csv', mode = 'a', index = False, header = False)
        time.sleep(1)

# get player stats
for idx, search_player_id in enumerate(search_player_ids):
    if idx == 0:
        player_stats = pcs.PlayerCareerStats(player_id = search_player_id)
        ps_content = player_stats.season_totals_regular_season.get_data_frame()
        ps_content.to_csv('player_stats.csv', index = False)
    else:
        player_stats = pcs.PlayerCareerStats(player_id = search_player_id)
        ps_content = player_stats.season_totals_regular_season.get_data_frame()
        ps_content.to_csv('player_stats.csv', mode = 'a', index = False, header = False)

"""

full_player_list = players.get_players()
print(len(full_player_list))