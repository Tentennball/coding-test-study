import sys
from collections import deque
si = sys.stdin.readline
T = int(si())
for _ in range(T):
    N, K = map(int, si().split())
    t = [0]+list(map(int, si().split()))
    tdone = [0]*(N+1)
    indegree = [0]*(N+1)
    adj = [[]*(N+1) for _ in range(N+1)]

    queue = deque()
    for i in range(1, K+1):
        a, b = map(int, si().split())
        adj[a].append(b)
        indegree[b]+=1

    for i in range(1, N+1):
        if(indegree[i]==0):
            queue.append(i)
            tdone[i] = t[i]
    while(queue):
        a = queue.popleft()
        for i in adj[a]:
            indegree[i]-=1
            if(indegree[i]==0):
                queue.append(i)
            tdone[i] = max(tdone[i], tdone[a]+t[i])

    ans = int(si())
    print(tdone[ans])