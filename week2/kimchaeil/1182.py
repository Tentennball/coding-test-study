import sys
input = sys.stdin.readline

def back_tracking(sum,depth):
    global cnt
    if depth==N:
        if sum == S:
            cnt+=1
        return
    back_tracking(sum+Sequence[depth],depth+1)
    back_tracking(sum,depth+1)

N, S = map(int, input().split())
Sequence = list(map(int, input().split()))
Sequence.sort()
cnt = 0
if S == 0:
    cnt -= 1
back_tracking(0,0)
print(cnt)