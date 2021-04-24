import os
import json
from app import app
import Game


class GameManager:
    game_list = []
    def __init__(self):
        self.load_games_info(os.getcwd() + "/games")

    @app.route('/make_step', methods=['POST'])
    def load_games_info(self, path):
        for file in os.listdir(path=path):
            game_config = json.load(open('/'.join([path, file]), 'r'))
            self.game_list.append([game_config['name'], game_config['status'], game_config['player_info']])