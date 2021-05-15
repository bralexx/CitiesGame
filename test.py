import app
import json
import unittest


class TestGame(unittest.TestCase):
    def setUp(self):
        app.app.run()

    def tearDown(self):
        pass

    def test_get_json(self):
        data = app.app.test_request_context('/get_json', method='GET')
        self.assertEqual(data['numberOfGames'], 0)
        


if __name__ == '__main__':
    unittest.main()