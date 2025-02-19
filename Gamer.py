import unittest
from IGamer import *
from unittest.mock import patch

class TestGamer(unittest.TestCase):
    
    def test_createGamer(self):
        gam = Gamer();
        self.assertIsNotNone(Gamer);
        
    def test_return_getNumber(self):
        gam = Gamer();
        with patch('builtins.input', return_value="123"):
            self.assertEqual(['1', '2', '3'], gam.getNumber());
            
    def test_return_getAttempt(self):
        gam = Gamer();
        with patch('builtins.input', return_value="1"):
            self.assertEqual("1", gam.getAttempt());

# Игрок 
class Gamer(IGamer):
    def getNumber(self):
        # todo ограничение по символам
        return [char for char in input()];

    def getAttempt(self):
        # todo ограничение по символам
        return input();