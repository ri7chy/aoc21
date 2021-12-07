import time
from collections import deque
start=time.time()
with open('07.in') as fi:
    a= [int(x) for x in fi.read()[:-1].split(",")]
a= deque(a)

def cost(crabs,pos,p):              #list, position, part1 or 2
    fuel = 0
    for i in range(len(crabs)):
        s = abs(crabs[i]-pos)
        fuel+= s if p == 1 else s*(s+1)/2
    return fuel

def run(part):
    costs = []
    for p in range(min(a),max(a)): costs = costs + [cost(a,p,part)]
    return min(costs)
print('part1', run(1))
print('part2', run(2))
end=time.time()
print(round(end-start,4))
