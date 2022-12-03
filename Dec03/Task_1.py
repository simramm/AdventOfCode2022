import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#
f = open(os.path.join(__location__,"Input.txt"))

# if test needed
#f = open(os.path.join(__location__,"Input_test.txt"))

input_list = f.read().split("\n")

#input_list = f.read().split()
#input_list = list(map(int, f.read().split('\n')))

#input_list = list(map(int, f.read().split(',')))


rucksacks=[]
for x in input_list:
    rucksacks.append([x[:int(len(x)/2)],x[int(len(x)/2):]])

numbers=[]

for rucksack in rucksacks:
    character=''
    for x in rucksack[0]:
        if x in rucksack[1] and x!=character:
            character=x
            if x.isupper():
                numbers.append(ord(x)-38)
            if x.islower():
                numbers.append(ord(x)-96)

print(sum(numbers))