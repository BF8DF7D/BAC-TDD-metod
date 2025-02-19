from abc import ABC, abstractmethod;

class IGamer(ABC):
    # Метод получения загаданного значения
    @abstractmethod
    def getNumber(self):
        pass;
    
    # Метод Получения числа
    @abstractmethod
    def getAttempt(self):
        pass
