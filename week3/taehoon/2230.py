import sys

N, M = map(int, sys.stdin.readline().split())
A = []

for i in range(N):
    A.append((int(sys.stdin.readline())))
A.sort()

left, right = 0, 1
ans = 2e9

while(right < N):
    if(A[right]-A[left]<M):
        right+=1
    else:
        ans = min(ans, A[right]-A[left])
        left+=1
        if(left==right):
            right+=1
print(ans)