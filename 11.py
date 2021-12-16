import time
start=time.time()
with open('11.in') as fi:
    a = [[int(x) for x in lines[:-1]] for lines in fi.readlines()]

dr = [1,0,-1,0,1,-1,1,-1]
dc = [0,1,0,-1,1,1,-1,-1]
height = len(a)
width = len(a[0])
def flashing(r,c,octo): #flashing octopuses recursively
    for i in range(8):
        rr,cc = r+dr[i], c+dc[i]
        if rr>=0 and cc >= 0 and rr < height and cc < width:
            a[rr][cc] +=1
            if (rr,cc) not in octo and a[rr][cc] >9:
                octo.add((rr,cc))
                octo = octo.union(flashing(rr,cc,octo))
    return octo

def step():
    flashes =0
    flashed = set()
    for r,row in enumerate(a):
        for c,col in enumerate(row):
            a[r][c]+= 1
    for r,row in enumerate(a):
        for c,col in enumerate(row):
            if a[r][c]> 9 and (r,c) not in flashed: #flashes
                flashed.add((r,c))
                flashed = flashed.union(flashing(r,c,flashed))
    for r,row in enumerate(a):
        for c,col in enumerate(row):
            if a[r][c] > 9: #flashes
                flashes += 1
                a[r][c]= 0

    return flashes,flashed
result = 0
n=0
done = False
while not done:
    n += 1
    flashes, fl = step()
    result += flashes
    #print(flashes)
    if n == 100:
        print(result)
    if len(fl)==10*10:
        done = True
        print(n)
end=time.time()
print(round(end-start,4))
