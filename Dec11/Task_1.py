import os
import math

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__,"Input.txt"))

data = [x.split("\n") for x in f.read().split("\n\n")]

class Monkey():
    def __init__(self,number,items,operation,test,forTrue,forFalse,inspects):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.forTrue = forTrue
        self.forFalse = forFalse
        self.inspects = inspects
        
monkeys={}

for mon in data:
    number=int(mon[0][7])
    items=list(map(int,mon[1][18:].split(','))) #tbd
    operation=mon[2][23:]    
    test=int(mon[3][21:])    
    forTrue=int(mon[4][29])
    forFalse=int(mon[5][30])
    inspects=0
    monkeys[number]=Monkey(number,items,operation,test,forTrue,forFalse,inspects)

for round in range(0,20):    
    for x in range(0,len(data)):        
        for item in monkeys[x].items:
            monkeys[x].inspects+=1
            
            prev=item          
            
            if monkeys[x].operation[0]=='+':
                item+=int(monkeys[x].operation[2])
            if monkeys[x].operation[0]=='*' and monkeys[x].operation[2]!='o' :
                item*=int(monkeys[x].operation[2:])
            if monkeys[x].operation[2]=='o':
                item=item*item
            
            #divide by 3            
            item=int(math.floor(item/3))
            
            if item % monkeys[x].test==0:
                monkeys[monkeys[x].forTrue].items.append(item)
            else:
                monkeys[monkeys[x].forFalse].items.append(item)
        monkeys[x].items.clear()                 
    
    # print('### AFTER ROUND ### ' + str(round+1))
    # for y in range(0,len(data)):
    #     print('monkey ' + str(monkeys[y].number))
    #     print(monkeys[y].items)
        
scores=[]
for x in monkeys:    
    scores.append(monkeys[x].inspects)

print(sorted(scores)[-1]*sorted(scores)[-2])
            
        
    
    
    

        






