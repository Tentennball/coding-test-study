import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0 for _ in range(N)] # 특정 과목의 선행 과목 수 -> 특정 노드를 가르키는 다른 노드의 수
result = [0 for _ in range(N)]
graph = [[] for _ in range(N)]


for _ in range(M):
  A, B = map(int, input().split())
  graph[A - 1].append(B - 1)
  indegree[B - 1] += 1

# 선행 과목의 수가 0이면 바로 수강 가능
step = 1        # 현재 단계의 학기
queue = deque()
for i in range(N):
  if indegree[i] == 0:
    queue.append(i)   # 수강 처리
    result[i] = step  # 해당 과목의 수강 학기 저장 

prev_step = step # 이전 단계의 학기
step += 1        # 1번 학기에 들을 수 있는 모든 과목을 처리하였으므로 + 1 -> 2번 학기 시작

while queue:
  # 수강한 과목에 대해 해당 과목의 후수 과목 조사
  curr = queue.popleft()
  # 학기가 변경되는 기준 -> 이전 학기의 과목들이 queue에서 다 빠져나온 경우
  if result[curr] != prev_step:
    prev_step = step
    step += 1
  # 수강한 과목의 후수과목에 대해 선행 과목 수를 1 줄임
  for next in graph[curr]:
    indegree[next] -= 1
    # 해당 후수 과목이 선행 과목수가 0이 되면
    if indegree[next] == 0:
      queue.append(next)  # 수강 처리
      result[next] = step # 수강 학기 저장

for s in result:
  print(s, end=' ')