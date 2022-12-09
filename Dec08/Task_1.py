import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

data = f.read().split("\n")
length=len(data)


visibleTrees=set()
for i in range(0,length):
    width=len(data[i])


    for x in range(0,width):

        if i==0 or i == length:
            visibleTrees.add((str(i)+','+str(x)))
        if x==0 or x == width:
            visibleTrees.add((str(i)+','+str(x)))

        tree=int(data[i][x])
        visibleUp=True
        visibleDown=True
        visibleLeft=True
        visibleRight=True

        # up
        for j in range(0,i):
            if int(data[j][x])>=tree:
                visibleUp=False
        # down
        for j in range(i+1, length):
            if int(data[j][x])>=tree:
                visibleDown=False

        # left
        for y in range(0,x):
            if int(data[i][y])>=tree:
                visibleLeft=False
        
        # right
        for y in range(x+1,width):
            if int(data[i][y])>=tree:
                visibleRight=False

        if visibleDown==True or visibleUp==True or visibleLeft==True or visibleRight==True:
            visibleTrees.add((str(i)+','+str(x)))

print(len(visibleTrees))



        





