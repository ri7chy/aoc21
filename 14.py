import time,sys
import networkx as nx
from collections import Counter,deque
start=time.time()
with open('14.in') as fi:
    polymer,r= fi.read()[:-1].split("\n\n")
lastchar = polymer[-1]
rules = dict()
chCount = dict()
polymers = Counter()

for i in range(len(polymer)-1):
    polymers[polymer[i]+polymer[i+1]] +=1
for x in r.split('\n'):
   a,b = x.split(' -> ')
   rules[a]=b
def step(polymers):
    npolymers = Counter() 
    for x in rules:
        npolymers[rules[x] + x[1]] += polymers[x]
        npolymers[x[0] + rules[x]] += polymers[x]
    return npolymers


for i in range(40):
    polymers= step(polymers)
    if i==9:
        chCount = Counter()
        for c in polymers:
            chCount[c[0]] += polymers[c]
        chCount[lastchar] += 1
        print('part1', max(chCount.values())-min(chCount.values()))
    if i==39:
        chCount = Counter()
        for c in polymers:
            chCount[c[0]] += polymers[c]
        chCount[lastchar] += 1
        print('part2', max(chCount.values())-min(chCount.values()))
end=time.time()
print(round(end-start,4))
