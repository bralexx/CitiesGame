import unittest
import GameManager
import Game

class TestGameManager(unittest.TestCase):
    def setUp(self):
        GameManager.create_game("name", ["1", "2"], 'A')
        self.game = GameManager.get_game(len(GameManager.game_list)-1)

    def tearDown(self):
        GameManager.delete_game(len(GameManager.game_list)-1)

    def test_is_step_possible(self):
        self.assertFalse(self.game.is_step_possible("hvjsdkjld"))
        self.assertTrue(self.game.is_step_possible("Amsterdam"))
        self.assertFalse(self.game.is_step_possible("AmsterHamster"))
        self.assertFalse(self.game.is_step_possible("Moscow"))

    def test_make_step(self):
        self.game.make_step("Amsterdam")
        self.assertEqual(self.game.status, "in process")
        self.assertEqual(len(self.game.used_cities), 1)
        self.assertEqual(self.game.current_letter, 'M')
        self.assertEqual(self.game.current_player, 1)
        self.assertEqual(len(self.game.step_list), 1)

if __name__ == '__main__':
    unittest.main()