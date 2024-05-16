import sys
import heapq  

input = sys.stdin.readline
INF = sys.maxsize
problem_no = 1

while True:
  N = int(input())
  if N == 0 : break

  graph = []
  for _ in range(N):
    graph.append(list(map(int, input().split())))
  
  # 특정 위치까지의 비용을 저장(INF로 초기화)
  cost = [[INF for _ in range(N)] for _ in range(N)]
  cost[0][0] = graph[0][0]

  # 시작 위치를 우선수위 큐에 넣고 시작
  h_queue = []
  heapq.heappush(h_queue, (cost[0][0], (0,0)))
  
  while h_queue:
    # 큐에 있는 위치 중 가장 비용이 낮은 위치에 대한 정보를 꺼냄
    curr_cost, pos = heapq.heappop(h_queue)
    x, y = pos
    
    # 꺼낸 위치에 대한 정보가 비용 배열에 저장된 값 보다 크면 고려 x
    if cost[x][y] < curr_cost:
      continue
    
    # 주변 위치 좌표
    aroud = [
      (x + 1, y),
      (x, y + 1),
      (x - 1, y),
      (x, y - 1)
    ]

    # 주변 위치 중 현재 위치를 거쳐서 가능 경우가 더 값이 적은 경우
    # 해당 위치로 가는 비용을 업데이트, 그 후 큐에 해당 주변 위치에 대한 정보 저장
    for ax, ay in aroud:
      if (0 <= ax < N) and (0 <= ay < N):
        tmp_cost = curr_cost + graph[ax][ay]
        if tmp_cost < cost[ax][ay]:
          cost[ax][ay] = tmp_cost
          heapq.heappush(h_queue, (cost[ax][ay], (ax,ay)))

  print(f'Problem {problem_no}: {cost[N-1][N-1]}')
  problem_no += 1
  