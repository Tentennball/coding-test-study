#9663번 문제 (N-Queens)
#백트래킹 이용
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

available_column=[True]*N #인덱스번째 column에 퀸을 놓을 수 있는가
available_upright=[True]*(2*N-1) #row+column이 인덱스값인 오른쪽위를 향하는 대각선에 퀸을 놓을 수 있는가
available_downright=[True]*(2*N-1) #row-column(최소 -(n-1), 최대 n-1)이 인덱스값+(n-1)인 오른쪽아래를 향하는 대각선에 퀸을 놓을 수 있는가

back_tracking(0)
print(cnt)