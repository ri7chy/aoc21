import time
start=time.time()
with open('03.in') as f:
    a=[x[:-1] for x in  f.readlines()]
a_copy = a.copy()
gamma = ''
eps= ''
#part1##################
for i in range(len(a[0])):
    z,o = 0,0
    for line in a:
        if line[i] =='1': o+=1
        else:   z+=1
    #print(z,o)
    if z>o:
        gamma = gamma+'0'
        eps= eps+'1'
    else:
        gamma = gamma +'1'
        eps= eps+'0'
#part2##################
for i in range(len(a[0])):
    z,o = 0,0
    for line in a:
        if line[i] =='1': o+=1
        else:   z+=1
    newlist = []
    if z<=o:
        for line in a:
            if line[i]=='1':
               newlist +=[line]
    else:
        for line in a:
            if line[i]=='0':
               newlist +=[line]
    a=newlist
    if len(a)==1: break
oxy=a[0]
a = a_copy
for i in range(len(a[0])):
    z,o = 0,0
    for line in a:
        if line[i] =='1': o+=1
        else:   z+=1
    newlist = []
    if z<=o:
        for line in a:
            if line[i]=='0':
               newlist +=[line]
    else:
        for line in a:
            if line[i]=='1':
               newlist +=[line]
    a=newlist
    if len(a)==1: break
co2=a[0]
print('part1', int(gamma,2)*int(eps,2))
print('part2', int(oxy,2)*int(co2,2))
end=time.time()
#print('part2',h*d)
#print('part2',p2)
print(round(end-start,4))
