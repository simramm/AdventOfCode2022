import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

data = f.read().split("\n")

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

senBeacs=[]
row=2000000
nobeacon=set()
for line in data:
    
    sensorx=int(line.split(' ')[2][2:-1])
    sensory=int(line.split(' ')[3][2:-1])
    beaconx=int(line.split(' ')[8][2:-1])
    beacony=int(line.split(' ')[9][2:])
    mandist=manhattan([sensorx,sensory],[beaconx,beacony])    
    senBeacs.append([sensorx,sensory,beaconx,beacony,mandist])
    
    if sensory+mandist<row or sensory-mandist>row:
        continue
        
    if sensory>row:
        rangex = mandist-(sensory-row)
    
    if sensory<row:
        rangex = mandist-(row-sensory)
    
    print(sensorx,sensory,beaconx,beacony,mandist,rangex)
    
    for x in range(sensorx-rangex,sensorx+rangex+1):
        nobeacon.add(x)
    
    
for line in senBeacs:
    if line[3]==row and line[2] in nobeacon:
        print(line)
        nobeacon.remove(line[2])

print(len(nobeacon))
    
        
    
 
    
    