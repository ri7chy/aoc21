import time
from queue import PriorityQueue
start=time.time()
with open('15.tst') as fi:
    cave =[[int(x) for x in line[:-1]] for line in fi.readlines()]
height = len(cave)
width = len(cave[0])
Q = dict()
for r in range(height):
    for c in range(width):
        Q[(r,c)] = cave[r][c]
def adjacent(r,c):
    dr,dc = [1,0,-1,0],[0,1,0,-1]
    adj=dict()
    for i in range(4):
        cc,rr = c + dc[i], r + dr[i]
        if 0 <=cc <= width and 0 <= rr <= height and (rr,cc) in Q:
            adj[(rr,cc)] = Q[(rr,cc)]
    #print(adj)
    return adj
def updatequeue(nodes,x,newrisk):
    newnodes = PriorityQueue()
    while nodes.queue != []:
        risk, node = nodes.get()
        if node ==x:
            if risk<=newrisk:
                newnodes.put((risk,node))
            else:
                print('found doubles','old',risk,node,'new',newrisk,x)
                newnodes.put((newrisk,node))
        else:
            newnodes.put((risk,node))
    return newnodes

def dijsktra(r,c):
    visited = dict()
    S = dict()
    newnodes = PriorityQueue()
    newnodes.put((0,(r,c)))
    while len(newnodes.queue):
        risk, (r,c)= newnodes.get()
        print('ACTUAL NODE',r,c,'risk',risk)
        #print(newnodes.queue)
        for x in adjacent(r,c): 
            changed = False
            for i in range(len(newnodes.queue)):
                if x == newnodes.queue[i][1]: 
                    newnodes = updatequeue(newnodes, x, Q[x]+risk)
                    changed = True
            if not changed: newnodes.put((Q[x]+risk,x))
        print(newnodes.queue)
        S[(r,c)] = risk
        print('Seen\n',S)
        Q.pop((r,c))
        if (height-1,width-1) in S.keys():
            print('part1',S[(height-1,width-1)])

            return(S)


dijsktra(0,0)
end=time.time()
print(round(end-start,4))
