class Picture:
    def __init__(self,description,w,h,framecolour):
        # private Description: String
        # private Width: Integer
        # private Height: Integer
        # private FrameColour: String
        self.__Description=description
        self.__Width=w #int(w)
        self.__Height=h #int(h)
        self.__FrameColour=framecolour
        
    def getDescription(self):
        return self.__Description
    def getWidth(self):
        return self.__Width
    def getHeight(self):
        return self.__Height
    def getFrameColour(self):
        return self.__FrameColour
    
    def SetDescription(self,newdescrption):
        self.__Description=newdescrption

def ReadData():
    
    try:
        count=0
        f=open("Pictures.txt")
        x=f.read().split()
        print(x)
        while count < len(x):
            y=x[count:count+4]
            count+=4
            PicArray[count//4]=Picture(y[0],int(y[1]),int(y[2]),y[3])
            
        f.close()
        return count//4
    except FileNotFoundError:   
        print("File Not Found.")


# PicArray: ARRAY[0:99] OF Picture
PicArray=[None for _ in range(100)]
ReadData()

x=input("Enter your requirements for a picture(colour of the frame) ").lower()
y=int(input("Enter your requirements for a picture(max width) "))
z=int(input("Enter your requirements for a picture(max height)) "))
for pic in PicArray:
    if pic is None:
        continue
    if x==pic.getFrameColour() and y>=pic.getWidth() and z>=pic.getHeight():
        print(f"{pic.getDescription()}, width:{pic.getWidth()}, height:{pic.getHeight()}")
        