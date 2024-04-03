import sys

input = sys.stdin.readline

N = int(input())

mt =[]

for _ in range(N):
    mt.append(list(map(int,input().split())))

for via in range(N):
    for start in range(N):
        for end in range(N):
            if mt[start][end]==1:
                continue
            if mt[start][via]+mt[via][end]>1:
                mt[start][end]=1

result = []
for _ in range(N):
    result.append(" ".join(map(str,mt[_])))
print("\n".join(result))