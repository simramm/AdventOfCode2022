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

numbers=[]
for y in range(0,len(input_list)-2,3):
    character=''
    for x in input_list[y]:
        if x in input_list[y+1] and x != character:
            if x in input_list[y+2]:
                character=x
                if x.isupper():
                    numbers.append(ord(x)-38)
                if x.islower():
                    numbers.append(ord(x)-96)
print(sum(numbers))


