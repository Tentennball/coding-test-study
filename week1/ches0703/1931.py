
import sys
# 회의가 끝나는 시간이 빨라야 많은 회의를 할 수 있음 

N = int(input())

schedule_list = []

for _ in range(N):
  schedule_list.append(list(map(int, sys.stdin.readline().split())))

schedule_list.sort(key=lambda x: (x[1],x[0]) )

n = 0
end = 0

for s in schedule_list:
  if s[0] >= end:
    end = s[1]
    n += 1 

print(n)
