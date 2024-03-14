N, C = map(int, input().split())

house = []

for i in range(N):
    house.append(int(input()))
house.sort()

def determine(distance):
    count = 1
    last = house[0]
    for i in range(1, N):
        if(house[i]-last >= distance):
            count += 1
            last = house[i]
    return count >= C

L, R, ans = 1, int(house[-1] - house[0]), 0

while(L<=R):
    mid = int((L + R) / 2)
    if(determine(mid)):
        ans=mid
        L = mid + 1
    else:
        R = mid - 1

print(ans)