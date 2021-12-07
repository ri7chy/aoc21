import sys, pygame
from pygame.locals import*
import time
start=time.time()
with open('05.in') as f:
    a= [[(int(x.split(',')[0]),int(x.split(',')[1])) for x in line[:-1].split(" -> ")] for line in f.readlines()]
    vents = dict()
for (sx,sy),(ex,ey) in a:
    dx = 1 if sx<ex else  -1
    dy = 1 if sy<ey else  -1
    if sx == ex:                        #vertical vents
        for y in range(sy,ey+dy,dy):
            if (sx,y) not in vents:
                vents[(sx,y)] = 1
            else:
                vents[(sx,y)] += 1
    if sy == ey:                        #horizontal vents
        for x in range(sx,ex+dx,dx):
            if (x,sy) not in vents:
                vents[(x,sy)] = 1
            else:
                vents[(x,sy)] += 1
print(sum(value > 1 for value in vents.values()))
for (sx,sy),(ex,ey) in a:               #diagonal vents
    dx = 1 if sx<ex else  -1
    dy = 1 if sy<ey else  -1
    steps = abs(sx-ex)+1
    if sx != ex and sy != ey:
        for s in range(steps):
            if (sx+s*dx,sy+s*dy) not in vents:
                vents[(sx+s*dx,sy+s*dy)] = 1
            else:
                vents[(sx+s*dx,sy+s*dy)] += 1
print(sum(value > 1 for value in vents.values()))
end=time.time()
print(round(end-start,4))
n=1000
Color_screen = (0,0,30)
Color_line = (44,44,44)
Color_x= (255,255,102)

def main():
    screen=pygame.display.set_mode((n,n))
    screen.fill(Color_screen)
    for (sx,sy),(ex,ey) in a:
        pygame.draw.line(screen,Color_line,(sx,sy),(ex,ey))
        #pygame.display.flip()
    for v in vents:
        if vents[v] > 1:
            x,y = v
            #print(x,y, vents[v])
            pygame.draw.line(screen,Color_x,v,v)#,(v[0]+1,v[1]+1))
    pygame.display.flip()
    pygame.image.save(screen,"05.png")
    screen.fill(Color_screen)
    while True:
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:

                sys.exit(0)

main()
