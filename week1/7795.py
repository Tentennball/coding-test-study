#먹을 것인가 먹힐 것인가
#정렬과 이분탐색을 이용함, 같은 값이 아닌 작은 값들 중 가장 큰 값을 찾아야 함을 이용
def quick_sort(arr): #퀵소트 정의
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    less_arr, equal_arr, greater_arr = [],[],[]
    for num in arr:
        if num<pivot:
            less_arr.append(num)
        elif num>pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(less_arr)+equal_arr+quick_sort(greater_arr)

def binary_search(target,arr): #이분탐색 정의
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    while low<=high:
        if arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
        mid = (low+high)//2
    return mid + 1

testcase = int(input()) #테스트 케이스 횟수 입력
for test in range(testcase): #테스트 케이스 횟수 만큼 반복
    input() #파이썬에선 A의 수 N과 B의 수 M이 필요 없음
    A = list(map(int, input().split())) #A 입력
    B = quick_sort(list(map(int, input().split()))) #B 입력 및 정렬
    result = 0 #result를 0으로 초기화
    for target in A:
        search_result = binary_search(target,B)
        result += search_result
    print(result) #결과 출력