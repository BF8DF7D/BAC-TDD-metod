from .IMode import IMode;
from Rule import RPositionsNums, RPresenceNums;
import unittest;
import logging;


class Test_MGuessNumEntirely(unittest.TestCase):
    
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
        self.args = [];
    
    
    def mainCycle(self):
        pass;
      
    
    def checkModeRule(self):
        result = [];
        for rule in self.rules:
            result.append(rule.cheackRule(*self.args));
        return result;
         
