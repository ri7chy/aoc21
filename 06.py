import time
start=time.time()
with open('06.in') as fi:
    a= [int(x) for x in fi.read()[:-1].split(",")]

fishs = dict()
for age in range(9): fishs[age]= sum(x==age for x in a)

def ticks(f):
    newborn = f[0]
    for i in range(8):
        if i!= 6: f[i] = f[i+1]
        else:     f[i] = f[i+1]+newborn
    f[8] = newborn
    return f

for i in range(256):
    fishs = ticks(fishs)
    if i == 79:    print("part1", sum(fishs.values()))
print("part2", sum(fishs.values()))

end=time.time()
print(round(end-start,4))
