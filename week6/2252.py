from collections import deque
n, m = map(int, input().split())

indegree = [0]*n
adj = [[]*n for _ in range(n)]
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    adj[a-1].append(b)
    indegree[b-1]+=1

for i in range(len(indegree)):
    if(indegree[i]==0):
        queue.append(i)
while(queue):
    a = queue.popleft()
    print(a+1, end=" ")
    for i in adj[a]:
        indegree[i-1]-=1
        if(indegree[i-1]==0):
            queue.append(i-1)