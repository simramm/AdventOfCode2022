import math
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
print(os.path.join(__location__,"Input.txt"))
f = open(os.path.join(__location__,"Input.txt"))

# if test needed
#f = open(os.path.join(__location__,"Input_test.txt"))

input_list = f.read().split("\n")

#input_list = f.read().split()
#input_list = list(map(int, f.read().split('\n')))

#input_list = list(map(int, f.read().split(',')))

print(input_list)
strategy =[]

for x in input_list:
    
    #print(x)
    strategy.append(x.split())

total_score=0
for x in strategy:

    round_score=0
    #print(x[0])

#x lose
#y draw
#z win


    if x[0]== "A":#rock
        
        if x[1]== "X":
            round_score+=3
        if x[1]== "Y":
            round_score+=4
        if x[1]== "Z":
            round_score+=8

    if x[0]== "B":#paper
        
        if x[1]== "X":
            round_score+=1
        if x[1]== "Y":
            round_score+=5
        if x[1]== "Z":
            round_score+=9
    if x[0]== "C":#scissors
        
        if x[1]== "X":
            round_score+=2
        if x[1]== "Y":
            round_score+=6
        if x[1]== "Z":
            round_score+=7

    total_score+=round_score

print(total_score)





#print(strategy)
'''

elves=[]
for x in input_list:
    elves.append(x.split("\n"))


'''
