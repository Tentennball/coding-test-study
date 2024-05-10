import sys
from collections import deque
si = sys.stdin.readline

N = int(si())
T = [0]*(N+1)
indegree = [0]*(N+1)
Tdone = [0]*(N+1)

adj = [[]*(N+1) for _ in range(N+1)]
queue = deque()

for i in range(1, N+1):
    inputs = list(map(int, si().split()))
    T[i] = inputs[0]
    indegree[i] = inputs[1]
    for j in range(2, len(inputs)):
        adj[inputs[j]].append(i)
for i in range(1, N+1):
    if(indegree[i]==0):
        queue.append(i)
        Tdone[i] = T[i]

while(queue):
    a = queue.popleft()
    for i in adj[a]:
        indegree[i]-=1
        if(indegree[i]==0):
            queue.append(i)
        Tdone[i] = max(Tdone[i], Tdone[a]+T[i]) # a는 이전노드고 T[i]는 후의 노드에 누적해주는거
print(Tdone)
print(Tdone[-1])