from abc import ABC, abstractstaticmethod

class IGamer(ABC):
    
    @abstractstaticmethod
    def getNumber(msg = "", err_msg = "", end_chr = ""):
        pass;
        
    @abstractstaticmethod
    def getOneNumber(msg = "", err_msg = "", end_chr = ""):
        pass;
    