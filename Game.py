import json


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
            self.player_info.update({player:[0, "in game"]})
        self.current_letter = start_letter
        self.current_player = 0
        all_cities = json.load(open("config/world-cities_json.json", 'r'))
        self.possible_dictionary = {}
        for city in all_cities:
            self.possible_dictionary.update({city['name']:city['country']})

    def __init__(self, data):
        self.name = data['name']
        self.status = data['status']
        self.used_cities = data['used_cities']
        self.step_list = data['step_list']
        self.player_info = data['player_info']
        self.player_list = data['player_list']
        self.current_letter = data['current_letter']
        self.current_player = data['current_player']

    def is_step_possible(self, city_name):
        if city_name not in self.used_cities and city_name in self.possible_dictionary and \
                city_name[0].lower() == self.current_letter:
            return True
        return False

    def make_step(self, city):
        if self.is_step_possible(city):
            self.step_list.append([True, self.player_list[self.current_player], city, self.possible_dictionary[city]])
            self.used_cities.append(city)
            self.player_info[self.player_list[self.current_player]][0] += 1
            self.current_player += 1
            self.current_letter = city[len(city) - 1]
        else:
            if city in self.used_cities:
                result = "This city has been already said, {} lost".format(self.player_list[self.current_player])
            elif not city[0].lower() == self.current_letter:
                result = "Wrong letter, {} lost".format(self.player_list[self.current_player])
            else:
                result = "This city doesn't exist, {} lost".format(self.player_list[self.current_player])
            self.step_list.append([False, self.player_list[self.current_player], result])
            self.player_info[self.player_list[self.current_player]][1] = "lost on step {}".format(len(self.step_list) + 1)
            self.player_list.pop(self.current_player)
        self.current_player %= len(self.player_list)
        self.win_condition()

    def win_condition(self):
        if len(self.player_list) == 1:
            self.status = "ended, winner is {}".format(self.player_list[0])

    def save_game(self):
        data = {}
        data.update({'name':self.name,
                     'status':self.status,
                     'used_cities':self.used_cities,
                     'step_list':self.step_list,
                     'player_info':self.player_info,
                     'player_list':self.player_list,
                     'current_letter':self.current_letter,
                     'current_player':self.current_player,
                     })
        file = open("games/{}.json".format(self.name), 'w')
        json.dumps(data, file)

