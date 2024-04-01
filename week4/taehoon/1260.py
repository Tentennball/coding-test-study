import queue

N, M, V = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(x):
    visited[x] = True
    print(x, end=" ")
    for y in range(1, N+1):
        if(arr[x][y]==False):
            continue
        if(visited[y]==True):
            continue
        dfs(y)

def bfs(z):
    queues.put(z)
    visited[z] = True
    while not queues.empty():
        x = queues.get()
        print(x, end= " ")
        for y in range(1, N+1):
            if(visited[y]==True):
                continue
            if(arr[x][y]==1):
                queues.put(y)
                visited[y] = True
        

for i in range(M):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1
dfs(V)
queues = queue.Queue()
print()
for i in range(1, N+1):
    visited[i] = False

bfs(V)