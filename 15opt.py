import time
from queue import PriorityQueue
start=time.time()
with open('15.in') as fi:
    raw=[[int(x) for x in line[:-1]] for line in fi.readlines()]
height = len(raw)
width = len(raw[0])
def cave(times):
    Q = dict()
    for r in range(height):
        for c in range(width):
            for ri in range(times):
                for ci in range(times):
                    x = (raw[r][c]+ci+ri) 
                    Q[(r+height*ri,c+width*ci)] = x if x<10 else x-9
    return Q

def adjacent(Q,r,c,h,w):
    dr,dc = [1,0,-1,0],[0,1,0,-1]
    adj=dict()
    for i in range(4):
        cc,rr = c + dc[i], r + dr[i]
        if 0 <=cc <= w and 0 <= rr <= h and (rr,cc) in Q:
            adj[(rr,cc)] = Q[(rr,cc)]
    return adj

def dijsktra(Q,r,c,h,w):
    visited = dict()
    S = dict()
    newnodes = dict()
    newnodes[(r,c)]= 0
    while len(newnodes):
        (r,c)= min(newnodes,key=newnodes.get)
        risk = newnodes.pop((r,c))
        for x in adjacent(Q,r,c,h,w): #insertin new nodes
            changed = False
            if x in newnodes.keys():  #checking for doubles
                if Q[x]+risk<newnodes[x]: 
                    newnodes[x]=Q[x]+risk
                changed = True
            if not changed: 
                newnodes[x]=Q[x]+risk
        S[(r,c)] = risk
        Q.pop((r,c))
        if (h-1,w-1) in S.keys():
            print('part',S[(h-1,w-1)])
            return(S)

dijsktra(cave(1),0,0,height*1,width*1)
dijsktra(cave(5),0,0,height*5,width*5)
end=time.time()
print(round(end-start,4))
