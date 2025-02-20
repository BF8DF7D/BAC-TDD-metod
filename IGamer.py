from abc import ABC, abstractmethod;

class IGamer(ABC):
    
    @abstractmethod
    def getHidden(self):
        pass;
        
    @abstractmethod
    def getAttempt(self):
        pass;
    