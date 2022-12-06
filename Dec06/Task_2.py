import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

input = f.read()
#input ='nppdvjthqldpwncqszvftbrmjlhg'

marker=[]

num_characters=0

for x in input:
    num_characters+=1
    if len(marker)>13:
        marker.pop(0)
    if x not in marker and len(marker)==len(set(marker)) and num_characters>14:
        print(marker,x)
        print(num_characters)
        break
    marker.append(x)
 




