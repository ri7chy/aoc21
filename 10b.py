import time,math
from statistics import median
start=time.time()
with open('10.in') as fi:
    a = [lines[:-1] for lines in fi.readlines()]

score_map = {")":3,"]":57,"}":1197,">":25137}
invert = {')':'(',']':'[','}':'{','>':'<'}
score_map2 = {"(":1,"[":2,"{":3,"<":4}

result = 0
for l in a:
    stack = []
    for c in l:
        if c in '([{<': stack.append(c)
        elif invert[c] != stack.pop():
            result += score_map[c]
            break
print(result)
scores = []
for l in a:
    stack = []
    for c in l:
        if c in '([{<': stack.append(c)
        elif invert[c] != stack.pop():
            break
    else:
        score = 0
        for s in stack[::-1]:
            score = score*5 +score_map2[s]
        scores.append(score)
print(median(scores))

end=time.time()
print(round(end-start,4))
