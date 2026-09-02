""" Main app for the Athletes module. It creates teams, athletes, and simulates a game between them."""
from Game import Game
from Team import Team
from Sport import Sport
from Athlete import Athlete
import json
from itertools import combinations

def load_json_file(file_path):
    """ Loads a JSON file and returns the data as a Python object."""
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
    return data

def convert_json_to_teams(json_data):
    """ Converts JSON data into a list of Team objects."""
    teams = []
    for team_data in json_data:
        team_name = team_data['name']
        sport_name = team_data['sport']['name']
        sport_league = team_data['sport']['league']
        sport_num_players = team_data['sport']['num_players']
        print(team_name, sport_name, sport_league, sport_num_players)
        
        sport = Sport(sport_name, sport_league, sport_num_players)
        team = Team(team_name, sport)
        
        for athlete_data in team_data['athletes']:
            athlete_name = athlete_data['name']
            athlete_number = athlete_data['number']
            # Se eliminó sport_name ya que sport ya contiene esa información
            athlete = Athlete(athlete_name, athlete_number, sport)
            team.add_athlete(athlete)
            
        teams.append(team)
    return teams

def main():
    """ Main function to create teams, athletes, and simulate a game."""
    tournament_data = load_json_file('C:/Users/irvin/OneDrive/Documentos/Curso_DS4_2026/Athlete/tournament.json')
    print("Tournament:", tournament_data)
    teams = convert_json_to_teams(tournament_data)
    
    # Generar las combinaciones de equipos para los partidos
    team_combinations = list(combinations(teams, 2))
    
    for local, visitor in team_combinations:
        print(f"Match {local.name} vs {visitor.name}")
        game = Game(local, visitor)
        game.play()
        game.display()
        print("\n")

if __name__ == "__main__":
    main()