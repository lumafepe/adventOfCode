with open("10.txt","r") as f:
    lines=list(map(lambda x:x[:-1],f.readlines()))


cycles=1
register=1

class Processor:
    cycles:int
    register:int
    
    def __init__(self):
        self.cycles=1
        self.register=1
        self.applyingAdd=False
        self.valueToAdd=0
        self.signals=[]
        self.screen=240*['.']
        
    def add(self,v=0):
        if not self.applyingAdd: self.valueToAdd=v
        else: self.register+=self.valueToAdd
        self.applyingAdd=not self.applyingAdd

    def process(self,lines:list[str]):
        while lines:
            self.signals.append(self.cycles*self.register)
            if abs(self.register-(self.cycles-1)%40)<=1: self.screen[self.cycles-1]='#'
            if self.applyingAdd:
                self.add()
            else:
                line=lines.pop(0)
                if line.startswith('addx'):
                    self.add(int(line.split(' ')[1]))
            self.cycles+=1
    
P=Processor()
P.process(lines)
print(sum([P.signals[i] for i in range(20,len(P.signals)-1,40)]))
for i in range(0,len(P.screen)-1,40):
    print("".join(P.screen[i:i+40]))