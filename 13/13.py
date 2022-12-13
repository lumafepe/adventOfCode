
with open("13.txt","r") as f:
    lines=list(map(lambda x:x[:-1],f.readlines()))
packets=[[[2]],[[6]]]


def compare(x1,x2): #1 0 -1
    if type(x1)==int and type(x2)==int: return 1 if x1<x2 else 0 if x1==x2 else -1
    elif type(x1)==list and type(x2)==list:
        i=0
        while i<min(len(x1),len(x2)):
            r=compare(x1[i], x2[i])
            if r==1 or r==-1:return r
            i+=1
        if len(x1)==len(x2): return 0
        if len(x1)==i: return 1
        else: return -1
    else:
        if type(x1) == int:x1=[x1]
        if type(x2) == int:x2=[x2]
        return compare(x1, x2)
           

while lines:
    exec(f"l1={lines.pop(0)}")
    exec(f"l2={lines.pop(0)}")
    lines.pop(0)
    packets.append(l1)
    packets.append(l2)
    
f=True
while f:
    f=False
    for j in range(1,len(packets)):
        if compare(packets[j-1], packets[j])==-1:
            t=packets[j-1]
            packets[j-1]=packets[j]
            packets[j]=t
            f=True
    
print((packets.index([[2]])+1)*(packets.index([[6]])+1))