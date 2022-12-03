file1 = open('1.txt', 'r')
l=file1.readlines()
file1.close()

max=[-1e9,-1e9,-1e9]

def insertO(l,v):
    if v>l[0]:
        if v>l[1]:
            l[0]=l[1]
            if v>l[2]:
                l[1]=l[2]
                l[2]=v
            else:
                l[1]=v
        else:
            l[0]=v
                
elfCount=0
for line in l:
    if line=='\n':
        insertO(max,elfCount)
        elfCount=0
    else:
        elfCount+=int(line[:-1])
insertO(max,elfCount)
print(sum(max))
