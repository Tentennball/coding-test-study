import sys
from collections import deque
input = sys.stdin.readline


N, M, V = map(int, input().split())

graph = [[] for _ in range(N)]

# print(graph)


for _ in range(M):
  start, end = map(int, input().split())
  graph[start - 1].append(end - 1)
  graph[end - 1].append(start - 1)
  
for vertex in graph:
  vertex.sort(reverse=True)

# DFS
stack = deque([V-1])
dfs = []

while len(stack):
  next = stack.pop()
  if next in dfs:
    continue
  else:
    dfs.append(next)
    stack.extend(graph[next])

for node in dfs:
  print(node + 1, end=" ")
print()

for vertex in graph:
  vertex.sort()

# BFS
queue = deque([V-1])
bfs = []

while len(queue):
  next = queue.popleft()
  if next in bfs:
    continue
  else:
    bfs.append(next)
    queue.extend(graph[next])

for node in bfs:
  print(node + 1, end=" ")
print()
