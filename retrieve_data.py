from nba_api.stats.endpoints import shotchartdetail as scd
from nba_api.stats.static import teams
from nba_api.stats.static import players
import pandas

# define global filter parameters
nba_league_id = "00"
season_id = "2015-16"
season_type = "Regular Season"

full_team_list = teams.get_teams()
team_list = []
for team in full_team_list:
    team_list.append({"id": team["id"], "full_name": team["full_name"]})

search_team = list(filter(lambda team: team["full_name"] == "Houston Rockets", team_list))
search_team_id = search_team[0]["id"]

full_player_list = players.get_players()
player_list = []
for player in full_player_list:
    player_list.append({"id": player["id"], "full_name": player["full_name"]})

search_player = list(filter(lambda player: player["full_name"] == "James Harden", player_list))
search_player_id = search_player[0]["id"]

shot_chart = scd.ShotChartDetail(team_id = search_team_id, player_id = search_player_id, context_measure_simple = "FGA", season_nullable = season_id, season_type_all_star = season_type)
sc_content = shot_chart.shot_chart_detail.get_data_frame()
sc_content.to_csv('shotchartdetail.csv')