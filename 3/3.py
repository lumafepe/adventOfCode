f = open("3.txt", "r")
l=f.readlines()
f.close()

def f(s):
    return s[:-1]

total=0
while l:
    l1,l2,l3=set(f(l.pop(0))),set(f(l.pop(0))),set(f(l.pop(0)))
    i=list(l1.intersection(l2,l3))[0]
    if i.isupper(): total+=(ord(i)-64+26)
    else: total+=(ord(i)-96)
print(total)