finalList = []
firstList = ['*']
s = 1
say = 97
s1 = int(input())
for i in range(s1):
    firstList.append(str(s))
    s+=1
for i in range(s1):
    lane = []
    lane.append((chr(say)))
    say+=1
    for i in range(s1):
        lane. append('x')
    finalList.append(lane)
print(' '.join(firstList))
for i in range(len(finalList)):
    print(' '.join(finalList[i]))

