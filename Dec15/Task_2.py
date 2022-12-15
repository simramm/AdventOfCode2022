import os
import time

t0 = time.time()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

data = f.read().split("\n")

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

t=4000000
senBeacs=[]
for line in data:
    
    sensorx=int(line.split(' ')[2][2:-1])
    sensory=int(line.split(' ')[3][2:-1])
    beaconx=int(line.split(' ')[8][2:-1])
    beacony=int(line.split(' ')[9][2:])
    mandist=manhattan([sensorx,sensory],[beaconx,beacony])    
    senBeacs.append([sensorx,sensory,beaconx,beacony,mandist])

# new approach
# go along the diamond's edges (man + 1)
# check for every point if covered by another sensor

def checkInReach(x,y):
    ans=False
    
    for sensor in senBeacs:    
        sensorx=sensor[0]
        sensory=sensor[1]
        man=sensor[4]
                
        if manhattan([x,y],[sensorx,sensory])<=man:
            ans=True
            break      
        
    return ans

for sensor in senBeacs:
    
    sensorx=sensor[0]
    sensory=sensor[1]
    man=sensor[4]+1
    
    # find points with manhattan distance + 1 from sensor
    
    y=0
    for x in range(sensorx-man,sensorx+man):
        if x<0 or x>t:
            continue
        
        y = sensory + (man-abs(x-sensorx))
        if y<0 or y>t:
            continue
        
        if not (checkInReach(x,y)):
            print(x,y,x*4000000+y)
            t1 = time.time()
            print(t1-t0)
            exit()
         
        y = sensory - (man-abs(x-sensorx))       
        if y<0 or y>t:
            continue
        
        if not (checkInReach(x,y)):
            print(x,y,x*4000000+y)
            t1 = time.time()
            print(t1-t0)
            exit()
    
    