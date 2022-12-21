import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

data = [x.split(",") for x in f.read().split("\n")]

cubes = [list(map(int,x)) for x in data]

total_surface=0

for cube in cubes:  
    
    surface = 6    
    
    x=cube[0]
    y=cube[1]
    z=cube[2]
    
    if [x+1,y,z] in cubes:
        surface-=1
    if [x-1,y,z] in cubes:
        surface-=1
    if [x,y+1,z] in cubes:
        surface-=1
    if [x,y-1,z] in cubes:
        surface-=1
    if [x,y,z+1] in cubes:
        surface-=1
    if [x,y,z-1] in cubes:
        surface-=1     

    total_surface+=surface

print(total_surface)