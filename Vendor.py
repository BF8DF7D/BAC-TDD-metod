import unittest

# Тест класса Поставщик
class TestVendor(unittest.TestCase):
    
    # Тест класса Поставщик: Создание экземпляра
    def test_crateVendor(self):
        vend = Vendor();
        self.assertIsNotNone(vend);
    
    # Тест метода Получение числа: Корректность return значений 
    def test_return_getNumber(self):
        vend = Vendor();
        num = vend.getNumber();
        for elem in num:
            self.assertIsInstance(elem, int);
            

# Поставщик
class Vendor:
    # Метод Получения числа
    def getNumber(self):
        # todo реализовать метод получения return значения
        return [3, 2, 1]; # [число, разбитое на вектор чисел]
        