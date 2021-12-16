import time,sys
import networkx as nx
from collections import Counter,deque
start=time.time()
with open('14.in') as fi:
    polymer,r= fi.read()[:-1].split("\n\n")
lastchar = polymer[-1]
rules = dict()
chCount = dict()
for x in r.split('\n'):
   a,b = x.split(' -> ')
   rules[a]=b

   

def loading(string):
    print "Loading..."
    for i in range(0, 100):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + string)
        sys.stdout.flush()
    print
def step(polymers):
    npolymers = ''
    for x in range(len(polymers)-1):
        npolymers += polymers[x] + rules[polymers[x]+polymers[x+1]]
    npolymers += polymers[-1]
    return npolymers



for i in range(40):
    polymer= step(polymer)
    chCount = Counter()
    for c in polymer:
        chCount[c[0]] += 1
    chCount[lastchar] += 1
    print('part1', max(chCount.values())-min(chCount.values()))
end=time.time()
print(round(end-start,4))
