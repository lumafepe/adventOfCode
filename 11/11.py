PARTTWO=True
with open("11.txt","r") as f:
    lines=list(map(lambda x:x[:-1],f.readlines()))

class Monkey:
    def __init__(self,id,items,test,toT,toF,operation):
        self.id=id
        self.items=items
        self.test=test
        self.toT=toT
        self.toF=toF
        self.operation=operation
        self.inspected=0
        
    def addItem(self,item):
        self.items.append(item)
        
    def getItem(self):
        return self.items.pop(0) if self.items else None

    def processItem(self,item):
        operation=self.operation.replace('old',str(item))
        newWorry=eval(operation)
        if PARTTWO: newWorry%=mod
        else: newWorry//=3
        self.inspected+=1
        if newWorry%self.test==0:
            return(newWorry,self.toT)
        return (newWorry,self.toF)
    def __str__(self):
        return str(self.inspected)
        
monkeys={}
monkeysl=[]

mod=1
while lines:
    id=int(lines.pop(0).replace('Monkey ','').replace(':',''))
    items=[int(k) for k in lines.pop(0).replace('  Starting items: ','').strip(' ').split(',')]
    operation=lines.pop(0).replace('  Operation: new = ','')
    test=int(lines.pop(0).replace('  Test: divisible by ',''))
    truet=int(lines.pop(0).replace('    If true: throw to monkey ',''))
    falset=int(lines.pop(0).replace('    If false: throw to monkey ',''))
    lines.pop(0)
    
    mod*=test
    monkeys[id]=Monkey(id, items, test, truet, falset, operation)
    monkeysl.append(id)

for _ in range(10000):
    for id in monkeysl:
        monkey=monkeys[id]
        item=monkey.getItem()
        while item:
            (item,dest)=monkey.processItem(item)
            monkeys[dest].addItem(item)
            item=monkey.getItem()

vas=list(map(lambda x:x.inspected,monkeys.values()))
vas.sort()
print(vas[-1]*vas[-2])
            
        