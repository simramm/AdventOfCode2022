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


for x in input_list:
    
    sum=0


