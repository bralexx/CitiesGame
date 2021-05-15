import json
import flask
import os


class Game:
    name = ""
    status = "in process"
    used_cities = []
    step_list = []
    player_info = {}
    player_list = []

    def __init__(self, name_, player_list_, start_letter):
        self.name = name_
        self.player_list = player_list_
        for player in player_list_:
            self.player_info.update({player: [0, "in game"]})
        self.current_letter = start_letter
        self.current_player = 0
        all_cities = json.load(open("cities/world-cities_json.json", 'r'))
        self.possible_dictionary = {}
        for city in all_cities:
            self.possible_dictionary.update({city['name']: city['country']})

    def load_game(data):
        new_game = Game(data['name'], data['player_list'], data['current_letter'])
        new_game.status = data['status']
        new_game.used_cities = data['used_cities']
        new_game.step_list = data['step_list']
        new_game.player_info = data['player_info']
        new_game.current_player = data['current_player']
        return new_game

    def is_step_possible(self, city_name):
        if city_name not in self.used_cities and city_name in self.possible_dictionary and \
                city_name[0].lower() == self.current_letter.lower():
            return True
        return False

    def make_step(self, city):
        if self.is_step_possible(city):
            self.step_list.append([True, self.player_list[self.current_player], city, self.possible_dictionary[city]])
            self.used_cities.append(city)
            self.player_info[self.player_list[self.current_player]][0] += 1
            self.current_player += 1
            self.current_letter = city[len(city) - 1].upper()
        else:
            if city in self.used_cities:
                result = "This city has been already said, {} lost".format(self.player_list[self.current_player])
            elif not city[0].lower() == self.current_letter.lower():
                result = "Wrong letter, {} lost".format(self.player_list[self.current_player])
            else:
                result = "This city doesn't exist, {} lost".format(self.player_list[self.current_player])
            self.step_list.append([False, self.player_list[self.current_player], result])
            self.player_info[self.player_list[self.current_player]][1] = "lost on step {}".format(len(self.step_list))
            self.player_list.pop(self.current_player)
        self.current_player %= len(self.player_list)
        self.win_condition()

    def win_condition(self):
        if len(self.player_list) == 1:
            self.status = "ended, winner is {}".format(self.player_list[0])
            self.step_list.append([False, self.player_list[0], "{} is winner!".format(self.player_list[0])])

    def save_game(self):
        data = {}
        data.update({'name': self.name,
                     'status': self.status,
                     'used_cities': self.used_cities,
                     'step_list': self.step_list,
                     'player_info': self.player_info,
                     'player_list': self.player_list,
                     'current_letter': self.current_letter,
                     'current_player': self.current_player,
                     })
        if not os.path.exists("games/"):
            os.mkdir("games/")
        file = open("games/{}.json".format(self.name), 'w')
        data = json.dumps(data)
        file.write(data)
        return file.name

    def render_game(self):
        players_ = []
        for player in self.player_info:
            if self.player_info[player][1] == "in game":
                players_.append([player, "made {} moves and still in game".format(self.player_info[player][0])])
            else:
                players_.append([player, self.player_info[player][1]])

        return flask.render_template("game.html",
                                     game_name=self.name,
                                     steps=zip(range(len(self.step_list)), self.step_list),
                                     current_player=self.player_list[self.current_player],
                                     current_letter=self.current_letter,
                                     status=self.status,
                                     players=players_)
