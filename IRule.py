from abc import ABC, abstractmethod;

class IRule(ABC):
    
    @abstractmethod
    def cheackRule(self):
        pass;