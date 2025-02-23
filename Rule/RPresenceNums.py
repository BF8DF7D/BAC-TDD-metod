from .IRule import IRule;
import unittest;
import logging;


class Test_RPresenceNums(unittest.TestCase):
    
    def test_instanse(self):
        self.assertIsNotNone(RPresenceNums());
        logging.debug("RPresenceNums: создание экземпляра объекта: успешно");

    
    def test_cheackRule(self):
        att = ['1', '3', '4', '3', '5'];
        hid = ['2', '3', '6', '7', '3'];
        
        self.assertEqual([True, True], 
                         RPresenceNums.cheackRule(att, hid));
        logging.debug("RPresenceNums.cheackRule: наличие цифры в числе: успешно");

class RPresenceNums(IRule):
    
    def cheackRule(att, hid):
    
        # удаление дублей
        att_set = [];
        for num_att in att:
            if num_att not in att_set:
                att_set.append(num_att);  
                
        # наличие цифры в числе
        result = [];
        for num_hid in hid:
            if num_hid in att_set:
                result.append(True);
        
        return result;