#27278번 문제(영내순환버스)
#누적합

import sys

input = sys.stdin.readline

def cal_get_off_time(start,end,time):
    result = 0
    if time <= t_sum_arr[start-1]:
        result = t_sum_arr[start-1]
    else:
        result = ((time//t_sum_arr[-1]))*t_sum_arr[-1] + t_sum_arr[start-1]
        if time%t_sum_arr[-1] > t_sum_arr[start-1]:
            result += t_sum_arr[-1]
    if start<end:
        result += t_sum_arr[end-1] - t_sum_arr[start-1]
    else:
        result += t_sum_arr[-1] + t_sum_arr[end-1] - t_sum_arr[start-1]
    return result

N, M = map(int, input().split())

t_arr = list(map(int, input().split()))

t_sum_arr = [0]
for i in range(len(t_arr)):
    t_sum_arr.append(t_arr[i]+t_sum_arr[i])

get_off_work_time = -1

for i in range(M):
    start, end, time = map(int, input().split())
    get_off_work_time = max(get_off_work_time, cal_get_off_time(start,end,time))

print(get_off_work_time)