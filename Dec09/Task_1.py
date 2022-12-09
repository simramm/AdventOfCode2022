import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))


data_raw = f.read().split("\n")
data=[]
for d in data_raw:
    data.append(d.split(' '))

class knot:
  def __init__(self, x, y):
    self.x = x
    self.y = y

head=knot(0,0)
tail=knot(0,0)

tail_positions={(str(tail.x) + ',' + str(tail.y))}

for m in data:
    direction=m[0]
    steps=int(m[1])
    for x in range(0,steps):

        if direction=='R':        
            head.x+=1
            if head.x-1>tail.x:
                tail.x=head.x-1
                tail.y=head.y

        if direction=='L':
            head.x-=1
            if head.x+1<tail.x:
                tail.x=head.x+1
                tail.y=head.y

        if direction=='U':
            head.y+=1
            if head.y-1>tail.y:
                tail.y=head.y-1
                tail.x=head.x                

        if direction=='D':
            head.y-=1
            if head.y+1<tail.y:
                tail.y=head.y+1
                tail.x=head.x
    
        tail_positions.add((str(tail.x) + ',' + str(tail.y)))
                
print(len(tail_positions))
