import os
from numpy import sign

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))
#f = open(os.path.join(__location__,"Input_test.txt"))


data_raw = f.read().split("\n")
data=[]
for d in data_raw:
    data.append(d.split(' '))

class knot:
  def __init__(self, x, y):
    self.x = x
    self.y = y

knots=[]
for x in range(0,10):
    knots.append(knot(0,0))

#head = knots[0]
tail_positions={(str(0) + ',' + str(0))}

for m in data:

    direction=m[0]
    steps=int(m[1])

    for x in range(0,steps):

        if direction=='R':        
            knots[0].x+=1
        if direction=='L':
            knots[0].x-=1
        if direction=='U':
            knots[0].y+=1
        if direction=='D':
            knots[0].y-=1
        
        for i in range(0, 9):

            xdist = knots[i].x-knots[i+1].x
            ydist = knots[i].y-knots[i+1].y

            if ydist**2 + xdist**2 > 2: 
                knots[i+1].y += sign(ydist)
                knots[i+1].x += sign(xdist) 

        tail_positions.add((str(knots[9].x) + ',' + str(knots[9].y)))

print(len(tail_positions))
