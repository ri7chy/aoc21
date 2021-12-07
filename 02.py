import time
start=time.time()
with open('02.in') as f:
    a= f.readlines()
#a=[int(x) for x in a]
h,d= 0,0
for x in a:
   move,steps = x.split(' ')
   steps = int(steps)
   if move == "down":
       d +=steps
   if move == "up":
       d -=steps
   if move == "forward":
       h += steps
print('part1',h*d)

h,d,aim = 0,0,0
for x in a:
   move,steps = x.split(' ')
   steps = int(steps)
   if move == "down":
       aim +=steps
   if move == "up":
       aim -=steps
   if move == "forward":
       h += steps
       d += aim * steps

end=time.time()
print('part2',h*d)
#print('part2',p2)
print(round(end-start,4))
