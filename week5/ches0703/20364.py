import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# 완전 이진트리이므로 배열 활용
ground = [False for _ in range(N + 1)]

def check(loc):
  global ground
  # 특정 노드 까지의 경로(경유 노드, 역순으로 저장됨)
  path = [loc]
  while path[-1]:
    path.append(path[-1] // 2)

  for stopover in reversed(path):
    if ground[stopover]:
      return stopover
  ground[loc] = True
  return 0


for _ in range(Q):
  loc = int(input())
  print(check(loc))


