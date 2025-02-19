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
        logging.info(" ТЕСТ: Manager.getEqualNumbers: return значения: успешно");
    
    
# Управляющий 
# Cледит за ходом игры и устанавливает правила
class Manager:
    
    # Метод Сравнение 
    # Сравнение попытки с угадываемым числом
    def getEqualNumbers(self, att, hidden):
        # todo реализовать метод поиска числа и возврата позиции.
        match att:
            case '3': return 0;
            case '2': return 1;
            case '1': return 2;
            case '0': return -1;



#    logging.info(" ТЕСТ: Vendor: создание экземпляра: успешно");
#    logging.info(" ТЕСТ: Vendor.getNumber: return значения: успешно");
#   logging.info(" ТЕСТ: Vendor.getAttempt: return значения: успешно");