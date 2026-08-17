# source: InheritanceTicket FRQ
import time
from datetime import date

def GetDayDiff(yr,mo,day):
    return int((date(yr,mo,day)-date.today()).days)

class Ticket:
    def __init__(self,sn):
        self.serialNumber = sn
        self.__price=-1

    def getPrice(self):
        return self.__price
    def toString(self):
        return "Number: " + self.serialNumber + "\nPrice: " + f"{self.getPrice()}"
class Advance(Ticket):
    def __init__(self,yr,mo,day,sn):
        super().__init__(sn)
        self.Num = GetDayDiff(yr,mo,day)
        self.__price=self.SetPrice()

    def SetPrice(self):
        if self.Num<10: return 40
        else: return 30
    def toString(self):
        return "Number: " + self.serialNumber + "\nPrice: " + f"{self.getPrice()}"

class StudentAdvance(Advance):
    def __init__(self,yr,mo,day,sn):  
        super().__init__(yr,mo,day,sn)
        self.__price=self.SetPrice()
        
    def SetPrice(self):
        return super().SetPrice()//2
    def getPrice(self):
        return self.__price
    def toString(self):
        return "Number: " + self.serialNumber + "\nPrice: " + f"{self.getPrice()}" + "\n(student ID required)"
    
a=Ticket("suhfuwhef")
b=Advance(2025,12,31,"suhfuwhef")
c=StudentAdvance(2025,12,31,"suhfuwhef")
print(f"{b.getPrice()}\n")
print(c.getPrice())
print(c.toString())


'''
子类定义了同名的“私有”变量时，getter需要override：

如果在子类中又写了一次 self.__value = ...，Python 会将其处理为 _Child__value。
此时，父类的 getter 访问的是 _Parent__value，它拿不到子类新定义的那个变量。所以b.getPrice()返回的是a.price
解决这个问题的办法就是override getPrice方法


'''