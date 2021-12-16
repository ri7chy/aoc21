import time
import pygame,sys
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
colours = {
    'screen' : '#0f0f23',
    'gray' :(44,44,44),
    'notflash' :(80,80,80),
    'nearflash' : (150,150,82),
    'flash' : (255,255,102)
}

screen=pygame.display.set_mode((500,550))
pygame.font.init()
thisfont = pygame.font.SysFont('couriernew', 50)

def display():
    thisfont = pygame.font.SysFont('couriernew', 40,False)
    screen.fill(colours['screen'])
    text = thisfont.render('n='+str(n),True,colours['nearflash'])
    screen.blit(text,(0,500))
    text = thisfont.render('flashes='+str(result),True,colours['nearflash'])
    screen.blit(text,(150,500))
    for r,row in enumerate(a):
        for c,col in enumerate(row):
            thisfont = pygame.font.SysFont('couriernew', 50,False)
            if -1<n<10 or 254<n<258: x = str(a[r][c])
            else: x = '*'
            if 1==a[r][c]:
                text = thisfont.render(x,True, colours['gray'])
            elif 1< a[r][c] < 8:
                text = thisfont.render(x,True, colours['notflash'])
            elif 8<=a[r][c] <= 9:
                text = thisfont.render(x,True, colours['nearflash'])
            else: 
                thisfont = pygame.font.SysFont('couriernew', 50,True)
                text = thisfont.render(x,True, colours['flash'])
            #print(text)
            screen.blit(text,(c*50,r*50))
    pygame.display.update()
    pygame.display.flip()
    if n<5: time.sleep(0.6)
    elif n<12: time.sleep(0.3)
    elif n<18: time.sleep(0.1)
    elif n<40: time.sleep(0.02)
    elif n<100: time.sleep(0.01)
    elif n<255: time.sleep(0.004)
    elif n<256: time.sleep(0.3)
    elif n<257: time.sleep(0.4)
    elif n<258: time.sleep(0.7)
    else : time.sleep(2)
    while False:
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:

                sys.exit(0)

while not done:
    
    n += 1
    flashes, fl = step()
    result += flashes
    #print(flashes)
    display()
    #time.sleep(0.05)
    
    if n == 100:
        print(result)
    if len(fl)==10*10:
        done = True
        print(n)

end=time.time()
print(round(end-start,4))
