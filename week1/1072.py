#게임
#이분탐색을 이용한 승률에 변화가 생기는 최소 게임(승)수
def cal_newz(alpha): #alpha만큼 게임을 더 했을 때의 승률 계산 함수 정의
    return ((y+alpha)*100)//(x+alpha)

def binary_search(low, high): #이진탐색 정의
    mid = (low+high)//2 #mid는 low와 high의 평균(버림)
    while low <= high: #low와 high가 교차할 때 까지
        newz = cal_newz(mid) #mid만큼 더 했을 때의 승률을 newz
        if newz - z == 1: # newz와 z의 차이가 1일때 (승률이 정수이기에 0이 아닌 최소 승률변화량은 1이다.)
            next_mid = binary_search(low, mid-1) # low이상 mid미만의 값 중에 newz와 z의 차이가 1인 값이 있는지 확인
            if next_mid == -1: #low이상 mid미만에 정답이 없다면 mid 반환 (이때 mid는 승률에 변화가 생기는 최소 게임수)
                return mid
            else: #있다면 next_mid 반환 (이때 next_mid는 승률에 변화가 생기는 최소 게임수)
                return next_mid
        elif newz - z > 1: #newz와 z의 차이가 1보다 크다면 high를 mid 왼쪽으로
            high = mid-1
        else: #newz와 z의 차이가 없다면 low를 mid 오른쪽으로
            low = mid+1
        mid = (low+high)//2 #mid 재계산
    return -1 #low와 high가 교차했다면 정답이 없다는 뜻이니 -1 반환

global x, y, z #총 게임수, 승수, 승률을 각각 x,y,z
x,y = map(int, input().split()) #x와 y를 입력
z=(y*100)//x #z계산
if z > 98: #승률이 99라면 진 전적이 있으므로 절때 100이 될 수 없음, 승률이 100이라면 더이상 높아질수 없음
    print(-1) #-1(답이 없음) 출력
else:
    low = 1 #승률이 변하지 않는 임의의 값
    high = 1 #승률이 변하는 임의의 값
    while cal_newz(high)==z: #high만큼 게임을 더 하였을 때 z에 변화가 생길 때 까지
        low = high #low를 high로
        high = 2*high #high를 두배로
    if high == 1: #high가 1이라는 뜻은 1번만 더 해도 z에 변화가 생김, 0이 답이 될 수 없으니 무조건 답은 1
        print(high)
    else: #high가 1이 아니라면 low와 high사이를 이분탐색
        alpha = binary_search(low,high)
        print(alpha) #결과 출력