#16510번 문제(Predictable Queue)
#누적합과 이분탐색
import sys

def binary_search(target,arr): #이분탐색 정의
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    while low<=high:
        if arr[mid]<target:
            low = mid+1
        elif arr[mid]>target:
            high = mid-1
        else:
            return mid+1
        mid = (low+high)//2
    return mid+1

input = sys.stdin.readline

N, M = map(int, input().split())
t_arr = list(map(int,input().split()))

t_sum_arr = [t_arr[0]]
for i in range(1,len(t_arr)):
    t_sum_arr.append(t_arr[i]+t_sum_arr[i-1])

for i in range(M):
    T = int(input())
    print(binary_search(T,t_sum_arr))