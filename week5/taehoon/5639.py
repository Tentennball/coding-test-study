import sys
sys.setrecursionlimit(10005)
values = []
si = sys.stdin.readline
def travel(l, r):
    if(l>r): return
    mid = r
    for i in range(l+1, r+1):
        if(values[i]>values[l]):
            mid = i-1
            break
    travel(l+1, mid)
    travel(mid+1, r)
    print(values[l])

while(True):
    line = si()
    if not line:
        break
    values.append(int(line))

travel(0, len(values)-1)