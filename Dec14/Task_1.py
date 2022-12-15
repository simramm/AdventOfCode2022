import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f=open(os.path.join(__location__,"Input.txt"))

# if test needed
#f = open(os.path.join(__location__,"Input_test.txt"))

data = f.read().split("\n")

rocks=[]
lowRock=0

for line in data:           
    
    xp,yp =0,0
    x,y = 0,0

    for coord in line.split(' -> '):        
        x,y = map(int,(coord.split(',')))
        lowRock=max(int(y),lowRock)        
        if xp==0 and yp==0:
            rocks.append(tuple([x,y]))
            xp,yp=x,y
            
        else:                
            if xp==x:                    
                for i in range(min(y,yp),max(y+1,yp+1)):
                    rocks.append(tuple([x,i]))
                    
            if yp==y:                    
                for i in range(min(x,xp),max(x+1,xp+1)):
                    rocks.append(tuple([i,y]))
                    
            xp,yp=x,y    

grid={}

for x in range(0,600):
    for y in range(0,200):
        grid[x,y]='e'

for rock in rocks:
    grid[rock[0],rock[1]]='r'

def dropSand(grid):
    fallen=False
    
    x=500
    y=0
    
    while fallen==False:
        
        if grid[x,y+1]=='e':
            y+=1
        if grid[x,y+1]=='r' or grid[x,y+1]=='s':
            if grid[x-1,y+1]=='e':
                y+=1
                x-=1
            elif grid[x-1,y+1]=='r' or grid[x-1,y+1]=='s' :
                if grid[x+1,y+1]=='e':
                    y+=1
                    x+=1
                elif grid[x+1,y+1]=='r' or grid[x+1,y+1]=='s' :
                    grid[x,y]='s'
                    fallen=True
        if y>180:
            fallen=True            
            
    return grid,y

y=0
counter=0
while y < lowRock:
    counter+=1
    grid,y=dropSand(grid)
print(counter-1)
            
        
    
    