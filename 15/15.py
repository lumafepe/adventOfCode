import multiprocessing
with open("15.txt","r") as f:
    lines=list(map(lambda x:
        list(map(lambda y: list(map(lambda z:int(z),y.split(', '))),x[:-1].replace('Sensor at x=','').replace('y=','').replace(' closest beacon is at x=','').split(':')
    )),f.readlines()))



def p(y):
    intervalos = []

    for s,b in lines:
        sx, sy=s
        bx, by=b
        d = abs(sx-bx)+abs(sy-by)
        if d - abs(sy - y) < 0: continue        
        intervalos.append((sx - (d - abs(sy - y)), sx + (d - abs(sy - y))))

    intervalos.sort()

    inters = []

    for menor, maior in intervalos:
        if not inters:
            inters.append((menor, maior))
            continue

        menorX, maiorX = inters[-1]

        if menor > maiorX + 1:
            inters.append((menor, maior))
            continue
        
        inters[-1] = (menorX,max(maiorX, maior))
    
    x = 0
    for menor, maior in inters:
        if x < menor:
            print(x * 4000000 + y)
            break
        if maior + 1>x: x=maior + 1
        if x > 4000000: break
    






with multiprocessing.Pool() as pool:
    pool.map(p, range(4000000 + 1))
