import flask
import json
import GameManager

app = flask.Flask(__name__)
GameManager.app = app

current_game = GameManager.Game


@app.route('/')
def start_manager():
    return GameManager.render_manager()


@app.route('/open_game_menu', methods=['POST'])
def open_game_menu():
    num_of_players = int(flask.request.form['num_of_players'])
    return flask.render_template('gameMenu.html', num_of_players=num_of_players)


@app.route('/create_new_game/<num_of_players>', methods=['POST'])
def create_new_game(num_of_players):
    players = []
    name = flask.request.form['game_name']
    for i in range(int(num_of_players)):
        x = flask.request.form['name{}'.format(i)]
        players.append(flask.request.form['name{}'.format(i)])
    first_letter = flask.request.form['letter']
    GameManager.create_game(name, players, first_letter)
    global current_game
    current_game = GameManager.get_game(len(GameManager.game_list) - 1)
    return current_game.render_game()


@app.route('/continue_game/<num_of_game>')
def continue_game(num_of_game):
    global current_game
    current_game = GameManager.load_game(int(num_of_game))
    return current_game.render_game()


@app.route('/delete_game/<num_of_game>')
def delete_game(num_of_game):
    GameManager.delete_game(int(num_of_game))
    return GameManager.render_manager()


@app.route('/save_current_game')
def save_current_game():
    current_game.save_game()
    return current_game.render_game()


@app.route('/save_exit_game')
def save_exit_game():
    current_game.save_game()
    return GameManager.render_manager()


@app.route('/exit_game')
def exit_game():
    return GameManager.render_manager()


@app.route('/make_step', methods=['POST'])
def make_step():
    global current_game
    step = flask.request.form['next_step']
    current_game.make_step(step)
    return current_game.render_game()


app.run()
