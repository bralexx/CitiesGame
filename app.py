from flask import Flask, jsonify, request, redirect


import flask
import json
import GameManager


app = Flask(__name__)
from Game import Game
#g = Game("test", ["1", "2", "3"], 'L')

next_step = "fnkldsflv;sd"
all_cities = json.load(open("config/world-cities_json.json", 'r'))
dictionary = {}
for city in all_cities:
    if city['name'][0] in dictionary:
        dictionary[city['name'][0]] += [{city['name'], city['country']}]
    else:
        dictionary.update({city['name'][0]:[{city['name'], city['country']}]})

all_steps = [[1, "name", "country"], [2, "name", "country"]]

@app.route('/')
def start_game():
    return flask.render_template('game.html', steps=all_steps, next_step=next_step)

# @app.route('/make_step', methods=['POST'])
# def make_step():
#     global all_steps, next_step
#     all_steps += [[len(all_steps) + 1, flask.request.form['next_step'], "country"]]
#     return redirect('/')
app.run()
