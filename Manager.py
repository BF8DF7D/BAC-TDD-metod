import unittest
import logging

# Тест класса Управляющий
class TestManager(unittest.TestCase):
    
    # Тест класса Управляющий: Создание экземпляра
    def test_Manager(self):
        manag = Manager();
        self.assertIsNotNone(manag);
        logging.info(" ТЕСТ: Manager: создание экземпляра: успешно");
    
    # Тест метода Сравнение числа: Корректность return значений 
    def test_return_getEqualNumbers(self):
        manag = Manager();
        self.assertEqual(0, manag.getEqualNumbers('3', ['3','2','1']));
        self.assertEqual(1, manag.getEqualNumbers('2', ['3','2','1']));
        self.assertEqual(2, manag.getEqualNumbers('1', ['3','2','1']));
        self.assertEqual(-1, manag.getEqualNumbers('0', ['3','2','1']));
        for i in range(4, 10):
            self.assertEqual(-1, manag.getEqualNumbers(str(i), ['3','2','1']));
        logging.info(" ТЕСТ: Manager.getEqualNumbers: return значения: успешно");
    
    
# Управляющий 
# Cледит за ходом игры и устанавливает правила
class Manager:
    
    # Метод Сравнение 
    # Сравнение попытки с угадываемым числом
    def getEqualNumbers(self, att, hidden):
        # todo реализовать метод поиска числа и возврата позиции.
        try:
            int_att = int(att) # числовое значение сивола цифры
        except ValueError:
            return -1;
        if (int_att <= 3 and int_att >= 1):
            return 3 - int_att;
        if (int_att == 0 or int_att > 3):
            return -1;



#    logging.info(" ТЕСТ: Vendor: создание экземпляра: успешно");
#    logging.info(" ТЕСТ: Vendor.getNumber: return значения: успешно");
#   logging.info(" ТЕСТ: Vendor.getAttempt: return значения: успешно");