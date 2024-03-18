import math

N_str = input()
# 입력 정수 변환
N = int(N_str)

# 입력 된 문자의 글자 수 : i 
i = len(N_str)

# 제곱근의 자리 수 : j = 올림(i/2)
j = math.ceil(i/2)


# N의 제곱근의 범위 = 10^(j-1) <= N_sqrt <= 10^(j)-1
left = 10**(j-1)
right = (10**(j)-1)
mid = (left + right) // 2
N_sqrt = -1
while left <= right:
  tmp = mid**2
  if tmp == N:
    N_sqrt = mid
    break
  elif tmp > N:
    right = mid - 1
  else :
    left = mid + 1
  mid = (left + right) // 2

print(N_sqrt)


