import time
start=time.time()
with open('09.in') as fi:
    a = [[int(x) for x in lines[:-1]] for lines in fi.readlines()]

height = len(a)
width = len(a[0])

def compare(r,c):
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    lowpoint = True
    for i in range(4):
        rr,cc = r+dr[i],c+dc[i]
        if rr>=0 and cc >= 0 and rr < height and cc < width:
            if a[r][c] >= a[rr][cc]: lowpoint = False

    return lowpoint

def main1():
    risklvl = 0
    for r in range(height):
        for c in range(width):
            if compare(r,c):
                risklvl += 1 + a[r][c]
    print(risklvl)
#First try for a recursive solution ... output is to low.
def compare_rek(r,c,basin):         # ro, co - origin
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    lowpoint = True
    compared = 0
    for i in range(4):
        rr,cc = r+dr[i],c+dc[i]
        if (rr,cc) not in basin and rr>=0 and cc >= 0 and rr < height and cc < width:
            if a[r][c] >= a[rr][cc]:
                lowpoint = False
            compared +=1 #to avoid, that an isolated high is counted
    if lowpoint and compared > 0:
        basin.add((r,c))
        for i in range(4):
            rr,cc = r+dr[i],c+dc[i]
            if (rr,cc) not in basin and rr>=0 and cc >= 0 and rr < height and cc < width:
                basin.union(compare_rek(rr,cc,basin))
    return basin

def main2b(): # main for part 2 with recursion / this solution finds not the exact basins
    basins = []
    for r in range(height):
        for c in range(width):
            basin = compare_rek(r,c,set())
            if len(basin) > 0:
                basins += [len(basin)] #compare_rek(r,c,-1,-1)

    print(basins)
    prod = 1
    for i in range(3):
        maximum = max(basins)
        basins.remove(maximum)
        print(maximum)
        prod *=maximum
    print(prod)

#solution for part 2 ... checking the borders by 9 and creating sets of basins
def checkadjacent(r,c,basins):
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    added = False
    if len(basins)==0:
        basins += [set({(r,c)})]
    else:
        for b in basins:
            for i in range(4):
                rr,cc = r+dr[i],c+dc[i]
                if (rr,cc) in b and a[rr][cc]!= 9 and rr>=0 and cc >= 0 and rr < height and cc < width:
                    b.add((r,c))
                    added = True
        if not added:
            basins += [set({(r,c)})]
            if r==0 and c==6: exit()
    return basins
# diagonal items created some new basin-sets wich belong togehter.. they are joined here.
def joinbasins(basins):
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    final=[]
    while (len(basins))!=0:
        found =False
        f2= None
        for r,c in b:
            for i in range(4):
                rr,cc = r+dr[i],c+dc[i]
                for b2 in basins:
                    if (rr,cc) in b2 and len(b.union(b2))!=len(b2) and not found:
                        f2 = b2
                        found = True
        if f2!=None:
            final += [b.union(f2)]
            basins.remove(f2)
        else:
            final += [b]
    return final

def main2():
    fin, bas = [],[]
    for r in range(height):
        for c in range(width):
            if a[r][c]!= 9:
                bas = checkadjacent(r,c,bas)
    fin= bas
    while len(fin) != len(joinbasins(fin.copy()
        fin = joinbasins(fin.copy())
    lenghts =[]
    for f in fin:
        lenghts+=[len(f)]
    prod = 1
    for i in range(3):
        maximum = max(lenghts)
        lenghts.remove(maximum)
        print(maximum)
        prod *=maximum
    print(prod)

main1()
main2()

end=time.time()
print(round(end-start,4))
