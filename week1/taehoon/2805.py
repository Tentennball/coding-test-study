N, M = map(int, (input().split()))

trees = list(map(int, (input().split())))

L, R, ans = 0, 2000000000, 0

def determine(H):
    sum = 0
    for i in range(N):
        if(H <= trees[i]):
            sum += trees[i] - H
    return sum>=M

while(L<=R):
    mid = int((L + R)/2)
    if(determine(mid)):
        ans=mid
        L=mid+1
    else:
        R=mid-1
print(ans)