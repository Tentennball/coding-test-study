N, K = map(int, input().split()) # 인형 개수, 라이언 개수

dolls = list(map(int, input().split()))

left = 0
right = 0
count = 0
length = N+1
while(left<=right and right<N):
    if(count<K):
        if(dolls[right]==1):
            count+=1
            if(count==K):
                continue
            right+=1
        else:
            right+=1
    else:
        if(dolls[left]==1):
            length = min(length, right-left+1)
            left+=1
            count-=1
            right+=1
        else:
            left+=1
if(length==N+1):
    length=-1
print(length)