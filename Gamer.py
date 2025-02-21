from IGamer import IGamer;
from unittest.mock import patch;
import unittest;
import logging;

class Test_Gamer(unittest.TestCase):
    
    # Тест getHidden: считывание числа
    def test_return_getNumber(self):
        inp_vector = ["", " ", "123fgag", "1345,34", "1345.34", "1345"];
        with patch('builtins.input', side_effect = inp_vector):
            self.assertEqual(['1', '3', '4', '5'], Gamer.getNumber());
        logging.debug("Gamer.getNumber: считывание числа: успешно");
    
    # Тест getAttempt: считывание числа
    def test_return_getOneNumber(self):
        inp_vector = ["", " ", "123fgag", "1345,34", "1345.34", "1345", "5"];
        with patch('builtins.input', side_effect = inp_vector):
            self.assertEqual('5', Gamer.getOneNumber());
        logging.debug("Gamer.getOneNumber: считывание числа: успешно");


class Gamer(IGamer):
    
    # Загадывание числа
    def getNumber(msg = "", err_msg = "", end_chr = ""):
        while True: 
            num_hid = input(msg);            
            try:
                int(num_hid);            
                return [char_num for char_num in num_hid];
            except ValueError:
                print(err_msg, end=end_chr);
        
        
    # Попытка отгадать цифру
    def getOneNumber(msg = "", err_msg = "", end_chr = ""):
        while True:
            num_att = input(msg);
            try:
                int(num_att);
                if len(num_att) == 1:
                    return num_att;
            except ValueError:
                print(err_msg, end=end_chr);