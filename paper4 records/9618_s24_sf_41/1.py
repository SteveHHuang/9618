# import datetime

# a=datetime.datetime.now()
# print(a.year)

# # help(datetime)

fr=open("Trees.txt",'r')
a=[]
for x in fr:
    a.append(x.strip())

fr.close()
print(a)