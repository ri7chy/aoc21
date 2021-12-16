import time
import networkx as nx
from collections import deque
start=time.time()
with open('13.in') as fi:
    p,folds = fi.read()[:-1].split("\n\n")
points = {tuple(int(x) for x in l.split(',')) for l in p.split('\n')}
folds = [x.split(' ')[2].split('=') for x in folds.split('\n')]

def minmax():
    maxc,maxr,minc,minr =0,0,10000,10000
    for x in points:
        if maxc<x[0]: maxc =x[0]
        if maxr<x[1]: maxr =x[1]
        if minc>x[0]: minc =x[0]
        if minr>x[1]: minr =x[1]
    return maxc,maxr,minc,minr

def translatetoLeft(cur,ax):
    return cur - 2*(cur-ax)

def translatetoRight(cur,ax):
    return cur + 2*(cur-ax)

def fold(points,vertical, number):
    npoints = set()
    maxc,maxr,minc,minr = minmax()
    if vertical == 'x':
        if number>= (maxc-minc)//2:
            #print('folding horizontal',vertical, number,'left' )
            for cCol,cRow in points:
                if cCol > number:
                    npoints.add((translatetoLeft(cCol,number),cRow))
                else: #cCol <= number
                    npoints.add((cCol,cRow))
        else:
            #print('folding horizontal',vertical, number,'right' )
            for cCol,cRow in points:
                if cCol > number:
                    npoints.add((cCol,cRow))
                else: #cCol <= number
                    npoints.add((translatetoRight(cCol,number),cRow))
    if vertical == 'y':
        if number>= (maxr-minr)//2:
            #print('folding vertical',vertical, number,'up' )
            for cCol,cRow in points:
                if cRow > number:
                    npoints.add((cCol,translatetoLeft(cRow,number)))
                else: #cCol <= number
                    npoints.add((cCol,cRow))
        else:
            #print('folding vertical',vertical, number,'up' )
            for cCol,cRow in points:
                if cRow > number:
                    npoints.add((cCol,cRow))
                else: #cCol <= number
                    npoints.add((cCol,translatetoRight(cRow,number)))

    return npoints
n=0
for direction,line in folds:
    points = fold(points,direction,int(line))
    if n==0: 
        n+=1
        print('part1 ',len(points))

maxc,maxr,minc,minr = minmax()
print('part2')
for Row in range(minr,maxr+1):
    out = ''
    for Col in range(minc,maxc+1):
        if (Col,Row) in points:
            out += '█'
        else:
            out += ' '
    print(out)

end=time.time()
print(round(end-start,4))
