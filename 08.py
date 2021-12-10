import time
from collections import Counter
start=time.time()
with open('08.in') as fi:
    #a= [[x[0].split(' '),x[1].split(' ')]
    a = [[x.split(' ') for x in lines[:-1].split(' | ')] for lines in fi.readlines()]
def commonletters(digits):
    counter = [Counter(d) for d in digits]
    return sum((counter[0]&counter[1]).values())

def analyse1(entry):
    inp,out = entry
    c = 0
    for o in out:
        if len(o) == 2: c+=1
        if len(o) == 3: c+=1
        if len(o) == 4: c+=1
        if len(o) == 7: c+=1
    return c

def decode(entry):
    entries = entry[0]+ entry[1]
    #precode
    for e in entries:
        if len(e) == 2: one = e
        if len(e) == 3: seven = e
        if len(e) == 4: four = e
        if len(e) == 7: eight =e
    output = ''
    #decode
    for e in entry[1]:
        if len(e) == 2: output += '1'
        elif len(e) == 3: output += '7'
        elif len(e) == 4: output += '4'
        elif len(e) == 7: output += '8'
        elif len(e) == 5:         #2,3,5
            if commonletters([e,one]) == 2:
                output += '3'
            elif commonletters([e,four]) == 3:
                output += '5'
            else:
                output += '2'
        elif len(e) == 6:         #0,6,9
            if commonletters([e,four]) == 4:
                output += '9'
            elif commonletters([e,seven]) == 3:
                output += '0'
            else:
                output += '6'
    return int(output)

print(sum(analyse1(e) for e in a))
print(sum(decode(e) for e in a))
end=time.time()
print(round(end-start,4))
