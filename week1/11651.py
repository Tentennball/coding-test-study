#좌표 정렬하기2
#퀵소트를 활용한 좌표 정렬(y값오름차순 -> x값오름차순)
def quick_sort(arr): #퀵소트 정의
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    less_arr, greater_arr = [], []
    for spot in arr:
        if spot[1]<pivot[1]:
            less_arr.append(spot)
        elif spot[1]>pivot[1]:
            greater_arr.append(spot)
        elif spot[0]<pivot[0]:
            less_arr.append(spot)
        elif spot[0]>pivot[0]:
            greater_arr.append(spot)
    less_arr = quick_sort(less_arr)
    greater_arr = quick_sort(greater_arr)
    less_arr.append(pivot)
    return less_arr + greater_arr

n = int(input())

spots =[]
for i in range(n):
    spots.append(list(map(int,input().split())))
spots = quick_sort(spots)
for i in range(n): #결과 출력
    print(spots[i][0],spots[i][1])