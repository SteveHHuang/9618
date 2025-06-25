import string
# counting the words in a .txt file

dictWord ={}

r = open ("/Users/hehuang/Documents/GitHub/9618/9618paper4/WordFreq./satReading.txt")

content = r.read()

r.close()    
print(string.punctuation)

content1 = content
content = content.lower().split()


for i in range(len(content)):
    dictWord[content[i]] = dictWord.get(content[i],0)+1
    # dictWord.get(content[i],0): 得到content[i]这个键的值，如果没有的话初始化为0 
    
    # ALT:
    # for word in content1:
    #     if word in dictWord:
    #         dictWord[word] +=1
    #     else:
    #         dictWord[word] = 1
        
        
    for symbol in string.punctuation:
        content[i] = content[i].strip(symbol)

WordFre = sorted(dictWord.items(), key = lambda x:x[1], reverse=True) 

print(WordFre)

