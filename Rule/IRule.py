from abc import ABC, abstractstaticmethod;

class IRule(ABC):
    
    @abstractstaticmethod
    def cheackRule(att, hid):
        pass;