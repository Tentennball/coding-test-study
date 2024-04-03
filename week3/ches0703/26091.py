import sys

N, M = map(int, sys.stdin.readline().split())
score_list = list(map(int, sys.stdin.readline().split()))
team_cnt = 0

# 점수를 정렬한 후 가장 낮은 사람과 가장 높은 사람의 합을 구함
# 해당 합이 M 이상이면 합격 -> 다음으로 낮은 사람과 다음으로 높음 사람과 합을 구한후 동일과정 반복
# 해당 합이 M 미만이면 낮은 점수 인원 탈락 -> 다음으로 낮은 사람과 가장 높음 사람과 합을 구한후 동일과정 반복
score_list.sort()
i = 0
j = len(score_list) - 1
while i < j:
  if score_list[i] + score_list[j] >= M:
    team_cnt += 1
    i += 1
    j -= 1
  else:
    i += 1

print(team_cnt)