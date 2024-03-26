N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def calculate(num, value):
    global ans
    if(num==N):
        if(value==S):
            ans+=1
    else:
        calculate(num+1, value + arr[num])
        calculate(num+1, value)
if(S==0):
    ans-=1

calculate(0, 0)
print(ans)