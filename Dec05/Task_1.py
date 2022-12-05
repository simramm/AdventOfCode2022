import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

input_list = f.read().split("\n")

crates=[]

crates.append(['R','S','L','F','Q'])
crates.append(['N','Z','Q','G','P','T'])
crates.append(['S','M','Q','B'])
crates.append(['T','G','Z','J','H','C','B','Q'])
crates.append(['P','H','M','B','N','F','S'])
crates.append(['P','C','Q','N','S','L','V','G'])
crates.append(['W','C','F'])
crates.append(['Q','H','G','Z','W','V','P','M'])
crates.append(['G','Z','D','L','C','N','R'])

moves=input_list[10:]
new_moves=[]
for move in moves:
    new_moves.append(move.split(' '))

for move in new_moves:
    amount = move[1]
    src = int(move[3])-1
    dst = int(move[5])-1


    for box in range(int(amount)):
        crates[dst].append(crates[src][-1])
        crates[src].pop(-1)

for crate in crates:
    print(crate[-1])
    



