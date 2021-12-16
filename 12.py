import time
import networkx as nx
from collections import deque
with open('12.in') as fi:
    a = [lines[:-1].split('-') for lines in fi.readlines()]
G = nx.Graph()
for x,y in a: 
    if y=='start' or x=='end':
        G.add_edge(y,x)    
    else:
        G.add_edge(x,y)    

def findPaths(s,seen,p2):
    #print(s,seen)
    if s =='end':
        #print('end found')
        return 1
    paths = 0
    for neighbor in G.neighbors(s):
        if neighbor.islower():
            if neighbor not in seen:
                paths += findPaths(neighbor,seen | {neighbor},p2)
            elif p2 and neighbor not in {'start','end'}:
                paths += findPaths(neighbor,seen | {neighbor},False)
        else: 
            paths += findPaths(neighbor,seen,p2)
    return paths

def bfs(s,e, p2=False):
    nodes = deque([(s,set(),True)])
    count = 0
    while nodes:
        start, seen, twice = nodes.popleft()
        if start == 'end':
            count += 1
            continue
        if start.islower():
            twice &= start not in seen 
            seen.add(start)
        for neighbor in G.neighbors(start):
            if neighbor not in seen or twice and neighbor != 'start':
                nodes.append((neighbor,seen.copy(),twice if p2 else False))
    return count
start=time.time()
print('bfs it')
print('part1 ',bfs('start','end'))
print('part2 ',bfs('start','end',True))
end=time.time()
print(round(end-start,4))
start=time.time()
print('dfs rek')
print('part1 ',findPaths('start',{'start'},False))
print('part2 ',findPaths('start',{'start'},True))
end=time.time()
print(round(end-start,4))
#options = {
        #'node_color' : '#AAAAAA',
        #'node_size' :500,
        #'with_labels': True,
        #'width' : 3,
        #}
#subax1 = plt.subplot(223)
#nx.draw_spring(G, **options)
#plt.show()
