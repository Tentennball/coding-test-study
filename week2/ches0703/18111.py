import sys

N, M, B = map(int, sys.stdin.readline().split())

# 특정 높이에 대한 구역이 얼마나 있는지를 저장하는 배열
h_cnt_list = [0 for _ in range(257)]

for _ in range(N):
  for h in map(int, sys.stdin.readline().split()):
    h_cnt_list[h] += 1


min_time = M * N * 256 * 2
opt_h = 0

for test_h in range(256, -1, -1):
  b = B
  time = 0
  for i in range(256, -1, -1):
    if i > test_h:
      diff = h_cnt_list[i] * (i - test_h)
      b += diff
      time += diff * 2
    elif i < test_h:
      diff = h_cnt_list[i] * (test_h - i)
      b -= diff
      time += diff

  if b >= 0 and min_time > time:

    opt_h = test_h
    min_time = time


print(min_time, opt_h)

