
with open("14.txt","r") as f:
    lines=list(map(lambda x:list(map(lambda y:list(map(int,y.split(','))),x[:-1].split(' -> '))),f.readlines()))

maxY=-1e9
minY=0

for line in lines:
    for x,y in line:
        if y>maxY:
            maxY=y

matrix=[]
for i in range(maxY+3):
    m=[]
    for i in range(1000):
        m.append('.')
    matrix.append(m)

for i in range(1000):
        matrix[-1][i]='#'

    


for line in lines:
    x2n,y2=line.pop()
    while line:
        x1n,y1=x2n,y2
        x2n,y2=line.pop()
        if x1n==x2n:
            for i in range(abs(y1-y2)+1):
                if y1>y2: matrix[i+y2][x1n]='#'
                else: matrix[i+y1][x2n]='#'
        else:
            for i in range(abs(x1n-x2n)+1):
                if x1n>x2n: matrix[y1][i+x2n]='#'
                else: matrix[y1][i+x1n]='#'
            
matrix[0][500]='+'

def go_down(x,y):
    x,y=x,y+1
    while matrix[y][x]=='.': y+=1
    return (x,y-1)

def go_left(x,y):
    x,y=x-1,y+1
    if matrix[y][x]=='.': return (x,y)
    return (x+1,y-1)

def go_right(x,y):
    x,y=x+1,y+1
    if matrix[y][x]=='.': return (x,y)
    return (x-1,y-1)      


def moviment(x,y):
    while True:
        x1,y1= go_down(x, y)
        x2,y2 = go_left(x1, y1)
        if x2==x1 and y2==y1:
            x2,y2 = go_right(x1, y1)
            if x2==x1 and y2==y1:
                return (x1,y1)
        x,y=x2,y2
            


sand=0
while matrix[0][500]!='o':
    x,y=500,0
    x1,y1=moviment(x,y)
    matrix[y1][x1]='o'
    sand+=1
print(sand)