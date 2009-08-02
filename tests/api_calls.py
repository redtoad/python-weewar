import unittest
from weewar.api import *

class TestReadOnlyAPI(unittest.TestCase):
    
    """
    Test correct bahaviour of API calls.
    """
    
    BOGUS_USER_ID = '???'
    BOGUS_GAME_ID = '???'

    def test_missing_game(self):
        """
        Wrong user ID raises exception.
        """
        self.assertRaises(GameNotFound, game, self.BOGUS_GAME_ID)

    def test_missing_user(self):
        """
        Wrong user ID raises exception.
        """
        self.assertRaises(UserNotFound, user, self.BOGUS_USER_ID)


if __name__ == '__main__':
    unittest.main()

