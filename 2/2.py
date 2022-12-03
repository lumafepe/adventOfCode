reponseShouldBe={
    'A':{
        'X':'Z',
        'Y':'X',
        'Z':'Y',
    },
    'B':{
        'X':'X',
        'Y':'Y',
        'Z':'Z',
    },
    'C':{
        'X':'Y',
        'Y':'Z',
        'Z':'X',
    }
}

reponseShouldBeP={
    'A':{
        'X':1+3,
        'Y':2+6,
        'Z':3+0,
        },
    'B':{
        'X':1+0,
        'Y':2+3,
        'Z':3+6,
        },
    'C':{
        'X':1+6,
        'Y':2+0,
        'Z':3+3,
        },
}

f = open("2.txt", "r")
l=f.readlines()
f.close()
points=0
for line in l:
    line=line[:-1]
    a,b=line.split(' ')
    points+=reponseShouldBeP[a][reponseShouldBe[a][b]]
print(points)
