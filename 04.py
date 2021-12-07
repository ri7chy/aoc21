import time
start=time.time()
with open('04.in') as f:
    a= f.read().split("\n\n")
calls = [int(x) for x in a[0].split(',')]
players = [[[int(row[i:i+2]) for i in range(0,len(row),3)] for row in p.split('\n')] for p in a[1:]]

def checkwin(x,actualcall):
    win=False
    hits = [[0 for i in range(5)] for r in range(5)]
    for r in range(5):
        for c in range(5):
            if x[r][c] in actualcall:
                hits[r][c] +=1
    for r in hits:
        count = 0
        for c in r: count +=c
        if count==5:
            win = True
    for c in range(5):
        count = 0
        for r in range(5):
            count +=hits[r][c]
        if count==5:
            win = True
    score = 0
    if win:
        for r in range(5):
            for c in range(5):
                if x[r][c] not in actualcall:
                    score += x[r][c]
    return win,score

winners = []
for i in range(len(calls)):
    for p in players:
        win, score = checkwin(p, calls[:i])
        if win:
            if p not in winners: winners+= [p]
        if len(winners) == 1 and score!=0:
            print('first', score*calls[i-1])
        if len(winners) == 100:
            print('last', score*calls[i-1])
    for w in winners:
        if w in players:
            players.remove(w)
end=time.time()
print(round(end-start,4))
