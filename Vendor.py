import unittest
from IGamer import *
import logging

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
        self.assertEquals('1', vend.getAttempt());
        logging.info(" ТЕСТ: Vendor.getAttempt: return значения: успешно");

# Поставщик
class Vendor(IGamer):
    def getNumber(self):
        # todo реализовать метод получения return значения
        return ['3', '2', '1']; # [число, разбитое на вектор чисел]

    def getAttempt(self):
        # todo реализовать метод получения return значения
        return '1';
