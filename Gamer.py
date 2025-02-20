from IGamer import IGamer;
from unittest.mock import patch;
import unittest;
import logging;

class Test_Gamer(unittest.TestCase):
    
    # Тест getHidden: считывание числа
    def test_return_getHidden(self):
        inp_vector = ["", " ", "123fgag", "1345,34", "1345.34", "1345"];
        with patch('builtins.input', side_effect = inp_vector):
            self.assertEqual(['1', '3', '4', '5'], Gamer.getHidden());
        logging.debug("Gamer.getHidden: считывание числа: успешно");
    
    # Тест getAttempt: считывание числа
    def test_return_getAttempt(self):
        inp_vector = ["", " ", "123fgag", "1345,34", "1345.34", "1345", "5"];
        with patch('builtins.input', side_effect = inp_vector):
            self.assertEqual('5', Gamer.getAttempt());
        logging.debug("Gamer.getAttempt: считывание числа: успешно");


class Gamer(IGamer):
    
    # Загадывание числа
    def getHidden():
        while True: 
            num_hid = input(" Загадайте число: ");            
            try:
                int(num_hid);            
                return [char_num for char_num in num_hid];
            except ValueError:
                pass
        
        
    # Попытка отгадать цифру
    def getAttempt():
        while True:
            num_att = input(" Введите отгадку: ");
            try:
                int(num_att);
                if len(num_att) == 1:
                    return num_att;
            except ValueError:
                pass;