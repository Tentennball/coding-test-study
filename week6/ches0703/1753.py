import sys
import heapq  

input = sys.stdin.readline

INF = sys.maxsize
V, E = map(int, input().split())
graph = [[] for _ in range(V)]

start = int(input()) - 1

for _ in range(E):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))

# start노드에서 다른 노드 사이의 거리를 저장(INF로 초기화)
dist = [INF for _ in range(V)]
dist[start] = 0

# 시작 노드를 우선순위 큐에 넣음
queue = []
heapq.heappush(queue, (0, start))

while queue:
    # 경로가 가장 짧은 노드의 정보를 꺼냄
    current_dist, current_node = heapq.heappop(queue)

    # 꺼낸 노드 정보에 대해 경로가 현재 dist에 저장된 값보다 크다면 무시
    if dist[current_node] < current_dist:
        continue

    # 꺼낸 노드를 거쳐서 그래프 상 다음 노드로 갈 때 
    # 꺼낸 노드를 거쳐서 가는 것이 더 짧은 경우 해당 값으로 업데이트
    # 그 후 다음 노드 정보를 우선순위 큐에 넣음
    for next_node, weight in graph[current_node]:
        distance = current_dist + weight
        if distance < dist[next_node]:
            dist[next_node] = distance
            heapq.heappush(queue, (distance, next_node))

for d in dist:
    print('INF' if d == INF else d)
