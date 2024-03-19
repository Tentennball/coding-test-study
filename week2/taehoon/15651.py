N, M = map(int, input().split())
selected = [0]*(M+1)

def recursion(num):
    if(num==M+1):
        for i in range(1, M+1):
            print(' '.join(map(str, [selected[i]])), end=' ')
        print()
    else:
        for i in range(1, N+1):
            selected[num] = i 
            recursion(num+1)
            selected[num] = 0
    
recursion(1)
