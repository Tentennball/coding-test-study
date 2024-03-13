#먹을 것인가 먹힐 것인가
#정렬과 이분탐색을 이용
def quick_sort(arr): #퀵소트 정의
    if len(arr)<=1: #매개변수로 받은 배열의 길이가 1 이하라면 그대로 반환
        return arr
    pivot = arr[len(arr)//2] #중앙 인덱스 피봇으로 설정
    less_arr, equal_arr, greater_arr = [],[],[] #피봇보다 작은 값들, 같은 값들, 보다 큰 값들을 저장할 배열 각각 선언
    for num in arr:
        if num<pivot: #피봇보다 작으면 less_arr에 추가
            less_arr.append(num)
        elif num>pivot: #피봇보다 크면 greater_arr에 추가
            greater_arr.append(num)
        else: #같으면 equal_arr에 추가
            equal_arr.append(num)
    return quick_sort(less_arr)+equal_arr+quick_sort(greater_arr) #정렬된 less_arr, equal_arr, greater_arr을 병합하여 반환

def binary_search(target,arr): #이분탐색 정의
    low = 0 #low는 0
    high = len(arr)-1 #high는 arr의 마지막 인덱스
    mid = (low+high)//2 #mid는 low와 high의 평균(내림)
    while low<=high: #low와 high가 교차되면 끝냄
        if arr[mid]==target: #mid에 위치한 값이 target과 같다면 mid 반환
            return mid
        elif arr[mid]<target: #mid에 위치한 값이 target보다 작다면 low를 mid의 오른쪽으로
            low=mid+1
        else: #mid에 위치한 값이 target보다 크면 high를 mid의 왼쪽으로
            high = mid-1
        mid = (low+high)//2 #mid 다시 계산
    return mid #mid 반환(이때 mid는 target보다 작은 값들 중 가장 큰 값의 위치, 없다면 -1)

testcase = int(input()) #테스트 케이스 횟수 입력
for test in range(testcase): #테스트 케이스 횟수 만큼 반복
    input() #파이썬에선 A의 수 N과 B의 수 M이 필요 없음
    A = list(map(int, input().split())) #A 입력
    B = quick_sort(list(map(int, input().split()))) #B 입력 및 정렬
    result = 0 #result를 0으로 초기화
    for target in A: #A의 값들에 대해
        search_result = binary_search(target,B) #같거나 가장 작은 값들 중 가장 큰 값의 위치 찾기, 없다면 -1
        while (B[search_result]==target) and (search_result>-1): #같은 경우 target보다 가장 작은 값들 중 가장 큰 값의 위치 찾기, 없다면 -1
            search_result-=1
        result += search_result+1 #search_result 위치까지가 A가 먹을 수 있는 생명체
    print(result) #결과 출력