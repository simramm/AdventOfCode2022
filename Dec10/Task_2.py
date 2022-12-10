import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

data = f.read().split("\n")


signal_strengths=[]
cycle=0
pos=-1
x=1
line=0
cycling=True

pixels=dict([])

while cycling:
    

    cmd=data[line].split(' ')[0]

    if cmd=='noop':


        cycle+=1
        pos+=1
        if pos>40:
            pos-=40

        # spite position = x-1, x, x+1

        if pos in (x-1,x,x+1):
            pixel='#'
        else:
            pixel='.'

        pixels[cycle]=[pixel]

        line+=1


    if cmd=='addx':

        # start executing

        cycle+=1
        pos+=1
        if pos>40:
            pos-=40
        

        if pos in (x-1,x,x+1):
            pixel='#'
        else:
            pixel='.'
        pixels[cycle]=[pixel]

        # finish executing

        value=int(data[line].split(' ')[1])

        cycle+=1
        pos+=1
        if pos>40:
            pos-=40
        line+=1

        if pos in (x-1,x,x+1):
            pixel='#'
        else:
            pixel='.'
        pixels[cycle]=[pixel]

        x+=value

    if line==len(data)-1:
        cycling=False



row=''
for x,y in pixels.items():
    row+=str(y[0])
    if len(row)==40:
        print(row)
        row=''



