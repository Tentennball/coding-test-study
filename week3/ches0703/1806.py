import sys
input = sys.stdin.readline

N, S = map(int, input().split())


numbers = list(map(int, input().split()))
min_length = sys.maxsize
start = end = 0
sum = 0
while True:
  if sum >= S:
    if min_length > end - start:
      min_length = end - start
    sum -= numbers[start]
    start += 1
  elif end == N:
    break
  else:
    sum += numbers[end]
    end += 1

if min_length == sys.maxsize:
  print(0)
else:
  print(min_length)


