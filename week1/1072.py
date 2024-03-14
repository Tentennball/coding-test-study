#게임
#이분탐색을 이용한 승률에 변화가 생기는 최소 게임(승)수
def cal_newz(alpha): #alpha만큼 게임을 더 했을 때의 승률 계산 함수 정의
    return ((y+alpha)*100)//(x+alpha)

def binary_search(low, high): #이진탐색 정의
    mid = (low+high)//2
    while low <= high:
        newz = cal_newz(mid)
        if newz - z == 1:
            next_mid = binary_search(low, mid-1)
            if next_mid == -1:
                return mid
            else:
                return next_mid
        elif newz - z > 1:
            high = mid-1
        else:
            low = mid+1
        mid = (low+high)//2
    return -1

global x, y, z #총 게임수, 승수, 승률을 각각 x,y,z
x,y = map(int, input().split()) #x와 y를 입력
z=(y*100)//x #z계산
if z > 98:
    print(-1)
else:
    low = 1
    high = 1
    while cal_newz(high)==z:
        low = high
        high = 2*high
    if high == 1:
        print(high)
    else:
        alpha = binary_search(low,high)
        print(alpha)