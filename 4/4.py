f = open("4.txt", "r")
l=f.readlines()
f.close()

def f(s):
    s1,s2=list(map(int,s.split('-')))
    return set(range(s1,s2+1))


total=0
for line in l:
    f1,f2 = map(f,line[:-1].split(','))
    if any(s in f1 for s in f2):
        total+=1
print(total)