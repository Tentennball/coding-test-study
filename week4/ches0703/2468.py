import sys
from collections import deque
input = sys.stdin.readline


# 입력
N = int(input())
area = []

for _ in range(N):
  area.append(list(map(int, input().split())))

# 반복 수를 줄이기 위해 최소 높이, 최대 높이 계산
min_h = min(map(min, area))
max_h = max(map(max, area))

max_cnt = 1   # 최대 안전지대 수
for h in range(min_h, max_h):
  # 해당 높이에 대한 안전 지대 수
  cnt = 0 
  # 해당 높이에 대해 검사를 진행할 때, 이미 안전지대로 배정된 위치인지 표시할 배열
  checked_area = [[False for _ in range(N)] for _ in range(N)]

  # 각 지역에 대해 dfs 수행
  for row in range(N):
    for col in range(N):
      # 단, 이미 언전지대로 배정되었거나 높이가 낮은 면 제외
      if checked_area[row][col] or area[row][col] <= h:
        continue
      else:
        checked_area[row][col] = True
        stack = deque([(row, col)])
        while len(stack):
          next = stack.pop()
          around = [(next[0] + 1, next[1]),  # bottom
                    (next[0] - 1, next[1]),  # top
                    (next[0], next[1] + 1),  # right
                    (next[0], next[1] - 1)]  # left
          # 주변 위치에 대해 해당 위치가 유효한 경우 큐에 추가
          for pos in around:
            if(0 <= pos[0] and pos[0] < N)        and \
              (0 <= pos[1] and pos[1] < N)        and \
              (not checked_area[pos[0]][pos[1]])  and \
              (area[pos[0]][pos[1]] > h):
              stack.append(pos)
              checked_area[pos[0]][pos[1]] = True
        cnt += 1
  max_cnt = max(cnt, max_cnt)

print(max_cnt)



# 고민
# 시간복잡도를 낮추기 위해 고민
# 1. 결과를 저장하는 bfs 배열 굳이 필요하지 않았음을 알게 됨(checked_area로 대체 가능)
# -> bfs에 값을 추가하고, bfs에 특정 위치의 값이 있는지 검사하는 로직을 제외할 수 있었음
# 3. 최소 높이, 최대 높이를 구해 높이에 대한 반복 수를 줄임