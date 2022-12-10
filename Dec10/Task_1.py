import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

# if test needed
#f = open(os.path.join(__location__,"Input_test.txt"))

data = f.read().split("\n")

#data = f.read().split()
#data = list(map(int, f.read().split('\n')))
#data = list(map(int, f.read().split(',')))

#print(data[0])


signal_strengths=[]
cycle=0
cpu=1
line=0
cycling=True
cycles=dict([])
while cycling:
    

    cmd=data[line].split(' ')[0]

    if cmd=='noop':
        cycle+=1
        cycles[cycle]=[cpu,cpu*cycle,line]
        line+=1


    if cmd=='addx':
        cycle+=1
        cycles[cycle]=[cpu,cpu*cycle,line]
        value=int(data[line].split(' ')[1])
        cycle+=1
        line+=1
        cycles[cycle]=[cpu,cpu*cycle,line]
        cpu+=value

    if line==len(data)-1:
        cycling=False



print('20',cycles[20])
print('60',cycles[60])
print('100',cycles[100])
print('140',cycles[140])
print('180',cycles[180])
print('220',cycles[220])
print(data[132])

print(int(cycles[20][1])+int(cycles[60][1])+int(cycles[100][1])+int(cycles[140][1])+int(cycles[180][1])+int(cycles[220][1]))
    