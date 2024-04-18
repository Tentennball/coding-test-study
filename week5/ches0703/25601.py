import sys

input = sys.stdin.readline



N = int(input())

type_dict = {}

# 특정 타입에 대해 부보요소를 저장하도록 함
for _ in range(N - 1):
  sub, super = input().split()
  type_dict[sub] = super


type1, type2 = input().split()

# sub type의 조상 요소 중 찾으려는 type이 있는 지 검사
def type_check(sub, super):
  cursor = sub
  while cursor in type_dict:
    cursor = type_dict[cursor]
    if cursor == super:
      return True
  return False

if type_check(type1, type2) or type_check(type2, type1):
  print(1)
else:
  print(0)

    