with open("8.txt","r") as f:
    lines=list(map(lambda x:[int(i) for i in x[:-1]],f.readlines()))
visibles=[]
for i in range(len(lines)):
    visibles.append([False]*len(lines[0]))

maxInRows=[row[0] for row in lines]

for colN in range(1,len(lines[0])-1):
    maxInCol=lines[0][colN]
    for rowN in range(1,len(lines)-1):
        cell=lines[rowN][colN]#number
        if cell>maxInRows[rowN]:
            visibles[rowN][colN]=True
            maxInRows[rowN]=cell
        if cell>maxInCol:
            visibles[rowN][colN]=True
            maxInCol=cell

cols=list(range(1,len(lines[0])-1))
cols.reverse()
maxInRows=[row[-1] for row in lines]
for colN in cols:
    maxInCol=lines[-1][colN]
    rows=list(range(1,len(lines)-1))
    rows.reverse()
    for rowN in rows:
        cell=lines[rowN][colN]#number
        if cell>maxInRows[rowN]:
            visibles[rowN][colN]=True
            maxInRows[rowN]=cell
        if cell>maxInCol:
            visibles[rowN][colN]=True
            maxInCol=cell           
            
            
            
            
visibles[0]=[True]*len(lines[0])
visibles[-1]=[True]*len(lines[0])
for rowN in range(1,len(lines)-1):
    visibles[rowN][0]=True
    visibles[rowN][-1]=True
c=0
for i in visibles:
    c+=len(list(filter(lambda x:x,i)))

print(c)

def su(x,yt,cell):
    c=0
    while yt>=0:
        if lines[yt][x]>=cell:
            c+=1
            break
        c+=1
        yt-=1
    return c
def sd(x,yt,cell):
    c=0
    while yt<=len(lines)-1:
        if lines[yt][x]>=cell:
            c+=1
            break
        c+=1
        yt+=1
    return c
def sl(xt,y,cell):
    c=0
    while xt>=0:
        if lines[y][xt]>=cell:
            c+=1
            break
        c+=1
        xt-=1
    return c
def sr(xt,y,cell):
    c=0
    while xt<=len(lines[0])-1:
        if lines[y][xt]>=cell:
            c+=1
            break
        c+=1
        xt+=1
    return c


maxScore=-1e9
for y in range(1,len(lines)-1):
    for x in range(1,len(lines[0])-1):
        cell=lines[y][x]
        sc=su(x,y-1,cell)*sd(x,y+1,cell)*sl(x-1,y,cell)*sr(x+1,y,cell)
        if sc>maxScore:
            maxScore=sc
print(maxScore)