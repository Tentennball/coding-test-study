import sys


N, X = map(int, sys.stdin.readline().split())

visit_list = list(map(int, sys.stdin.readline().split()))

# 특정 기간의 방문자 수의 합을 저장할 리스트
sum_list = [sum(visit_list[0:X])]
# 반복문 상 이전 기간의 방문자 수의 합
prev_sum = sum_list[0]
# 반복문 상 이전 기간 시작날 방문자 수
prev_start_val = visit_list[0]
for i in range(X, N):
  # 현재 기간 방문자 수의 합 = 이전 기간의 방문자 수의 합 - 상 이전 기간 시작날 방문자 수 + 현재 기간의 마지막 날 방문자 수
  sum_list.append(prev_sum - prev_start_val + visit_list[i])
  prev_start_val = visit_list[i-X + 1]
  prev_sum = sum_list[-1]

max_sum = max(sum_list)

if max_sum == 0:
  print("SAD")
else:
  print(max_sum)
  print(sum_list.count(max_sum))
