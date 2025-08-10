import string

# print(string.ascii_lowercase)

# 20250623
# Count each lower and upper alphabet in a file
# dictionary 字典: key-value 键值对

dictLetter ={}
for char in string.ascii_lowercase:
    dictLetter[char] = 0

with open("/Users/hehuang/Documents/GitHub/9618/9618paper4/WordFreq./satReading.txt") as Reading:
    content = Reading.read()

print(content)
    
        
for temp in content:
    print(temp.lower() in dictLetter)
    if temp.lower() in dictLetter:
        
        dictLetter[temp.lower()] += 1
        
print(dictLetter)
    
    
LetterFre = sorted(dictLetter.items(), key = lambda x:x[1], reverse=True) 
# reverse = True: descending order; 
# False: ascending order

print(LetterFre)

