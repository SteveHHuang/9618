MealOption1 = 0 # MealOption1, a global variable, type of integer, initialised to 0
MealOption2 = 0 # MealOption2, a global variable, type of integer, initialised to 0

# Python好像无法实现BYREF 没有c++的指针功能

def MealsCount():
    
    global MealOption1, MealOption2
    
    MealOption = int(input("Please input the option.\n"))
    
    if MealOption == 1:
        MealOption1+=1
        MealsCount()
        
    elif MealOption == 2:
        MealOption2+=1
        MealsCount()
        
    else:
        print(MealOption1, " ", MealOption2)
        
        
    
    
    