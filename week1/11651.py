#좌표 정렬하기2
#퀵소트를 활용한 좌표 정렬(y값오름차순 -> x값오름차순)
def quick_sort(arr): #퀵소트 정의
    if len(arr)<=1: #매개변수로 받은 배열의 길이가 1 이하면 바로 반환
        return arr
    pivot = arr[len(arr)//2] #중앙 인덱스 피봇으로 설정
    less_arr, greater_arr = [], [] #피봇보다 작은 좌표들, 보다 큰 좌표들을 저장할 배열 각각 선언, 같은 좌표는 없기에 equal_arr은 필요 없음
    for spot in arr:
        if spot[1]<pivot[1]: #피봇의 y좌표보다 비교대상의 y좌표가 작으면 less_arr에 추가
            less_arr.append(spot)
        elif spot[1]>pivot[1]: #피봇의 y좌표보다 비교대상의 y좌표가 크면 greater_arr에 추가
            greater_arr.append(spot)
        elif spot[0]<pivot[0]: #y좌표가 같을 때 피봇의 x좌표보다 비교대상의 x좌표가 작으면 less_arr에 추가
            less_arr.append(spot)
        elif spot[0]>pivot[0]: #y좌표가 같을 때 피봇의 x좌표보다 비교대상의 x좌표가 크면 greater_arr에 추가
            greater_arr.append(spot)
    less_arr = quick_sort(less_arr) #less_arr 퀵소트
    greater_arr = quick_sort(greater_arr) #greater_arr 퀵소트
    less_arr.append(pivot) #정렬된 less_arr에 pivot 추가
    return less_arr + greater_arr #정렬된 less_arr과 정렬된 greater_arr을 병합하여 반환

n = int(input()) #좌표 개수 입력

spots =[] #좌표들을 저장할 배열 선언
for i in range(n): #좌표들 입력
    spots.append(list(map(int,input().split())))
spots = quick_sort(spots) #좌표들 정렬
for i in range(n): #결과 출력
    print(spots[i][0],spots[i][1])