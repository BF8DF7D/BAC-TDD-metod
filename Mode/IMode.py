from abc import ABC, abstractmethod;

class IMode(ABC):
    
    @abstractmethod
    def mainCycle(self):
        pass
    
    @abstractmethod
    def checkModeRule(self):
        pass
