import unittest
from IGamer import *
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Тест класса Поставщик
class TestVendor(unittest.TestCase):
    
    # Тест класса Поставщик: Создание экземпляра
    def test_crateVendor(self):
        vend = Vendor();
        self.assertIsNotNone(vend);
        logging.info(" ТЕСТ: Vendor: создание экземпляра: успешно");
 
    # Тест метода Получение числа: Корректность return значений 
    def test_return_getNumber(self):
        vend = Vendor();
        num = vend.getNumber();
        for elem in num:
            self.assertIsInstance(int(elem), int);
        logging.info(" ТЕСТ: Vendor.getNumber: return значения: успешно");
    
    def test_return_getAttempt(self):
        vend = Vendor();
        atts = vend.getAttempt()
        self.assertEquals('1', next(atts));
        self.assertEquals('2', next(atts));
        self.assertEquals('3', next(atts));
        logging.info(" ТЕСТ: Vendor.getAttempt: return значения: успешно");

# Поставщик
class Vendor(IGamer):
    iterabl = ['1', '2', '3']
        
    def getNumber(self):
        # todo реализовать метод получения return значения
        return ['3', '2', '1']; # [число, разбитое на вектор чисел]

    def getAttempt(self):
        # todo реализовать метод получения return значения
        for itel in iter(self.iterabl): 
            yield itel;
