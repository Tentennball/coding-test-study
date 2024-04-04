N = int(input())
arr = [[-1]*(N+2) for _ in range(N+2)]

ans = []
visited = [[False]*(N+2) for _ in range(N+2)]
count = 0
piece = 0
def dfs(x,y):
    global count
    visited[x][y] = True
    if(x>0 and arr[x-1][y]==1 and (visited[x-1][y] != True)):
        count+=1
        dfs(x-1, y)
    if(y<N and arr[x][y+1]==1 and (visited[x][y+1] != True)):
        count+=1
        dfs(x, y+1)
    if(x<N and arr[x+1][y]==1 and (visited[x+1][y] != True)):
        count+=1
        dfs(x+1, y)
    if(y>0 and(arr[x][y-1] == 1) and (visited[x][y-1] != True)):
        count+=1
        dfs(x, y-1)
        

for i in range(1, N+1):
    input_str = input()
    inputs = [int(char) for char in input_str]
    for j in range(1, N+1):
        arr[i][j] = inputs[j-1]

for i in range(1, N+1):
    for j in range(1, N+1):
        if(arr[i][j]==1 and visited[i][j]==False):
            count += 1
            piece+=1
            dfs(i,j)
            ans.append(count)
            count=0
ans.sort()
print(piece)
for i in ans:
    print(i)