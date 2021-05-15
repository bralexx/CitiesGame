import json
import unittest
import requests
import GameManager
import Game

class TestGameManager(unittest.TestCase):
    def setUp(self):
        GameManager.load_games_info()

    def tearDown(self):
        pass

    def test_game_list(self):
        self.assertTrue(len(GameManager.game_list) >= 0)
        for game in GameManager.game_list:
            self.assertEqual(len(game), 4)

    def test_load_game(self):
        if len(GameManager.game_list) > 0:
            game = GameManager.load_game()
            self.assertIs(game, Game)

    def test_get_game(self):
        if len(GameManager.game_list) > 0:
            game = GameManager.get_game(0)
            self.assertIs(game, Game)

    def test_create_game(self):
        prevSize = len(GameManager.game_list)
        GameManager.create_game("name", ["1"], 'A')
        self.assertEqual(prevSize + 1, len(GameManager.game_list))
        game = GameManager.get_game(prevSize);
        self.assertEqual(game.name, "name")
        self.assertEqual(game.player_list, ["1"])
        self.assertEqual(game.current_letter, 'A')

    def test_delete_game(self):
        if len(GameManager.game_list) > 0:
            prevSize = len(GameManager.game_list)
            GameManager.delete_game(0)
            self.assertEqual(prevSize - 1, len(GameManager.game_list))


if __name__ == '__main__':
    unittest.main()