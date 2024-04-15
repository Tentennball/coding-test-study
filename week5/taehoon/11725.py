import sys

N = int(input())
arr = list([] for _ in range(N+1))
parent = [0]*(N+1)
sys.setrecursionlimit(100005)

def dfs(x, par):
    for y in arr[x]:
        if(y==par): continue
        parent[y] = x
        dfs(y, x)


for _ in range(N-1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

dfs(1,-1)
for i in parent:
    if(i==0):
        continue
    print(i)