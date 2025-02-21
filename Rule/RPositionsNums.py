from .IRule import IRule;
import unittest;
import logging;


class Test_RPositionsNums(unittest.TestCase):
    
    def test_cheackRule(self):
        att = ['1', '3', '4', '3', '5'];
        hid = ['2', '3', '6', '7', '3'];
        
        self.assertEqual([True], 
                         RPositionsNums.cheackRule(att, hid))
        logging.debug("RPositionNums.cheackRule: совпадение пазиций: успешно");
        

class RPositionsNums(IRule):
    
    def cheackRule(*args):
        att, hid = args;
        
        result = [];
        for i in range(len(att)): 
            if (att[i] == hid[i]):
                result.append(True);
        
        return result;
    