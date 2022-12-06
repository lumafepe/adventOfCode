v=14
with open("6.txt","r") as f:
    line,i=f.readlines()[0],0
    while len(set(line[i:i+v])) != len(line[i:i+v]):
        i+=1
print(i+v)