# 20250923
# a
class Animal:
    def __init__(self, name, sound, size, intelligence):
        self.Name = name # Name, type of string
        self.Sound = sound # Sound, type of string
        self.Size = size # Size, type of integer
        self.Intelligence = intelligence # Intelligence, type of integer
    def Description(self):
        result = f"The animal's name is {self.Name}, it makes a{self.Sound} its size is {self.Size} and its intelligence level is {self.Intelligence} "
        return result
    
#b
class Parrot(Animal):
    def __init__(self, name, sound, size, intelligence, wingSpan, numwords):
        super().__init__(name, sound, size, intelligence)
        self.WingSpan = wingSpan # WingSpan, type of integer
        self.NumberWords = numwords #NumberWords, type of integer
    
    def ChangeNumberWords(self, num):
        self.NumberWords+=num
    
    def Description(self):
        result = f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}. It has a wingspan of {self.WingSpan} cm and can say {self.NumberWords} words."
        return result
#c
class Wolf(Animal):
    def __init__(self, name, sound, size, intelligence, TerritorySize):
        super().__init__(name, sound, size, intelligence)
        self.TerritorySize = TerritorySize # TerritorySize, type of integer
    def SetTerritorySize(self, num):
        self.TerritorySize += num
    
    def Description(self):
        result = f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}. Its territory {self.TerritorySize} square miles."
        return result

# d
p1=Parrot("Chewie", "Squawk", 1, 10, 30, 29) # Chewie
w1=Wolf("Nighteyes", "Howl", 8, 7, 100) # Nighteyes
a1=Animal("Copper", "Neigh", 10, 6) # Copper

w1.SetTerritorySize(-20)
p1.ChangeNumberWords(2)

print(p1.Description())
print(w1.Description())
print(a1.Description())