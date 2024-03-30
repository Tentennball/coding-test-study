import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A_arr = list(map(int, input().split()))

max_volume = 0
start=0
end=-1

while(True):
    if start>end:
        end=start
        sum = A_arr[start]
    elif sum<M:
        max_volume = max(sum, max_volume)
        end += 1
        if end>=len(A_arr):
            break
        sum+=A_arr[end]
    elif sum == M:
        max_volume = sum
        break
    else:
        sum-=A_arr[start]
        start += 1
        if start>=len(A_arr):
            break

print(max_volume)