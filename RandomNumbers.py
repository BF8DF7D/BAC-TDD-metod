import unittest;
import random;
import logging;

class Test_RandomNumbers(unittest.TestCase):
    
    # Тест getCharNumber: покрытие всех значений
    def test_fullrandom_getCharNumber(self):
        
        TEST_RANGE = 50;
        STOP = False;
        
        random_res = ['_' for elem in range(0, 9)];
        test_step = 0;
        
        while not STOP:
            rend_gener = RandomNumbers.getCharNumber();
            random_res[int(rend_gener) - 1] = rend_gener;
            
            if (random_res == RandomNumbers.data):
                self.assertTrue(True);
                STOP = True;
            elif (test_step >= TEST_RANGE):
                self.assertTrue(False);
                STOP = True;
                
            test_step += 1;
            
        logging.debug("RandomNumbers.getCharNumber: покрытие значений: успешно")


# Рандомизация
class RandomNumbers:
    
    data = [str(num) for num in range(1, 10)];
    
    @staticmethod
    def getCharNumber():
        return random.choice(RandomNumbers.data);    
        