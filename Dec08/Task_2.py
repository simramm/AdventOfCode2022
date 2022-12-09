import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

data_raw = f.read().split("\n")
data=[]

for d in data_raw:
    data.append(list(map(int,d)))
    
scenicScores=[]
maxScore=0
length=len(data)

for i in range(0,length):
    width=len(data[i])
    for x in range(0,width):

        #calculate scenic score
        scenicUp=1
        scenicDown=1
        scenicLeft=1
        scenicRight=1

        #up
        j=i
        while j>1 and data[i][x]>data[j-1][x]:
            scenicUp+=1
            j-=1
        if i==0:
            scenicUp=0

        #down
        j=i
        while j<length-2 and data[i][x]>data[j+1][x]:
            scenicDown+=1
            j+=1
        if i==length-1:
            scenicDown=0

        #left
        y=x
        while y>1 and data[i][x]>data[i][y-1]:
            scenicLeft+=1
            y-=1
        if x==0:
            scenicLeft=0

        #right    
        y=x
        while y<width-2 and data[i][x]>data[i][y+1]:
            scenicRight+=1
            y+=1
        if x==width-1:
            scenicRight=0

        scenicScores.append([i,x,(scenicUp*scenicDown*scenicLeft*scenicRight)])
        maxScore=max(maxScore,scenicUp*scenicDown*scenicLeft*scenicRight)


print(maxScore)