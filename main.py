from Vendor import *;
from Manager import *;
from functools import reduce;



if __name__ == '__main__':
    
    unittest.main();
    manager = Manager();
    vendor = Vendor();
    
    hid = vendor.getNumber(); # [3, 2, 1]
    att_hid = ['_' for i in range(len(hid))];
    rem = len(hid);
    
    
    print("\n ИГРА УГАДАЙ ЧИСЛО");
    STOP = False;
    while not STOP:
        print(f"Число: {reduce(lambda x,y: x + y, att_hid)}");
        att = input("Введите цифру: ");
        pos = manager.getEqualNumbers(att, hid);
        if (pos != -1):
            rem -= 1;
            att_hid[pos] = att;
        else:
            print("Такой цифры в этом числе нет");
        if (not rem):
            STOP = True;
    
    print(f"Вы угадали число: {reduce(lambda x,y: x + y, att_hid)}")
        

