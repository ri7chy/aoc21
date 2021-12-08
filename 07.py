import time
from collections import deque
start=time.time()
with open('07.in') as fi:
    a= [int(x) for x in fi.read()[:-1].split(",")]
a= deque(a)

def cost(crabs,pos,p):              #list, position, part1 or 2
    fuel = 0
    #fuel = sum([abs(crabs[i]-pos) if p == 1 else abs(crabs[i]-pos)*(abs(crabs[i]-pos)+1)//2 for i in range(len(crabs))])
    for i in range(len(crabs)):
        s = abs(crabs[i]-pos)
        fuel+= s if p == 1 else s*(s+1)//2
    return fuel

def run(part):
    mincost = 99999999999999
    for p in range(min(a),max(a)):
        ncost = cost(a,p,part)
        if ncost<mincost: mincost = ncost
    return (mincost)


print('part1', run(1))
print('part2', run(2))
end=time.time()
print(round(end-start,4))
