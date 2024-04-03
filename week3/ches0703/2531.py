import sys

# 입력
N, d, k, c = map(int, sys.stdin.readline().split())
belt = []
for _ in range(N):
  belt.append(int(sys.stdin.readline()))

# 윈도우를 이동시키며 set형태로 변환
# set -> 중복된 요소 삭제. 즉 set의 길이가 해당 윈도우 내의 초밥 종류가 됨
# set에 c가 포함되는 지를 확인 하여 초밥 종류를 파악하여 최대 종류 수를 업데이트한다
window_list = []
max_kind_of_sushi = 0
for i in range(N):
  window = None
  if i + k <= N:
    window = set(belt[i:i + k])
  else:
    window = set(belt[i:] + belt[:((i + k) - N)])
  kind_of_sushi = len(window)
  if c not in window:
    kind_of_sushi += 1

  if kind_of_sushi > max_kind_of_sushi:
    max_kind_of_sushi = kind_of_sushi 


print(max_kind_of_sushi)
