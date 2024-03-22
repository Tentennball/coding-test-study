N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
include = [False for _ in range(len(arr))]


def powerSet(i):
  if i == len(arr):
    tmp = 0
    global cnt
    if True not in include:
      return
    for j in range(len(arr)):
      if include[j]:
        tmp += arr[j]
    if tmp == S:
      cnt += 1

  else:
    include[i] = True
    powerSet(i + 1)
    include[i] = False
    powerSet(i + 1)


powerSet(0)
print(cnt)
