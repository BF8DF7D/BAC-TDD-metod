from abc import ABC, abstractstaticmethod

class IGamer(ABC):
    
    @abstractstaticmethod
    def getHidden():
        pass;
        
    @abstractstaticmethod
    def getAttempt():
        pass;
    