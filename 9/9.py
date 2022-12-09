with open("9.txt","r") as f:
    lines=list(map(lambda x:x[:-1].split(),f.readlines()))
signoid = lambda x: 0 if x==0 else -1 if x<0 else 1
class Head:
    x:int
    y:int
    def __init__(self):
        self.x=0
        self.y=0
    def move(self,d:str):
        if d=='U': self.y+=1
        elif d=='R': self.x+=1
        elif d=='D': self.y-=1
        else: self.x-=1
class Tail:
    x:int
    y:int
    visited:set[int,int]
    def __init__(self):
        self.x=0
        self.y=0
        self.visited={(0,0)}
    def follow(self,head:Head):
        if abs(head.x-self.x)>1 or abs(head.y-self.y)>1:
            self.y+=signoid(head.y-self.y)
            self.x+=signoid(head.x-self.x)
            self.visited.add((self.x,self.y))
    
heads=[Head()]
for i in range(9):
    heads.append(Tail())
    
for m,d in lines:
    for i in range(int(d)):
        for n,t in enumerate(heads):
            if n==0:
                heads[n].move(m)
            else:
                t.follow(heads[n-1])
print(len(heads[-1].visited))