import sys
input = sys.stdin.readline

def back_tracking(depth):
    global cnt
    if depth == N:
        cnt+=1
        return
    for i in range(N):
        if available_column[i] and available_upright[depth+i] and available_downright[depth-i + N-1]:
            available_column[i]=False
            available_upright[depth+i]=False
            available_downright[depth-i + N-1]=False
            back_tracking(depth+1)
            available_column[i]=True
            available_upright[depth+i]=True
            available_downright[depth-i + N-1]=True

N = int(input())
cnt=0

available_column=[True]*N
available_upright=[True]*(2*N-1)
available_downright=[True]*(2*N-1)

back_tracking(0)
print(cnt)
