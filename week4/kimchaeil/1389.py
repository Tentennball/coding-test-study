import sys

input = sys.stdin.readline

N, M = map(int, input().split())

mt = [[N for _ in range(N)] for _ in range(N)]

for _ in range(N):
    mt[_][_] = 0

for _ in range(M):
    i, j = map(int, input().split())
    mt[i-1][j-1] = 1; mt[j-1][i-1]=1

for via in range(N):
    for start in range(N):
        for end in range(N):
            if mt[start][end] <= 1: continue
            mt[start][end] = min(mt[start][end], mt[start][via]+mt[via][end])

result = []
for _ in range(N):
    result.append(sum(mt[_]))

print(result.index(min(result))+1)