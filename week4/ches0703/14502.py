import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

lap = []
max_safe = 0
for _ in range(N):
  lap.append(list(map(int, input().split())))


# 벽을 세울 수 있는 모든 경우의 수에 대해 
# 세운 벽의 수가 3이면 안전영역 검사 
def wall(wall_count):
  if wall_count == 3:
    virus_bfs()
    return
  for row in range(N):
    for col in range(M):
      if lap[row][col] == 0:
        lap[row][col] = 1
        wall(wall_count + 1)
        lap[row][col] = 0


def virus_bfs():

  virus_spread_map = [[-1 for _ in range(M)] for _ in range(N)]
  # 바이러스가 확산 된 멥 생성
  for row in range(N):
    for col in range(M):
      if (lap[row][col] == 2):
        virus_spread_map[row][col] = 2
        queue = deque([(row, col)])
        while len(queue):
          curr = queue.popleft()
          around = [
            (curr[0] - 1, curr[1]),
            (curr[0] + 1, curr[1]),
            (curr[0], curr[1] - 1),
            (curr[0], curr[1] + 1)
          ]
          for pos in around:
            if(0 <= pos[0] and pos[0] < N)   and \
              (0 <= pos[1] and pos[1] < M)   and \
              (virus_spread_map[pos[0]][pos[1]] == -1)  and \
              (lap[pos[0]][pos[1]] == 0):
              queue.append((pos[0], pos[1]))
              virus_spread_map[pos[0]][pos[1]] = 2
  # 확산 된 맵에서 안전지대의 수 계산
  safe_cnt = 0
  for row in range(N):
    for col in range(M):
      if virus_spread_map[row][col] == 0:
        safe_cnt += 1
  global max_safe
  max_safe = max(max_safe, safe_cnt)


def solve():
  wall(0)
  print(max_safe)

solve()