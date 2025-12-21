# AP CSA 2019 FRQ Q3
# review of OOP
# 2025.11.24

class Delimiters:
    def __init__(self,open,close):
        self.__openDel = open
        self.__closeDel = close
       
    # def getopenDel(self):
    #     return self.__openDel
       
    # def getclosedDel(self):
    #     return self.__closeDel
        
    def getDelimitersList(self,tokens):
        ArrayList=[]
        for item in tokens:
            if item==self.__closeDel or item==self.__openDel:
                ArrayList.append(item)
        return ArrayList
           
    def isBalanced(self,Delimiters):
        countClosedDel=0
        countOpenDel=0
        for item in Delimiters:
            if item==self.__closeDel:
                countClosedDel+=1
            elif item==self.__openDel:
                countOpenDel+=1
            
            if countOpenDel < countClosedDel: return False
            
        if countClosedDel == countOpenDel: return True      
        else: return False
        