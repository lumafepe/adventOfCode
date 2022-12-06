with open("6.txt","r") as f:
    lines,i,f=f.readlines(),0,14
    while len(set(lines[0][i:f])) != len(lines[0][i:f]):
        i,f=i+1,f+1
print(f)
        
