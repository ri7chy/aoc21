import time
start=time.time()
with open('10.in') as fi:
    a = [lines[:-1] for lines in fi.readlines()]

#for l in a: print(l)

def corrupted(line):
    #print('corrupted',line)
    for i in range(len(line)-1):
        if line[i] in ['(','[','{','<']:
            if line[i+1] not in ['(','[','{','<']:
                return line[i+1]
    return ''

def shorten(line):
    miss = False
    oldline = ''
    while len(line)!=len(oldline):
        oldline = line
        if '()' in line:
            line = line.replace('()','')
        elif '[]' in line:
            line = line.replace('[]','')
        elif '{}' in line:
            line = line.replace('{}','')
        elif '<>' in line:
            line = line.replace('<>','')
    #print(line)
    return line

def score(line):
    print('score of ', line)
    s = 0
    for i in range(len(line)-1,-1,-1):
        if line[i] == '(' : point = 1
        elif line[i] == '[' : point = 2
        elif line[i] == '{' : point = 3
        elif line[i] == '<' : point = 4
        s = s*5 + point
        print(line[i],i, s)
    return s

illegalChar = {')':0,']':0,'}':0,'>':0}
incomplete = []
for l in a:
    char = corrupted(shorten(l))
    if char != '': illegalChar[char] +=1
    else: incomplete += [l]

errorscore = illegalChar[')']*3 + illegalChar[']']*57 + illegalChar['}']*1197 + illegalChar['>']*25137
print(errorscore)
#print(illegalChar)
scores = []
for l in incomplete:
    scores += [score(shorten(l))]
#print(scores)
scores.sort()
print(scores[len(scores)//2])
end=time.time()
print(round(end-start,4))
