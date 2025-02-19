import unittest

# Тест класса Поставщик
class TestVendor(unittest.TestCase):
    def test_crateVendor(self):
        vend = Vendor();
        self.assertIsNotNone(vend);

# Поставщик
# класс предоставляющий угадываемое число
class Vendor:
    def __init__(self):
        # todo реализовать методы класса Поставщика
        None;
        
if __name__ == '__main__':
    unittest.main();
    
        

