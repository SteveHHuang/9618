def SortDescending():
    global Animals
    ArrayLength=len(Animals)
    for x in range(ArrayLength):
        for y in range(ArrayLength-x-1):
            if Animals[y][0:1]<Animals[y+1][0:1]:
                Temp=Animals[y]
                Animals[y]=Animals[y+1]
                Animals[y+1]=Temp




#main
Animals=["" for _ in range(10)]
Animals[0]="horse"
Animals[1]="lion"
Animals[2]="rabbit"
Animals[3]="mouse"
Animals[4]="bird"
Animals[5]="deer"
Animals[6]="whale"
Animals[7]="elephant"
Animals[8]="kangaroo"
Animals[9]="tiger"
SortDescending()
for animal in Animals:
    print(animal)