import time
start=time.time()
a=open('01.in').read().split("\n")[:-1]
a=[int(x) for x in a]
p1,p2,prev=0,0,0
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        p1+=1

for i in range(len(a)-2):
    x = a[i] + a[i+1] + a[i+2]
    if prev<x and i!=0:
        p2+=1
    prev = x

end=time.time()
print('part1',p1)
print('part2',p2)
print(round(end-start,4))
