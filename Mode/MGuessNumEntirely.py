from Rule import *;
from .IMode import IMode;

from IGamer import IGamer;
from Gamer import Gamer;
from CmpGamer import CmpGamer;

import unittest;
import logging;


class Test_MGuessNumEntirely(unittest.TestCase):
    
    def test_instanse(self):
        mode = MGuessNumEntirely();
        
        self.assertIsNotNone(mode);
        for elem in mode.rules:
            self.assertTrue(issubclass(elem, IRule));
        for elem in mode.gamers:
            self.assertTrue(issubclass(elem, IGamer));
    
        logging.debug("MGuessNumEntirely: создание экземпляра объекта: успешно");

    
    def test_checkModeRule(self):
        att = ['2', '4', '6', '8', '9'];
        hid = ['1', '5', '6', '7', '6'];
        
        mode = MGuessNumEntirely();
        mode.args = [att, hid];
        
        self.assertEqual([[True], [True, True]], mode.checkModeRule())
        logging.debug("MGuessNumEntirely.checkModeRule: правила режима: успешно")

class MGuessNumEntirely(IMode):
    def __init__(self):
        self.rules = [RPositionsNums, RPresenceNums];
        self.gamers = [Gamer, CmpGamer];
        self.args = [];
    
    
    def mainCycle(self):
         gam, cmp = self.gamers;
         
         him = cmp.getNumber();
         
         print(f" Загадано число длинной {len(him)}");
         logging.info(f" Загаданное слово {him}");
         
         msg = " Попытка отгадать: ";
         err_msg = " Это не число";
         end_chr = "\n"
         
         STOP = False;
         while not STOP: 
            att = gam.getNumber(msg, err_msg, end_chr);
            
            if (len(att) == len(him)): 
                
                self.args = [att, him];
                res_pos, res_pres = self.checkModeRule();
                
                print(f" Одинаковых цифр: {len(res_pres)}")
                print(f" Цифр на своей позиции: {len(res_pos)}")
                
                if (len(him) == len(res_pos)):
                    print(" Вы угадали")
                    STOP = True;
                else:
                    print("")
                    
            else:
                print(" Число не той длины.");
            
             
         
      
    
    def checkModeRule(self):
        result = [];
        att, hid = self.args;
        for rule in self.rules:
            result.append(rule.cheackRule(att, hid));
        return result;
         
