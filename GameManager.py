import os
import json
import flask
from Game import Game

app = 0
game_list = []


def render_manager():
    game_list.clear()
    load_games_info()
    return flask.render_template('managerMenu.html', game_list=zip(range(len(game_list)), game_list))


def load_games_info(path=os.getcwd() + "/games"):
    global game_list
    game_list = []
    if os.path.exists(path):
        for file in os.listdir(path=path):
            try:
                game_config = json.load(open("games/" + file, 'r'))
                game_list.append([game_config['name'], game_config['status'], game_config['player_info'], "games/" + file])
            except (Exception):
                continue


def load_game(game_number):
    return Game.load_game(json.load(open(game_list[game_number][3])))


def create_game(name, players, start_letter):
    game = Game(name, players, start_letter)
    file = game.save_game()
    game_list.append([game.name, game.status, game.player_info, file])


def get_game(num_of_game):
    game = Game.load_game(json.load(open(game_list[num_of_game][3], 'r')))
    return game


def delete_game(num_of_game):
    os.remove(game_list[num_of_game][3])
    load_games_info()
