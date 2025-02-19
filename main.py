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
        
# Тест класса Управляющий
class TestManager(unittest.TestCase):
    # Тест класса Управляющий: Создание экземпляра
    def test_Manager(self):
        manag = Manager();
        self.assertIsNotNone(manag);


# Поставщик
class Vendor:
    # Метод Получения числа
    def getNumber(self):
        # todo реализовать метод получения return значения
        return [3, [1, 2, 3]]; # [Кол-во цифр в числе, [cамо число]]
        
# Управляющий 
# Cледит за ходом игры и устанавливает правила
class Manager:
    # todo методы сравнения результатов угадывания.
    # todo методы выбора сложности игры.
    # todo методы выбора режима игры.
    None;


if __name__ == '__main__':
    unittest.main();
    
        

