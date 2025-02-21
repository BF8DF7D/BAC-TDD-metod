from IGamer import IGamer;
from RandomNumbers import RandomNumbers;
import random;
import unittest;
import logging;


class Test_CmpGamer(unittest.TestCase):
    
    # Тест getHidden: покрытие всех значений
    # Проверяет все числа в указаном промежутке длинны
    # масивы длинной от 3 до 5
    def test_fullrandom_getHidden(self):
        TEST_RANGE = 50;
        BASE_RANDOM = 3
        STOP = False;
        
        data = [True for _ in range(3)]
        random_res = [False for _ in range(3)];
        test_step = 0;
        
        while not STOP:
            rend_gener = CmpGamer.getHidden();
            random_res[len(rend_gener) - BASE_RANDOM] = True;
            
            if (random_res == data):
                self.assertTrue(True);
                STOP = True;
            elif (test_step >= TEST_RANGE):
                self.assertTrue(False);
                STOP = True;
                
            test_step += 1;

        logging.debug("CmpGamer.getHidden: покрытие значений: успешно")


class CmpGamer(IGamer):
    
    # Загадывание числа
    def getHidden(msg = "", err_msg = "", end_chr = ""):
        return [RandomNumbers.getCharNumber() 
                for _ in range(random.randint(3, 5))];
        
            
    # Попытка отгадать цифру
    def getAttempt(msg = "", err_msg = "", end_chr = ""):
        return RandomNumbers.getCharNumber();

    
