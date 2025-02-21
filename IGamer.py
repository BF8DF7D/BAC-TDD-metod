from abc import ABC, abstractstaticmethod

class IGamer(ABC):
    
    @abstractstaticmethod
    def getHidden(msg = "", err_msg = "", end_chr = ""):
        pass;
        
    @abstractstaticmethod
    def getAttempt(msg = "", err_msg = "", end_chr = ""):
        pass;
    