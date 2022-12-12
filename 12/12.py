graph={}
end=None
start=None
aas=[]
from queue import Queue
with open("12.txt","r") as f:
    lines=list(map(lambda x:[j for j in x[:-1]],f.readlines()))
    for lN,line in enumerate(lines):
        for cN,cell in enumerate(line):
            if cell=='E':
                end=(lN,cN)
                lines[lN][cN]='z'
            if cell=='S':
                aas.append((lN,cN))
                lines[lN][cN]='a'
            if cell=='a':
                aas.append((lN,cN))
        
proc=[(end,0)]
while proc:
    (y,x),cost=proc.pop(0)
    print((y,x))
    if (y,x) in graph:
        if cost<graph[(y,x)]:
            graph[(y,x)]=cost
        else:
            continue
    else: graph[(y,x)]=cost
    toS=[(y,x+1),(y,x-1),(y+1,x),(y-1,x)]
    for i in toS:
        if y<0 or y>len(lines)-1:
            continue
        if x<0 or x>len(lines[y])-1:
            continue
        if i[0]<0 or i[0]>len(lines)-1:
            continue
        if i[1]<0 or i[1]>len(lines[i[0]])-1:
            continue
        if ord(lines[y][x])-ord(lines[i[0]][i[1]])<=1:
            proc.append((i,cost+1))
            
print(min([graph[i] if i in graph else 1e9 for i in aas]))
    
    



            
