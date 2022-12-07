import os
import collections

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

input = f.read().split("\n")

directories=set()
directory_sizes={}
cwd='/'

for i in range(0,len(input)-1):

    # back to root
    if input[i][:7]=='$ cd /':
        cwd='/'
        directories.add(cwd)

    # one level up
    if input[i][:7]=='$ cd ..':
        if cwd!='/':
            cwd=cwd[:(cwd.rfind('/'))]

    # one level down
    if input[i][:4]=='$ cd' and input[i][:7]!='$ cd ..' and input[i][:7]!='$ cd /':
        if cwd!='/':
            cwd+='/'
        cwd+=input[i][5:]
        directories.add(cwd)

    #sum files directly in folder cwd        
    if input[i+1]=="$ ls":
        dirsize=0
        if i<len(input):
            j=i+2
        while input[j][0]!='$':
            if input[j][0].isdigit():
                dirsize+=int(input[j].split(' ')[0])
            j+=1
            if (j>len(input)-1):
                break            
        directory_sizes[cwd]=dirsize



directory_sums={}
for x in sorted(directories):
    for s in directory_sizes.items():
        if s[0].startswith(x):
            if x in directory_sums:
                directory_sums[x]=directory_sums[x]+int(s[1])
            else:
                directory_sums[x]=int(s[1])


tobedeleted=30000000-(70000000 - max(directory_sums.values()))
min=70000000
for x,y in directory_sums.items():

    if y > tobedeleted and y < min:
        min=y

print(min)