import sys

input = sys.stdin.readline

def back_tracking(start, depth):
    global visited
    if depth == 5:
        return True
    visited[start]=True
    for _ in friend[start]:
        if not visited[_]:
            if back_tracking(_, depth+1):
                return True
    visited[start]=False
    return False

N, M = map(int, input().split())
visited = [False for _ in range(N)]
friend = [[] for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    friend[i].append(j); friend[j].append(i)

found = False
for _ in range(N):
    if back_tracking(_, 1):
        found = True
        break
if found: print(1)
else: print(0)