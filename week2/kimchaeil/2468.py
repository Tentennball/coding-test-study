#2468번 문제 (안전 영역)
# BFS(너비우선탐색)를 이용하였다
#DFS(깊이우선탐색)을 사용하려 했으나 스택을 이용한 방법의 경우 구현 실패, 재귀를 이용한 방법의 경우 RecursionError(최대 재귀 깊이 초과)

import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(row,column,visited):
    visited[row][column] = True
    que = []
    que.append((row,column))
    while que:
        x, y = que.pop(0)
        for i in range(4):
            x += dx[i]; y += dy[i]
            if 0 <= x < N and 0 <= y < N and not visited[x][y]:
                visited[x][y] = True
                que.append((x,y))
            x -= dx[i]; y -= dy[i]

input = sys.stdin.readline
N = int(input()) #행과 열의 개수

graph=[] #지역 그래프
max_height = 0 #지역 내의 최고 높이
for i in range(N):
    graph.append(list(map(int,input().split())))
    max_height = max(max(graph[i]),max_height)

result = 0
for precipitation in range(max_height):
    visited = [[graph[i][j] <= precipitation for j in range(N)] for i in range(N)] #이미 확인한 곳이거나 강수량보다 높지 않은 곳은 True
    cnt = 0
    for row in range(N):
        for column in range(N):
            if not visited[row][column]:
                BFS(row,column,visited)
                cnt+=1
    result = max(result,cnt)

print(result) #결과 출력