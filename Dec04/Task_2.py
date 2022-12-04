import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

input_list = f.read().split("\n")

assignments=[]
for x in input_list:    
    assignments.append(x.split(','))

newassignments=[]
for assignment in assignments:
    newassignments.append(assignment[0].split('-'))
    newassignments.append(assignment[1].split('-'))

sum=0
for i in range(0,len(newassignments)-1,2):

    start1=int(newassignments[i][0])
    start2=int(newassignments[i+1][0])
    end1=int(newassignments[i][1])
    end2=int(newassignments[i+1][1])
    
    if start1 >= start2 and start1 <= end2:
        sum+=1
        continue
    if start2 >= start1 and start2 <= end1:
        sum+=1
        continue
    if end1 >= start2 and end1 <= end2:
        sum+=1
        continue
    if end2 >= start1 and end2 <= end1:
        sum+=1
        continue
    
print(sum)