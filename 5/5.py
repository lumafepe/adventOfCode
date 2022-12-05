f = open("5.txt", "r")
lines=f.readlines()
f.close()


l=[['T','V','J','W','N','R','M','S'],
['V','C','P','Q','J','D','W','B'],
['P','R','D','H','F','J','B'],
['D','N','M','B','P','R','F'],
['B','T','P','R','V','H'],
['T','P','B','C'],
['L','P','R','J','B'],
['W','B','Z','T','L','S','C','N'],
['G','S','L']]
dock={}
for k,i in enumerate(l):
    i.reverse()
    dock[str(k+1)]=i


for line in lines:
    line=line[:-1].split(' ')
    t=[dock[line[3]].pop() for i in range(int(line[1]))]
    t.reverse()
    dock[line[5]]+=t
        
print("".join(i[-1] for i in l))