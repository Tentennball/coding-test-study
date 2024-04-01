N, S = map(int, input().split())

arr = list(map(int, input().split()))
sum = arr[0]
ans = N+1
left, right = 0, 0
while((left <= right) and (right < N)):
    if(sum<S and right < N):
        if(right+1==N):
            left+=1
            continue
        right+=1
        sum+=arr[right]
    else:
        ans = min(ans, right-left+1)
        sum-=arr[left]
        left+=1
if(ans==N+1):
    ans=0
print(ans)