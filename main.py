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
        q, num = vend.getNumber();
        self.assertEqual(q, len(num));
        
        



# Поставщик
class Vendor:
    # Метод Получения числа
    def getNumber(self):
        # todo реализовать метод получения выходного значения
        return [3, [1, 2, 3]]; # [Кол-во цифр в числе, [cамо число]]
        
if __name__ == '__main__':
    unittest.main();
    
        

