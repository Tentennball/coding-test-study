N = int(input())
arr = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
count = 0
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
        

for i in range(N):
    input_str = input()
    inputs = [int(char) for char in input_str]
    for j in range(N):
        arr[i][j] = inputs[j]

dfs(0,1)

print(count)