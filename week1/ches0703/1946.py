import sys
N = int(input())

for _ in range(N):
  num_of_people = int(input())
  ranking = []
  
  for _ in range(num_of_people):
    ranking.append(list(map(int, sys.stdin.readline().split())))
  ranking.sort(key=lambda x: x[0])
  # 점수를 입력 받은 후 서류 점수 랭킹으로 정렬
  count = 1
  # 서류 점수 순서 상 다음 지원자가 가질 수 있는 등수의 최소 값
  min_ranking = ranking[0][1]

  # 면접 점수 순으로 리스트 순회
  # 특정 지원자가 최소 등수를 지키지 못함 -> 불합격
  # -> 해당 지원자 보다 서류 및 면접 점수가 높음 사람이 존재
  # ex. 서류2등, 면접5등인 인원이 합격한 경우 서류 3등, 면점 6등은 떨어져야 함 
  # 특정 지원자가 최소 등수를 지킨 경우 -> 합격
  # 추가로 면접 점수 순으로 순회하므로 최소 등수를 변경하여야 함
  # ex. 서류2등, 면접5등인 인원이 합격한 경우, 서류 4등 면접 2등이라면 합격이 되고, 이후 인원들은 2등보다 높은 순위를 가져야 함
  # 서류점수 1등을 제외한 나머지 지원자는 1등의 면접 점수 보다 높은 면접 점수를 가져야 함
  for r in ranking:
    if r[1] < min_ranking:
      min_ranking = r[1]
      count += 1
      if r[1] == 1:
        break

  print(count)

