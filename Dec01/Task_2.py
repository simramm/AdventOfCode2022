import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
print(os.path.join(__location__,"Input.txt"))
f = open(os.path.join(__location__,"Input.txt"))

# if test needed
#f = open(os.path.join(__location__,"Input_test.txt"))

input_list = f.read().split("\n\n")

elves=[]
for x in input_list:
    elves.append(x.split("\n"))


max_calories=[]
for elf in elves:
    sum_calories=0
    for calories in elf:
        sum_calories+=int(calories)
    max_calories.append(sum_calories)




print(sum(sorted(max_calories,reverse=True)[:3]))

