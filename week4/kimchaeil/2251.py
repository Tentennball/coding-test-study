from collections import deque
import sys

input = sys.stdin.readline
A, B, C = map(int, input().split())

queue = deque()
queue.append((0, 0))

visited = [[False] * (B + 1) for _ in range(A + 1)]
visited[0][0] = True

answer = []

def pour(a_water, b_water):
    if not visited[a_water][b_water]:
        visited[a_water][b_water] = True
        queue.append((a_water, b_water))
        
def bfs():
    while queue:
        a_water, b_water = queue.popleft()
        c_water = C - a_water - b_water
        
        if a_water == 0:
            answer.append(c_water)
            
        #a to b
        move = min(a_water, B - b_water)
        pour(a_water - move, b_water + move)
        #a to c
        move = min(a_water, C - c_water)
        pour(a_water - move, b_water)
        #b to a
        move = min(b_water, A - a_water)
        pour(a_water + move, b_water - move)
        #b to c
        move = min(b_water, C - c_water)
        pour(a_water, b_water - move)
        #c to a 
        move = min(c_water, A - a_water)
        pour(a_water + move, b_water)
        #c to b
        move = min(c_water, B - b_water)
        pour(a_water, b_water + move)
        
bfs()

answer.sort()
for i in answer:
    print(i, end=" ")